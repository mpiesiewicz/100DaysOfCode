import requests
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/blog/')
def home():
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    posts = response.json()
    return render_template("index.html", posts=posts)


@app.route('/blog/<num>')
def get_post(num):
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    posts = response.json()
    post = posts[int(num)-1]
    return render_template('post.html', post=post)


if __name__ == "__main__":
    app.run(debug=True)
