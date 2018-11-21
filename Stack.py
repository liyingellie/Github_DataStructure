################# Customized Stack
class Item(object):
    def __init__(self, val):
        assert isinstance(val, (int, float)), '%s is not a number!' % val
        self.val = val
        self.maxVal = None


class MaxStack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def getMax(self):
        if not self.isEmpty():
            return self.top().maxVal

    def push(self, val):
        item = Item(val)

        if self.isEmpty():
            item.maxVal = val
        else:
            preTop = self.top()
            item.maxVal = max(preTop.maxVal, val)
            self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


s = MaxStack()

print(s.isEmpty())

for v in (3, 1, 5, 2, 9, 2, 4, 11):
    s.push(v)
    print('size=%s, max=%s' % (s.size(), s.getMax()))

print('### Remove element from stack...')
while not s.isEmpty():
    s.pop()
    print('size=%s, max=%s' % (s.size(), s.getMax()))
