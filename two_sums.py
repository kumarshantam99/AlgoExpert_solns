# Return two numbers in an array thbat add upto a target value

def twoNumberSum(array, targetSum):
    # Write your code here.
	
	lookup={}
	for num in array:
		if targetSum-num in lookup:
			return [targetSum-num,num]
		lookup[num]=True
	return []

# Time Complexity: O(n) Space Complexity: O(n)


def twoNumberSum2(array, targetSum):
    # Write your code here.
	
	array.sort() #O(logn) complexity
    left=0
    right=len(array)-1

    while left<right:
        currenSum=array[left]+array[right]
        if currenSum==targetSum:
            return [array[left],array[right]]
        elif currenSum<targetSum:
            left+=1
        else:
            right-=1
    return []

# Time complexity: O(nlogn) Space Complexity: O(1)




