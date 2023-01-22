import re
import functools
import operator

import core
from core.utils.regex import Literals

# getting separate words from string to replace with
_STRING_TO_REPLACE_WITH_WORDS = core.STRING_TO_REPLACE_WITH.split(Literals.WHITESPACE.value)


def _build_ignore_case_chr_regex(char: str):
    """ Building ignore case regex like [B,b][L,l][A,a][C,c][K,k]"""

    # we can skip whitespaces
    if char == Literals.WHITESPACE.value:
        return char
    return f'[{char.upper()},{char.lower()}]'


def _build_regex():
    """ Building regex for cases when we have zero or more tags and whitespaces between words """
    ignore_case_regex_chars = map(lambda x: _build_ignore_case_chr_regex(x),
                                  core.STRING_TO_REPLACE)
    ignore_case_regex = ''.join(ignore_case_regex_chars)

    # we can have arbitrary amount of whitespaces and tags between words
    parts_of_regex_to_replace_whitespace_with = (Literals.ONE_OR_MORE_WHITESPACES_REGEX.value,
                                                 Literals.ZERO_OR_MORE_HTML_TAGS_WITH_WHITESPACES_OR_NEWLINES_REGEX.value,
                                                 Literals.ZERO_OR_MORE_WHITESPACES_REGEX.value)
    regex_to_replace_whitespace_with = functools.reduce(operator.add, parts_of_regex_to_replace_whitespace_with)

    # we can just replace existing whitespaces with our regex to find arbitrary amount of whitespaces and tags
    ignore_case_regex_divided_by_tags = ignore_case_regex.replace(Literals.WHITESPACE.value,
                                                                  regex_to_replace_whitespace_with)

    return ignore_case_regex_divided_by_tags


def _convert_case(match_obj):
    # check if we have tags in our matches
    tags = re.search(Literals.ONE_OR_MORE_HTML_TAGS_WITH_WHITESPACES_OR_NEWLINES_REGEX.value, match_obj.group(0))
    # concatenating words, whitespaces and tags
    if tags:
        return functools.reduce(operator.add, (_STRING_TO_REPLACE_WITH_WORDS[0],
                                               Literals.WHITESPACE.value,
                                               # for case when dividing tags are divided by whitespaces
                                               tags.group(0),
                                               _STRING_TO_REPLACE_WITH_WORDS[1]))

    # or just returning string to replace with
    return core.STRING_TO_REPLACE_WITH


def replace_content(initial_content: str):
    return re.sub(_build_regex(), _convert_case, initial_content)
