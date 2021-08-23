class Solution:
    def mergeSort(self,array):
        if len(array) > 1:
            mid = len(array) //2
            left = array[mid:]
            right = array[:mid]

            self.mergeSort(left)
            self.mergeSort(right)

            i = j = k = 0;

            while i < len(left) and j < len(right):
                if(left[i] < right[j]):
                    array[k] = left[i]
                    i +=1
                else:
                    array[k] = right[j]
                    j +=1
                k +=1
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1


s = Solution()
array = [9,10,1,89,12,5,43,2]
s.mergeSort(array)
print(array)