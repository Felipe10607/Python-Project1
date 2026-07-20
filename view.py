#parte de interface com o usuário, como telas, menus, botões, etc.
import Controller
import os.path

if __name__ == "__main__":
    while True:
        local = input("Digite o local de cadastro (categoria, estoque, venda, fornecedor) ou 'sair' para encerrar: ")
        if local == "sair":
            break
        if local == "categoria":
            while True:
                acao = input("Digite a ação desejada (cadastrar, remover, alterar, mostrar) ou 'voltar' para voltar: ")
                if acao == "voltar":
                    break
                if acao == "cadastrar":
                    nome_categoria = input("Digite o nome da categoria: ")
                    categoria = Controller.Categoria(nome_categoria)
                    Controller.ControllerCategoria().cadastrar_categoria(categoria)
                elif acao == "remover":
                    nome_categoria = input("Digite o nome da categoria: ")
                    categoria = Controller.Categoria(nome_categoria)
                    Controller.ControllerCategoria().remover_categoria(categoria)
                elif acao == "alterar":
                    nome_categoria_antiga = input("Digite o nome da categoria antiga: ")
                    nome_categoria_nova = input("Digite o nome da categoria nova: ")
                    categoria_antiga = Controller.Categoria(nome_categoria_antiga)
                    categoria_nova = Controller.Categoria(nome_categoria_nova)
                    Controller.ControllerCategoria().alterar_categoria(categoria_antiga, categoria_nova)
                elif acao == "mostrar":
                    Controller.ControllerCategoria().mostrarCategoria()
                else:
                    print("Ação inválida!")
        if local == "estoque":
            while True:
                acao = input("Digite a ação desejada (cadastrar, remover, alterar, mostrar) ou 'voltar' para voltar: ")
                if acao == "voltar":
                    break
                if acao == "cadastrar":
                    nome_produto = input("Digite o nome do produto: ")
                    preco_produto = float(input("Digite o preço do produto: "))
                    categoria_produto = input("Digite a categoria do produto: ")
                    quantidade_produto = int(input("Digite a quantidade do produto: "))
                    categoria = Controller.Categoria(categoria_produto)
                    produto = Controller.Produtos(nome_produto, preco_produto, categoria)
                    Controller.ControllerEstoque().cadastrarProduto(produto, quantidade_produto)
                elif acao == "remover":
                    nome_produto = input("Digite o nome do produto: ")
                    Controller.ControllerEstoque().removerProduto(nome_produto)
                elif acao == "alterar":
                    nome_produto_antigo = input("Digite o nome do produto antigo: ")
                    nome_produto_novo = input("Digite o nome do produto novo: ")
                    preco_produto_novo = float(input("Digite o preço do produto novo: "))
                    categoria_produto_novo = input("Digite a categoria do produto novo: ")
                    quantidade_produto_novo = int(input("Digite a quantidade do produto novo: "))
                    categoria_nova = Controller.Categoria(categoria_produto_novo)
                    produto_novo = Controller.Produtos(nome_produto_novo, preco_produto_novo, categoria_nova)
                    Controller.ControllerEstoque().alterarProduto(nome_produto_antigo, produto_novo, quantidade_produto_novo)
                elif acao == "mostrar":
                    Controller.ControllerEstoque().mostrarEstoque()
                else:
                    print("Ação inválida!")
        if local == "venda":
            while True:
                acao = input("Digite a ação desejada (cadastrar, mostrar) ou 'voltar' para voltar: ")
                if acao == "voltar":
                    break
                if acao == "cadastrar":
                    nome_produto = input("Digite o nome do produto: ")
                    vendedor = input("Digite o nome do vendedor: ")
                    comprador = input("Digite o nome do comprador: ")
                    quantidade_vendida = int(input("Digite a quantidade vendida: "))
                    Controller.ControllerVenda().cadastrarVenda(nome_produto, vendedor, comprador, quantidade_vendida)
                elif acao == "mostrar":
                    Controller.ControllerVenda().mostrarVendas()
                else:
                    print("Ação inválida!")
        if local == "fornecedor":
            while True:
                acao = input("Digite a ação desejada (cadastrar, remover, alterar, mostrar) ou 'voltar' para voltar: ")
                if acao == "voltar":
                    break
                if acao == "cadastrar":
                    nome_fornecedor = input("Digite o nome do fornecedor: ")
                    cnpj_fornecedor = input("Digite o CNPJ do fornecedor: ")
                    telefone_fornecedor = input("Digite o telefone do fornecedor: ")
                    categoria_fornecedor = input("Digite a categoria do fornecedor: ")
                    categoria = Controller.Categoria(categoria_fornecedor)
                    fornecedor = Controller.Fornecedor(nome_fornecedor, cnpj_fornecedor, telefone_fornecedor, categoria)
                    Controller.ControllerFornecedor().cadastrarFornecedor(fornecedor)
                elif acao == "remover":
                    nome_fornecedor = input("Digite o nome do fornecedor: ")
                    Controller.ControllerFornecedor().removerFornecedor(nome_fornecedor)
                elif acao == "alterar":
                    nome_fornecedor_antigo = input("Digite o nome do fornecedor antigo: ")
                    nome_fornecedor_novo = input("Digite o nome do fornecedor novo: ")
                    cnpj_fornecedor_novo = input("Digite o CNPJ do fornecedor novo: ")
                    telefone_fornecedor_novo = input("Digite o telefone do fornecedor novo: ")
                    categoria_fornecedor_novo = input("Digite a categoria do fornecedor novo: ")
                    categoria_nova = Controller.Categoria(categoria_fornecedor_novo)
                    fornecedor_novo = Controller.Fornecedor(nome_fornecedor_novo, cnpj_fornecedor_novo, telefone_fornecedor_novo, categoria_nova)
                    Controller.ControllerFornecedor().alterarFornecedor(nome_fornecedor_antigo, fornecedor_novo)
                elif acao == "mostrar":
                    Controller.ControllerFornecedor().mostrarFornecedores()
                else:
                    print("Ação inválida!")
            if local not in ["categoria", "estoque", "venda", "fornecedor"]:
                print("Local inválido!")
            if not os.path.exists("vendas.txt"):
                with open("vendas.txt", "w") as f:
                    pass
