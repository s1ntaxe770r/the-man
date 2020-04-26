import os
from flask import Flask, url_for, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from time import strftime



project_dir = os.path.dirname(os.path.abspath(__file__))
db_file = "sqlite:///{}".format(os.path.join(project_dir, "todo.db"))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = db_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.today())

    def __repr__(self):
        return '<Todo: {}>'.format(self.task)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form != " ":
            todo = Todo(task=request.form.get("task"))
            db.session.add(todo)
            db.session.commit()
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)


@app.route("/delete", methods=["POST"])
def delete():
    todo = request.form.get("task")
    task = Todo.query.filter_by(task=todo).first()
    db.session.delete(task)
    db.session.commit()
    return redirect("/")


@app.route('/social',methods=['GET'])
def social():
	url  = 'https://github.com/s1ntaxe770r'
	return redirect(url)


if __name__ == '__main__':
    app.run()
