import time
import hashlib

from six import text_type, binary_type


def uid(name):
    """
    Generates UID uniquely for name by the means of hash function,
    since allure requests that.
    """
    return hashlib.sha256(name).hexdigest()


def sec2ms(sec):
    return int(round(sec * 1000.0))

def now():
    """
    Return current time in the allure-way representation.
    """
    return sec2ms(time.time())

def unicode_helper(text):
    if isinstance(text, text_type):
        return text
    elif isinstance(text, binary_type):
        return text.decode('utf-8', 'replace')
    else:
        return text_type(text)
