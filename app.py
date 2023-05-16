from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template("index.html")


@app.route("/login")
def login():
  return render_template("login.html")


# invalid URL
@app.errorhandler(404)
def page_not_found(e):
  return render_template("404.html"), 404


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
