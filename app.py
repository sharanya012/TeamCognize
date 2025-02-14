from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {}  # Dummy storage for now

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email in users and users[email] == password:
            return redirect(url_for("home"))
        else:
            return "Invalid credentials"
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        users[email] = password
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/claim", methods=["GET", "POST"])
def claim():
    if request.method == "POST":
        return "Claim submitted!"
    return render_template("claim.html")

if __name__ == "__main__":
    app.run(debug=True)
