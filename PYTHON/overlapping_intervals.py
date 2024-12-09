'''
Given an array of Intervals arr[][], where arr[i] = [starti, endi]. The task is to merge all of the overlapping Intervals.

Examples:

Input: arr[][] = [[1,3],[2,4],[6,8],[9,10]]
Output: [[1,4], [6,8], [9,10]]
Explanation: In the given intervals we have only two overlapping intervals here, [1,3] and [2,4] which on merging will become [1,4]. Therefore we will return [[1,4], [6,8], [9,10]].

Input: arr[][] = [[6,8],[1,9],[2,4],[4,7]]
Output: [[1,9]]
Explanation: In the given intervals all the intervals overlap with the interval [1,9]. Therefore we will return [1,9].

Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ starti ≤ endi ≤ 105
'''

def mergeOverlap(arr):
		#Code here
		# Step 1: Sort the intervals based on the starting times
    arr.sort(key=lambda x: x[0])
        
        # Step 2: Initialize the merged list
    merged = []
        
    for interval in arr:
            # If merged is empty or there is no overlap, add the interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
                # There is an overlap, merge the current interval with the last one
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

arr = [[1,3],[2,4],[6,8],[9,10]]
print(mergeOverlap(arr))

"""
sorting it is a big deal and very helpful , and we sorted as per the fist element of a interval . 
so that we dont need to like check each interval with every other interval (nested for) , we just simply 
check if overlap or not , since [i] is in sorted and if [i] of next is smaller than [j] of previous then overlap 
so merged may we have new elements , and each time before putting the next interval we just check if that next interval is 
overlapping with the previous or not , if not then directly put it in , else make the last/previous one updated 
and in that previous one only the [j] will be updated , since [i] is already in order/sorted , so smaller [i] is in the previous one 
and we only play with the last interval of the megred list , since sorted hai thus no tension that overlapping 
interval will occour later or where , etc ...
"""

class Solution:
    @classmethod
    def mergeOverlap(self, arr):
		#Code here
		# Step 1: Sort the intervals based on the starting times
        arr.sort(key=lambda x: x[0])
        
        # Step 2: Initialize the merged list
        merged = []
        
        for interval in arr:
            # If merged is empty or there is no overlap, add the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There is an overlap, merge the current interval with the last one
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

print(Solution.mergeOverlap(arr))

#same as above , just here we wrote that funciton inside a class (making it a method) and then simply called that class method .

