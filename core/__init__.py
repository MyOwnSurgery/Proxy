import os

from flask import Flask

from core.utils.regex import Literals
from core.utils import exceptions

STRING_TO_REPLACE = os.getenv('STRING_TO_REPLACE')
STRING_TO_REPLACE_WITH = os.getenv('STRING_TO_REPLACE_WITH')
URL = os.getenv('TARGET_URL')
BROWSER = os.getenv('BROWSER')


def _validate_input():
    if len(STRING_TO_REPLACE.split(Literals.WHITESPACE.value)) \
            != len(STRING_TO_REPLACE_WITH.split(Literals.WHITESPACE.value)):
        raise exceptions.DifferentLengthsOfStrings("Strings lengths should be equal")
    # too hard for arbitrary number of words...
    if len(STRING_TO_REPLACE.split(Literals.WHITESPACE.value)) > 2:
        raise exceptions.TooMuchWordsInStrings("Strings should contain 2 words")


def create_app():
    _validate_input()
    app = Flask(__name__)
    return app
