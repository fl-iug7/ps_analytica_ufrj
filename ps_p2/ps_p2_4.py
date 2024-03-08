"""
Frequência de números
"""

def number_frequency_calculator(number):
    """
    A função contabiliza a frequência de cada número inteiro recebido na entrada até que um input
    'f' encerre a função.

    Uma matriz foi utilizada para armazenar listas de tamanho 2, com o primeiro elemento sendo o 
    número fornecido na entrada e o segundo elemento a sua frequência.

    Por fim, mesmo que a entrada esteja fora do padrão, a função continue e apenas ignora o erro.
    """

    #Matriz para armazenar os números e suas respectivas frequências
    number_and_frequency_list = []

    while number != 'f':
        try:
            number = int(number)

            #Iteração que realiza a montagem da matriz.
            #A cada iteração se um novo número é fornecido, adiciona uma nova lista na matriz com o número e a frequência inicial 1.
            #Caso a entrada seja um número já fornecido, encontra-se a posição do elemento na matriz e atualiza sua frequência.
            for index in range(len(number_and_frequency_list.copy()) + 1):
                if len(number_and_frequency_list) >= 1:
                    if number_and_frequency_list[index][0] == number:
                        number_and_frequency_list[index][1] += 1
                        break

                    if index == len(number_and_frequency_list) - 1:
                        number_and_frequency_list.append([number, 1])
                        break

                else:
                    number_and_frequency_list.append([number, 1])

            number = input()

        except ValueError:
            #Ignora e prossegue com o loop caso haja alguma entrada fora do padrãoS
            number = input()

    for element in number_and_frequency_list:
        if element[1] > 1:
            print("O", element[0],"apareceu", element[1], "vezes")

        else:
            print("O", element[0],"apareceu", element[1], "vez")


number_input = input()
number_frequency_calculator(number_input)
