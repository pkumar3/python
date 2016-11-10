def selSort(arr):
	for i in range(0,len(arr)-1):
		small = i
		for j in range(i+1,len(arr)):
			if arr[j] < arr[small]:
				small = j
		temp = arr[i]
		arr[i] = arr[small]
		arr[small] = temp

def main():
	arr = [9,2,3,5,1]
	selSort(arr)
	print arr

if __name__ == '__main__':
	main()