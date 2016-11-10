def bubbleSort(arr):
	temp = 0
	for i in range(0,len(arr)):
		for j in range(1,len(arr)-i):
			if arr[j-1] > arr[j]:
				temp = arr[j-1]
				arr[j-1] = arr[j]
				arr[j] = temp

def main():
	arr = [9,2,1,3,5]
	bubbleSort(arr)
	print arr

if __name__ == '__main__':
	main()