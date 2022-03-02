<<<<<<< HEAD
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
            return max(max_count, count)

 
# Alternate Solution, above sol has less memory and less runtime

def findMaxCounsecutiveOnes(self, nums: List[int]) -> int:
    map(len, ''.join(map(str, num)).split('0'))
        
        
=======
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
            return max(max_count, count)

 
# Alternate Solution, above sol has less memory and less runtime

def findMaxCounsecutiveOnes(self, nums: List[int]) -> int:
    map(len, ''.join(map(str, num)).split('0'))
        
        
>>>>>>> 2d8319d170ef6f026fca7327b39a71e5297cfca9
