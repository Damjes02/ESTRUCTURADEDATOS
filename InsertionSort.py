
def insertionSort(arr):


	for i in range(1, len(arr)):

		key = arr[i]
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key



arr = [18, 108, 41, 10, 8, 17, 23, 21, 69, 89, 1000, 257, 3003, 4, 7, 30]
insertionSort(arr)
for i in range(len(arr)):
	print ("% d" % arr[i])
