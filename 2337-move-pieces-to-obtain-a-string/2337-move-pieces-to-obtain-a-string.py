class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace('_', '') != target.replace('_', ''):
            return False
        start_L = [i for i, c in enumerate(start) if c == 'L']
        target_L = [i for i, c in enumerate(target) if c == 'L']
        start_R = [i for i, c in enumerate(start) if c == 'R']
        target_R = [i for i, c in enumerate(target) if c == 'R']
        if any(s < t for s, t in zip(start_L, target_L)):
            return False
        if any(s > t for s, t in zip(start_R, target_R)):
            return False
        return True
