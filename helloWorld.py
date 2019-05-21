from flask import Flask
#import pdb
#pdb.set_trace()

app = Flask(__name__)
@app.route("/")

def helloWorld():
    return "Hello World!"

class mamiferos():

    def __init__(self, name, dono, acao):
        self.name = name
        self.dono = dono
        self.acao = acao
    
    @app.route("/dog")

    def latir():
        return '{}'.format(cachorro.acao)

cachorro = mamiferos('zeze', 'Vanessa', 'Au! Au! Au! Au! Au!')
#print(cachorro.latir())

#print('O nome do cachorro é:', cachorro.name, 'O dono(a) dele é:', cachorro.dono, 'Acao:', cachorro.latir())

app.run(debug=True)  