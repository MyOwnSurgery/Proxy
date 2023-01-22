class InvalidInput(Exception):
    """ Base class for input errors """


class NoSuchBrowser(InvalidInput):
    """ Specified browser is not enlisted """


class DifferentLengthsOfStrings(InvalidInput):
    """ Different lengths of string to replace and string to replace with """


class TooMuchWordsInStrings(InvalidInput):
    """ More than 2 words in strings """


class BrowserFault(Exception):
    """ Problem with connecting driver to browser """
