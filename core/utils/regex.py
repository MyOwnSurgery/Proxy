from enum import Enum


class Literals(Enum):
    """ Some helping stuff """
    WHITESPACE = ' '
    NEWLINE = '\n'
    HTML_TAG_REGEX = r'(<(?:\"[^\"]*\"["\"]*|"[^"]*"["\"]*|[^"\">])+>)'
    HTML_TAG_WITH_WHITESPACES_OR_NEWLINES_REGEX = r'(<(?:\"[^\"]*\"["\"]*|"[^"]*"["\"]*|[^"\">])+>[( |\n)]{0,})'
    ZERO_OR_MORE_REGEX = '{0,}'
    ONE_OR_MORE_REGEX = '{1,}'
    ZERO_OR_MORE_WHITESPACES_REGEX = '[( |\n)]{0,}'
    ONE_OR_MORE_WHITESPACES_REGEX = '[( |\n)]{1,}'
    ZERO_OR_MORE_HTML_TAGS_WITH_WHITESPACES_OR_NEWLINES_REGEX = \
        HTML_TAG_WITH_WHITESPACES_OR_NEWLINES_REGEX + ZERO_OR_MORE_REGEX
    ONE_OR_MORE_HTML_TAGS_WITH_WHITESPACES_OR_NEWLINES_REGEX = \
        HTML_TAG_WITH_WHITESPACES_OR_NEWLINES_REGEX + ONE_OR_MORE_REGEX
