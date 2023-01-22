from enum import Enum
import os
from typing import Tuple, Union


Extension = str


class Types(Enum):
    IMAGE = 'image'
    SCRIPT = 'script'
    CSS = 'css'
    SVG = 'svg'
    HTML = 'html'


EXTENSION_2_TYPE = {'.jpg': Types.IMAGE, '.png': Types.IMAGE, '.ico': Types.IMAGE,
                    '.js': Types.SCRIPT,
                    '.css': Types.CSS,
                    '.svg': Types.SVG}


def get_type_by_path(path: str) -> Tuple[Types, Union[Extension, None]]:
    split = os.path.splitext(path)
    if len(split) == 1:
        return Types.HTML, None

    _, extension = split
    file_type = EXTENSION_2_TYPE.get(extension, None)

    # try to process as html
    if not file_type:
        return Types.HTML, None

    return file_type, extension
