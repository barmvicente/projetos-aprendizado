from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<border>")
def index(border):
    return render_template("index.html", border_radius=border)

if __name__ == '__main__':
    app.run(debug=True)
