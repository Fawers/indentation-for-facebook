import os
import re

from flask import Flask, request, render_template, url_for, make_response


app = Flask(__name__)


INDENT_CHARACTER_FOUR_SPACES = ' ' * 4  # default indent character
INDENT_CHARACTER_IDEOGRAPHIC_SPACE = '\u3000'  # output indent character
# http://www.fileformat.info/info/unicode/char/3000/index.htm


def do_it(content, indent_character=INDENT_CHARACTER_FOUR_SPACES):
    """
    This is the function that will actually do the work. A regular
    expression will be used to search for `indent_character` and replace
    each occurence of such with `INDENT_CHARACTER_IDEOGRAPHIC_SPACE`.
    """

    pattern = re.compile(r'^(?:{})+'.format(indent_character), re.M)
    result, occurences = pattern.subn(
        lambda match: match.group().replace(
            indent_character,
            INDENT_CHARACTER_IDEOGRAPHIC_SPACE),
        content
    )

    return result, occurences


@app.route('/')
def home():
    """
    Home page. Forms will be presented here.
    """

    return render_template('home.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    """
    Result view. This view must either display the result in the
    browser or mark it as an attachment for download. If the request
    contains the "text/plain" Accept header value, show the result as
    is, without any html.
    """
    if request.method == 'GET':
        response = make_response()
        response.headers['Refresh'] = '0; ' + url_for('home')
        return response

    indent_char = request.form.get('indent-char', 'spaces')
    indent_level = int(request.form.get('indent-level', '4'))
    download = request.form.get('download', 'no')

    origin = request.form.get('from', 'textarea')

    if origin == 'file':
        content = request.files['content'].read().decode()
    elif origin == 'textarea':
        content = request.form['content']
    else:
        return render_template('400.html'), 400

    if indent_char == 'spaces':
        indent_char = ' ' * indent_level
    elif indent_char == 'tabs':
        indent_char = '\t' * indent_level

    result = do_it(content, indent_char)

    if request.headers['Accept'] == 'text/plain':
        return make_response(result[0])

    if download == 'yes':
        file_ext = os.path.splitext(request.files['content'].filename)[1] \
            if request.files else '.txt'
        response = make_response(result[0])
        response.headers['Content-Disposition'] = 'attachment; filename="{}"' \
            .format('result' + file_ext)

        return response

    return render_template('result.html', content=result[0],
                           occurences=result[1])


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    response = make_response('Trying to open email context...')
    response.headers['Refresh'] = '1; {}'.format(
        'mailto:fabricioswerneck@gmail.com?subject=[Indentation for Facebook]')
    return response


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=1, host='0.0.0.0')
