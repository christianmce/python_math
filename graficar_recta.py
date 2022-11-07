# Autor: Dr. Christian Mauricio Castillo Estrada
# Universidad Autónoma de Chiapas - LIDTS Facultad de Negocios

import matplotlib.pyplot as plt

def f1(x):
	return 4*x + 1

valores = [1,2,3]
for cx in valores:
	print(cx,' - ', f1(cx))

plt.plot(valores,[f1(valorx) for valorx in valores])
plt.show() #dibujar la línea recta
