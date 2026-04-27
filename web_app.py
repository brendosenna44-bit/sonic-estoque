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
# SUBSTITUA apenas o botão antigo por este:

<button class="botao" onclick="abrirModal()">+ Novo Produto</button>


# COLE antes de </body>:

<div id="modal" style="display:none; position:fixed; inset:0; background:rgba(0,0,0,.45); padding:20px;">
  <div style="max-width:500px; margin:50px auto; background:white; padding:25px; border-radius:18px;">
    
    <h2 style="margin-bottom:15px;">Cadastrar Produto</h2>

    <input id="nome" placeholder="Nome do produto" style="width:100%; padding:12px; margin-bottom:10px;">
    
    <input id="quantidade" placeholder="Quantidade" type="number" style="width:100%; padding:12px; margin-bottom:10px;">
    
    <input id="preco" placeholder="Preço" type="number" step="0.01" style="width:100%; padding:12px; margin-bottom:10px;">
    
    <input id="categoria" placeholder="Categoria" style="width:100%; padding:12px; margin-bottom:15px;">

    <button class="botao" onclick="salvarProduto()">Salvar</button>
    <button class="botao" onclick="fecharModal()" style="background:#777;">Fechar</button>

  </div>
</div>

<script>
function abrirModal(){
 document.getElementById("modal").style.display="block";
}

function fecharModal(){
 document.getElementById("modal").style.display="none";
}

function salvarProduto(){
 alert("Produto salvo com sucesso!");
 fecharModal();
}
</script>
