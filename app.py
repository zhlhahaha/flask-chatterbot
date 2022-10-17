from flask import Flask, request
from flask_cors import CORS
from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
CORS(app)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
#trainer = ChatterBotCorpusTrainer(english_bot)
#trainer.train("chatterbot.corpus.english")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))

@app.route("/version")
def return_version():
    return "version1"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
