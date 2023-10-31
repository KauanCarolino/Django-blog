users = {
    "kauan": "123456",
    "jucelio": "010010"
}


opcao = input("[1] Autenticacao, [2] Cadastro, [3] Deletar usuario [3] Verificar Usuarios: ")

if opcao == "1":
  tentativa_max = 3

  def autenticacao():
    print("Autenticacao de Usuario")
    user_login = input("Digite seu Usuario: ").lower().strip()
    tentativa = 0

    if user_login in users:
      while(tentativa < tentativa_max):
        if users[user_login] == input("Digite sua senha: "):
          print("Acesso autorizado!")
          print(user_login)
          break
        else:
          tentativa += 1
          restante = tentativa_max - tentativa

          if restante > 0:
            print("usuario ou senha incorreta, tentativas restantes ",restante)
          else:
            print("Numero de tentativas excedidas. Acesso bloqueado!")
            break
  autenticacao()

elif opcao == "2":
  def cadastro():
    print("Cadastro de Usuario")

    user_cadastro = input("Digite o novo Usuario: ").lower().strip()

    if user_cadastro in users:
      print("Usuario existente")
    else:
      senha = input("Digite a nova senha: ").strip()
      senha_confirmacao = input("Digite novamente a senha: ").strip()

      if senha == senha_confirmacao:
        users[user_cadastro] = senha
        print("Usuario cadastrado com sucesso")
        print(users)
      else:
        print("senhas diferentes")

  cadastro()

elif opcao == "3":
  def deletar():
    print("Remoção de Usuario")
    user_del = input("Qual usuario vc deseja deletar: ").lower().strip()

    if user_del in users:
      users.pop(user_del)
      print("Usuario removido com sucesso!")
      print(users)
    else:
      print("usuario não existente, tente novamente!")
  deletar()

elif opcao == "4":
  print(users)
else:
  print("Adeus")