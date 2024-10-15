class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map = {}
        result = []
        min_sum = float('inf')  

        for i in range(len(list1)):
            map[list1[i]] = i

        for i in range(len(list2)):
            if list2[i] in map:
                index_sum = i + map[list2[i]] 

                if index_sum < min_sum:  
                    min_sum = index_sum
                    result = [list2[i]]  

                elif index_sum == min_sum: 
                    result.append(list2[i])
        return result
