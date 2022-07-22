from jogo import Jogo

matriz = [[0] * 3 for i in range(3)]

z = 0

for x in range(len(matriz)): #le cada coluna
    for y in range(len(matriz[x])): #le cada linha
        matriz[x][y] = z
        z += 1

j = Jogo()

j.show_board(matriz)

casa =- 1
while casa < 9:
    print("\n É a sua vez de jogar...")
    casa = int(input("Selecione o número da casa: "))

    if casa >= 0 and casa <=8: # tenho que jogar entre zero e oito
        matriz = j.set_casa(matriz, casa, 'O')
        j.show_board(matriz)

        print("\n É a vez do computador")
        matriz = j.computer_turn(matriz) #matriz vai para atras a para frente
