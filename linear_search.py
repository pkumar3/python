def lSearch(n, arr):
	for i in range(0, len(arr)):
		if n == arr[i]:
			return i

def main():
	my_arr = [1,2,3,4,5]
	print lSearch(3, my_arr)

if __name__ == '__main__':
	main()