palabra1 = None
palabra2 = None
while not palabra1:
	try:
		palabra1=str(input('pon una palabra: '))
	except ValueError:
		print('dije palabraa ')
while not palabra2:
	try:
		palabra2=str(input('pon otra: '))
	except ValueError:
		print('dije palabraa ')
list1=list(palabra1)
list2=list(palabra2)

from utils.funcion import ordernum1


"print(list1)"
ordernum1(list1)
e=list1
"print(e)"
"print(list2)"
ordernum1(list2)
u=list2
"print(u)"

if e==u:
	print(f'{palabra1} y {palabra2} son anagramas')
else:
	print(f'{palabra1} y {palabra2} no son anagramas')
