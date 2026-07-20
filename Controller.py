#serve para aplicar as funções de negócio, como regras, cálculos, etc.
from dao import *
from models import *
from datetime import datetime

class ControllerCategoria:
    def cadastrar_categoria(self, novacategoria : Categoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novacategoria.categoria:
                existe = True
                break
        if not existe:
            DaoCategoria.salvar(novacategoria)
            print(f"Categoria {novacategoria.categoria} cadastrada com sucesso!")
        else:
            print(f"Categoria {novacategoria.categoria} já existe!")

    def remover_categoria(self, categoria : Categoria):
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == categoria.categoria:
                x.remove(i)
                with open("categorias.txt", "w") as f:
                    for j in x:
                        f.write(f"{j.categoria}\n")
                print(f"Categoria {categoria.categoria} removida com sucesso!")
                return
        print(f"Categoria {categoria.categoria} não encontrada!")

    def alterar_categoria(self, categoria_antiga : Categoria, categoria_nova : Categoria):
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == categoria_antiga.categoria:
                i.categoria = categoria_nova.categoria
                if not categoria_nova.categoria:
                    print(f"Categoria {categoria_nova.categoria} não pode ser vazia!")
                    return
                if categoria_nova.categoria in [cat.categoria for cat in x if cat != i]:
                    print(f"Categoria {categoria_nova.categoria} já existe!")
                    return
                with open("categorias.txt", "w") as f:
                    for j in x:
                        f.write(f"{j.categoria}\n")
                print(f"Categoria {categoria_antiga.categoria} alterada para {categoria_nova.categoria} com sucesso!")
                return
        print(f"Categoria {categoria_antiga.categoria} não encontrada!")

    def mostrarCategoria(self):
        x = DaoCategoria.ler()
        for i in x:
            print(f"- {i.categoria}")

class ControllerEstoque:
    def cadastrarProduto(self, produto : Produtos, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(map(lambda x: x.categoria, y))
        if produto.categoria.categoria not in h:
            print(f"Categoria {produto.categoria.categoria} não cadastrada!")
            return
        estoque = Estoque(produto, quantidade)
        DaoEstoque.salvar(estoque)
        print(f"Produto {produto.nome} cadastrado com sucesso no estoque!")

    def removerProduto(self, produto : Produtos):
        x = DaoEstoque.ler()
        for i in x:
            if i.produto.nome == produto.nome:
                x.remove(i)
                with open("estoque.txt", "w") as f:
                    for j in x:
                        f.write(f"{j.produto.nome},{j.quantidade}\n")
                print(f"Produto {produto.nome} removido com sucesso do estoque!")
                return
        print(f"Produto {produto.nome} não encontrado no estoque!")
    
    def alterarProduto(self, produto_antigo : Produtos, produto_novo : Produtos, quantidade):
        x = DaoEstoque.ler()
        for i in x:
            if i.produto.nome == produto_antigo.nome:
                i.produto = produto_novo
                i.quantidade = quantidade
                with open("estoque.txt", "w") as f:
                    for j in x:
                        f.write(f"{j.produto.nome},{j.quantidade}\n")
                print(f"Produto {produto_antigo.nome} alterado para {produto_novo.nome} com sucesso no estoque!")
                return
        print(f"Produto {produto_antigo.nome} não encontrado no estoque!")

    def mostrarEstoque(self):
        x = DaoEstoque.ler()
        for i in x:
            print("====Produto====")
            print(f"- {i.produto.nome} ({i.quantidade} unidades)")

class ControllerVenda:
    def cadastrarVenda(self, venda : Venda):
        x = DaoEstoque.ler()
        for i in x:
            if i.produto.nome == venda.itensVendido.nome:
                if i.quantidade >= venda.quantidade:
                    i.quantidade -= venda.quantidade
                    DaoEstoque.salvar(i)
                    DaoVenda.salvar(venda)
                    print(f"Venda de {venda.quantidade} unidade(s) de {venda.itensVendido.nome} realizada com sucesso!")
                    return
                else:
                    print(f"Quantidade insuficiente em estoque para a venda de {venda.itensVendido.nome}!")
                    return
        print(f"Produto {venda.itensVendido.nome} não encontrado no estoque!")

    def relatorioProduto(self):
        vendas = DaoVenda.ler()
        relatorio = {}
        for venda in vendas:
            produto = venda.itensVendido
            if produto.nome not in relatorio:
                relatorio[produto.nome] = 0
            relatorio[produto.nome] += venda.quantidade
        return relatorio
    
    def mostrarVendas(self, relatorio=None):
        if relatorio is None:
            vendas = DaoVenda.ler()
        else:
            vendas = [venda for venda in DaoVenda.ler() if venda.itensVendido.nome in relatorio]
        for venda in vendas:
            dados = venda.split(",")
            venda = Venda(Produtos(dados[0], 0, None), dados[1], dados[2], int(dados[3]), datetime.strptime(dados[4], "%Y-%m-%d %H:%M:%S.%f"))
            print("====Venda====")
            print(f"- Produto: {venda.itensVendido.nome}")
            print(f"- Vendedor: {venda.vendedor}")
            print(f"- Comprador: {venda.comprador}")
            print(f"- Quantidade: {venda.quantidade}")
            print(f"- Data: {venda.data}")

class ControllerFornecedor:
    def cadastrarFornecedor(self, fornecedor : Fornecedor):
        x = DaoFornecedor.ler()
        for i in x:
            if i.cnpj == fornecedor.cnpj:
                print(f"Fornecedor {fornecedor.nome} já cadastrado!")
                return
        DaoFornecedor.salvar(fornecedor)
        print(f"Fornecedor {fornecedor.nome} cadastrado com sucesso!")

    def removerFornecedor(self, fornecedor : Fornecedor):
        x = DaoFornecedor.ler()
        for i in x:
            if i.cnpj == fornecedor.cnpj:
                x.remove(i)
                with open("fornecedores.txt", "w") as f:
                    for j in x:
                        f.write(f"{j.nome},{j.cnpj},{j.telefone},{j.categoria.categoria}\n")
                print(f"Fornecedor {fornecedor.nome} removido com sucesso!")
                return
        print(f"Fornecedor {fornecedor.nome} não encontrado!")

    def alterarFornecedor(self, fornecedor_antigo : Fornecedor, fornecedor_novo : Fornecedor):
        x = DaoFornecedor.ler()
        for i in x:
            if i.cnpj == fornecedor_antigo.cnpj:
                i.nome = fornecedor_novo.nome
                i.telefone = fornecedor_novo.telefone
                i.categoria = fornecedor_novo.categoria
                with open("fornecedores.txt", "w") as f:
                    for j in x:
                        f.write(f"{j.nome},{j.cnpj},{j.telefone},{j.categoria.categoria}\n")
                print(f"Fornecedor {fornecedor_antigo.nome} alterado para {fornecedor_novo.nome} com sucesso!")
                return
        print(f"Fornecedor {fornecedor_antigo.nome} não encontrado!")

class ControllerCliente:
    def cadastrarCliente(self, cliente : Pessoa):
        x = DaoPessoa.ler()
        for i in x:
            if i.cpf == cliente.cpf:
                print(f"Cliente {cliente.nome} já cadastrado!")
                return
        DaoPessoa.salvar(cliente)
        print(f"Cliente {cliente.nome} cadastrado com sucesso!")

    def removerCliente(self, cliente : Pessoa):
        x = DaoPessoa.ler()
        for i in x:
            if i.cpf == cliente.cpf:
                x.remove(i)
                with open("pessoas.txt", "w") as f:
                    for j in x:
                        f.write(f"{j.nome},{j.cpf},{j.telefone},{j.email},{j.endereco}\n")
                print(f"Cliente {cliente.nome} removido com sucesso!")
                return
        print(f"Cliente {cliente.nome} não encontrado!")

    def alterarCliente(self, cliente_antigo : Pessoa, cliente_novo : Pessoa):
        x = DaoPessoa.ler()
        for i in x:
            if i.cpf == cliente_antigo.cpf:
                i.nome = cliente_novo.nome
                i.telefone = cliente_novo.telefone
                i.email = cliente_novo.email
                i.endereco = cliente_novo.endereco
                with open("pessoas.txt", "w") as f:
                    for j in x:
                        f.write(f"{j.nome},{j.cpf},{j.telefone},{j.email},{j.endereco}\n")
                print(f"Cliente {cliente_antigo.nome} alterado para {cliente_novo.nome} com sucesso!")
                return
        print(f"Cliente {cliente_antigo.nome} não encontrado!")
a = ControllerVenda()
a.cadastrarVenda(Venda(Produtos("Celular", 1500.00, Categoria("Eletrônicos")), "João", "Maria", 1, datetime.now()))
a.mostrarVendas()
