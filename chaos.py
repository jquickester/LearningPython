def main():
	print("This program illustrates a chaotic function")
	x = eval(input("Enter a number between 0 and 1: "))
	y = eval(input("Enter another number between 0 and 1: "))
	for i in range(10):
		x = 3 * x * (1-x)
		y = 3 * y * (1-y)
		print(x, "   ", y)
main()
