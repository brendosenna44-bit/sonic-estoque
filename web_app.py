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
