from flask import Flask, render_template
from flask_login import current_user
from database import db
from werkzeug.security import generate_password_hash
from blueprints.auth import auth, login_manager
from models import User
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.login_site'
login_manager.login_message = "User needs to be logged in to view this page"

app.register_blueprint(auth)


@app.context_processor
def inject_user_status():
    return dict(logged_in=current_user.is_authenticated)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('home.html')

@app.route('/blog', methods=['GET', 'POST'])
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            hashed_password = generate_password_hash('admin', method='pbkdf2')
            admin = User(username='admin', password=hashed_password, role='superadmin')
            db.session.add(admin)
            db.session.commit() 
        app.run(debug=True, port=5000)