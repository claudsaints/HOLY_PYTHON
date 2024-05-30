signal = {"+","-","/","*"}
should_continue = False
def calc(x,y,z):
	if z == "+":
		return x + y
	elif z == "-":  
		return x - y
	elif z == "/" and y == 0:
		return 0
	elif z == "/":
		return x / y
	elif z == "*":
		return x * y


			
print ("Calculator, each one of this simbols + - / * ")

sin = (input("choice one simbol: "))
for x in signal:	
	if x == sin:
		should_continue = True
		one = float(input ("choice the first number: "))
while should_continue:		
	two = float(input ("choice the second number: "))

	res = calc(one,two,sin)
	
	print(f"The result of {one}{sin}{two} is: {res}")

	if input('Do you want to continue? type "y" for continue, or type "n" for start a new calculator') == 'y':
		one = res
	else:
		should_continue = False
			
			
			
			
			
			
			
			
		
