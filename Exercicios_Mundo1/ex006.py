unidade = float(input('Digite um valor em metros para converte-lo para as demais uniades de medidas: '))

km = unidade / 1000
hm = unidade / 100
dam = unidade / 10
dm = unidade * 10
cm = unidade * 100
mm = unidade * 1000

print(f'O valor em:\nKm: {km:.3f}\nHm: {hm:.2f}\nDam: {dam:.2f}\nDm: {dm:.2f}\nCm: {cm:.2f}\nMm: {mm:.2f}')
