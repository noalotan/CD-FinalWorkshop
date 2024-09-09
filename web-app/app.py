from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head><title>Welcome to My Web Page</title></head>
    <body>
        <h1>Hello, World!</h1>
        <p>Welcome to my simple web page served using Flask.</p>
    </body>
    </html>
    '''

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory('.', filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

