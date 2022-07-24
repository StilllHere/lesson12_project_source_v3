import json

def read_file():
    """
    Чтение из файла
    """
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_word(word):
    """
    Поиск постов
    """
    result =[]
    for post in read_file():
        if word.lower() in post['content'].lower():
           result.append(post)
    return result


def save_picture(picture):
    filename = picture.filename
    path = f'./uploads/{filename}'
    picture.save(path)
    return path

def add_post(post):
    posts = read_file()
    posts.append(post)
    with open('posts.json','w', encoding='utf-8') as f:
        json.dump(posts, f)
    return posts