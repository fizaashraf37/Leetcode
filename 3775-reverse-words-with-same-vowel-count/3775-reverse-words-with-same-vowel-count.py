class Solution:
    def reverseWords(self, s: str) -> str:

        ans = s.split(" ")
        first_vowels_count = self.count_vowels(ans[0])

        for i in range(1, len(ans)):
            if self.count_vowels(ans[i]) == first_vowels_count:
                ans[i] = ans[i][::-1]

        return " ".join(ans)

    def count_vowels(self, s: str) -> int:
        vowels_count = 0
        for char in s:
            if char in "aeiou":
                vowels_count += 1
        return vowels_count
        