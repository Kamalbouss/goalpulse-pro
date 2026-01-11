from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate_video():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        
        return jsonify({
            'success': True,
            'message': response.text
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
