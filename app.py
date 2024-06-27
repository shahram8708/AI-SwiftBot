from flask import Flask, request, jsonify, render_template
from transformers import pipeline, GPT2Tokenizer
import random

app = Flask(__name__)

tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-125M")
chatbot = pipeline("text-generation", model="EleutherAI/gpt-neo-125M", tokenizer=tokenizer, truncation=True, pad_token_id=tokenizer.eos_token_id)

previous_responses = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = get_bot_response(user_message)
    return jsonify({'reply': response})

def get_bot_response(message):
    global previous_responses
    if message in previous_responses:
        response = previous_responses[message]
    else:
        outputs = chatbot(message, max_length=100, pad_token_id=tokenizer.eos_token_id)
        generated_text = outputs[0]['generated_text']
        
        lines = generated_text.split('\n')
        unique_responses = []

        for line in lines:
            answer = line.strip()
            if answer:
                unique_responses.append(answer)

        if message in previous_responses.values():
            unique_responses = [resp for resp in unique_responses if resp != message]

        if unique_responses:
            response = random.choice(unique_responses)
        else:
            response = "I'm sorry, I didn't understand that."

        previous_responses[message] = response

    return response

if __name__ == '__main__':
    app.run(debug=True)
