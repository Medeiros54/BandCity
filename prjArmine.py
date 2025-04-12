# Boas vindas do Cliente.
while True:
    boasVindas = print('Olá, bem vindo ao BandPet Creator! Aqui você usa dois parâmetros para criar um nome para sua banda de acordo com sua cidade e seu pet! /' \
'Está pronto pra isso?')
    aceitar = input('Você deseja continuar? Digite SIM ou NÃO. ' )

    if aceitar == 'sim' or aceitar == 'Sim' or aceitar == 'SIM':
     print('Beleza! Vamos lá. ')
     nomeCidade = input('Digite o nome da sua Cidade: ')
     nomePet = input('Digite o nome do seu Pet: ')
    
     nomeBanda = nomeCidade + ' ' + nomePet    

     print(f'O nome de sua banda é: {nomeBanda.upper()}')
     print('Obrigado por participar! Isso é tudo!')
     break

    elif aceitar == 'não' or aceitar == 'Não' or aceitar == 'NÃO':
      print('Que pena. Até a próxima.')
    break
    
else:
     print('Resposta Inválida, digite apenas SIM ou NÃO..')