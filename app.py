from flask import Flask, render_template

app= Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/sobre.html')
def sobre():
    return render_template('sobre.html')    


@app.route('/contato.html')
def contato():
    return render_template('contato.html')  
    

@app.route('/projeto.html')
def projeto():
    return render_template('projeto.html') 