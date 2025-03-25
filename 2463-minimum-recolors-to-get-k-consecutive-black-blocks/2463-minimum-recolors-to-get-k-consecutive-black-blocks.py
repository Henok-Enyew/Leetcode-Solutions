class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        mp = collections.Counter(blocks[:k])
        whites = mp['W']
        blacks = mp['B']
        minimum = whites
        left , right = 1,k
        print(whites,blacks,minimum)
        while right < len(blocks) and right - left == k-1:
            if blocks[right] == 'W' :
                whites +=1
            else:
                blacks+=1
            if blocks[left-1] == 'W':
                whites-=1
            else:
                blacks-=1
            minimum = min(minimum, whites)
            left+=1
            right+=1
            print(minimum)
        return minimum