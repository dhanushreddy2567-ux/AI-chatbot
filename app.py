from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app) 

# Put your working Google API key here
genai.configure(api_key="AIzaSyBtGNJ9401GWIaTS2BQsT2-cI96TKMC3cM")

# Using the universal free-tier fallback model!
model = genai.GenerativeModel('gemini-flash-latest') 

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_input = data.get('message', '')
    
    system_instruction = "You are 'UniHelp Bot', a friendly, official helpdesk chatbot for gitam university. Answer concisely and clearly."
    
    try:
        response = model.generate_content(
            system_instruction + "\nUser: " + user_input,
        )
        bot_reply = response.text
        
    except Exception as e:
        print(f"Error: {e}")
        bot_reply = "I'm having a little trouble connecting to the network. Please try again!"

    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    print("🚀 Backend is running on http://127.0.0.1:5001")
    app.run(debug=True, port=5001)