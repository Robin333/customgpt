import pickle
from flask import Flask, jsonify, request

app = Flask(__name__)

# Load the vectorized data
with open('vectorized_data.pkl', 'rb') as file:
    vectorized_data = pickle.load(file)

@app.route('/use-vectorized-data', methods=['POST'])
def use_vectorized_data():
    # You can process the vectorized_data here as needed
    # For example, you might want to format it into a prompt for the Custom GPT model

    # Example: Get additional context from the request, if necessary
    context = request.json.get('context', '')

    prompt = f"This is the vectorized data: {vectorized_data}\nWith the context: {context}\nPlease provide insights:"

    # Use the prompt with your Custom GPT model here
    # ...

    return jsonify({"prompt": prompt})

if __name__ == '__main__':
    app.run()
