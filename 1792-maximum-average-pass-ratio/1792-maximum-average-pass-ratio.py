import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Helper function to calculate the improvement in pass ratio when adding one student
        def improvement(passed, total):
            return (passed + 1) / (total + 1) - passed / total
        
        # Max-heap to prioritize classes by improvement
        max_heap = []
        for passed, total in classes:
            heapq.heappush(max_heap, (-improvement(passed, total), passed, total))
        
        # Assign extra students
        for _ in range(extraStudents):
            gain, passed, total = heapq.heappop(max_heap)
            passed += 1
            total += 1
            heapq.heappush(max_heap, (-improvement(passed, total), passed, total))
        
        # Calculate the final average pass ratio
        total_ratio = 0
        for _, passed, total in max_heap:
            total_ratio += passed / total
        
        return total_ratio / len(classes)
