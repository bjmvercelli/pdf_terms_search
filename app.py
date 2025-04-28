from flask import Flask, request, render_template, jsonify
import pdfplumber
import os
import re

app = Flask(__name__)

# Store extracted terms in memory (in a real app, consider using a database)
medical_terms = []

def extract_medical_terms(pdf_path):
    terms = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            # Look for patterns like "CODE - TERM" or similar medical term patterns
            # This pattern matching should be adjusted based on your specific PDF format
            matches = re.finditer(r'(\d+(?:\.\d+)*)\s*[-–]\s*([^\n]+)', text)
            for match in matches:
                code = match.group(1)
                term = match.group(2).strip()
                terms.append({
                    'code': code,
                    'term': term
                })
    return terms

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    global medical_terms
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and file.filename.endswith('.pdf'):
        # Save temporarily
        temp_path = 'temp.pdf'
        file.save(temp_path)
        try:
            medical_terms = extract_medical_terms(temp_path)
            os.remove(temp_path)  # Clean up
            return jsonify({'message': f'Processed {len(medical_terms)} terms'})
        except Exception as e:
            if os.path.exists(temp_path):
                os.remove(temp_path)
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    if not query:
        return jsonify([])
    
    results = [
        term for term in medical_terms
        if query in term['code'].lower() or query in term['term'].lower()
    ]
    return jsonify(results)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 