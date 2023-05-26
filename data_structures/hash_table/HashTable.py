class HashTable:
    def __init__(self) -> None:
        self.table = [[] for _ in range(1000000)]
    
    def insert(self, value):
        if self.search(value) is False:
            index = self._hash_function(value)
            self.table[index].append(value)
        
    def remove(self, value):
        if self.search(value):
            index = self._hash_function(value)
            self.table[index].remove(value)

    def search(self, value):
        index = self._hash_function(value)
        for i in range(len(self.table[index])):
            if self.table[index][i] == value:
                return True
        return False

    def _hash_function(self, value):
        return value % 1000000
    
hash_table = HashTable()
print("*************************")
print(1024, hash_table.search(1024))
print(124, hash_table.search(124))
print(24, hash_table.search(24))
print(25, hash_table.search(25))

hash_table.insert(1024)
print("*************************")
print(1024, hash_table.search(1024))
print(124, hash_table.search(124))
print(24, hash_table.search(24))
print(25, hash_table.search(25))

hash_table.insert(124)
print("*************************")
print(1024, hash_table.search(1024))
print(124, hash_table.search(124))
print(24, hash_table.search(24))
print(25, hash_table.search(25))

hash_table.insert(24)
print("*************************")
print(1024, hash_table.search(1024))
print(124, hash_table.search(124))
print(24, hash_table.search(24))
print(25, hash_table.search(25))

hash_table.insert(25)
print("*************************")
print(1024, hash_table.search(1024))
print(124, hash_table.search(124))
print(24, hash_table.search(24))
print(25, hash_table.search(25))

hash_table.remove(24)
print("*************************")
print(1024, hash_table.search(1024))
print(124, hash_table.search(124))
print(24, hash_table.search(24))
print(25, hash_table.search(25))


hash_table.remove(1024)
print("*************************")
print(1024, hash_table.search(1024))
print(124, hash_table.search(124))
print(24, hash_table.search(24))
print(25, hash_table.search(25))



