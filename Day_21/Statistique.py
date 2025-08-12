from collections import Counter
import math

class Statistique:
    def __init__(self, data):
        self.data = sorted(data)
    
    def count(self):
        return len(self.data)
    
    def sum(self):
        return sum(self.data)
    
    def min(self):
        return min(self.data)
    
    def max(self):
        return max(self.data)
    
    def range(self):
        return self.max() - self.min()
    
    def mean(self):
        return round(self.sum() / self.count(), 1)
    
    def median(self):
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return round((self.data[mid - 1] + self.data[mid]) / 2, 1)
        else:
            return self.data[mid]
    
    def mode(self):
        freq = Counter(self.data)
        mode_val, count = freq.most_common(1)[0]
        return {'mode': mode_val, 'count': count}
    
    def var(self):
        m = self.mean()
        return round(sum((x - m) ** 2 for x in self.data) / self.count(), 1)
    
    def std(self):
        return round(math.sqrt(self.var()), 1)
    
    def freq_dist(self):
        freq = Counter(self.data)
        total = self.count()
        return [(round((count / total) * 100, 1), value) for value, count in freq.items()]
    
    def describe(self):
        return {
            'Count': self.count(),
            'Sum': self.sum(),
            'Min': self.min(),
            'Max': self.max(),
            'Range': self.range(),
            'Mean': self.mean(),
            'Median': self.median(),
            'Mode': (self.mode()['mode'], self.mode()['count']),
            'Variance': self.var(),
            'Standard Deviation': self.std(),
            'Frequency Distribution': self.freq_dist()
        }
