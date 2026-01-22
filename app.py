from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return f'''
    <html>
        <head><title>Simple Docker App</title></head>
        <body>
            <h1>Hello from Docker Ubuntu!</h1>
            <p>Container ID: {os.uname().nodename}</p>
            <p>Current directory: {os.getcwd()}</p>
            <p>Files in directory: {', '.join(os.listdir())}</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
