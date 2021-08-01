from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
import amazon

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
    def generate():
        yield "<br/>"
        yield amazon.crawl(input, 1)
    return Response(generate(), mimetype="text/html")

if __name__ == "__main__":
    app.run()

