
from statistics import mode


borrow = [5, 3, 0, 2, 5, 1, 0, 4, 5, 2]

average = sum(borrow) / len(borrow)

highest = max(borrow)
lowest = min(borrow)


zero_count = borrow.count(0)

most_common = mode(borrow)


print("Borrowing Records:", borrow)
print("Average Borrowings:", average)
print("Highest Borrow Count:", highest)
print("Lowest Borrow Count:", lowest)
print("Members with Zero Borrowings:", zero_count)
print("Mode of Borrow Count:", most_common)
