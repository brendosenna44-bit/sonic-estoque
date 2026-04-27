from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# =========================
# BANCO SIMPLES EM MEMÓRIA
# =========================
produtos = []

# =========================
# HTML COMPLETO
# =========================
HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Sistema de Estoque</title>
    <style>
        body {
            font-family: Arial;
            background: #f5f5f5;
            margin: 0;
            padding: 0;
        }
        header {
            background: #2c3e50;
            color: white;
            padding: 15px;
            text-align: center;
        }
        .container {
            padding: 20px;
        }
        input {
            padding: 8px;
            margin: 5px;
        }
        button {
            padding: 8px 12px;
            cursor: pointer;
        }
        table {
            width: 100%;
            margin-top: 20px;
            border-collapse: collapse;
            background: white;
        }
        th, td {
            padding: 10px;
            border: 1px solid #ddd;
            text-align: center;
        }
        th {
            background: #eee;
        }
    </style>
</head>
<body>

<header>
    <h1>Sistema de Estoque</h1>
</header>

<div class="container">

    <h2>Cadastrar Produto</h2>

    <form method="POST" action="/add">
        <input type="text" name="nome" placeholder="Nome do produto" required>
        <input type="text" name="codigo" placeholder="Código" required>
        <input type="number" name="quantidade" placeholder="Quantidade" required>
        <button type="submit">Cadastrar</button>
    </form>

    <h2>Lista de Produtos</h2>

    <table>
        <tr>
            <th>Nome</th>
            <th>Código</th>
            <th>Quantidade</th>
        </tr>

        {% for p in produtos %}
        <tr>
            <td>{{ p.nome }}</td>
            <td>{{ p.codigo }}</td>
            <td>{{ p.quantidade }}</td>
        </tr>
        {% endfor %}
    </table>

</div>

</body>
</html>
"""

# =========================
# ROTAS
# =========================
@app.route("/")
def index():
    return HTML.replace("{% for p in produtos %}", "").replace("{% endfor %}", "").replace("{{ p.nome }}", "").replace("{{ p.codigo }}", "").replace("{{ p.quantidade }}", "")

@app.route("/add", methods=["POST"])
def add():
    nome = request.form["nome"]
    codigo = request.form["codigo"]
    quantidade = request.form["quantidade"]

    produtos.append({
        "nome": nome,
        "codigo": codigo,
        "quantidade": quantidade
    })

    return redirect(url_for("index"))

# =========================
# EXECUÇÃO LOCAL
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
