import logging

from flask import render_template_string, Response

import core
from core import create_app, requester, replacer
from core.utils import exceptions
from core.utils.extensions import get_type_by_path, Types

app = create_app()

logging.basicConfig(filename='record.log',
                    level=logging.INFO,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>')
def replace_text(path: str):
    """ Replace specified string instances
        Or scrape target url for content if request is not a webpage """
    # determine types and extensions
    request_type, extension = get_type_by_path(path=path)

    app.logger.info(f'{request_type} is requested with {extension} extension')

    # try to get content from website
    try:
        if request_type == Types.SCRIPT or request_type == Types.CSS:
            return render_template_string(source=requester.get_text_like_file(path=path))
        if request_type == Types.IMAGE:
            return Response(requester.get_image(path), mimetype=f'image/{extension}')
        if request_type == Types.SVG:
            return Response(requester.get_svg(path), mimetype=f'image/{extension}')

        # if webpage is requested we try to get it
        initial_content = requester.get_page_content(path=path)
    except exceptions.BrowserFault:
        app.logger.error(f'Something is wrong with browser specified ({core.BROWSER})')
        raise
    except Exception as ex:
        app.logger.error(f'Unexpected error {str(ex)}')
        raise
    # and get processed content
    replaced_content = replacer.replace_content(initial_content=initial_content)
    return render_template_string(source=replaced_content)


if __name__ == '__main__':
    app.run()
