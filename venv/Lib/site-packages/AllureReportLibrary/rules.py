import re
import sys

from lxml import objectify
from namedlist import namedlist

from utils import unicode_helper


def make_element(name, namespace):
    return getattr(objectify.ElementMaker(annotate=False, namespace=namespace,), name)


class Rule(object):
    _check = None

    def if_(self, check):
        self._check = check
        return self

    def check(self, data):
        if self._check:
            return self._check(data)
        else:
            return True


class Ignored(Rule):
    def if_(self, check):
        return False


class Element(Rule):

    def __init__(self, name='', namespace=''):
        self.name = name
        self.namespace = namespace

    def value(self, name, data):
        return make_element(self.name or name, self.namespace)(unicode_helper(data))


class Attribute(Rule):

    def value(self, name, data):
        return unicode_helper(data)


class Nested(Rule):

    def value(self, name, data):
        return data.toxml()


class Many(Rule):

    def __init__(self, rule, name='', namespace=''):
        self.rule = rule
        self.name = name
        self.namespace = namespace

    def value(self, name, data):
        return [self.rule.value(name, x) for x in data]


class WrappedMany(Many):

    def value(self, name, data):
        values = super(WrappedMany, self).value(name, data)
        return make_element(self.name or name, self.namespace)(*values)


def xmlfied(el_name, namespace='', fields=[], **kw):
    items = fields + list(kw.items())

    class Listener(namedlist('XMLFied', [(item[0], None) for item in items])):

        def toxml(self):
            el = make_element(el_name, namespace)

            def entries(cl):
                return [(name, rule.value(name, getattr(self, name)))
                        for (name, rule) in items
                        if isinstance(rule, cl) and rule.check(getattr(self, name))]

            elements = entries(Element)
            attributes = entries(Attribute)
            nested = entries(Nested)
            manys = sum([[(m[0], v) for v in m[1]] for m in entries(Many)], [])

            return el(*([element for (_, element) in elements + nested + manys]),
                      **dict(attributes))

    return Listener
