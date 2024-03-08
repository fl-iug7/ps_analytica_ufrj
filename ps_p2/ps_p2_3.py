"""
Calculadora de troco
"""

def change_calculator(number):
    """
    A função recebe um número e retorna o menor número de notas e moedas possíveis no qual 
    o valor pode ser decomposto. Para isso, foram consideradas as notas de 100, 50, 20, 10, 5, 
    2 e as moedas de 1, 0.50, 0.25, 0.10, 0.05 e 0.01 para a elaboração da função.

    Basicamente, a lógica da função consiste em sucessivamente subtrair a entrada fornecida pela 
    parte inteira da sua divisão pelo os valores das notas e moedas. A cada divisão inteira o 
    "valor total" diminui com base no resultado da divisão multiplicado pelo valor da nota ou 
    moeda utilizada (i.e. 5*100: 5 notas de 100 reais).

    Por fim, caso o usuário forneça alguma entrada fora do padrão, o programa irá retornar uma 
    mensagem informando que o input foi inválido.  
    """

    try:
        #Copiando o valor da entrada para uma variável que será alterada ao longo da função
        total_amount_remain = float(number)

        #Caso o número fornecido seja negativo, a função retorna a mensagem abaixo
        if total_amount_remain < 0:
            print("Input inválido")

        #Lista com todas as possíveis notas e moedas em ordem crescente de valor
        bills_and_coins = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

        #Iteração que realiza o cálculo descrito acima.
        for element in bills_and_coins.copy():
            if element == 100:
                print("NOTAS:")
                text_print = "nota(s) de R$"

            if element == 1:
                print("\nMOEDAS:")
                text_print = "moeda(s) de R$"

            print(total_amount_remain//element, text_print, element)
            total_amount_remain -= (total_amount_remain//element)*element

    except ValueError:
        #Caso a entrada fornecida esteja fora do padrão, a função retorna a mensagem abaixo
        print("Input inválido")


money_amount = input()
change_calculator(money_amount)
