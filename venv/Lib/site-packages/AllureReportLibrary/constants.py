class Robot(object):
    PASS = 'PASS'
    FAIL = 'FAIL'

ROBOT_OUTPUT_FILES = ['output.xml','log.html','report.html']
SEVERITIES = ['blocker', 'critical', 'normal', 'minor', 'trivial']
STATUSSES = ['failed', 'broken', 'canceled', 'pending', 'passed']