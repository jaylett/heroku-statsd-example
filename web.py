import statsd
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    counter = statsd.Counter("Homepage hits")
    counter += 1
    return "Hello World!"

if __name__ == "__main__":
    app.run()
