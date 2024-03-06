# To check this api use postman And Read readme.md file for better understanding


from flask import Flask, request, jsonify
from twilio.rest import Client

app = Flask(__name__)

# Twilio API credentials
# Get your own credential from ( https://console.twilio.com/ )
account_sid = ''
auth_token = ''
twilio_number = ''

# Initialize Twilio client
client = Client(account_sid, auth_token)

@app.route('/send_verification_code', methods=['POST'])
def send_verification_code():
    # Parse recipient's phone number from request body
    number = request.form.get('number') 
    print(number)

    if not number:
        return jsonify({'error': 'Recipient number is required'}), 400
    
    # Ensure phone number is in E.164 format
    if not number.startswith('+'):
        number = '+92' + number  # Assuming Pakistan country code is +92

    # Generate verification code (you can generate it dynamically if needed)
    verification_code = '123456'

    try:
        # Send SMS with verification code
        message = client.messages.create(
            body=f'Your verification code is: {verification_code}',
            from_=twilio_number,
            to=number
        )
        print(message.body)


        return jsonify({'message': 'Verification code sent successfully', 'verification_code': verification_code}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
