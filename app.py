from flask import Flask
from flask import render_template
from flask import request
#import pandas as pd


app = Flask(__name__)

@app.route('/')
def base(contador = 1):
    return render_template("base.html", contador=contador)

@app.route('/base', methods = ['GET','POST'])
def reinicio_base(contador = 1):
    if request.method == 'POST':
        return render_template("base.html", contador=contador)

@app.route('/index', methods = ['GET','POST'])
def index():    
    if request.method == 'POST':
        contadorII = request.form.get('my_output')
        contadorII = int(contadorII) + 1
        
        lista=[]
        if (contadorII+1) < 6:
            for item in range(1,contadorII+1):
                lista.append(item)
        else:
            for item in range(contadorII-4,contadorII+1):
                lista.append(item)

        # df = pd.DataFrame(lista,columns=['turno'])
        # print(df)
        return render_template("index.html", contador=contadorII, lista=lista)


if __name__=='__main__':
    app.run(debug=True, port=8000)
