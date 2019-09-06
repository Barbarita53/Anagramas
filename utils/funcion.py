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


