from flask import Flask, request, jsonify
import pickle
from document_processing import extract_text, preprocess_text
from health_guidance_comparison import compare_health_parameters
from openai_integration import generate_gpt_report

app = Flask(__name__)

# Load the vectorized health guidance information
with open('vectorized_data.pkl', 'rb') as file:
    health_guidance_data = pickle.load(file)

@app.route('/upload-and-compare', methods=['POST'])
def upload_and_compare():
    # Get the uploaded file
    uploaded_file = request.files.get('file')
    
    if not uploaded_file:
        return jsonify({"error": "No file uploaded."}), 400
    
    # Extract and preprocess text from the uploaded file
    document_text = extract_text(uploaded_file)
    preprocessed_text = preprocess_text(document_text)
    
    # Compare the document against health guidance parameters
    comparison_results = compare_health_parameters(preprocessed_text, health_guidance_data)
    
    # Use Custom GPT to generate a report based on comparison
    gpt_prompt = "Here are the comparison results for the uploaded diabetes patient support document: \n" + \
                 f"{comparison_results}\n" + \
                 "Please summarize the findings and suggest any necessary actions based on the health guidance parameters."
                 
    gpt_report = generate_gpt_report(gpt_prompt)
    
    return jsonify({"report": gpt_report})

if __name__ == '__main__':
    app.run()
