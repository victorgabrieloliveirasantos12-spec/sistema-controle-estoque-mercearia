from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template_string("""
        <h1>Controle de Estoque e Vendas</h1>
        <p>Bem-vindo ao sistema da mercearia!</p>
    """)

if __name__ == "__main__":
    app.run()
