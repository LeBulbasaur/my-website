from flask import Flask, render_template
from tools.trambus import get_trambus_schedule

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('home.html')

@app.route('/tools', methods=['GET', 'POST'])
def tools():
    return render_template('tools.html')

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True, port=5000)