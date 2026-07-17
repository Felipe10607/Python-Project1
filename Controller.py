
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

a = ControllerCategoria()
a.alterar_categoria(Categoria("Frutas"), Categoria("Verduras"))
