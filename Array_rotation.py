def leftRotate(arr,d,n):
	for i in range(d):
		leftRotateByOne(arr,n)


def leftRotateByOne(arr,n):
	temp =arr[0]
	for i in range(n-1):
	    arr[i] = arr[i+1]
	arr[n-1] = temp

def printArray(arr,n):
	for i in range(n):
	     print("%d"% arr[i],end=" ")



arr = [1,2,3,4,5,6]
leftRotate(arr,5,6)
printArray(arr, 6)
