from flask import Flask, request

from api.gpt_response import get_chatgpt_reply, revoke_chats

from dotenv import load_dotenv

load_dotenv('.env')

app = Flask(__name__)


@app.route('/get-reply/', methods=['POST'])
def return_chatgpt_reply():
    query = request.json['query']
    return {'query': query, 'reply': get_chatgpt_reply(content=query)}


@app.route('/revoke-chats/', methods=['PATCH'])
def return_revoke_reply():
    revoke_chats()
    return {'revoked': True}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
