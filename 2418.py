class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        persons = list(zip(names, heights))

        persons.sort(key=lambda x: x[1], reverse=True)

        sorted_persons = [name for name, height in persons]

        return sorted_persons