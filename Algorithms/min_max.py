class MinMax:
    def __init__(self, a, low, high):
        self.min = None
        self.max = None
        self.a = a
        self.low = low
        self.high = high

    def minMax(self, low=None, high=None):
        if low is None:
            low = self.low
        if high is None:
            high = self.high

        if low == high:
            self.min = self.a[low]
            self.max = self.a[low]

        elif low == high - 1:
            if self.a[low] < self.a[high]:
                self.min = self.a[low]
                self.max = self.a[high]
            else:
                self.min = self.a[high]
                self.max = self.a[low]

        else:
            mid = (low + high) // 2
            min1 = max1 = None

            self.minMax(low, mid)

            min1, max1 = self.min, self.max
            self.minMax(mid + 1, high)

            if min1 < self.min:
                self.min = min1
            if max1 > self.max:
                self.max = max1

def main():
    a = list(map(int, input('Enter space separated array items: ').split()))
    minMax = MinMax(a, 0, len(a)-1)
    minMax.minMax()
    print('Min:', minMax.min)
    print('Max:', minMax.max)

if __name__ == '__main__':
    main()