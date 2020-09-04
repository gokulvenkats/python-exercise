from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<username>')
def hello(username=None):
    nameofusr = username or "World"
    return f"Hello {nameofusr}!"

if __name__ == '__main__':
    app.run()