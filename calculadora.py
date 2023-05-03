def soma(a, b):
	return a + b


def sub(a, b):
	return a - b


def div(a, b):
	return a / b


def mult(a, b):
	return a * b


def linha():
	print('-='*30)


linha()
print('''1| Adição
2| Subtração
3| Multiplicação
4| Divisão''')
while True:
	escolha = input('Selecione uma operação: ')
	linha()
	if escolha in('1', '2', '3', '4'):
		try:
			n1 = float(input('Escolha o primeiro número: '))
			n2 = float(input('Escolha o segundo número: '))
		except ValueError:
			print('Inválido. Por favor, escolha um número válido.')
			continue
		if escolha == '1':
			print(f'{int(n1)} + {int(n2)} = {int(soma(n1, n2))}')
		elif escolha == '2':
			print(f'{int(n1)} - {int(n2)} = {int(sub(n1, n2))}')
		elif escolha == '3':
			print(f'{int(n1)} x {int(n2)} = {int(mult(n1, n2))}')
		elif escolha == '4':
			print(f'{n1} / {n2} = {div(n1, n2)}')
		while True:
			continuar = input('Deseja continuar? (s/n): ').lower()
			if continuar == 's':
				break
			elif continuar == 'n':
				print('Fechando programa...')
				exit()
			else:
				print('Resposta inválida.')

		
				
			







