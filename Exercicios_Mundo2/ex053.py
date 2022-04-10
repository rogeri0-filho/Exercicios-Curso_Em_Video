pmaior = 0
pmenor = 0

for c in range(1, 6):
    p = float(input(f'Peso da {c}ª pessoa: '))

    if c == 1:
        pmaior = p
        pmenor = p

    else:
        if p > pmaior:
            pmaior = p

        if p < pmenor:
            pmenor = p

print(f'O MAIOR peso foi {pmaior}Kg!\n'
      f'O MENOR peso foi {pmenor}Kg!')
