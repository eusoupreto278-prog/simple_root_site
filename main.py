from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Documentacao')
def docs():
    return render_template('docs.html')

if __name__ == '__main__':
    app.run()