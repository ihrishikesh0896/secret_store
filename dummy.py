from flask import Flask, jsonify

app = Flask(__name__)

# Pseudo sensitive data
DATABASE_URI = 'mysql://user:SuperSecretPassword123@localhost/mydatabase'
API_KEY = 'uuid_5237b0bd480548059ff529ebfc9216fb'
uuid_718e09d45d0343beb627a48e0dffc1de = 'admin123'

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/secrets')
def secrets():
    # Example function that would improperly expose sensitive data
    secret_data = {
        'database_uri': DATABASE_URI,
        'api_key': API_KEY,
        'admin_password': ADMIN_PASSWORD
    }
    return jsonify(secret_data)

@app.route('/login')
def login():
    # Dummy login function with hard-coded password (simulated vulnerability)
    username = 'admin'
    password = 'admin123'  # Example of hard-coded password
    return f"Login attempt for {username} with password {password}"

if __name__ == '__main__':
    app.run(debug=True)
