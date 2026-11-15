from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>Controle de Estoque e Vendas</h1>
    <p>Bem-vindo ao sistema da mercearia!</p>
    <a href="/estoque">Consultar estoque</a>
    """

@app.route("/estoque")
def estoque():
    produtos = [
        {"nome": "Arroz", "preco": "R$ 25,00", "quantidade": 10},
        {"nome": "Feijão", "preco": "R$ 8,00", "quantidade": 5},
        {"nome": "Açúcar", "preco": "R$ 4,50", "quantidade": 2}
    ]

    linhas = ""
    for produto in produtos:
        linhas += f"""
        <tr>
            <td>{produto['nome']}</td>
            <td>{produto['preco']}</td>
            <td>{produto['quantidade']}</td>
        </tr>
        """

    return f"""
    <h1>Consulta de Estoque</h1>
    <table border="1" cellpadding="10">
        <tr>
            <th>Produto</th>
            <th>Preço</th>
            <th>Quantidade</th>
        </tr>
        {linhas}
    </table>
    <p><a href="/">Voltar ao início</a></p>
    """

if __name__ == "__main__":
    app.run(debug=True)
