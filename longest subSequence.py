#:: find the longest sub sequence in an array given
def LIS(array):
    lenghtOfArray = len(array) #lenght og the array
    lisCalculator = [1]*lenghtOfArray  #initialize the a claculator to 1
    longestSubSequence = 0

    for i in range(1, lenghtOfArray):   # for each variable in the array
        for j in range(i):   #find the lenght longest sub sequence by comparison
            if array[i] > array[j] and lisCalculator[i] < lisCalculator[j] + 1:
                lisCalculator[i] = lisCalculator[j] + 1

    for i in range(lenghtOfArray):
        if longestSubSequence < lisCalculator[i]:
            longestSubSequence = lisCalculator[i]
    return longestSubSequence


a = [10, 22, 9, 33, 21, 50, 41, 60]
print(LIS(a))
