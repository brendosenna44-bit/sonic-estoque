from flask import Flask, render_template_string, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "sonicprime123"

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

LOGIN_HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Login</title>
<style>
body{
font-family:Arial;
background:#2563eb;
display:flex;
justify-content:center;
align-items:center;
height:100vh;
margin:0;
}
.box{
background:white;
padding:30px;
border-radius:15px;
width:320px;
}
input{
width:100%;
padding:10px;
margin-bottom:10px;
box-sizing:border-box;
}
button{
width:100%;
padding:10px;
background:#2563eb;
color:white;
border:none;
cursor:pointer;
}
.erro{
background:#fecaca;
padding:10px;
margin-bottom:10px;
}
</style>
</head>
<body>
<div class="box">
<h2>SÔNIC PRIME</h2>
<p>Gestão Inteligente</p>

{% if erro %}
<div class="erro">Login inválido</div>
{% endif %}

<form method="POST">
<input name="usuario" placeholder="Usuário">
<input name="senha" type="password" placeholder="Senha">
<button>Entrar</button>
</form>
</div>
</body>
</html>
"""

PAINEL_HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Painel</title>
<style>
body{
font-family:Arial;
background:#0f172a;
color:white;
margin:0;
padding:20px;
}
.topo{
display:flex;
justify-content:space-between;
align-items:center;
background:#111827;
padding:20px;
border-radius:15px;
margin-bottom:20px;
}
a{
color:white;
text-decoration:none;
background:#dc2626;
padding:8px 12px;
border-radius:8px;
}
.form{
display:flex;
gap:10px;
flex-wrap:wrap;
margin-bottom:20px;
}
input{
padding:10px;
border:none;
border-radius:8px;
}
.nome{width:280px;}
.qtd{width:100px;}
button{
padding:10px 14px;
background:#2563eb;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}
.layout{
display:flex;
gap:20px;
flex-wrap:wrap;
}
.esquerda{
flex:3;
min-width:320px;
}
.direita{
flex:1;
min-width:250px;
}
.card{
background:#111827;
padding:15px;
border-radius:15px;
margin-bottom:15px;
}
table{
width:100%;
border-collapse:collapse;
background:#111827;
border-radius:15px;
overflow:hidden;
}
th,td{
padding:12px;
border-bottom:1px solid #1e293b;
text-align:left;
}
.baixo{
color:yellow;
}
.verde{
background:#16a34a;
padding:6px 10px;
border-radius:8px;
}
@media(max-width:900px){
.layout{flex-direction:column;}
}
</style>
</head>
<body>

<div class="topo">
<div>
<h2>SÔNIC PRIME</h2>
<p>Gestão Inteligente</p>
</div>
<a href="/logout">Sair</a>
</div>

<div class="layout">

<div class="esquerda">

<form class="form" method="POST" action="/add">
<input class="nome" name="nome" placeholder="Nome do produto" required>
<input class="qtd" type="number" name="quantidade" placeholder="Qtd" required>
<button>+ Novo Produto</button>
</form>

<h3>Produtos</h3>

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
<span class="baixo">Baixo</span>
{% else %}
Normal
{% endif %}
</td>
<td><a href="/lixeira/{{p[0]}}">Excluir</a></td>
</tr>
{% endfor %}
</table>

<br>

<h3>Lixeira</h3>

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
<td><a class="verde" href="/restaurar/{{l[0]}}">Restaurar</a></td>
</tr>
{% endfor %}
</table>

</div>

<div class="direita">

<div class="card">
<h3>Dashboard</h3>
<p>Produtos: {{produtos|length}}</p>
<p>Lixeira: {{lixo|length}}</p>
</div>

<div class="card">
<p>Total Estoque</p>
<h2>{{ total }}</h2>
</div>

</div>

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if session.get("logado"):
        return redirect("/painel")

    erro = False

    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario == "admin" and senha == "1234":
            session["logado"] = True
            return redirect("/painel")
        else:
            erro = True

    return render_template_string(LOGIN_HTML, erro=erro)

@app.route("/painel")
def painel():
    if not session.get("logado"):
        return redirect("/")

    cursor.execute("SELECT * FROM produtos WHERE ativo=1")
    produtos = cursor.fetchall()

    cursor.execute("SELECT * FROM produtos WHERE ativo=0")
    lixo = cursor.fetchall()

    total = sum([p[2] for p in produtos]) if produtos else 0

    return render_template_string(
        PAINEL_HTML,
        produtos=produtos,
        lixo=lixo,
        total=total
    )

@app.route("/add", methods=["POST"])
def add():
    if not session.get("logado"):
        return redirect("/")

    nome = request.form["nome"]
    quantidade = int(request.form["quantidade"])

    cursor.execute(
        "INSERT INTO produtos (nome, quantidade) VALUES (?,?)",
        (nome, quantidade)
    )
    conn.commit()

    return redirect("/painel")

@app.route("/lixeira/<int:id>")
def lixeira(id):
    cursor.execute("UPDATE produtos SET ativo=0 WHERE id=?", (id,))
    conn.commit()
    return redirect("/painel")

@app.route("/restaurar/<int:id>")
def restaurar(id):
    cursor.execute("UPDATE produtos SET ativo=1 WHERE id=?", (id,))
    conn.commit()
    return redirect("/painel")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
