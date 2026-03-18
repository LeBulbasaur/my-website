from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('home.html')

@app.route('/blog', methods=['GET', 'POST'])
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True, port=5000)