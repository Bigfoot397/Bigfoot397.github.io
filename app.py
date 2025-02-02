pip install flask openai
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Your OpenAI API key (keep it secret)
openai.api_key = "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"  # Replace with your actual API key

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    user_message = data.get("message")
    
    # Call OpenAI API with user message
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Or use "gpt-4" if you have access
            prompt=user_message,
            max_tokens=150
        )
        gpt_reply = response.choices[0].text.strip()
        return jsonify({'reply': gpt_reply})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
