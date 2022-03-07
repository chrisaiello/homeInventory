from flask import Flask
import os
from models import db
from views import blueprint

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "thingsdb.db"))

app = Flask(__name__, instance_relative_config=True)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db.init_app(app)

app.register_blueprint(blueprint)
  
if __name__ == "__main__":
    app.run(debug=True, port=8080)