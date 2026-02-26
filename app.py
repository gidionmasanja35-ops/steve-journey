from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.message import EmailMessage
import mysql.connector   

app = Flask(__name__)
CORS(app)

# Email setup
EMAIL = "gidionmasanja35@gmail.com"
PASSWORD = "rkyweyhdeqlezijn"

db_config = {
    "host": "localhost",   
    "user": "root",          
    "password": "", 
    "database": "bookingdb"     
}

# Home route
@app.route("/")
def home():
    return "Backend is working ✅"

# Booking / message route
@app.route("/send", methods=["POST"])
def send():

    data = request.json

    name = data["name"]
    email = data["email"]
    phone = data["phone"]
    package = data["package"]
    date = data["date"]
    people = data["people"]
    message = data["message"]

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO bookings (name, email, phone, package, date, people, message)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (name, email, phone, package, date, people, message))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as db_error:
        return jsonify({"status": "error", "msg": f"Database error: {db_error}"})

    # Send email notification
    msg = EmailMessage()
    msg["Subject"] = "New Tour Booking / Message"
    msg["From"] = EMAIL
    msg["To"] = EMAIL
    msg.set_content(f"""
NEW WEBSITE MESSAGE

Name: {name}
Email: {email}
Phone: {phone}

Package: {package}
Date: {date}
People: {people}

Message:
{message}
""")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)

        return jsonify({"status": "ok", "msg": "Booking saved and email sent!"})

    except Exception as e:
        return jsonify({"status": "error", "msg": f"Email error: {str(e)}"})


if __name__ == "__main__":
    app.run(debug=True)
