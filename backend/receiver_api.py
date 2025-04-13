from flask import Flask, request, redirect, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/submit-receiver', methods=['POST'])
def submit_receiver():
    name = request.form.get('name')
    email = request.form.get('email')
    food_type = request.form.get('foodType')
    location = request.form.get('location')
    distance = request.form.get('distance')
    pickup_time = request.form.get('pickupTime')

    # Print the received data for debugging purposes
    print("🤝 Receiver Data Received:")
    print(f"Name: {name}, Email: {email}, Food: {food_type}, Location: {location}, Distance: {distance}, Time: {pickup_time}")
    
    # After successful data processing, render the success page
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)