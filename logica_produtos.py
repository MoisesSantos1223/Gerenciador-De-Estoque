def cadastro_Produtos_iniciais():
   
    produto1 = {
        "nome": "Camisa",
        "preco": 20,
        "quantidade": 3
    }
    produto2 = {
        "nome": "Blusa",
        "preco": 50,
        "quantidade": 1
    }
    produto3 = {
        "nome": "Calsa",
        "preco": 30,
        "quantidade": 1
    }

    lista = [produto1, produto2, produto3]
    
    return lista

produtos = cadastro_Produtos_iniciais()

def listar_produtos(produtos):
    
    for produto in produtos:
        print(f"Nome: {produto['nome']}")
        print(f"Preço: {produto['preco']}")
        print(f"Quantidade: {produto['quantidade']}")

def cadastrar_produto(produtos,nome, preco, quantidade):
    
    print("Digite apenas números!")
   
    produto4 = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    
    produtos.append(produto4)

def remover_produto(produtos, nome_remover):
    for produto in produtos:
        if produto["nome"].strip().lower() == nome_remover.strip().lower():
            produtos.remove(produto)
            return True
    return False
     
#Essa é a parte do menu, onde vai rodar no terminal
'''''
def menu(produtos):
     print("MENU ")
     print("="*50)

     
     print("Escolha umas das opções abaixo")
     print("1| lista de produtos:")
     print("2| Cadastrar produto")
     print("3| Remover produto")
     print("4| buscar produto")
     print("5| Sair do sistema")
     print("="*100)
    
     
     while True:
         print("="*50)
         menu_escolha = int(input("Escolha um números da opção acima: "))

         if menu_escolha == 1:
             listar_produtos(produtos)
             continue
         elif menu_escolha == 2:
             cadastrar_produto(produtos)
             continue
         elif menu_escolha == 3:
             remover_produto(produtos)
             continue
         elif menu_escolha == 4:
             buscar_produto(produtos)
             continue
         elif menu_escolha == 5:
             print("Você saiu do sistema....")
             break
         else:
             print("Algo de errado \nTente novamente mais tarde")

menu(produtos)

 '''