import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Entregua Laboratório DevOps - FIAP 8ASO Grupo 08 <br/> Lucca Ecclissi - RM342996<br/> Magno Melo - RM343228<br/> JT Fernandes - RM343281 "

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)