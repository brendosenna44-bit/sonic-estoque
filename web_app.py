from flask import Flask, render_template_string, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# ===== BANCO =====
conn = sqlite3.connect("estoque.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    quantidade INTEGER
)
""")
conn.commit()

# ===== HTML (INTERFACE MOBILE) =====
HTML = """
<!DOCTYPE html>
<html>
<head>
<title>SÔNIC 1.0</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body { font-family: Arial; background:#121212; color:white; text-align:center; }
.container { width:90%; margin:auto; }
input { padding:10px; margin:5px; width:90%; border-radius:5px; border:none; }
button { padding:10px; width:95%; margin:5px; border:none; border-radius:5px; }
.green { background:#00c853; }
.red { background:#d50000; color:white; }
.blue { background:#2962ff; color:white; }
table { width:100%; margin-top:20px; }
th, td { padding:8px; border-bottom:1px solid #444; }
</style>
</head>
<body>

<div class="container">
<h2>🚀 SÔNIC 1.0</h2>

<form method="POST" action="/add">
<input name="nome" placeholder="Produto">
<input name="qtd" placeholder="Quantidade">
<button class="green">Cadastrar</button>
</form>

<form method="POST" action="/entrada">
<input name="nome" placeholder="Produto">
<input name="qtd" placeholder="Entrada">
<button class="blue">Entrada</button>
</form>

<form method="POST" action="/saida">
<input name="nome" placeholder="Produto">
<input name="qtd" placeholder="Saída">
<button class="red">Saída</button>
</form>

<h3>Estoque</h3>
<table>
<tr><th>Nome</th><th>Qtd</th></tr>
{% for p in produtos %}
<tr><td>{{p[0]}}</td><td>{{p[1]}}</td></tr>
{% endfor %}
</table>

</div>

</body>
</html>
"""

# ===== ROTAS =====
@app.route("/")
def index():
    cursor.execute("SELECT nome, quantidade FROM produtos")
    produtos = cursor.fetchall()
    return render_template_string(HTML, produtos=produtos)

@app.route("/add", methods=["POST"])
def add():
    nome = request.form["nome"]
    qtd = int(request.form["qtd"])

    cursor.execute("INSERT INTO produtos (nome, quantidade) VALUES (?,?)", (nome, qtd))
    conn.commit()
    return redirect("/")

@app.route("/entrada", methods=["POST"])
def entrada():
    nome = request.form["nome"]
    qtd = int(request.form["qtd"])

    cursor.execute("UPDATE produtos SET quantidade = quantidade + ? WHERE nome=?", (qtd, nome))
    conn.commit()
    return redirect("/")

@app.route("/saida", methods=["POST"])
def saida():
    nome = request.form["nome"]
    qtd = int(request.form["qtd"])

    cursor.execute("UPDATE produtos SET quantidade = quantidade - ? WHERE nome=?", (qtd, nome))
    conn.commit()
    return redirect("/")

# ===== START =====
app.run(host="0.0.0.0", port=5000, debug=True)
