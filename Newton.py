def NewtonInterpolation():

	file = open("Ninput1.txt", "r")
	
	x0 = float(file.readline().replace('\n',''))
	x = [float(number) for number in file.readline().replace('\n','').split(' ')]
	y = [float(number) for number in file.readline().replace('\n','').split(' ')]
	d = []
	new = []

	d.append(y)

	while (len(new) != 1):
		
		length = len(y)
		new = []
		#print(y)
		#print(d)
		#print(length)
		for i in range(1, length):
			new.append((y[i] - y[0]) / (x[i] - x[0]))

		d.append(new)
		#print(new)
		y = new

	#print(d)
	#input("Press 'Enter'")

	mult = []
	p = d[0][0]
	#print("p = {}".format(p))
	s = 0
	z = 1

	for i in range(1, len(d)):
		s = d[i][0]
		#print(s)
		for j in range(0, z):
			s = s*(x0 - x[j])
		#print("s = {}".format(s))
		p = p + s
		s = 0
		z =  z + 1

	print(p)

	#0.7652-(0.484*(1.2-1))-(0.1077*(1.2-1)*(1.2-1.3))+(0.064*(1.2-1)*(1.2-1.3)*(1.2-1.6))+(0.004*(1.2-1)*(1.2-1.3)*(1.2-1.6)*(1.2-1.9))

	#0.6710436


def NewtonRaphsonExponentiation():

	#Read the values from an input file
	file = open("N2input1.txt", "r")
	a = float(file.readline().replace('\n',''))
	m = float(file.readline().replace('\n',''))
	n = float(file.readline().replace('\n',''))

	print(a, m, n)
	Answer = a**(m/n) #Just for comparison

	estimate = int(m/n)

	x_current = 0 #Current is initialized to be 0 to enter the while loop 
	x_next = a #Our guess is the value of a

	while(abs(x_current - x_next) > 0.0000001): #Iterate until the computed solution is close enough to the actual solution
		x_current = x_next 
		x_next = x_current - ( ((x_current ** n) - (a ** m)) / (n * (x_current ** (n - 1))) ) #Main formula of Newton-Raphson, f(x) = (x^n)-(a^m) and f'(x)= n(x^(n-1))
		#print("x_current = {}".format(x_current))

	print("Computed solution: {}".format(x_next))
	print("Actual solution:   {}".format(Answer))


#def NewtonRaphsonTrigonometric():



NewtonRaphsonExponentiation()
#NewtonRaphsonTrigonometric()