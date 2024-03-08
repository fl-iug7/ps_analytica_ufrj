"""
    Calculadora de ângulo entre ponteiros do relógio
"""

def clock_angle_calculator(clock_time):
    """
        A função recebe uma string no formato hh:mm de um horário e retorna o valor do 
        menor ângulo entre os ponteiros do relógio. Ao receber o input 'f', o programa encerra.

        A cada 12 horas o ponteiro das horas realiza uma volta completa no relógio, isto é
        12 horas equivalem a 360°. Dessa forma, cada hora equivale a 30°

        A mesma lógica se aplica ao ponteiro dos minutos. A cada 60 minutos o ponteiro dos
        minutos realiza uma volta completa. Desse modo, cada minuto equivale a 6°

        Além disso, vale ressaltar que o ponteiro das se move gradualmente e diretamente
        proporcional ao ponteiro dos minutos. Esse deslocamento é igual ao valor da divisão: 
        (minutos)/60. 
        
        Por fim, caso o usuário forneça uma entrada inválida, isto é, string fora do padrão hh:mm
        será retornado uma mensagem informando a invalidez da entrada.
    """

    if len(clock_time) != 5:
        return print("Input inválido")

    try:
        #Divindo a entrada em hora, minuto e convertendo para inteiro
        hour = float(clock_time[:2])
        minute = float(clock_time[3:])

        #Ajustando o valor das horas caso seu valor seja maior que 12
        if hour <= 12:
            hour_angle = (hour + (minute/60))*30

        else:
            hour_angle = (hour - 12 + (minute/60))*30

        #Calculando o valor do ângulo do ponteiro dos minutos
        minute_angle = (minute*30)/5

        #Calculando o valor dos 2 possíveis ângulos entre os ponteiros
        angle_1 = abs(hour_angle - minute_angle)
        angle_2 = 360.0 - angle_1

        #Escolhendo o menor entre eles
        min_angle = min(angle_1, angle_2)

        return print("O menor ângulo é de", min_angle)

    except ValueError:
        #Caso o usuário forneça uma entrada fora do padrão hh:mm
        return print("Input inválido")


time = input()

while time != 'f':
    clock_angle_calculator(time)
    time = input()
