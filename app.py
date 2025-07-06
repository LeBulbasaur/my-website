from flask import Flask, render_template
from tools.trambus import get_trambus_schedule

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('home.html')

@app.route('/tools', methods=['GET', 'POST'])
def tools():
    return render_template('tools.html')

@app.route('/tools/trambus', methods=['GET', 'POST'])
def trambus():
    schedule = get_trambus_schedule('1234567890')
    return render_template('tools/trambus.html', schedule=schedule)

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True, port=5000)