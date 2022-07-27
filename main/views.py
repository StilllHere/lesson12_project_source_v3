#создание блюпринта
from flask import Blueprint, render_template, request, logging
from utils import read_file, get_posts_by_word
from json import JSONDecodeError
import logging

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

@main_blueprint.route('/')
def root_page():
    return render_template('index.html')

@main_blueprint.route('/search')
def search_page():
    s = request.args.get('s')
    logging.info('Выполняем поиск')
    try:
        if s:
            posts = get_posts_by_word(s)
            return render_template('post_list.html', word=s, posts=posts)
        else:
            return "Вы ничего не ввели"
    except FileNotFoundError:
        return "Файл не найден"
    except JSONDecodeError:
        return "Не превращается в список"

