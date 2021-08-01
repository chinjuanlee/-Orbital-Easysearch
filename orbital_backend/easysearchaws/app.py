from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
import amazon
import qoo10
import shopee
import ezbuy

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def hello_world():
    return "hello world!"

@app.route('/<input>/amazon', methods=["GET", "POST"])
@cross_origin()
def amazon_server(input):
    return amazon.crawl(input)

@app.route('/<input>/qoo10', methods=["GET", "POST"])
@cross_origin()
def qoo10_server(input):
    return qoo10.crawl(input)

@app.route('/<input>/shopee', methods=["GET", "POST"])
@cross_origin()
def shopee_server(input):
    return shopee.api_call(input)

@app.route('/<input>/ezbuy', methods=["GET", "POST"])
@cross_origin()
def ezbuy_server(input):
    return ezbuy.api_call(input)

if __name__ == "__main__":
    app.run()

