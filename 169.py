class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        val = None
        for num in nums:
            if val is None:
                val = num
                count += 1
            else:
                if num == val:
                    count += 1
                else:
                    count -= 1
            if count == 0:
                val = None
        return val


# Every time an element a_i = j of the data-stream is observed,

# If the key is empty we set the value of the key to j, and we initialize the count to 1.
# If the key is not empty, and equal to j, we increment the count by 1.
# If the key is not empty, and not equal to j, we decrement the count by 1
# If the count becomes zero as a result of this decrementing, we set the key to null-entity.
            
