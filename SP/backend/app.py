from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from datetime import datetime
from api.routes import api_blueprint

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(api_blueprint, url_prefix='/api')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)