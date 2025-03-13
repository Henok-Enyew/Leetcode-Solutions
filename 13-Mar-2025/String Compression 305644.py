# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        left,right,count = 0,0,0
        while right < len(chars):
            chars[left] = chars[right]
            while right < len(chars) and chars[left] == chars[right]:
                count+=1
                right+=1
            left+=1
            if count>1:
                if count > 9:
                    st = str(count)
                    for s in st:
                        chars[left] = s
                        print(chars[left])
                        left+=1
                    
                else:
                    chars[left] = str(count)
                    left+=1
            count=0
        return left