from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SÔNIC PRIME</title>

<style>
:root{
    --bg:#f5f7fa;
    --card:#ffffff;
    --text:#111827;
    --sub:#6b7280;
    --line:#e5e7eb;
    --primary:#2563eb;
}

@media (prefers-color-scheme: dark){
:root{
    --bg:#0f172a;
    --card:#111827;
    --text:#f9fafb;
    --sub:#9ca3af;
    --line:#1f2937;
    --primary:#3b82f6;
}
}

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Arial, Helvetica, sans-serif;
}

body{
background:var(--bg);
color:var(--text);
padding:20px;
}

.container{
max-width:1100px;
margin:auto;
}

.topo{
background:var(--card);
padding:25px;
border-radius:18px;
box-shadow:0 10px 25px rgba(0,0,0,.08);
margin-bottom:20px;
}

.topo h1{
font-size:32px;
margin-bottom:6px;
}

.topo p{
color:var(--sub);
}

.grid{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:20px;
}

.card{
background:var(--card);
padding:20px;
border-radius:18px;
box-shadow:0 10px 25px rgba(0,0,0,.06);
}

.card h3{
font-size:15px;
color:var(--sub);
margin-bottom:8px;
}

.numero{
font-size:30px;
font-weight:bold;
}

.tabela{
background:var(--card);
padding:20px;
border-radius:18px;
box-shadow:0 10px 25px rgba(0,0,0,.06);
overflow:auto;
}

table{
width:100%;
border-collapse:collapse;
}

th,td{
padding:14px;
text-align:left;
border-bottom:1px solid var(--line);
}

th{
color:var(--sub);
font-size:14px;
}

.botao{
background:var(--primary);
color:white;
padding:12px 18px;
border:none;
border-radius:10px;
cursor:pointer;
margin-top:15px;
}

.botao:hover{
opacity:.9;
}
</style>
</head>

<body>
<div class="container">

<div class="topo">
<h1>🚀 SÔNIC PRIME</h1>
<p>Gestão Inteligente</p>
<button class="botao">+ Novo Produto</button>
</div>

<div class="grid">

<div class="card">
<h3>Total Produtos</h3>
<div class="numero">38</div>
</div>

<div class="card">
<h3>Itens em Estoque</h3>
<div class="numero">524</div>
</div>

<div class="card">
<h3>Entradas Hoje</h3>
<div class="numero">12</div>
</div>

<div class="card">
<h3>Saídas Hoje</h3>
<div class="numero">7</div>
</div>

</div>

<div class="tabela">
<table>
<thead>
<tr>
<th>Produto</th>
<th>Quantidade</th>
<th>Status</th>
</tr>
</thead>

<tbody>
<tr>
<td>Teclado USB</td>
<td>42</td>
<td>Normal</td>
</tr>

<tr>
<td>Mouse Gamer</td>
<td>18</td>
<td>Baixo</td>
</tr>

<tr>
<td>Monitor 24"</td>
<td>9</td>
<td>Crítico</td>
</tr>

<tr>
<td>Cadeira Office</td>
<td>31</td>
<td>Normal</td>
</tr>
</tbody>
</table>
</div>

</div>
</body>
</html>
"""

@app.route("/")
def inicio():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
