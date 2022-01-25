class Solution:
    def validMountainArray(self, arr):
        length = len(arr)
        if(length < 3):
            return False
        for i in range(length):
            if(i == length - 1):
                return False
            if(arr[i+1] < arr[i]):
                if(i == 0):
                    return False
                if(i == len(arr) - 1):
                    return False
                for j in range(i, len(arr)-1):
                    if(arr[j+1] >= arr[j]):
                        return False
                return True
            if(arr[i+1] == arr[i]):
                return False