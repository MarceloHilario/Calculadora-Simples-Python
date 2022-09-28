continuar_usando = "SIM"

while continuar_usando == "SIM":
  print("SELECIONE A OPERAÇÃO DESEJADA")
  print("+ para Adição")
  print("- para Subtração")
  print("* para Multiplicação")
  print("/ para Divisão")

  operacao = input("Qual operação você deseja realizar? ")

  if operacao == "+":
    a1 = float(input("Digite o primeiro valor: "))
    a2 = float(input("Digite o segundo valor: "))
    adicao = a1 + a2
    print("A soma entre",a1,"e",a2,"é:",adicao)
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()

  if operacao == "-":
    b1 = float(input("Digite o primeiro valor: "))
    b2 = float(input("Digite o segundo valor: "))
    subtracao = b1 - b2
    print("A subtração entre",b1,"e",b2,"é:",subtracao)
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()

  if operacao == "*":
    c1 = float(input("Digite o primeiro valor: "))
    c2 = float(input("Digite o segundo valor: "))
    multiplicacao = c1 * c2
    print("A multiplicação entre",c1,"e",c2,"é:",multiplicacao)
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()

  if operacao == "/":
    d1 = float(input("Digite o primeiro valor: "))
    d2 = float(input("Digite o segundo valor: "))
    while d2 == 0:
      print("O segundo valor não pode ser zero!")
      d2 = float(input("Digite o segundo valor (diferente de zero): "))
    divisao = d1 / d2
    print("A divisão entre",d1,"e",d2,"é:",divisao)
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()
