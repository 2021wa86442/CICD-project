from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/kernel")
def kernel():
    version = subprocess.check_output(["uname", "-r"], text=True).strip()
    return render_template("kernel.html", version=version)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
