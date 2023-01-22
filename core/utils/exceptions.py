class NoSuchBrowser(Exception):
    """ Specified browser is not enlisted """


class BrowserFault(Exception):
    """ Problem with connecting driver to browser """


class DifferentLengthsOfStrings(Exception):
    """ Different lengths of string to replace and string to replace with """


class TooMuchWordsInStrings(Exception):
    """ More than 2 words in strings """


