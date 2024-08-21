class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mh = 0
        h = 0
        for i in range(len(gain)):
            h += gain[i]
            mh = max(mh, h)
        return mh
            