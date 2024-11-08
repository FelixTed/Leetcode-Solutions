class Solution(object):
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        print(intervals)
        newIntervals = []

        currentInterval = [intervals[0][0],intervals[0][1]]
        for i in range(len(intervals)-1):
            currentEl = max(intervals[i][1],currentInterval[1])
            nextEl = intervals[i+1][0]
            if currentEl >= nextEl:
                currentInterval[1] = max(intervals[i+1][1],currentInterval[1])
            else:
                newIntervals.append(currentInterval)
                currentInterval = [intervals[i+1][0],intervals[i+1][1]]
        newIntervals.append(currentInterval)
        return newIntervals
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        