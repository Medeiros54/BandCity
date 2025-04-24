# Começo um loop para rodar sem erro
while True: 
    # Boas vindas do Cliente.
    boasVindas = print('Olá, bem vindo ao BandPet Creator! Aqui você usa dois parâmetros para criar um nome para sua banda de acordo com sua cidade e seu pet! /' \
'Está pronto pra isso?')
    aceitar = input('Você deseja continuar? Digite SIM ou NÃO. ' )
    #condições para rodar corretamente 
    if aceitar == 'sim' or aceitar == 'Sim' or aceitar == 'SIM':
     print('Beleza! Vamos lá. ')
     nomeCidade = input('Digite o nome da sua Cidade: ')
     nomePet = input('Digite o nome do seu Pet: ')
    # Nome Final
     nomeBanda = nomeCidade + ' ' + nomePet    

     print(f'O nome de sua banda é: {nomeBanda.upper()}')
     print('Obrigado por participar! Isso é tudo!')
     break #fim do primeiro laço

    elif aceitar == 'não' or aceitar == 'Não' or aceitar == 'NÃO':
      print('Que pena. Até a próxima.')
    break #fim do segundo laço
     
else: #caso a pessoa tente quebrar o programa, EU TENHO O PODER DO NÃO! 
     print('Resposta Inválida, digite apenas SIM ou NÃO.')