#Faça um programa que converte a notação de 24 horas para a notação de 12 horas
#Por exemplo, o programa deve converter 14:25 em 14:25 PM A entrada é dada em dois inteiros. 
#Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.
#Registre a informação AM/PM como um valor 'A' para AM e 'P' para PM Assim,
# a função para fazer as específicas terá um parâmetro formal para registrar se é AM ou PM Inclui um loop que permite que o usuário repita esse cálculo para novos valores de entrada
#todas as vezes que desejar.
def converterhorario(hora, minuto):
    if hora == 0:
        return f"12:{minuto:02} A.M."
    elif hora < 12:
        return f"{hora}:{minuto:02} A.M."
    elif hora == 12:
        return f"{hora}:{minuto:02} P.M."
    else:
        return f"{hora-12}:{minuto:02} P.M."
def imprimir_resultado(hora, minuto):
    resultado = converterhorario(hora, minuto)
    print(f"{hora:02}:{minuto:02} em 24 horas é igual a {resultado}")
def main():
    while True:
        hora = int(input("Digite a hora (0-23): "))
        minuto = int(input("Digite o minuto (0-59): "))
        imprimir_resultado(hora, minuto)
        resposta = input("gostaria de repetir? (s/n): ")
        if resposta.lower() != "s":
            break
if __name__ == "__main__":
    main()










