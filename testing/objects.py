import random;

class Counter:
    def __init__(self):
        self.count = 0
        self.addCount = 0

    def add(self):
        self.count += random.randint(1,10)
        self.addCount += 1

    def sub(self):
        self.count -= 1

    def getCount(self):
        return self.count

    def getAverage(self):
        return self.count/self.addCount


a = Counter()
a.add()
a.add()
print(a.getCount())
print(a.getAverage())
