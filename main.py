from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from GoalPulse! 🚀"

@app.route('/api/health')
def health():
    return {"status": "ok"}, 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 10000))  # Render يستخدم 10000 وليس 5000!
    app.run(host='0.0.0.0', port=port, debug=False)
