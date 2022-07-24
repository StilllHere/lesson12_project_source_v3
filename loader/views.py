from flask import Blueprint, render_template, request, logging
from utils import save_picture, add_post
from json import JSONDecodeError
import logging

ALLOWED_EXTENSIONS={'jpeg', 'png'}

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

@loader_blueprint.route('/post')
def page_add_post():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def post_adding():
    picture = request.files.get('picture')
    content = request.form.get('content')
    if not picture or not content:
        return'ошибка загрузки'
    extension = picture.filename.split('.')[-1]
    if extension not in ALLOWED_EXTENSIONS:
        logging.info('Файл не картинка')
        return 'Расширение не то'
    try:
        path_pic: str = '../.' + save_picture(picture)
        new_post= add_post({'pic': path_pic,'content': content})
        return render_template('post_uploaded.html', post=new_post)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return "Файл не найден"
    except JSONDecodeError:
        return "Не превращается в список"
