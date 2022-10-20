class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_dict = collections.Counter(words)
        words_dict = {key: value for key, value in sorted(words_dict.items())}
        res = []
        while len(res) < k:
            max_key = max(words_dict, key=words_dict.get)
            res.append(max_key)
            words_dict.pop(max_key)

        return res