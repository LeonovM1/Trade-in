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


@app.route('/catalog')
def catalog():
  return render_template("catalog.html")


@app.route('/Audi_r8')
def Audi_r8():
  return render_template("auto/Audi_r8.html")


@app.route('/Audi_s8')
def Audi_s8():
  return render_template("auto/Audi_s8.html")


@app.route('/Bmw_i8')
def Bmw_i8():
  return render_template("auto/Bmw_i8.html")


@app.route('/Bmw_m5')
def Bmw_m5():
  return render_template("auto/Bmw_m5.html")


@app.route('/Moskvich')
def Moskvich():
  return render_template("auto/Moskvich.html")


@app.route('/tesla')
def tesla():
  return render_template("auto/tesla.html")


@app.route('/urls')
def urls():
  return render_template("url's.html")


@app.route('/FAQs')
def FAQs():
  return render_template("FAQs.html")


@app.route('/login')
def login():
  return render_template("login.html")


@app.route("/registration")
def registration():
  return render_template("registration.html")

if __name__ == "__main__":
  app.run(debug=True)


