from flask import Flask, jsonify, request #Importando servidor, conversor para json e acessar os dados vindo e indo das nossas requisições
app01 = Flask(__name__) #atribuindo a uma varável o servidor
livros = [
    {
        'id': 1,
        'Nome': 'Hamlet',
        'Autor': 'William Shakespeare'
    },
    {
        'id':2,
        'Nome': 'A Odisseia',
        'Autor':'Homero'
    },
    {
        'id':3,
        'Nome': 'A revolução dos bichos',
        'Autor':'George Orwell'
    }
]
#Consultar livros:
@app01.route('/livros',methods=['GET']) #methods para aceitar somente o metodo get(de busca)
def consultar ():
    return jsonify(livros)

#Consultar ID:
@app01.route('/livros/<int:id>', methods=['GET']) #Definindo uma rota de consulta para ID do livro
def id_livros(id): #definindo uma função onde será pesquisado id de um livro
    for livro in livros: #percore a lista de livros
        if livro.get('id') == id: #Verificando se o id do livro é igual ao id pasado como parametro
            return jsonify(livro.get('Nome')) #caso o iD seja igual, retorna o nome do livro
            
#Editando um livro:
@app01.route('/livros/<int:id>', methods=['PUT']) #Adicionando uma rota e especificando que terá um metodo put que permite alteração
def livro_editado_via_id(id):
    livro_modificado =  request.get_json() #armazenando a informação alterada do usurario em uma variavel
    for indice,livro in enumerate(livros): #percorrendo o livro e id
        if livro.get('id')==id: # Se o id do livro percorrido por igual a id buscado
            livros[indice].update(livro_modificado) #Faça uma alteração nesse livro com a iformação passada pelo usuario
            return jsonify(livros[indice]) #Retorne para o usuario o livro modificado

#Criar um livro:
@app01.route('/livros', methods = ['POST']) # Adicionando rota com metodo que permite adicionar algo
def novo_livro(): #Criando função que permite criar e adicionar um livro
    livro_novo = request.get_json() #armazenando na variável a informação sobre o livro a ser criado
    livros.append(livro_novo) #Adicionando novo livro a lista de livros
    return jsonify(livros) #Retornando lista de livros

#Excluir livro:
@app01.route('/livros/<int:id>', methods = ['DELETE']) #Adicionando rota com metodo para deleta um livro
def excluir_livro(id): #Criando uma função que permite excluir um livro da lista
    for indice, livro in enumerate(livros): 
        if livro.get('id') == id: 
            del livro[indice] 
            return jsonify(livros) 

       




app01.run(port=5000,host='localhost', debug=True)