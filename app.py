from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Controle de Estoque e Vendas</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: white;
                color: #222;
                padding: 20px;
            }
            .alto-contraste {
                background: black;
                color: yellow;
            }
            a, button {
                padding: 10px;
                margin: 5px;
                cursor: pointer;
            }
            .alto-contraste a {
                color: yellow;
            }
        </style>
    </head>
    <body>
        <h1>Controle de Estoque e Vendas</h1>
        <p>Bem-vindo ao sistema da mercearia!</p>
        <a href="/estoque">Consultar estoque</a>
        <button onclick="document.body.classList.toggle('alto-contraste')">
            Ativar/desativar alto contraste
        </button>
    </body>
    </html>
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
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Consulta de Estoque</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: white;
                color: #222;
                padding: 20px;
            }}
            .alto-contraste {{
                background: black;
                color: yellow;
            }}
            table {{
                border-collapse: collapse;
            }}
            th, td {{
                border: 1px solid currentColor;
                padding: 10px;
            }}
            button, a {{
                padding: 10px;
                margin: 5px;
                cursor: pointer;
            }}
            .alto-contraste a {{
                color: yellow;
            }}
        </style>
    </head>
    <body>
        <h1>Consulta de Estoque</h1>
        <button onclick="document.body.classList.toggle('alto-contraste')">
            Ativar/desativar alto contraste
        </button>
        <table>
            <tr>
                <th>Produto</th>
                <th>Preço</th>
                <th>Quantidade</th>
            </tr>
            {linhas}
        </table>
        <p><a href="/">Voltar ao início</a></p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
