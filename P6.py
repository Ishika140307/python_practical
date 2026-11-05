
class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

   
    def insert(self, key):
        index = key % self.size

        for i in range(self.size):
            pos = (index + i) % self.size

            if self.table[pos] is None or self.table[pos] == "DELETED":
                self.table[pos] = key
                print("Key Inserted:", key)
                return

        print("Hash Table is Full")

   
    def search(self, key):
        index = key % self.size

        for i in range(self.size):
            pos = (index + i) % self.size

            if self.table[pos] is None:
                break

            if self.table[pos] == key:
                print("Key Found")
                return

        print("Key Not Found")

   
    def delete(self, key):
        index = key % self.size

        for i in range(self.size):
            pos = (index + i) % self.size

            if self.table[pos] is None:
                break

            if self.table[pos] == key:
                self.table[pos] = "DELETED"
                print("Key Deleted")
                return

        print("Key Not Found")

    
    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


h = HashTable()

h.insert(10)
h.insert(20)
h.insert(30)
h.insert(15)

print("\nHash Table:")
h.display()

h.search(20)
h.delete(20)

print("\nUpdated Hash Table:")
h.display()
