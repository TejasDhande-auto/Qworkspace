from AllureListener import AllureListener
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger


class AllureReportLibrary:
    """
    Allure Report Library
    
    The Allure Adaptor for Robot Framework is a Library that can be included
    in the Robot scripts to generate Allure
    compatible XML files which can then be used to generate the Allure HTML
    reports. These reports provide a clear and dynamic overview of the status
    of the test run through several graphs and a time line overview of the run
    itself.

    Optionally an argument can be provided to have the Allure adapter store its 
    files in a different folder from the normal Robot Framework log files. 

        Library           AllureReportLibrary     C:\\Temp\\Allure
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = '1.1.1'

    def __init__(self, AllureOutputPath=None):
        # In case Listener is added via Command Line, then Library should not
        # another one. That would result in duplicate log files for Suite.
        # Since RED runs this class to get the documentation, the Try/Except is needed.
        try:
            AllureListenerActive = BuiltIn().get_variable_value('${AllureListenerActive}', False)
            if AllureListenerActive is False:
                self.ROBOT_LIBRARY_LISTENER = AllureListener(AllureOutputPath, 'Library')
        except:
            pass
        return None
        
    def set_output_dir(self, output_dir):
        """
        This is the output method short line.
        
        This is the output method long line.
        """
        print 'set output dir'