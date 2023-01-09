def simple_interest():
	p = int(input('The principal is ',))
	t = int(input('The time period is ',))
	r = int(input('The rate of interest is ',))
	si = (p * t * r)/100
	print('The Simple Interest is', si)

#_main_
simple_interest()