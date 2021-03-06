from flask import Flask, render_template, url_for, request, jsonify, redirect
from pathlib import Path

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
