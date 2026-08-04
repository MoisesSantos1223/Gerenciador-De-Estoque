import tkinter as tk
import logica_produtos as logica

produtos = []

def cadastro_produtos_tekinter():
    nome = campo_nome.get()
    preco = campo_preco.get()
    quantidade = campo_quantidade.get()

    logica.cadastrar_produto(
        logica.produtos,
        nome,
        preco,
        quantidade
    )

    mensagem.config(text="Produto cadastrado com sucesso!")

    campo_nome.delete(0, tk.END)
    campo_preco.delete(0, tk.END)
    campo_quantidade.delete(0, tk.END)

    print(logica.produtos)

def remover_produt_tekinter():
    nome_remover = campo_remover.get()
    removido = logica.remover_produto(
        logica.produtos,
        nome_remover
    )

    if removido == True:
        mensagem.config(text="Produto removido com sucesso!")
    else:
        mensagem.config(text="Produto não encontrado!")

        campo_remover.delete(0, tk.END)

    print(logica.produtos)
    
def atualizar_tabela():
    for linha in tabela_produto.get_children():
        tabela_produto.delete(linha)

        for produto in logica.produtos:
            tabela_produto.insert(
                "",
                "end",
                values=(
                    produto["nome"]
                    produto["preco"]
                    produto["quantidade"]
                )
            )

janela = tk.Tk()

janela.title("Cadastro de Produtos")
janela.geometry("600x400")


#Tabela
titulo = tk.Label(janela, text="Cadastro de Produto")
titulo.pack()
#titulo nome
texto_nome = tk.Label(janela, text="Nome do produto: ")
texto_nome.pack()
#barra nome
campo_nome = tk.Entry(janela)
campo_nome.pack()

#Preço
preco_produto = tk.Label(janela, text="Digite o preço do produto: ")
preco_produto.pack()

campo_preco = tk.Entry(janela)
campo_preco.pack()

#Quantidade
quantidade_produto = tk.Label(
    janela,
    text="Digite a quantidade do produto: "
)
quantidade_produto.pack()

campo_quantidade = tk.Entry(janela)
campo_quantidade.pack()

#Botão cadastrar

botao_cadastrar = tk.Button(
    janela,
    text="cadastrar produto",
    command=cadastro_produtos_tekinter
)

botao_cadastrar.pack()

mensagem = tk.Label(janela, text="")
mensagem.pack()

#remover produto
remover_prudto = tk.Label(
    janela,
    text="Nome do produto que deseja remover:"
)
remover_prudto.pack()

campo_remover = tk.Entry(janela)
campo_remover.pack()


#botão para remover 

botão_remover = tk.Button(
    janela,
    text="Remover Produto",
    command=remover_produt_tekinter 
)
botão_remover.pack()



janela.mainloop()