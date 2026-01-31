from flask import Flask
from routes.user_routes import user_bp
from routes.task_routes import task_bp

app = Flask(__name__)

# REGISTER BLUEPRINTS
app.register_blueprint(user_bp)
app.register_blueprint(task_bp)

@app.route("/")
def home():
    return "User Task Management Backend running"

if __name__ == "__main__":
    app.run(debug=True)
