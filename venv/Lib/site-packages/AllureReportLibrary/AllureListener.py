from six import text_type, iteritems
from itertools import cycle
from contextlib import contextmanager
from functools import wraps
import os
import uuid
import re
from lxml import etree
import py
import re
import io
import shutil
import threading
import sys
import socket
from sys import version

# for debugging purpose not needed by application
import pprint


from robot.libraries.Screenshot import Screenshot
from robot.running.userkeyword import UserLibrary
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from robot.version import get_version, get_full_version, get_interpreter

from allure.utils import now

from allure.structure import Environment, EnvParameter, TestLabel, Failure, Attach, TestSuite, TestStep
from structure import TestCase # Overriding TestCase due to missing severity attribute. 

from allure.constants import Status, Label
from constants import Robot, ROBOT_OUTPUT_FILES, SEVERITIES, STATUSSES

from allure.common import AttachmentType
from common import AllureImpl

from version import VERSION

class AllureListener(object):
    ROBOT_LISTENER_API_VERSION = 2
    
    def __init__(self, allurelogdir=None, source='Listener'):
        self.stack = []
        self.testsuite = None
        self.callstack = []
        self.allurelogdir = allurelogdir
        self.AllureProperties = []
        self.AllureIssueIdRegEx=''


        # Setting this variable prevents the loading of a Library added Listener.
        # I case the Listener is added via Command Line, the Robot Context is not
        # yet there and will cause an exceptions. Similar section in start_suite.
        try:
            AllureListenerActive = BuiltIn().get_variable_value('${AllureListenerActive}', false)
            BuiltIn().set_global_variable('${AllureListenerActive}', True)
        except:
            logger.console('')
            


    
# Listener functions

    def start_test(self, name, attributes):
        if len(str(attributes.get('doc'))) > 0:
            description = str(attributes.get('doc'))
        else:
            description = name

        test = TestCase(name=name,
                description=description,
                start=now(),
                attachments=[],
                labels=[],
#                 parameters=[],
                steps=[])

        self.stack.append(test)
        return
    
    def end_test(self, name, attributes):

        test = self.stack[-1]
        if attributes.get('status') == Robot.PASS:
            test.status = Status.PASSED
#             test.description=attributes.get('message')
        elif attributes.get('status')==Robot.FAIL:
            test.status = Status.FAILED
            test.failure = Failure(message=attributes.get('message'), trace='')
        elif attributes.get('doc') is not '':
            test.description = attributes.get('doc')


        
        if attributes['tags']:
            for tag in attributes['tags']:
                if re.search(self.AllureIssueIdRegEx, tag):
                    test.labels.append(TestLabel(
                        name=Label.ISSUE,
                        value=tag))
                if tag.startswith('feature'):
                    test.labels.append(TestLabel(
                        name='feature',
                        value=tag.split(':')[-1]))
                if tag.startswith('story'):
                    test.labels.append(TestLabel(
                        name='story',
                        value=tag.split(':')[-1]))
                elif tag in SEVERITIES:
                    test.labels.append(TestLabel(
                        name='severity',
                        value=tag))
                elif tag in STATUSSES:
                    test.status = tag  # overwrites the actual test status with this value.

#         test.labels.append(TestLabel(
#             name='thread',
#             value=str(threading._get_ident())))
#         self.testsuite.tests.append(test)
        self.PabotPoolId =  BuiltIn().get_variable_value('${PABOTEXECUTIONPOOLID}')
        if(self.PabotPoolId is not None):
            self.threadId = 'PabotPoolId-' + str(self.PabotPoolId)
        else:
            self.threadId = threading._get_ident()
                
        test.labels.append(TestLabel(
            name='thread',
            value=str(self.threadId)))

        self.testsuite.tests.append(test)
 # ----------------------------------------------------- 
        test.stop = now()        
        return test

    def start_suite(self, name, attributes):
        
        self.SuitSrc =      BuiltIn().get_variable_value('${SUITE_SOURCE}')
        self.issuetracker = BuiltIn().get_variable_value('${ISSUE_TRACKER}')
        self.logdir =       BuiltIn().get_variable_value('${OUTPUT_DIR}')
        self.RobotLogDir =  BuiltIn().get_variable_value('${ALLURE_OUTPUT_DIR}')

        # Reading the Allure Properties file for the Issue Id regular expression
        # for the Issues and the URL to where the Issues/Test Man links should go.
        seperator = "="
        self.AllurePropPath = self.SuitSrc + '\\allure.properties'
        if os.path.exists(self.AllurePropPath) is True: 
            with open(self.SuitSrc+'\\allure.properties') as f:
                for line in f:
                    if seperator in line:
                        name, value = line.split(seperator, 1)
                        self.AllureProperties.append({name.strip() : value.strip()})
                        if name.strip() == 'allure.issues.id.pattern':
                            self.AllureIssueIdRegEx = value.strip()
        
        # Setting this variable prevents the loading of a Library added Listener.
        # I case the Listener is added via Command Line, the Robot Context is not
        # yet there and will cause an exceptions. Similar section in __init__.
        ListenerList = BuiltIn().get_variable_value('${AllureListenerActive}', False)
        BuiltIn().set_global_variable('${AllureListenerActive}', True)

        # When running a Robot folder, the folder itself is also considered a Suite
        # The full check depends on the availability of all the vars which are 
        # only available when a Robot file has started.
        IsSuiteDirectory = os.path.isdir(self.SuitSrc)
        if(not(IsSuiteDirectory)):
            ''' Check if class received Output Directory Path through initialisation. '''
            if self.allurelogdir is None:
                '''' Check if in the Robot file the variable has been set.'''
                if self.RobotLogDir is not None:
                    self.allurelogdir = self.RobotLogDir
                else:
                    ''' No Path was provided, so using output dir with additional sub folder. '''
                    self.allurelogdir = BuiltIn().get_variable_value('${OUTPUT_DIR}') + "\\Allure"

            self.AllureImplc = AllureImpl(self.allurelogdir)

            
        if attributes.get('doc') is not '':
            description = attributes.get('doc')
        else:
            description = name
        
        self.testsuite = TestSuite(name=name,
                title=name,
                description=description,
                tests=[],
                labels=[],
                start=now())

        return

    def end_suite(self, name, attributes):

        self.testsuite.stop = now()
        logfilename = '%s-testsuite.xml' % uuid.uuid4()

        # When running a folder, the folder itself is also considered a Suite
        # The full check depends on the availability of all the vars which are 
        # only available when a Robot file has started.
        IsSuiteDirectory = os.path.isdir(BuiltIn().get_variable_value("${SUITE_SOURCE}"))
        if(not(IsSuiteDirectory)):
            with self.AllureImplc._reportfile(logfilename) as f:
                self.AllureImplc._write_xml(f, self.testsuite)

        return

    def start_keyword(self, name, attributes):
        if(attributes.get('type') == 'Keyword'):
            keyword = TestStep(name=name,
                    title=name,
                    attachments=[],
                    steps=[],
                    start=now(),)
            if self.stack:
    #             self.stack[-1].steps.append(keyword)
                self.stack.append(keyword)
            return keyword

    def end_keyword(self, name, attributes):
        """
        Stops the step at the top of ``self.stack``
        Then adds it to the previous one, as this is a 
        """
        # Check to see if there are any items to add the log message to
        # this check is needed because otherwise Suite Setup may fail.
        if len(self.stack) > 0:
            if(attributes.get('type') == 'Keyword'):
        #         pprint.pprint(attributes)
                step = self.stack.pop()
                 
                if(attributes.get('status') == 'FAIL'):
                    step.status = 'failed'
                elif(attributes.get('status') == 'PASS'):
                    step.status = 'passed'
                     
                step.stop = now()
                 
                # Append the step to the previous item. This can be another step, or
                # another keyword.
                self.stack[-1].steps.append(step)      
    
        return

    def log_message(self, msg):

        # Check to see if there are any items to add the log message to
        # this check is needed because otherwise Suite Setup may fail.
        if len(self.stack) > 0:
#             if msg['level']=='INFO':
            if self.stack[-1].title == 'Selenium2Library.Capture Page Screenshot':
                screenshot = re.search('[a-z]+-[a-z]+-[0-9]+.png',msg['message'])
                if screenshot:
                    self.attach('{}'.format(screenshot.group(0)) , screenshot.group(0))
            
        return

    def close(self): 

        environment = {}    
        environment['id'] = 'Robot Framework'
        environment['name'] = socket.getfqdn()
        environment['url']= 'http://'+socket.getfqdn()+':8000'
        
        env_dict = (\
                    {'Robot Framework Full Version': get_full_version()},\
                    {'Robot Framework Version': get_version()},\
                    {'Interpreter': get_interpreter()},\
                    {'Python version': sys.version.split()[0]},\
                    {'Allure Adapter version': VERSION},\
                    {'Robot Framework CLI Arguments': sys.argv[1:]},\
                    {'Robot Framework Hostname': socket.getfqdn()},\
                    {'Robot Framework Platform': sys.platform}\
                    )

        for key in env_dict:
            self.AllureImplc.environment.update(key)
        self.AllureImplc.store_environment(environment)        

        # store the Allure properties
        #
        with self.AllureImplc._attachfile('allure.properties') as f:

            li = self.AllureProperties
            lilen = int(len(self.AllureProperties))
            
            for i in range(lilen):
                if i < len(li):
                    key = list(li[i].keys())[0]
                    value = list(li[i].values())[0]
                    f.write(key+'='+value+'\n')
    
        f.close()
        return


# Helper functions

    def attach(self, title, contents, attach_type=AttachmentType.PNG):
        """
        This functions created the attachments and append it to the test.
        """
        contents = os.path.join(self.logdir, contents)
        with open(contents, 'rb') as f:
            file_contents = f.read()
        
        attach = Attach(source=self.AllureImplc._save_attach(file_contents, attach_type),
                        title=title,
                        type=attach_type)
        self.stack[-1].attachments.append(attach)
        return
    def get_properties(self):
        # Reading the Allure Properties file for the Issue Id regular expression
        # for the Issues and the URL to where the Issues/Test Man links should go.
        AllureProperties = {}
        seperator = "="
        self.AllurePropPath = self.SuitSrc + '\\allure.properties'
        if os.path.exists(self.AllurePropPath) is True: 
            with open(self.SuitSrc+'\\allure.properties') as f:
                for line in f:
                    if seperator in line:
                        name, value = line.split(seperator, 1)
                        AllureProperties[name.strip()] = value.strip()
                        if name.strip() == 'allure.issues.id.pattern':
                            self.AllureIssueIdRegEx = value.strip()
        return AllureProperties