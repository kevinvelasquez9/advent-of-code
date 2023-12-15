from collections import defaultdict

from abstract_day import AbstractDay


def get_hash(s):
    ans = 0
    for c in s:
        ans = (ans + ord(c)) * 17 % 256
    return ans


def power(box, slot, focal):
    return (box + 1) * (slot + 1) * focal


class Day15(AbstractDay):
    def part1(self):
        steps = self.data.split(",")
        return sum([get_hash(s) for s in steps])

    def part2(self):
        steps = self.data.split(",")
        boxes = defaultdict(list)
        for s in steps:
            if s.endswith("-"):
                lens = s[:-1]
                h = get_hash(lens)
                boxes[h] = [t for t in boxes[h] if t[0] != lens]
            else:
                lens, focal = s.split("=")
                focal = int(focal)
                h = get_hash(lens)
                boxes[h] = [(lens, focal) if t[0] == lens else t for t in boxes[h]]
                if not any(t[0] == lens for t in boxes[h]):
                    boxes[h].append((lens, focal))

        return sum(
            [power(box, slot, focal) for box, slots in boxes.items() for slot, (lens, focal) in enumerate(slots)]
        )
