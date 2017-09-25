class Collector:
    def __init__(self):
        self.default = {}

    def collect(self, product, characteristic):
        if product not in self.default: self.default[product] = CharacteristicsCollector()
        self.default[product].collect(characteristic)

    def addCollector(self, product, collector):
        for k,v in collector.data.items():
            self.collect(product, k)

    def calculate_total(self):
        res = CharacteristicsCollector()
        for product, characteristics_collector in self.default.items():
            for characteristic, counts in characteristics_collector.data.items():
                res.collect(characteristic, count=counts)
        return res.data

class CharacteristicsCollector:
    def __init__(self):
        self.data = {}

    def collect(self, characteristic, count=1):
        if characteristic not in self.data: self.data[characteristic] = 0
        self.data[characteristic] += count