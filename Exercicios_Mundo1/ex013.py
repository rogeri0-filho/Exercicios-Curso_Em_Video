dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos Km foram percorridos: '))
valor = (dias * 60) * (km * 0.15)

print(f'O valor total a ser pago é de R${valor:.2f}!')
