from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html')

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True, port=5000)