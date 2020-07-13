
#Exemplo 01 - somatória de numeros
def soma(num1: int, num2: int)->int:

    retorno = num1 + num2
    print(f'A soma do {num1} + {num2} = {retorno}')
    return retorno

#soma(1,2)

#Exemplo 02 - 4 variáveis - nota de usuário

# nota01 = int(input("insira sua nota 01: "))
# nota02 = int(input("insira sua nota 02: "))
# nota03 = int(input("insira sua nota 03: "))
# nota04 = int(input("insira sua nota 04: "))
#
# media = (nota01+nota02+nota03+nota04) / 4
#
# print('As média entre as notas: {},{},{},{} => {}'.format(nota01,nota02,nota03,nota04,media))


#Exemplo 03 -

def media(nota01:int, nota02:int, nota03:int, nota04:int):

    media = (nota01+nota02+nota03+nota04) / 4
    print('As média entre as notas: {},{},{},{} => {}'.format(nota01,nota02,nota03,nota04,media))
    return media

def media_print():

    nota01 = int(input("insira sua nota 01: "))
    nota02 = int(input("insira sua nota 02: "))
    nota03 = int(input("insira sua nota 03: "))
    nota04 = int(input("insira sua nota 04: "))

    media = (nota01+nota02+nota03+nota04) / 4
    print('As média entre as notas: {},{},{},{} => {}'.format(nota01,nota02,nota03,nota04,media))

# ex 03 - Salário e Horas

# input_horas_trabalhadas_mes = int(input('quantas horas vc trabalha por mes?'))
# ganha_por_hora = float(input('quantas você ganha por hora?'))
#
# salario_final =input_horas_trabalhadas_mes * ganha_por_hora
#
# print('Você trabalha {} horas no mês, e ganha de salário mensal {}' .format(input_horas_trabalhadas_mes,salario_final) )

# ex 04 - salario e horas, descontar do salário 24%
#
# input_horas_trabalhadas_mes = int(input('quantas horas vc trabalha por mes?'))
# ganha_por_hora = float(input('quantas você ganha por hora?'))
#
# salario_final =input_horas_trabalhadas_mes * ganha_por_hora
#
# print('Você trabalha {} horas no mês, e ganha de salário mensal {}' .format(input_horas_trabalhadas_mes,salario_final) )
#
# descontado_salario_final = salario_final*(1-0.24)
#
# print('Com o desconto 24% seu salário será: {}' .format(descontado_salario_final))

# ex 05 - utilizar uma função

def funcao01():
    input_horas_trabalhadas_mes = int(input('quantas horas vc trabalha por mes?'))
    ganha_por_hora = float(input('quantas você ganha por hora?'))

    salario_final = input_horas_trabalhadas_mes * ganha_por_hora

    print('Você trabalha {} horas no mês, e ganha de salário mensal {}'.format(input_horas_trabalhadas_mes,
                                                                               salario_final))

    descontado_salario_final = salario_final * (1 - 0.24)

    print('Com o desconto 24% seu salário será: {}'.format(descontado_salario_final))
    print('Seu salario bruto: {} e seu salario depois do desconto é esse:{}'.format(descontado_salario_final,salario_final))

funcao01()