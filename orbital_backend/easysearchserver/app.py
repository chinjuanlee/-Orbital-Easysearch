from flask import Flask, request
from flask_cors import CORS, cross_origin
import ezbuy
import shopee
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def hello_world():
    return "hello world!"
    
@app.route('/<input>/ezbuy', methods=["GET", "POST"])
@cross_origin()
def ezbuy_server(input):
    ezbuy.api_call(input)
    return "ezbuy api call successful"

@app.route('/<input>/shopee', methods=["GET", "POST"])
@cross_origin()
def shopee_server(input):
    shopee.api_call(input)
    return "shopee api call successful"

if __name__ == "__main__":
    app.run()

