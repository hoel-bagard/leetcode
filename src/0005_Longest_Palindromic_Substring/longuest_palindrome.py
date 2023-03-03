from typing_extensions import Self


class Solution:
    @staticmethod
    def palindrome_length_with_center(string: str, center_left_idx: int, center_right_idx: int) -> int:
        left, right = center_left_idx, center_right_idx
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left, right = left - 1, right + 1
        return right - left - 1

    def longestPalindrome(self: Self, s: str) -> str:  # noqa: N802
        start, end = 0, 0
        for center in range(0, len(s)):
            length_odd = self.palindrome_length_with_center(s, center, center)
            length_even = self.palindrome_length_with_center(s, center, center+1)
            length = max(length_odd, length_even)
            if length > end - start:
                start = center - (length-1) // 2
                end = center + length // 2 + 1

        return s[start:end]


class SolutionBruteForce:
    @staticmethod
    def is_palindrome(string: str) -> bool:
        half_length, is_odd = divmod(len(string), 2)
        return string[:half_length] == string[half_length+is_odd:][::-1]

    def longestPalindrome(self: Self, s: str) -> str:  # noqa: N802
        for window_length in range(len(s)+1, 1, -1):
            for start in range(0, len(s)+1-window_length):
                if self.is_palindrome(substring := s[start:start+window_length]):
                    return substring
        return s[0] if len(s) else ""
