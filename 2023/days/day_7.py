from abstract_day import AbstractDay


def five(h, js):
    if len(h) == 0:
        return True
    for c in h:
        if h.count(c) == 5 - js:
            return True
    return False


def four(h, js):
    return five(h, js + 1)


def house(h, js):
    for c in h:
        for j in range(1 + js):
            if h.count(c) == 3 - j:
                p = h.replace(c, "")
                if p[0] == p[1] or js - j > 0:
                    return True
    return False


def three(h, js):
    return five(h, js + 2)


def two_pairs(h, js):
    if js >= 1:
        return pair(h, 0)
    for c in h:
        if h.count(c) == 2:
            h_ = h.replace(c, "")
            for c_ in h_:
                if h_.count(c_) == 2:
                    return True
    return False


def pair(h, js):
    return five(h, js + 3)


def high(h, js):
    return True


def score(h, wilds):
    fs = [five, four, house, three, two_pairs, pair, high]
    for i, f in enumerate(fs):
        to_replace = "J" if wilds else " "
        if f(h.replace(to_replace, ""), h.count(to_replace)):
            return len(fs) - i


class Day7(AbstractDay):
    def part1(self):
        return self._solve(
            ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"],
            False
        )

    def part2(self):
        return self._solve(
            ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"],
            True
        )

    def _solve(self, order, wilds):
        ranks = {c: len(order) - i for i, c in enumerate(order)}
        scores = []
        for line in self.lines:
            hand, bid = line.split(" ")
            rs = tuple([ranks[d] for d in hand])
            scores.append((score(hand, wilds), *rs, int(bid)))
        scores.sort(reverse=True)
        ans = 0
        for i, s in enumerate(scores):
            ans += s[-1] * (len(scores) - i)
        return ans
