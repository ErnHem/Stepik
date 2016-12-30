class MoneyBox:
    def __init__(self, capacity):
        self.max = capacity
        self.sum = 0
    def can_add(self, v):
        if (v+self.sum) > self.max:
            return False
        else:
            return True
    def add(self, v):
        if self.can_add(v)==True:
            self.sum += v
            return
        else:
            return
