import logging
from flask import Flask, request, render_template, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint


app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler(filename="basic.log", encoding='utf-8', mode='a+')])

if __name__ == "__main__":
    app.run()

