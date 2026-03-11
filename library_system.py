# Classe para representar um livro
class Livro:
    def __init__(self, titulo, autor, ano_publicacao, num_copias):
        self.titulo = titulo  # Título do livro
        self.autor = autor  # Autor do livro
        self.ano_publicacao = ano_publicacao  # Ano de publicação do livro
        self.num_copias = num_copias  # Número de cópias disponíveis do livro

# Classe para representar um usuário
class Usuario:
    def __init__(self, nome, id, contato):
        self.nome = nome  # Nome do usuário
        self.id = id  # ID do usuário
        self.contato = contato  # Contato do usuário
        self.livros_emprestados = []  # Lista de livros emprestados pelo usuário

# Classe para representar a biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = []  # Lista de livros na biblioteca
        self.usuarios = []  # Lista de usuários da biblioteca

    # Método para cadastrar um livro na biblioteca
    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    # Método para cadastrar um usuário na biblioteca
    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    # Método para verificar a disponibilidade de um livro
    def verificar_disponibilidade(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.num_copias > 0:
                    return f"Livro disponível. Quantidade: {livro.num_copias}"
                else:
                    return "Livro indisponível."
        return "Livro não encontrado."

    # Método para emprestar um livro a um usuário
    def emprestar_livro(self, id_usuario, titulo):
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                for livro in self.livros:
                    if livro.titulo == titulo and livro.num_copias > 0:
                        livro.num_copias -= 1
                        usuario.livros_emprestados.append(livro)
                        return "Empréstimo realizado com sucesso!"
                return "Livro não disponível para empréstimo."
        return "Usuário não encontrado."

    # Método para devolver um livro
    def devolver_livro(self, id_usuario, titulo):
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                for livro in usuario.livros_emprestados:
                    if livro.titulo == titulo:
                        livro.num_copias += 1
                        usuario.livros_emprestados.remove(livro)
                        return "Devolução realizada com sucesso!"
                return "Livro não encontrado na lista de empréstimos do usuário."
        return "Usuário não encontrado."

    # Método para consultar um livro por título, autor ou ano de publicação
    def consultar_livro(self, consulta, tipo):
        resultados = []
        for livro in self.livros:
            if tipo == 'titulo' and livro.titulo == consulta:
                resultados.append(livro)
            elif tipo == 'autor' and livro.autor == consulta:
                resultados.append(livro)
            elif tipo == 'ano_publicacao' and livro.ano_publicacao == consulta:
                resultados.append(livro)
        return resultados if resultados else "Nenhum livro encontrado."

    # Método para gerar um relatório da biblioteca
    def gerar_relatorio(self):
        relatorio = "Relatório da Biblioteca:\n"
        relatorio += "\nLivros:\n"
        for livro in self.livros:
            relatorio += f'Título: {livro.titulo}, Autor: {livro.autor}, Ano de Publicação: {livro.ano_publicacao}, Número de cópias: {livro.num_copias}\n'
        relatorio += "\nUsuários:\n"
        for usuario in self.usuarios:
            relatorio += f'Nome: {usuario.nome}, ID: {usuario.id}, Contato: {usuario.contato}, Livros emprestados: {[livro.titulo for livro in usuario.livros_emprestados]}\n'
        return relatorio

# Função para exibir o menu de opções ao usuário
def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n1. Cadastrar Livro")
        print("2. Cadastrar Usuário")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Consultar Livro")
        print("6. Gerar Relatório")
        print("7. Sair")
        opcao = input("\nEscolha uma opção: ")
        if opcao == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano_publicacao = input("Digite o ano de publicação do livro: ")
            num_copias = int(input("Digite o número de cópias do livro: "))
            livro = Livro(titulo, autor, ano_publicacao, num_copias)
            biblioteca.cadastrar_livro(livro)
        elif opcao == '2':
            nome = input("Digite o nome do usuário: ")
            id = input("Digite o ID do usuário: ")
            contato = input("Digite o contato do usuário: ")
            usuario = Usuario(nome, id, contato)
            biblioteca.cadastrar_usuario(usuario)
        elif opcao == '3':
            print("\n1. Verificar Disponibilidade")
            print("2. Realizar Empréstimo")
            sub_opcao = input("\nEscolha uma opção: ")
            id_usuario = input("Digite o ID do usuário: ")
            titulo = input("Digite o título do livro: ")
            if sub_opcao == '1':
                print(biblioteca.verificar_disponibilidade(titulo))
            elif sub_opcao == '2':
                print(biblioteca.emprestar_livro(id_usuario, titulo))
            else:
                print("Opção inválida. Por favor, tente novamente.")
                continue
        elif opcao == '4':
            id_usuario = input("Digite o ID do usuário: ")
            titulo = input("Digite o título do livro: ")
            print(biblioteca.devolver_livro(id_usuario, titulo))
        elif opcao == '5':
            print("\n1. Consultar por Título")
            print("2. Consultar por Autor")
            print("3. Consultar por Ano de Publicação")
            tipo_consulta = input("\nEscolha uma opção: ")
            consulta = input("Digite sua consulta: ")
            if tipo_consulta == '1':
                resultados = biblioteca.consultar_livro(consulta, 'titulo')
            elif tipo_consulta == '2':
                resultados = biblioteca.consultar_livro(consulta, 'autor')
            elif tipo_consulta == '3':
                resultados = biblioteca.consultar_livro(consulta, 'ano_publicacao')
            else:
                print("Opção inválida. Por favor, tente novamente.")
                continue
            if resultados == "Nenhum livro encontrado.":
                print(resultados)
            else:
                for livro in resultados:
                    print(f'Título: {livro.titulo}, Autor: {livro.autor}, Ano de Publicação: {livro.ano_publicacao}, Número de cópias: {livro.num_copias}')
        elif opcao == '6':
            print(biblioteca.gerar_relatorio())
        elif opcao == '7':
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Executando a função menu se o script for executado diretamente
if __name__ == "__main__":
    menu()
