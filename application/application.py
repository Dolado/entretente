from flask import Flask, render_template
app = Flask(__name__)


tool_pages = []

@app.route("/")
def index():
    return render_template("index.html", num_tools=len(tool_pages))

@app.route("/p/<string:tool>/")
def test_slug(tool):
    return "Esto... {}".format(tool)
