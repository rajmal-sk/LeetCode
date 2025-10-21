class RandomizedSet:

    def __init__(self):
        self.mp = defaultdict()

    def insert(self, val: int) -> bool:
        if self.mp.get(val) is not None:
            return False
        else:
            self.mp[val] = True
            # arr.append(val)
            return True

    def remove(self, val: int) -> bool:
        if self.mp.get(val) is None:
            return False
        else:
            del self.mp[val]
            return True

    def getRandom(self) -> int:
        keys = list(self.mp.keys())
        return random.choice(keys)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()