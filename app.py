from flask import Flask, redirect, url_for, request, render_template
from deep_translator import GoogleTranslator
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    languages_data = json.load(open("./data/languages.json"))
    return render_template("index.html", languages=languages_data)


@app.route("/", methods=["POST"])
def index_post():
    try:
        original_text = request.form["text"]
        target_language = request.form["target_language"]
        source_language = request.form["source_language"]

        if not original_text or not target_language:
            return redirect(url_for("index"))

        translation = GoogleTranslator(
            source=source_language, target=target_language
        ).translate(text=original_text)

        print(translation)

        return render_template(
            "results.html", translated_text=translation, original_text=original_text
        )

    except:
        return redirect(url_for("index"))