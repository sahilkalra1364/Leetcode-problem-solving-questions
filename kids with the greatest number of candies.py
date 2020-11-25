class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        li=[]
        import math
        lar=-math.inf
        for i in candies:
            if i>lar:
                lar=i     
        for i in candies:
            if i+extraCandies>=lar:
                li.append(True)
            else:
                li.append(False)
        return li        
                
        
