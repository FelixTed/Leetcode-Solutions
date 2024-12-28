class Solution(object):
    def maximumPopulation(self, logs):
        minYear = 2051
        maxYear = 0

        for element in logs:
            for year in element:
                minYear = min(year,minYear)
                maxYear = max(year,maxYear)

        maxPeople = 0
        year = minYear
        for i in range(minYear, maxYear + 1):
            count = 0
            for person in logs:
                if i >= person[0] and i < person[1]:
                    count+=1
            if count > maxPeople:
                year = i
                maxPeople = count
        return year
        """
        :type logs: List[List[int]]
        :rtype: int
        """
    