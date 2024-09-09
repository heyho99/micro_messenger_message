#09091644

# message_service.py
from flask import Flask, request, jsonify
from flask_cors import CORS  # CORSをインポート

app = Flask(__name__)
CORS(app)  # CORSを有効にする

# インメモリデータベース（メッセージ用）
messages_db = []

@app.route('/messages', methods=['POST'])
def send_message():
    data = request.json
    sender_id = data.get('sender_id')
    receiver_id = data.get('receiver_id')
    content = data.get('content')
    
    if not sender_id or not receiver_id or not content:
        return jsonify({'error': '送信者ID、受信者ID、またはコンテンツが不足しています'}), 400
    
    message = {
        'sender_id': sender_id,
        'receiver_id': receiver_id,
        'content': content
    }
    messages_db.append(message)
    return jsonify({'message': 'メッセージが正常に送信されました'}), 201

@app.route('/messages/<user_id>', methods=['GET'])
def get_messages(user_id):
    user_messages = [msg for msg in messages_db if msg['receiver_id'] == user_id]
    return jsonify(user_messages), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
