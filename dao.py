#serve para o acesso dos arquivos de dados, como banco de dados, arquivos, etc.
#basicamente aqui se trata das funções que tratam diretamente nos arquivos tangendo em ler e salvar.
from models import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria : Categoria):
        with open("categorias.txt", "a") as f:
            f.write(f"{categoria.categoria}\n")

    @classmethod
    def ler(cls):
        with open("categorias.txt", "r") as f:
            cls.categoria = f.readlines()
        cls.categoria =  list(map(lambda x: x.replace("\n", ""), cls.categoria))
        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))
        return cat
    
class DaoVenda:
    @classmethod
    def salvar(cls, venda : Venda):
        with open("vendas.txt", "a") as f:
            f.write(f"{venda.itensVendido.nome},{venda.vendedor},{venda.comprador},{venda.quantidade},{venda.data}\n")

    @classmethod
    def ler(cls):
        with open("vendas.txt", "r") as f:
            cls.venda = f.readlines()
        #o lambda é utilizado para substituirmos a quebra de linha.
        cls.venda =  list(map(lambda x: x.replace("\n", ""), cls.venda))
        print(cls.venda)

Eletronico = Categoria("Eletrônicos")
celular = Produtos("Celular", 1500.00, Eletronico)
minha_venda = Venda(celular, "João", "Maria", 1)

DaoVenda.salvar(minha_venda)
vendas_salvas = DaoVenda.ler()
print(vendas_salvas)

class DaoEstoque:
    @classmethod
    def salvar(cls, estoque : Estoque):
        with open("estoque.txt", "a") as f:
            f.write(f"{estoque.produto.nome},{estoque.quantidade}\n")

    @classmethod
    def ler(cls):
        with open("estoque.txt", "r") as f:
            cls.estoque = f.readlines()
        cls.estoque = list(map(lambda x: x.replace("\n", ""), cls.estoque))
        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                produto, quantidade = i.split(",")
                est.append(Estoque(Produtos(produto, 0, None), int(quantidade)))
        return est
    
class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor : Fornecedor):
        with open("fornecedores.txt", "a") as f:
            f.write(f"{fornecedor.nome},{fornecedor.cnpj},{fornecedor.telefone},{fornecedor.categoria.categoria}\n")

    @classmethod
    def ler(cls):
        with open("fornecedores.txt", "r") as f:
            cls.fornecedor = f.readlines()
        cls.fornecedor = list(map(lambda x: x.replace("\n", ""), cls.fornecedor))
        forn = []
        if len(cls.fornecedor) > 0:
            for i in cls.fornecedor:
                nome, cnpj, telefone, categoria = i.split(",")
                forn.append(Fornecedor(nome, cnpj, telefone, Categoria(categoria)))
        return forn
