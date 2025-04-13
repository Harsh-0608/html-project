from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'ZeroWaste Backend is running!'

# Donor submission route
@app.route('/submit-donor', methods=['POST'])
def submit_donor():
    name = request.form.get('name')
    email = request.form.get('email')
    food_type = request.form.get('foodType')
    location = request.form.get('location')
    quantity = request.form.get('quantity')
    description = request.form.get('description')
    pickup_deadline = request.form.get('pickupDeadline')

    print("🚚 Donor Data Received:")
    print(f"Name: {name}, Email: {email}, Food: {food_type}, Location: {location}, Quantity: {quantity}, Description: {description}, Deadline: {pickup_deadline}")

    return jsonify({'message': 'Donor data received successfully'}), 200

# Receiver submission route
@app.route('/submit-receiver', methods=['POST'])
def submit_receiver():
    name = request.form.get('name')
    email = request.form.get('email')
    food_type = request.form.get('foodType')
    location = request.form.get('location')
    distance = request.form.get('distance')
    pickup_time = request.form.get('pickupTime')

    print("🤝 Receiver Data Received:")
    print(f"Name: {name}, Email: {email}, Food: {food_type}, Location: {location}, Distance: {distance}, Time: {pickup_time}")

    return jsonify({'message': 'Receiver data received successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
