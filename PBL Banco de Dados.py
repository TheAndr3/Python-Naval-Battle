#/*******************************************************************************
#Autor: André Vinicius Diz Freitas
#Componente Curricular: MI DE ALGORITMOS
#Concluido em: 09/05/2023
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/

#Random para randomizar com o bot
import random
#Definir o dicionário que sera usado mais na frente
tamanho_navios = {"grande": 4, "medio": 3, "pequeno": 2}

# cria o tabuleiro com água/vazio
def cria_tabuleiro():
    tabuleiro = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append("~")
        tabuleiro.append(linha)
    return tabuleiro

# exibe o tabuleiro na tela
def exibe_tabuleiro(tabuleiro):
    # Exibe o cabeçalho do tabuleiro
    print('     ' + ' '.join([str(i) for i in range(1,11)]))
    #abaixo das colunas há isto para melhor vizualização
    print('--+' + '-'*20 + '--')
    
    # Exibe cada linha do tabuleiro bonitinha
    for i, linha in enumerate(tabuleiro):
        linha_str = ' '.join(['~' if c == ' ' else c for c in linha])
        print('{:>2d} | {}'.format(i+1, linha_str))
    
    # Exibe o rodapé do tabuleiro
    print('--+' + '-'*20 + '--')


#Aqui é a função que forma o tabuleiro do bot, por falta de tempo por conta do ocorrido do computador, não consegui criar a
#a tempo uma matriz invisivel pra sobrepor o tabuleiro, portanto ficara assim.
def exibe_tabuleiro_bot(tabuleiro):
    # Exibe o cabeçalho do tabuleiro
    print('     ' + ' '.join([str(i) for i in range(1,11)]))
    print('--+' + '-'*20 + '--')
    
    # Exibe cada linha do tabuleiro
    for i, linha in enumerate(tabuleiro):
        linha_str = ' '.join(['~' if c == ' ' else c for c in linha])
        print('{:>2d} | {}'.format(i+1, linha_str))
    
    # Exibe o rodapé do tabuleiro
    print('--+' + '-'*20 + '--')

#Verifica se uma posição é válida no tabuleiro
def posicao_valida(tabuleiro, linha, coluna):
    if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
        return False
    if tabuleiro[linha][coluna] != "~":
        return False
    return True

#Coloca os navios no tabuleiro
def coloca_navio(tabuleiro, linha, coluna, tamanho, direcao):
    if direcao == "horizontal":
        for i in range(tamanho):
            if not posicao_valida(tabuleiro, linha, coluna+i):
                return False
        for i in range(tamanho):
            tabuleiro[linha][coluna+i] = "O"
    elif direcao == "vertical":
        for i in range(tamanho):
            if not posicao_valida(tabuleiro, linha+i, coluna):
                return False
        for i in range(tamanho):
            tabuleiro[linha+i][coluna] = "O"
    else:
        return False
    return True

#Pede ao jogador para colocar seus navios no tabuleiro
def coloca_navios_jogador(tabuleiro):
    navios = {"grande": 1, "medio": 2, "pequeno": 3}
    tamanho_navios = {"grande": 4, "medio": 3, "pequeno": 2}
    navios_colocados = 0
    for tamanho in navios:
        for i in range(navios[tamanho]):
            navio_colocado = False
            while not navio_colocado:
                print("Coloque um navio " + tamanho + " (tamanho " + str(tamanho_navios[tamanho]) + ")")
                linha = int(input("Linha inicial (1-10): ")) - 1
                coluna = int(input("Coluna inicial (1-10): ")) - 1
                direcao = input("Direção (horizontal ou vertical): ")
                if coloca_navio(tabuleiro, linha, coluna, tamanho_navios[tamanho], direcao):
                    exibe_tabuleiro(tabuleiro)
                    navios_colocados += 1
                    navio_colocado = True
                else:
                    print("Posição inválida. Tente novamente.")
            if navios_colocados == sum(navios.values()):
                navio_colocado = True
                break

#Coloca os navios aleatoriamente 
def coloca_navios_computador(tabuleiro):
    navios = {"grande": 1, "medio": 2, "pequeno": 3}
    for tamanho in navios:
        for i in range(navios[tamanho]):
            while True:
                linha = random.randint(0, 9)
                coluna = random.randint(0, 9)
                direcao = random.choice(["horizontal", "vertical"])
                if coloca_navio(tabuleiro, linha, coluna, tamanho_navios[tamanho], direcao):
                    break
                else:
                    print("Posição inválida. Tente novamente.")

#Função do tiro baseado nas figuras que estão no tabuleiro
def ataca(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == "~":
        tabuleiro[linha][coluna] = "X"
        print("Errou!")
    elif tabuleiro[linha][coluna] == "O":
        tabuleiro[linha][coluna] = "#"
        print("Acertou!")
        return True
    else:
        print("Você já atacou essa posição!")
        return False

#Verificação para o fim do jogo, se todos os navios forem atingidos
def verifica_fim_de_jogo(tabuleiro):
    for linha in tabuleiro:
        if "O" in linha:
            return False
    return True

#Função main/principal, onde roda o jogo e as mensagens de aviso, separadas por '-'.
def batalha_naval():
    print("Bem-vindo ao jogo Batalha Naval!")
    tabuleiro_jogador = cria_tabuleiro()
    tabuleiro_computador = cria_tabuleiro()
    print("Coloque seus navios:")
    exibe_tabuleiro(tabuleiro_jogador)
    coloca_navios_jogador(tabuleiro_jogador)

    print("O computador está colocando seus navios...")
    coloca_navios_computador(tabuleiro_computador)

    # Imprime os tabuleiros no início do jogo
    print("Seu tabuleiro:")
    exibe_tabuleiro(tabuleiro_jogador)
    print("Tabuleiro do computador:")
    exibe_tabuleiro_bot(tabuleiro_computador)

    #Sistema de rodadas, começando pelo computador e assim rodando até o fim do jogo.
    fim_de_jogo = False
    jogador_atual = False # Começa com o computador
    while not fim_de_jogo:
        print('--------------------------')
        if jogador_atual:
            print("Sua vez de atacar!")
            exibe_tabuleiro(tabuleiro_jogador)
            print('Seu tabuleiro')
            exibe_tabuleiro_bot(tabuleiro_computador)
            print('Tabuleiro do Inimigo')
            linha = int(input("Linha (1-10): ")) - 1
            coluna = int(input("Coluna (1-10): ")) - 1
            if ataca(tabuleiro_computador, linha, coluna):
                print("Você acertou um navio do computador!")
                if verifica_fim_de_jogo(tabuleiro_computador):
                    print("Parabéns, você ganhou o jogo!")
                    fim_de_jogo = True
                else:
                    print("Você tem direito a um tiro extra!")
            else:
                print("Você errou o alvo!")
                jogador_atual = False

        else:
            print("Agora é a vez do computador!")
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            if ataca(tabuleiro_jogador, linha, coluna):
                print("O computador acertou um de seus navios!")
                if verifica_fim_de_jogo(tabuleiro_jogador):
                    print("Você perdeu o jogo!")
                    fim_de_jogo = True
                else:
                    print("O computador tem direito a um tiro extra!")
            else:
                print("O computador errou o alvo!")
                jogador_atual = True

#Função ´principal que roda todas as demais
batalha_naval()