# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:

    def __init__(self):
        self.mp_count = collections.Counter()
        self.mp_freq = collections.Counter()

    def add(self, number: int) -> None:
        prev = self.mp_freq[number]
        self.mp_freq[number] += 1
        new = self.mp_freq[number]

        self.mp_count[prev] -=1
        self.mp_count[new] +=1 
    def deleteOne(self, number: int) -> None:
        if self.mp_freq[number] > 0:
            prev = self.mp_freq[number]
            self.mp_freq[number] -= 1
            new = self.mp_freq[number]

            self.mp_count[prev] -=1
            self.mp_count[new] +=1 

    def hasFrequency(self, frequency: int) -> bool:
        return self.mp_count[frequency] > 0
# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)