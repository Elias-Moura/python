'''Exercícios
Digamos que você está criando o sistema para registrar a chegada de hóspedes em um hotel.
No hotel, os hóspedes podem ter quartos com 1,2,3 e 4 pessoas. Seus sistema deve conseguir:

1- Identificar quantas pessoas o hópede que acabou de chegar vai ter no quarto.
2- De acordo com a quantidade de pessoas do hópede, ele deve fazer um for para perguntar o cpf e o nome
de cada pessoa, a dim de registra-la no quarto
3- O seu programa então deve gerar uma lista com todas as pessoas que ficarão no quarto em que cada item dessa
lista é o nome da pessoa e o cpf da pessoa assim:

quarto = [
    ['joão', 'cpf: 00000000000'].
    ['Julia', 'cpf: 11111111111'],
    ['Mateus', 'cpf: 22222222222'],
    ['Lara', 'cpf: 33333333333'],
]

Para simplificar, não vamos nos preocupar com a possibilidade de "tentar colocar mais de 1 hóspede,
 digitar o cpf errado, etc. Nosso objetivo é treinar a criação de uma rotina de cadastro.
'''

qtde_pessoas = int(input('Quantas pessoas terão no quarto? '))
quarto = []

for i in range(qtde_pessoas):
    nome = input('Qual o nome? ')
    cpf = input('Qual é o cpf? ')
    hospede = [nome, 'cpf: {}'.format(cpf)]
    quarto.append(hospede)

print(quarto)
