"""
Movimentação do cavalo no xadrez

"""
def knight_movement_calculator(knight_positions):
    """
    A função recebe uma string que possui a posição inicial e a possível posição final do cavalo 
    em um jogo de xadrez e retorna uma resposta confirmando se a posição final é considerada 
    válida ou inválida. Ao receber o input 'f', o programa encerra.

    A lógica escolhida para a função foi baseada no fato do tabuleiro ser simples e pequeno (8 x 8), 
    além do fato de que o cavalo possui poucas possíveis posições finais e todas são fáceis de 
    calcular. Por isso, dado a posição inicial da peça, inicia-se uma lista com todas as suas 
    possíveis posições finais (incluindo as impossíveis, i.e. fora do tabuleiro)

    Então, basta agora verificar se a posição final fornecida na entrada corresponde à alguma 
    posição presente na lista.

    Além disso, para simplificar os cálculos das posições entre as colunas (número) e as linhas 
    (caracter), foi usado a função ord() para retornar o valor ASCII do caracter e subtraido de 
    96 (valor ASCII do caracter anterior "a"). Desse modo, tanto as linhas quanto as colunas 
    estão com valores de 1 à 8.

    Por fim, caso o usuário forneça alguma entrada fora do padrão, o programa irá retornar uma 
    mensagem informando que o input foi inválido. O programa funciona ainda que os caracteres 
    (válidos) fornecidos estejam em maiúsculo.
    """

    try:
        #Separando a string entre as posições iniciais e finais
        position_1 = knight_positions[:2]
        position_2 = knight_positions[3:]

        #Calculando a posição inicial
        row_1 = int(ord(position_1[0].lower()) - 96)
        column_1 = int(position_1[1])

        #Calculando a posição final
        row_2 = int(ord(position_2[0].lower()) - 96)
        column_2 = int(position_2[1])

        #Inicializando a lista com as possíveis posições finais do cavalo
        final_position_list = [(row_1 + 1, column_1 + 2), (row_1 + 1, column_1 - 2), (row_1 - 1, column_1 + 2), (row_1 - 1, column_1 - 2),  (row_1 + 2, column_1 + 1), (row_1 + 2, column_1 - 1), (row_1 - 2, column_1 + 1), (row_1 - 2, column_1 - 1)]

        #Conferindo a posição final fornecida com as possíveis posições finais
        for element in final_position_list:
            if (row_2, column_2) == element and 1 <= row_2 <= 8 and 1 <= column_2 <= 8:
                return print("VÁLIDO")

        return print("INVÁLIDO")

    except ValueError:
        #Caso o usuário forneça alguma entrada fora do padrão a mensagem abaixo será fornecida
        return print("INVÁLIDO")


positions = input()

while positions != 'f':
    knight_movement_calculator(positions)
    positions = input()
