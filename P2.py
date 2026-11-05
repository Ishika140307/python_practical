
ids = [101, 205, 310, 415, 520, 625, 730]
key = int(input("Enter Customer ID to search: "))

found = False

for i in ids:
    if i == key:
        found = True
        break

if found:
    print("Linear Search: ID Found")
else:
    print("Linear Search: ID Not Found")
low = 0
high = len(ids) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if ids[mid] == key:
        found = True
        break
    elif key < ids[mid]:
        high = mid - 1
    else:
        low = mid + 1

if found:
    print("Binary Search: ID Found")
else:
    print("Binary Search: ID Not Found")
