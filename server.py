from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def sayhello():
    return render_template("challenge.html")

if __name__ == "__main__":
    app.run(debug=True)
