from problems.arrays_strings import (
    contains_duplicate,
    is_anagram,
    two_sum,
    group_anagrams,
    top_k_frequent,
    product_except_self,
    longest_consecutive,
    encode,
    decode
)

def test_contains_duplicate():
    nums = [1, 2, 3, 1]
    assert contains_duplicate(nums) is True

def test_is_anagram():
    s = "anagram"
    t = "nagaram"
    assert is_anagram(s, t) is True

def test_two_sum():
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum(nums, target) == [0, 1]

def test_group_anagrams():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(strs)
    # Sort for consistent comparison
    result = [sorted(group) for group in result]
    result.sort(key=lambda x: x[0])
    
    expected = [["bat"], ["eat", "tea", "ate"], ["tan", "nat"]]
    expected = [sorted(group) for group in expected]
    expected.sort(key=lambda x: x[0])
    
    assert result == expected

def test_top_k_frequent():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    assert set(top_k_frequent(nums, k)) == {1, 2}

def test_product_except_self():
    nums = [1, 2, 3, 4]
    assert product_except_self(nums) == [24, 12, 8, 6]

def test_longest_consecutive():
    nums = [100, 4, 200, 1, 3, 2]
    assert longest_consecutive(nums) == 4

def test_encode_decode():
    original = ["Hello", "World"]
    encoded = encode(original)
    decoded = decode(encoded)
    assert decoded == original
