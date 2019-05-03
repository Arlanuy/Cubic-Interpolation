


file = open("Ninput1.txt", "r")
#x0 = 1.2
x0 = float(file.readline().replace('\n',''))
#x = [0, 0.001, 0.002, 0.003, 0.004, 0.005]
#y = [1.121, 1.123, 1.1255, 1.127, 1.128, 1.1285]

#x = [1, 1.3, 1.6, 1.9, 2.2]
x = [float(number) for number in file.readline().replace('\n','').split(' ')]
#y = [0.7652, 0.62, 0.4554, 0.2818, 0.1104]
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