class MedianFinder:
    def __init__(self):
        self.numbers = []
        self.length = 0

    def addNum(self, num: int) -> None:
        self.numbers.append(num)
        self.length += 1

    def findMedian(self) -> float:
        self.numbers.sort()
        if self.length % 2 == 0:
            # even
            return sum(self.numbers[self.length // 2 - 1:self.length // 2 + 1]) / 2
        else:
            return self.numbers[self.length // 2]


mf = MedianFinder()
mf.addNum(-1)
mf.addNum(-2)
mf.addNum(-3)
mf.findMedian()
