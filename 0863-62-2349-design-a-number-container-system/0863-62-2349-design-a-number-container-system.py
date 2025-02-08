from sortedcontainers import SortedList

class NumberContainers:
    def __init__(self):
        self.index_to_num = {}
        self.num_to_indices = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_num:
            old_num = self.index_to_num[index]
            self.num_to_indices[old_num].discard(index)
            if not self.num_to_indices[old_num]:
                del self.num_to_indices[old_num]
        
        self.index_to_num[index] = number
        if number not in self.num_to_indices:
            self.num_to_indices[number] = SortedList()
        self.num_to_indices[number].add(index)

    def find(self, number: int) -> int:
        if number in self.num_to_indices and self.num_to_indices[number]:
            return self.num_to_indices[number][0]
        return -1