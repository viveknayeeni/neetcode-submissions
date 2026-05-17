class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            word_sorted = tuple(sorted(word))
            if word_sorted not in d:
                d[word_sorted] = [word]
            else:
                d[word_sorted].append(word)
        return list(d.values())

            