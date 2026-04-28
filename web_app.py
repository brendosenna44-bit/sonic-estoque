from flask import Flask, render_template_string, request, redirect
import sqlite3

app = Flask(__name__)

# BANCO
conn = sqlite3.connect("estoque.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    quantidade INTEGER,
    ativo INTEGER DEFAULT 1
)
""")
conn.commit()

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SÔNIC PRIME</title>

<style>
body{
font-family:Arial;
background:#0f172a;
color:white;
padding:20px;
margin:0;
}

.container{
max-width:1100px;
margin:auto;
}

.topo{
background:#111827;
padding:25px;
border-radius:18px;
margin-bottom:20px;
}

h1{margin:0;}
p{color:#94a3b8;}

input{
padding:12px;
width:100%;
margin-bottom:10px;
border:none;
border-radius:10px;
}

button{
padding:12px;
border:none;
border-radius:10px;
cursor:pointer;
}

.azul{background:#2563eb;color:white;}
.vermelho{background:#dc2626;color:white;}
.verde{background:#16a34a;color:white;}
.cinza{background:#475569;color:white;}

table{
width:100%;
border-collapse:collapse;
background:#111827;
border-radius:18px;
overflow:hidden;
}

th,td{
padding:14px;
border-bottom:1px solid #1e293b;
text-align:left;
}

.alerta{
color:#facc15;
font-weight:bold;
}

a{
text-decoration:none;
color:white;
padding:8px 12px;
border-radius:8px;
}
</style>
</head>

<body>
<div class="container">

<div class="topo">
<h1>🚀 SÔNIC PRIME</h1>
<p>Gestão Inteligente</p>
</div>

<form method="POST" action="/add">
<input name="nome" placeholder="Nome do produto" required>
<input name="quantidade" type="number" placeholder="Quantidade" required>
<button class="azul">+ Novo Produto</button>
</form>

<br>

<h2>📦 Produtos</h2>

<table>
<tr>
<th>Nome</th>
<th>Qtd</th>
<th>Status</th>
<th>Ação</th>
</tr>

{% for p in produtos %}
<tr>
<td>{{p[1]}}</td>
<td>{{p[2]}}</td>

<td>
{% if p[2] < 10 %}
<span class="alerta">Baixo</span>
{% else %}
Normal
{% endif %}
</td>

<td>
<a href="/lixeira/{{p[0]}}" class="vermelho">Excluir</a>
</td>
</tr>
{% endfor %}
</table>

<br><br>

<h2>🗑️ Lixeira</h2>

<table>
<tr>
<th>Nome</th>
<th>Qtd</th>
<th>Ação</th>
</tr>

{% for l in lixo %}
<tr>
<td>{{l[1]}}</td>
<td>{{l[2]}}</td>
<td>
<a href="/restaurar/{{l[0]}}" class="verde">Restaurar</a>
</td>
</tr>
{% endfor %}
</table>

</div>
</body>
</html>
"""

@app.route("/")
def inicio():
    cursor.execute("SELECT * FROM produtos WHERE ativo=1")
    produtos = cursor.fetchall()

    cursor.execute("SELECT * FROM produtos WHERE ativo=0")
    lixo = cursor.fetchall()

    return render_template_string(HTML, produtos=produtos, lixo=lixo)

@app.route("/add", methods=["POST"])
def add():
    nome = request.form["nome"]
    quantidade = int(request.form["quantidade"])

    cursor.execute(
        "INSERT INTO produtos (nome, quantidade) VALUES (?,?)",
        (nome, quantidade)
    )
    conn.commit()

    return redirect("/")

@app.route("/lixeira/<int:id>")
def lixeira(id):
    cursor.execute("UPDATE produtos SET ativo=0 WHERE id=?", (id,))
    conn.commit()
    return redirect("/")

@app.route("/restaurar/<int:id>")
def restaurar(id):
    cursor.execute("UPDATE produtos SET ativo=1 WHERE id=?", (id,))
    conn.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
