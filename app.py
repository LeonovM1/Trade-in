from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html")


@app.route('/about')
def about():
  return render_template("about.html")


@app.route('/benefit')
def benefit():
  return render_template("benefit.html")


if __name__ == "__main__":
  app.run(debug=True)


