#bubblesort followed from geeksforgeeks.org's example.
def bubbleSort(arr):
    n = len(arr)

    #go trhough all array elements
    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test above
arr = [99, 69, 48, 9, 33, 1, 87, 121, 43]

bubbleSort(arr) #sorts the array
arr.pop(-1) #pops the -1th item
arr.append(1000) #adds 1000 to the array



arr.reverse() #reverses the array
arr.append(290) #adds 290 to the array



bubbleSort(arr) # sorts the array 

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),
