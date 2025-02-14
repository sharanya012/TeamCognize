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
    return render_template('claim.html')

@app.route('/submit_claim', methods=['POST'])
def submit_claim():
    car_make = request.form['make']
    car_model = request.form['model']
    car_year = request.form['year']
    reg_number = request.form['reg_number']
    owner = request.form['owner']
    damage_desc = request.form['damage_desc']
    damage_photo = request.files['damage_photo']

    # Save the uploaded file (for now, not processing it)
    damage_photo.save(f"static/uploads/{damage_photo.filename}")

    return "Claim Submitted Successfully!"

if __name__ == '__main__':
    app.run(debug=True)
