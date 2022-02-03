def maxProfit(self, prices: List[int]) -> int:
    min = prices[0]
    max = prices[0]
    min2 = prices[0]       #min2 的最大的作用就是在保证了最大“跨度”的情况下保留继续寻找最小值的可能性
    flag = 0             #flag 的作用是让程序分辨是否有min2存在的情况，如果没有min2，在之后的遍历中不需要每一次遍历都求最大值和最小值的差值
    currentDiff = 0
    testDiff = 0
    for i in range(len(prices)):
        if (prices[i] < min and flag == 0):
            min2 = prices[i]
            flag = 1
        if (max < prices[i] and flag == 0):     
            max = prices[i]
            currentDiff = prices[i] - min
        if (max < prices[i] and flag == 1):
            max = prices[i]
            min = min2
            flag = 0
            currentDiff = prices[i] - min
        if (max > prices[i] and flag == 1):
            testDiff = prices[i] - min2
            if (testDiff > currentDiff):
                min = min2
                max = prices[i]
                flag = 0
                currentDiff = testDiff
    return currentDiff