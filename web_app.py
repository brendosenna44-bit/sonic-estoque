# SUBSTITUA APENAS O HTML DO PAINEL_HTML PELO ABAIXO

PAINEL_HTML = """
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
min-width:260px;
}

.container{
max-width:1300px;
margin:auto;
}

.topo{
background:#111827;
padding:25px;
border-radius:18px;
margin-bottom:20px;
display:flex;
justify-content:space-between;
align-items:center;
}

.card{
background:#111827;
padding:18px;
border-radius:18px;
margin-bottom:15px;
}

.grid{
display:grid;
grid-template-columns:1fr 1fr;
gap:10px;
}

.numero{
font-size:28px;
font-weight:bold;
margin-top:8px;
}

.form-linha{
display:flex;
gap:10px;
flex-wrap:wrap;
margin-bottom:15px;
}

input{
padding:10px;
border:none;
border-radius:10px;
font-size:15px;
}

.nome{
flex:2;
min-width:220px;
max-width:420px;
}

.qtd{
width:110px;
}

button{
padding:10px 16px;
border:none;
border-radius:10px;
cursor:pointer;
}

.azul{background:#2563eb;color:white;}
.vermelho{background:#dc2626;color:white;}
.verde{background:#16a34a;color:white;}

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

.barra{
height:12px;
background:#1e293b;
border-radius:20px;
overflow:hidden;
margin-top:8px;
}

.fill{
height:12px;
background:#2563eb;
}

@media(max-width:900px){
.layout{
flex-direction:column;
}
}
</style>
</head>

<body>
<div class="container">

<div class="topo">
<div>
<h1>🚀 SÔNIC PRIME</h1>
<p>Gestão Inteligente</p>
</div>

<a href="/logout" class="vermelho">Sair</a>
</div>

<div class="layout">

<div class="esquerda">

<form method="POST" action="/add">
<div class="form-linha">
<input class="nome" name="nome" placeholder="Nome do produto" required>
<input class="qtd" name="quantidade" type="number" placeholder="Qtd" required>
<button class="azul">+ Novo Produto</button>
</div>
</form>

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
<td><a href="/lixeira/{{p[0]}}" class="vermelho">Excluir</a></td>
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
<td><a href="/restaurar/{{l[0]}}" class="verde">Restaurar</a></td>
</tr>
{% endfor %}
</table>

</div>

<div class="direita">

<div class="card">
<h3>📊 Dashboard</h3>
</div>

<div class="grid">

<div class="card">
Produtos
<div class="numero">{{produtos|length}}</div>
</div>

<div class="card">
Lixeira
<div class="numero">{{lixo|length}}</div>
</div>

<div class="card">
Baixo
<div class="numero">
{{ produtos|selectattr(2,'lt',10)|list|length }}
</div>
</div>

<div class="card">
Total
<div class="numero">
{{ produtos|sum(attribute=2) }}
</div>
</div>

</div>

<div class="card">
<h4>📈 Estoque Geral</h4>
<div class="barra"><div class="fill" style="width:85%;"></div></div>
</div>

<div class="card">
<h4>📉 Produtos Baixos</h4>
<div class="barra"><div class="fill" style="width:35%;"></div></div>
</div>

</div>

</div>

</div>
</body>
</html>
"""
