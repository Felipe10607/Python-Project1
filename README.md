Projeto desenvolvido em Python com o objetivo de aplicar os conceitos de Programação Orientada a Objetos (POO) e a arquitetura MVC (Model - View - Controller) na prática.

A aplicação simula um sistema de gerenciamento de loja, permitindo organizar funcionalidades como cadastro de categorias, produtos, estoque e vendas. O foco principal do projeto foi praticar separação de responsabilidades entre as camadas do sistema e melhorar a organização do código. 
## Objetivo

Este projeto foi criado como exercício prático para consolidar conhecimentos em:

- Programação Orientada a Objetos.
- Organização de código com arquitetura MVC.
- Manipulação de arquivos `.txt` para persistência de dados.
- Estruturação de regras de negócio em um sistema simples de loja.

## Estrutura do projeto

A arquitetura MVC foi utilizada para separar melhor as responsabilidades do sistema:

- **Model**: representa as entidades do sistema, como Produto, Categoria, Estoque e Venda.
- **Controller**: concentra as regras de negócio, validações e fluxo das operações.
- **View**: responsável pela interação com o usuário, exibindo informações e resultados.

Essa separação ajudou a deixar o projeto mais organizado, embora durante o desenvolvimento tenha ficado claro que o planejamento inicial da estrutura é essencial para evitar retrabalho. 
## Funcionalidades

- Cadastro de categorias.
- Cadastro de produtos.
- Controle de estoque.
- Registro de vendas.
- Geração de relatórios simples de produtos vendidos.
- Leitura e gravação de dados em arquivos `.txt`.

## Aprendizados

Durante o desenvolvimento, percebi que aplicar MVC na prática exige mais planejamento do que parece no início. Em vários momentos foi necessário voltar à estrutura do projeto para adicionar novas funções, ajustar responsabilidades entre classes e melhorar a organização geral do código.

Um dos principais aprendizados foi entender que, antes de começar a programar, vale a pena definir melhor o escopo do sistema, as entidades envolvidas e o papel de cada camada da arquitetura. Isso reduz erros, retrabalho e facilita a manutenção do projeto.

## Melhorias futuras

Algumas melhorias que podem ser adicionadas nas próximas versões:

- Implementar um sistema de logs para registrar chamadas de funções e facilitar a depuração.
- Melhorar a persistência dos dados, substituindo arquivos `.txt` por uma solução mais estruturada.
- Criar uma interface mais amigável para interação com o usuário.
- Adicionar tratamento de exceções em mais pontos do sistema.
- Reorganizar partes do código para deixá-lo mais modular e escalável.

## Ideia de melhoria com logs

Uma melhoria interessante para o projeto é adicionar um arquivo de log para registrar as operações realizadas pelo sistema. O módulo `logging` da biblioteca padrão do Python permite gravar mensagens em arquivo com nível, horário e codificação configuráveis. 
Isso me ajudaria a acompanhar chamadas de funções, identificar o fluxo de execução e entender com mais clareza de onde os erros estão vindo, especialmente em trechos com funções encadeadas.
