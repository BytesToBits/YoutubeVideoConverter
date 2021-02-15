from flask import Flask, render_template, request

from ytConvert import YTSource

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html', data=None)
    else:
        data = YTSource(request.form['url']).convert(request.form['type'])
        return render_template('index.html', data=data)

@app.route("/terms-of-use/")
def tos():
    return render_template('termsofuse.html')

@app.route("/privacy/")
def privacy():
    return render_template('privacy.html')

@app.route("/copyright/")
def copyright():
    return render_template('copyright.html')

if __name__ == "__main__":
    app.run(debug=True)