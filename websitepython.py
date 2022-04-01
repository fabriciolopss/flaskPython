
from flask import Flask, render_template
import os
app = Flask(__name__, static_folder = 'static')



@app.route("/")
def hello():
    with open("cardapio.txt", "r", encoding="utf-8") as f:
        data = f.readlines()
    return render_template('index.html', data = data)

@app.route("/ru1.html/")
def hello_world():
    with open("cardapio.txt", "r", encoding="utf-8") as f:
        data = f.readlines()
        data[7] = data[7].replace("]", "")
    return render_template('ru1.html', data = data)

if __name__ == "__main__":
    app.run()