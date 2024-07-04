# Sistema de perguntas e respostas simples
from os import system

perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1','3','4','5'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25','55','10','51'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4','5','2','1'],
        'Resposta': '5'
    },
]

right_answers = 0
wrong_answers = 0

for question in perguntas:

    print(question.get('Pergunta'))

    for option in enumerate(question.get('Opções')):
        print(f'[{option[0]}] {option[1]}')

    answer = int(input("\nResposta: "))

    if question['Opções'][answer] == question.get('Resposta'):
        print("Acertou.")
        right_answers += 1
    else:
        print("Errou.\n")
        wrong_answers += 1


system('cls')
print(f'Acertou: {right_answers}')
print(f'Errou: {wrong_answers}')

    

