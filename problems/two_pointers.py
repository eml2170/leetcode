# https://leetcode.com/problems/valid-palindrome/submissions/
def isPalindrome(s: str) -> bool:
    # O(n) space
    # cleaned = list(filter(lambda x: x.isalnum(), s.lower()))
    # return cleaned == cleaned[::-1]

    start, end = 0, len(s) - 1
    while start < end:
        while not s[start].isalnum() and start < end:
            start += 1

        while not s[end].isalnum() and start < end:
            end -= 1

        if s[start].lower() != s[end].lower():
            return False

        start += 1
        end -= 1
    return True

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
def twoSumNoSpace(numbers: list[int], target: int) -> list[int]:
    i, j = 0, len(numbers) - 1
    while i < j:
        sum_ij = numbers[i] + numbers[j]
        if sum_ij == target:
            return [i,j]
        elif sum_ij < target:
            i += 1
        else:
            j -= 1

# https://leetcode.com/problems/3sum/
def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()
    for i in range(len(nums) - 1):
        if i > 0 and nums[i] == nums[i - 1]:
            # skip past initial duplicates
            continue

        # find two_sum(-nums[i])
        target = -1 * nums[i]

        # only need to look to the right since we've already considered the left
        start = i + 1
        end = len(nums) - 1

        while start < end:
            twosum = nums[start] + nums[end]

            if twosum < target:
                start += 1

            elif twosum > target:
                end -= 1

            else:
                res.append([nums[i], nums[start], nums[end]])
                # skip past duplicates
                while start < end and nums[start] == nums[start + 1]:
                    start += 1
                while start < end and nums[end] == nums[end - 1]:
                    end -= 1

                start += 1
                end -= 1
    return res

# https://leetcode.com/problems/3sum-closest/
def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort()

    min_delta = float("inf")
    for i in range(len(nums)):
        left, right = i + 1, len(nums) - 1

        while left < right:
            x = nums[i] + nums[left] + nums[right]

            if abs(target - x) < abs(min_delta):
                min_delta = target - x

            if x == target:
                return x
            elif x < target:
                left += 1
            else:
                right -= 1

    return target - min_delta


# https://leetcode.com/problems/container-with-most-water/
def maxArea(height: list[int]) -> int:
    l, r = 0, len(height) - 1
    max_area = 0
    while l < r:
        area = (r - l) * min(height[l], height[r])
        if area > max_area:
            max_area = area

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area

# https://leetcode.com/problems/move-zeroes/
def move_zeros_in_place(nums: list[int]) -> None:
    l, r = 0, 0
    while r < len(nums):
        if nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
        r += 1