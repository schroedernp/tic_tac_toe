class Jogo:
    def show_board(self, board):
        print("%s | %s | %s" %(board[0][0], board[0][1], board[0][2])) #os valores serao substituidos no local destas porcentagens
        print("--|---|--")
        print("%s | %s | %s" % (board[1][0], board[1][1], board[1][2]))
        print("--|---|--")
        print("%s | %s | %s" % (board[2][0], board[2][1], board[2][2]))

    def set_casa(self, matriz, casa, simbolo):
        a = casa // 3
        b = casa - a * 3
        matriz[a][b] = simbolo
        return matriz

    # vez do computador jogar
    def computer_turn(self, matriz):
        jogado = 0
        #verificar horizontal
        for x in range(len(matriz)):
            #col vai ter o numero da coluna onde deve jogar
            col = self.check_line(matriz[x]) # nesta linha ja sei se devo colocar um X ou nao
            if col > -1:
                matriz[x][col] = 'X'#coluna vai ser maior que me -1
                jogado = True # se eu verificar as horizontais, ja nao preciso verificar as horizontais e verticais
                break

        #Verificar colunas
        if jogado == False:  # se ele ainda nao jogou....
            coluna = []
            for x in range(len(matriz)):
                for y in range(len(matriz[0])):
                    coluna.append([matriz[y][x], x, y])
                #col vai ter o numero da coluna onde deve jogar
                col = self.check_column(coluna, matriz)
                if len(col) > 0:
                    linha = col[0]
                    coluna = col[1]
                    matriz[linha][coluna] = 'X'
                    jogado = True
                    break #termina os loops for x e for y
                coluna.clear() # limpa a lista da coluna = []

        #Verificar diagonal
        if jogado == False:
            diagonal = [[0, 2], [1,1] , [2,0]] # é uma lista de lista...
            col = self.check_diagonal(diagonal, matriz) #chamo o método - a diagonal começa da esquerda para a direita
            if len(col) > 0:
                linha = col [0]
                coluna = col[1]
                matriz [linha][coluna] = 'X'
                jogado = True
            else:
                #segunda diagonal...
                diagonal = [[0,0], [1,1], [2, 2]]
                col = self.check_diagonal(diagonal, matriz)
                if len(col) > 0:
                    linha = col[0]
                    coluna =col[1]
                    matriz[linha][coluna] = 'X'
                    jogado = True


        # Finalmente, jogar
        if jogado == False:
            matriz = self.jogar(matriz)
        self.show_board(matriz)

        return matriz





    def check_line(self, linha):
        marcas = 0 # computador das marcas
        jogo = []

        a = linha.count('O') # o a vai me dar o numro de vezes que aparece o O
        if a <= 1:
            return -1

        for n in range(len(linha)): #esta parte pode substituir o for e o if abaixo.
            if linha [n] != 'O' and linha[n] != 'X':
                return n
        return -1

        # for n in range(len(linha)): # para saber qual deles esta em branco
        #     if linha[0] == 'O':
        #         marcas += 1
        #     elif linha[n] != 'X':
        #         jogo.append()
        # if len(jogo) == 1 and marcas == 2:
        #     return jogo[0]
        # else:
        #     return -1


    def check_diagonal(self, diagonal, matriz):
        marcas = 0
        jogo = []
        for n in range(len(diagonal)):  # diagonal é uma lista
            linha = diagonal[n][0]
            coluna = diagonal[n][1]
            if matriz[linha][coluna] == 'O':
                marcas += 1
            elif matriz[linha][coluna] != 'X':
                jogo.append([linha, coluna])
        if len(jogo) == 1 and marcas == 2:
            return jogo[0]
        else:
            return[]

    def check_column(self, coluna, matriz):
        marcas = 0
        jogo = []
        for n in coluna:
            linha = n[2]
            col = n[1]
            if matriz[linha][col] == 'O':
                marcas += 1 # se for zero ele soma as marcas....
            elif matriz[linha][col] != 'X':
                jogo.append([linha,col])

        if len(jogo) == 1 and marcas == 2:
            return jogo[0]
        else:
            return[]


    def jogar(self, matriz):
        #Verificar as linhas se já tem uma cruz...
        y = 0
        for linha in matriz:
            if 'X' in linha:
                for x in len(linha):
                    if linha[x] != 'O' and linha[x] != 'X':
                        matriz[y][x] = 'X'
                        return matriz
            y += 1
        #Verificar as colunas se já têm uma cruz
        num_cruzes = 0
        casa_para_jogar = []
        for coluna in range(3):
            for linha in range(3):
                if matriz[linha][coluna] == 'X':
                    num_cruzes += 1
                elif matriz[linha][coluna] != 'O':
                    casa_para_jogar.append(linha)
            if num_cruzes > 0 and len(casa_para_jogar) > 0:
                matriz[casa_para_jogar[0][coluna]] = 'X'
                return matriz
            num_cruzes = 0
            casa_para_jogar = []

        #Verificar se as diagonais já têm uma cruz
        diagonal_esq_dir = [matriz[0][0], matriz[1][1], matriz[2][2]]
        diagonal_dir_esq = [matriz[0][2], matriz[1][1], matriz[2][0]]

        #Diagonal da esquerda
        num_cruzes = 0
        casa_para_jogar = []
        for n in range(len(diagonal_esq_dir)):
            if diagonal_esq_dir[n] == 'X':
                num_cruzes += 1
            elif diagonal_esq_dir[n]:
                casa_para_jogar.append(n)

        if num_cruzes > 0 and len(casa_para_jogar) > 0:
            if casa_para_jogar[0] == [0]:
                matriz[0][0] = 'X'
                return matriz
            elif casa_para_jogar[0] == 1:
                matriz[1][1] = 'X'
            elif casa_para_jogar[0] == 2:
                matriz[2][2] = 'X'
                return matriz

        #Diagonal da direita
        num_cruzes = 0
        casa_para_jogar = []
        for n in range(len(diagonal_dir_esq)):
            if diagonal_dir_esq[n] == 'X':
                num_cruzes += 1
            elif diagonal_dir_esq[n] != 'O':
                casa_para_jogar.append(n)

        if num_cruzes > 0 and len(casa_para_jogar) > 0:
            if casa_para_jogar[0] == 0:
                matriz[0][2] = 'X'
                return matriz
            elif casa_para_jogar[0] ==1:
                matriz[1][1] = 'X'
                return matriz
            elif casa_para_jogar[0] ==2:
                matriz[2][0] = 'X'
                return matriz

        #Finalmente se não há cruzes repetidas, põe uma cruz na primeira casa livre que aparecer
        for linha in range(len(matriz)):
            for coluna in range(len(matriz[linha])):
                if matriz[linha][coluna] != 'O' and matriz[linha][coluna] != 'X': #verifico se tem O ou X... Se nao tiver é pq a casaestá vazia
                    matriz[linha][coluna] = 'X'
                    return matriz










