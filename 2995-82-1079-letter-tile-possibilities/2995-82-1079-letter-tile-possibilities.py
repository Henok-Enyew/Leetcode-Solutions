from itertools import permutations

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        unique_sequences = set()
        for length in range(1, len(tiles) + 1):
            for seq in permutations(tiles, length):
                unique_sequences.add(seq)
        return len(unique_sequences)