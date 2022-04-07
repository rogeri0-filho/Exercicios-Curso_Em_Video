frase = str(input('Digite uma frase: ')).upper()

print(f'A letra "A" aparece {frase.count("A")} vezes.')
print(f'A primeira aparição foi na {frase.find("A") + 1}ª posição.')
print(f'A ultima aparição foi na {frase.rfind("A") + 1}ª posição.')

#a contagem começa a partir do 0, por isso o + 1
