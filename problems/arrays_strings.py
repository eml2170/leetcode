import json
from collections import defaultdict


# https://leetcode.com/problems/contains-duplicate/
def contains_duplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

# https://leetcode.com/problems/valid-anagram/
def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# https://leetcode.com/problems/two-sum/
def two_sum(nums: list[int], target: int) -> list[int]:
    nums_set = {num: idx for num, idx in zip(nums, range(len(nums)))}
    for i, num in enumerate(nums):
        if target - num in nums_set and i != nums_set[target-num]:
            return [i, nums_set[target - num]]

# https://leetcode.com/problems/group-anagrams/
def group_anagrams(strs: list[str]) -> list[list[str]]:
    def _get_freq(s):
        freq = {}
        for c in sorted(s):
            freq[c] = freq.get(c, 0) + 1
        return json.dumps(freq)
    
    letter_freqs = defaultdict(list)
    for word in strs:
        freq = _get_freq(word)
        letter_freqs[freq].append(word)
    return list(letter_freqs.values())

# https://leetcode.com/problems/top-k-frequent-elements/
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    freq_counts = {}
    for num in nums:
        freq_counts[num] = freq_counts.get(num, 0) + 1

    arr = [[] for _ in range(len(nums) + 1)]
    for x, freq in freq_counts.items():
        arr[freq].append(x)

    out = []
    for i in range(len(arr) - 1, 0, -1):
        for x in arr[i]:
            out.append(x)
            if len(out) == k:
                return out

# https://leetcode.com/problems/product-of-array-except-self/
def product_except_self(nums: list[int]) -> list[int]:
    #         prefix_products = [1] * len(nums)
    #         suffix_products = [1] * len(nums)

    #         prefix = 1
    #         for i in range(len(nums)):
    #             prefix_products[i] = prefix
    #             prefix *= nums[i]

    #         suffix = 1
    #         for i in range(len(nums) - 1, -1, -1):
    #             suffix_products[i] = suffix
    #             suffix *= nums[i]

    #         return [p*s for p, s in zip(prefix_products, suffix_products)]

    products = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        products[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        products[i] *= suffix
        suffix *= nums[i]

    return products

# https://leetcode.com/problems/longest-consecutive-sequence/
def longest_consecutive(nums: list[int]) -> int:
    longest = 0
    nums_set = set(nums)
    for num in nums:
        if num - 1 not in nums_set:
            # start of sequence
            candidate = 1
            x = num + 1
            while x in nums_set:
                candidate += 1
                x += 1
            if candidate > longest:
                longest = candidate
    return longest

# https://leetcode.com/problems/encode-and-decode-strings/
def encode(strs: list[str]) -> str:
    """Encodes a list of strings to a single string.
    """
    return "".join([f"{len(x)}#{x}" for x in strs])

def decode(s: str) -> list[str]:
    """Decodes a single string to a list of strings.
    """
    strs = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        strs.append(s[j + 1:j + 1 + length])
        i = j + 1 + length
    return strs