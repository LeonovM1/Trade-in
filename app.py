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


@app.route('/mypage')
def mypage():
  return render_template("mypage.html")


@app.route('/badauto')
def badauto():
  return render_template("badauto.html")

if __name__ == "__main__":
  app.run(debug=True)


