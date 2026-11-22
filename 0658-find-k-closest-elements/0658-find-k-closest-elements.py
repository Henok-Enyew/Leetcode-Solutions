class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        low = 0
        
        high = len(arr) - k
        
        while low < high:
            
            mid = low + (high-low)//2
            
            if x<=arr[mid]:
                
                high=mid
                
            elif arr[mid+k]<=x:
                
                low = mid+1
                
            else:
                
                middist = abs(x-arr[mid])
                
                midkdist = abs(x-arr[mid+k])
                
                if middist <= midkdist:
                    
                    high=mid
                    
                else:
                    
                    low=mid+1
            
                    
        return arr[low:low+k]