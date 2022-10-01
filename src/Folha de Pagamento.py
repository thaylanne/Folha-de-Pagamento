hora_valor = float(input("Digite quanto você recebe por hora: "))
hora_trabalhada = float(input("Digite quantas horas você trabalhou esse mês: "))

salario_bruto = hora_trabalhada * hora_valor

if salario_bruto <= 900:
    desconto_ir = 0.0
elif salario_bruto <= 1500:
    desconto_ir = 5
elif salario_bruto <= 2500:
    desconto_ir = 10
else:
    desconto_ir = 20

IR = salario_bruto * (desconto_ir / 100)
INSS = salario_bruto * (10 / 100)
FGTS = salario_bruto * (11 / 100)
total_de_descontos = IR + INSS
salario_liquido = salario_bruto - total_de_descontos

print(f"Salário Bruto : R$ {salario_bruto:.2f}")
print(f"IR : R$ {IR:.2f}")
print(f"INSS : R$ {INSS:.2f}")
print(f"FGTS : R$ {FGTS:.2f}")
print(f"Total de Descontos : R$ {total_de_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")

