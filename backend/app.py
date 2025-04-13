from flask import Flask, render_template
from donor_api import donor_form_submission
from backend.receiver_api import receiver_form_submission

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Donor form route
@app.route('/donor', methods=['GET', 'POST'])
def donor_form():
    return donor_form_submission()

# Receiver form route
@app.route('/receiver', methods=['GET', 'POST'])
def receiver_form():
    return receiver_form_submission()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
