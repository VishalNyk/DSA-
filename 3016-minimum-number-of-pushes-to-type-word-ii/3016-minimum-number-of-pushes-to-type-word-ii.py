from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        frequencies = Counter(word)
        sorted_freqs = sorted(frequencies.values(), reverse=True)
        
        pushes = 0
        for index, freq in enumerate(sorted_freqs):
            pushes_per_letter = (index // 8) + 1
            pushes += freq * pushes_per_letter
            
        return pushes
