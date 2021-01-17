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


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        n = len(nums)
        for key in hashmap:
            if hashmap[key] > n / 2:
                return key



from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return count.most_common(1)[0][0]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sort first
        nums.sort()

        start = 0
        end = len(nums) - 1
        mid = start + (end - start) // 2
        target = nums[mid]

        return target

        # if the question was if there is a majority element..then below approach...

        # first binary search to look for start of the target num
        end = mid - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        start_idx = start
        # 2nd binary search for end index of the target num
        start = start + (end - start) // 2 + 1
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1

        end_idx = end

        target_count = end_idx - start_idx + 1
        return target if target_count > len(nums) / 2 else False
