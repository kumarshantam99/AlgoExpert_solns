# Write whatever you want here.

# Given a sorted array, print a sorted array of square of each elements in the array.

# If array has positive elements the output array will be sorted by default.

# Not a case with array containing negative elements: 1. Square the array and then sort it making the time complexity to be O(nlogn) 2. have two pointers tracking the highest and lowest in the array, square the value that has the highest absolute value amongst the two and then insert that to the right of the output array


def sortedSquaredArray(array):
    # Write your code here.
    low = 0
    high = len(array)-1
    output_i = len(array)-1
     output = [None]*(output_i+1)
      while output_i >= 0:
           if abs(array[high]) > abs(array[low]):

                output[output_i] = (array[high])**2
                output_i -= 1
                high -= 1
            else:
                output[output_i] = (array[low])**2
                output_i -= 1
                low += 1

    return output


# Time Complexity: O(n) Space complexity: O(n)

