from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

@app.route('/')
def index():
    name = "Gabriel"
    return{"name": name}

@app.route('/health')
def health():
    return{"status": "healthy"}

# Load the sentiment analysis model once when the app starts
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    # Get the text from the request
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    text = data['text']
    
    # Run sentiment analysis
    result = sentiment_analyzer(text)[0]
    
    return jsonify({
        
        'text': text,
        'sentiment': result['label'],
        'confidence': result['score']
    })

if __name__ == '__main__':
    app.run(debug=True)