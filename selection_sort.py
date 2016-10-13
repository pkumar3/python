def selSort(arr):
	small = arr[0]
	temp = 0
	for i in range(0,len(arr)-1):
		for j in range(i+1,len(arr)):
			if arr[j] < small:
				temp = arr[i]
				arr[i] = arr[j]
				arr[j] = temp

def main():
	arr = [9,2,3,5,1]
	print selSort(arr)

if __name__ == '__main__':
	main()