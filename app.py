from flask import Flask, jsonify, render_template, g
import scripts.env as env
import os

# globals
app = Flask("Flask-Env")


# index
@app.route("/")
def index():
    return 'Hello World. Your private key is [{}]'.format(os.environ['PRIVATE_KEY'])


if __name__ == '__main__':
    # load vars from .env file, for dev purposes only
    env.load() 
    app.run(debug=True)