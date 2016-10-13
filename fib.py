def fib(n):
	if n == 0:
		return 0
	if n < 2:
		return 1
	return fib(n-1) + fib(n-2)

def main():
	print(fib(6))

if __name__ == "__main__":
	main()