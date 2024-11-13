from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = defaultdict(list)
        
        for word in strs:
            char_count = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                char_count[index] += 1
            key = tuple(char_count)
            
            anagrams_map[key].append(word)
        
        return list(anagrams_map.values())