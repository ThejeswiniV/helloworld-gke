from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    target = os.environ.get('TARGET', 'World')
    return 'Hello World \n This is Thejeswini V'.format(target)
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
