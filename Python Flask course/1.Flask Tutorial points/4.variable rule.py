from flask import Flask
app = Flask(__name__)
@app.route("/flask")
def Hello():
    return "hello Flask"
@app.route("/python/")
def python():
    return "hello Python"

if __name__ == "__main__":
    app.run(debug=True)