<<<<<<< HEAD
# my solution
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                even_count += 1
        return even_count
# another solution
def findNumbers(self, nums: List[int]) -> int:
=======
# my solution
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                even_count += 1
        return even_count
# another solution
def findNumbers(self, nums: List[int]) -> int:
>>>>>>> 2d8319d170ef6f026fca7327b39a71e5297cfca9
    return sum(len(str(num)) % 2 == 0 for num in nums)