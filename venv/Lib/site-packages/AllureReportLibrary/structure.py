from allure.rules import xmlfied, Attribute, Element, WrappedMany, Nested, Many, \
    Ignored
from allure.constants import ALLURE_NAMESPACE, COMMON_NAMESPACE
from allure.structure import IterAttachmentsMixin

# overwriting the base class in allure.structure with an additional URL param.
class Environment(xmlfied('environment',
                          namespace=COMMON_NAMESPACE,
                          id=Element(),
                          name=Element(),
                          url=Element(), # Added
                          parameters=Many(Nested()))):
    pass

# Overwriting the base class in allure.structure with an additional SEVERITY attribute.
class TestCase(IterAttachmentsMixin,
               xmlfied('test-case',
                       id=Ignored(),  # internal field, see AllureTestListener
                       name=Element(),
                       title=Element().if_(lambda x: x),
                       description=Element().if_(lambda x: x),
#                        description=Element(),
                       failure=Nested().if_(lambda x: x),
                       steps=WrappedMany(Nested()),
                       attachments=WrappedMany(Nested()),
                       labels=WrappedMany(Nested()),
                       status=Attribute(),
                       severity=Attribute(), # Added
                       start=Attribute(),
                       stop=Attribute())):
    pass