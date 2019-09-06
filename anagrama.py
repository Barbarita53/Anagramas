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


def ordernum1(list1):
	n=len(list1)
	cambios = True
	while cambios:
		cambios = False
		for i in range(0, n-1):
			p=i+1
			if list1[p]<list1[i]:
				h = list1[i]
				list1[i]=list1[p]
				list1[p]= h
				cambios=True
			

"""def ordernum2(list2):
	cambios = True
	while cambios:
		for j in range(0, m-1):
			k=j+1
			if list2[k]<list2[j]:
				b = list2[j]
				list2[j]=list2[k]
				list2[k]= b
				cambios=True
			else:
				cambios=False"""
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

