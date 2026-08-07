# Gerenciador De Estoque
---
## Explicação sobre o meu projeto

Nesse projeto tem dois arquivos logica_produtos.py e interfase.py, na logica_produtos.py ela é cabeçado
projeto, onde tem cadastro de produtos, remover produto, lista de produto já cadastrado. Nisso eu
fiz esse arquivo com base nos meus estudos e com os meus conhecimentos, já a interfase.py eu fiz com
ajuda do chatgpt, queria algo visual e simples onde eu poderia aprender.

## Oque o meu projeto faz?

No gerenciador de projetos, ele já vem com três produtos cadastrado inicialmente sendo camisa, blusa e
calsa, onde ele fica em uma tabela com os nomes preço e quantidade de produto desejado.
No Gerenciador de Estoque pode cadastrar o nome do Produto, preço e a quantidade, e a função de remover produto.


## Tela do Projeto

<p align="center">
    <img src="./assets/tela-inicial-560.png"
         alt="Tela Inicial do Gerenciador de Estoque">
</p>

## Cadastro de Produto

<p align="center">
    <img src="./assets/cadastro-produto-620.png"
         alt="Tela de Cadastro de Produtos">
</p>

<p align="center">
    <em>Tela responsável pelo cadastro de novos produtos.</em>
</p>

## Explicação

Na imagem acima, é a parte de cadastro de produtos, onde vc digita o nome do produto, preço e
quantidade.
Como eu fiz pra adicionar o produto? na parte do nome tem uma variavel que recebe o nome digitado,
a mesma coisa com preço e quantidade, essas variavel eu coloco em um dicionario novo e adiciono na
lista, para adicionar um novo produto.

## Remover produto

<p align="center">
    <img src="./assets/remover.png"
         alt="Tela de Remoção de Produtos"
         width="650">
</p>

<p align="center">
    <em>Tela utilizada para remover produtos cadastrados.</em>
</p>

## Explicação

Para eu conseguir remover produto, eu criei uma função que dentro dela eu uso o for para selecionar 1 produto dentro da lista. Quando selecionado, eu crio um if e quando o produto for escolhido pelo usario vai ser excluido dentro do if. 
