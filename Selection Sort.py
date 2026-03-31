class Solution:
    def sortArray(self, nums):
        def findSmallest(nums):
            smallest = nums[0]
            smallest_index = 0
            for i in range(1,len(nums)):
                if nums[i] < smallest:
                    smallest = nums[i]
                    smallest_index = i
            return smallest_index

        def selectionSort(nums):
            newArr = []
            copiedArr = list(nums)
            for i in range(len(nums)):
                smallest = findSmallest(copiedArr)
                newArr.append(copiedArr.pop(smallest))
            return newArr
        return selectionSort(nums)

sol = Solution()
result = sol.sortArray([5,2,3,1])
print(result)
