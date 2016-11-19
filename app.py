# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
import markovify
import random

app = Flask(__name__)

@app.route('/chat', methods=["GET"])
def index():

    userSpeech = request.args.get('user').encode('utf-8')

    newSpeech = ""

    with open('raw.txt') as f:
      rawText = f.read()

    model = markovify.Text(rawText, state_size=1)

    for i in range(1):
      newSpeech += " " + model.make_short_sentence(140)

    return jsonify({
      "content": newSpeech
    })

if __name__ == "__main__":
    app.run(debug=True)
