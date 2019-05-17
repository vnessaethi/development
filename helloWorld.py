from flask import Flask

app = Flask(__name__)
@app.route("/")

def helloWorld():
    return "Hello World!"

class mamiferos():
    def __init__(self, name, dono):
        self.name = name
        self.dono = dono
    
    def latir(self):
        print('{0} está latindo: Au! Au! Au! Au! Au!'.format(self.name))

zeze = mamiferos('zeze', 'Vanessa')

print('O nome do cachorro é:', zeze.name, 'O dono(a) dele é:', zeze.dono)

zeze.latir()

app.run()   