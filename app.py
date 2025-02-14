from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/claim')
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
