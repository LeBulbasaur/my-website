from flask import Flask, render_template
from os import path
from articles import load_articles
import json
from flask import abort

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('home.html')


@app.route('/blog', methods=['GET', 'POST'])
def blog():
    articles_dir = path.join(app.root_path, "articles")
    articles = load_articles(articles_dir)
    return render_template('blog.html', articles=articles)


@app.route('/blog/<slug>', methods=['GET'])
def article(slug):
    """Show raw/prettified JSON for a single article identified by slug."""
    articles_dir = path.join(app.root_path, "articles")
    articles = load_articles(articles_dir)
    for a in articles:
        if a.get('slug') == slug:
            return render_template('article.html', article=a)
    abort(404)

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True, port=5000)