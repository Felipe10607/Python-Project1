#criar as classes do modelo de dados, como usuário, produto, pedido, etc.
from datetime import datetime
class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

class Produtos:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto : Produtos, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Venda:
    def __init__(self,itensVendido : Produtos, vendedor, comprador,quantidadeVendida,data = datetime.now()):
        self.itensVendido = itensVendido
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidade = quantidadeVendida
        self.data = data
        
class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria

class Pessoa:
    def __init__(self, nome, cpf, telefone, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, telefone, email, endereco, cargo, salario, clt):
        super().__init__(nome, cpf, telefone, email, endereco)
        self.cargo = cargo
        self.salario = salario
        self.clt = clt

