def bSearch(n, arr, start, end):
	if start > end:
		return -1
	mid = (start + end) / 2
	if n == arr[mid]:
		return mid
	if n > arr[mid]:
		return bSearch(n, arr, mid+1, end)
	return bSearch(n, arr, start, mid-1)

def main():
	arr = [1,2,3,4,5,6,7,8,9,10]
	print bSearch(7, arr, 0, len(arr))

if __name__ == '__main__':
	main()