#given two non-empty arrays, determine whteher the second array is a subsequence of the first array.

def isValidSubsequence(array,sequence):
    seqPointer=0
	for value in array:
		if seqPointer==len(sequence):
			break
		if sequence[seqPointer]==value:
			seqPointer+=1
	return seqPointer==len(sequence)


# Time Complexity: O(N) space complexity: O(1)