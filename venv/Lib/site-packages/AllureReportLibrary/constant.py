class Status(object):
    FAILED = 'failed'
    BROKEN = 'broken'
    PASSED = 'passed'
    CANCELED = 'canceled'
    PENDING = 'pending'


class Label(object):
    DEFAULT = 'allure_label'
    FEATURE = 'feature'
    STORY = 'story'
    ISSUE = 'issue'
    TESTCASE = 'testId'
    THREAD = 'thread'
    HOST = 'host'


class Severity(object):
    BLOCKER = 'blocker'
    CRITICAL = 'critical'
    NORMAL = 'normal'
    MINOR = 'minor'
    TRIVIAL = 'trivial'


class Robot(object):
    PASS = 'PASS'
    FAIL = 'FAIL'


SEVERITIES = ['blocker', 'critical', 'normal', 'minor', 'trivial']
ROBOT_OUTPUT_FILES = ['output.xml','log.html','report.html']
ALLURE_NAMESPACE = "urn:model.allure.qatools.yandex.ru"
COMMON_NAMESPACE = "urn:model.commons.qatools.yandex.ru"
