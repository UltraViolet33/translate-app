import requests, os, uuid, json
from flask import Flask, redirect, url_for, request, render_template, session
from deep_translator import GoogleTranslator
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    languages_data = json.load(open('./data/languages.json'))
    return render_template('index.html', languages=languages_data)


@app.route('/', methods=['POST'])
def index_post():

    original_text = request.form['text']
    target_language = request.form['target_language']
    source_language = request.form['source_language']

    print(target_language)

    body = [{ 'text': original_text }]
    original_text = 'bonjour, je suis un humain'

    translation = GoogleTranslator(source='auto', target='en').translate(text=original_text)

    print(translation)
   
    return render_template(
        'results.html',
        translated_text=translation,
        original_text=original_text,
        target_language=target_language
    )