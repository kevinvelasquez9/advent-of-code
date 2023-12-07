from abstract_day import AbstractDay


def _is_nice1(s: str) -> bool:
    vowels = set([v for v in "aeiou"])
    bad = set("ab,cd,pq,xy".split(","))
    num_vowels, has_twice = 0, False
    for i, c in enumerate(s):
        if c in vowels:
            num_vowels += 1
        if i < len(s) - 1:
            cc = s[i:i + 2]
            if cc == cc[::-1]:
                has_twice = True
            if cc in bad:
                return False
    return num_vowels >= 3 and has_twice


def _is_nice2(s: str) -> bool:
    pairs = {}
    has_pairs, has_sandwich = False, False
    for i, c in enumerate(s):
        if i < len(s) - 2 and c == s[i + 2]:
            has_sandwich = True
        if i < len(s) - 1:
            letters = s[i:i + 2]
            if letters not in pairs:
                pairs[letters] = i + 1
            elif i != pairs[letters]:
                has_pairs = True
    return has_pairs and has_sandwich


class Day5(AbstractDay):
    def part1(self):
        nice = 0
        for line in self.lines:
            nice += 1 if _is_nice1(line) else 0
        return nice

    def part2(self):
        nice = 0
        for line in self.lines:
            nice += 1 if _is_nice2(line) else 0
        return nice
