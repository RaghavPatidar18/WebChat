from flask import Flask, render_template, request, jsonify
from ingest_data import ingest_data
from answer_question import answer_question

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ingest', methods=['POST'])
def ingest():
    data = request.json
    urls = data.get('urls', [])
    if not urls:
        return jsonify({'error': 'Please enter at least one valid URL.'}), 400
    
    result = ingest_data(urls)
    return jsonify({'message': result})

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    query = data.get('query', '')
    if not query:
        return jsonify({'error': 'Please enter a question.'}), 400
    
    response = answer_question(query)
    return jsonify({'answer': response})

if __name__ == '__main__':
    app.run(debug=True)
