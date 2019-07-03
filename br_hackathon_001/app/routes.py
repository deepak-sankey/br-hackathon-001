# routes.py

from flask import render_template
from flask import request, jsonify

from app import app
from app.utils.strings import getTopCharacters

# Views:
@app.route('/')
def index():
    return render_template("200.html")

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")


# APIs:
@app.route('/getLogoChars', methods=['POST'])
def getLogoChars():
    companyId = request.form['companyId']
    responseData = getTopCharacters(companyId,3)
    return responseData


