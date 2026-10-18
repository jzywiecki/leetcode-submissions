class MyHashSet:

    def __init__(self):
        self.internal_set = []

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        self.internal_set.append(key)

    def remove(self, key: int) -> None:
        to_remove = -1
        for i in range(len(self.internal_set)):
            if self.internal_set[i] == key:
                to_remove = i
        
        if to_remove != -1:
            del self.internal_set[to_remove]

    def contains(self, key: int) -> bool:
        for k in self.internal_set:
            if key == k:
                return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)