
class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None

class StudentList:
    def __init__(self):
        self.head = None

    # Add student
    def add(self, roll, name, marks):
        new = Node(roll, name, marks)
        new.next = self.head
        self.head = new

    # Display records
    def display(self):
        temp = self.head
        while temp:
            print(temp.roll, temp.name, temp.marks)
            temp = temp.next

    # Search student
    def search(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                print("Student Found:", temp.name)
                return
            temp = temp.next
        print("Student Not Found")

    # Delete student
    def delete(self, roll):
        temp = self.head
        prev = None
        while temp:
            if temp.roll == roll:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                print("Record Deleted")
                return
            prev = temp
            temp = temp.next
        print("Student Not Found")

    # Update student
    def update(self, roll, name, marks):
        temp = self.head
        while temp:
            if temp.roll == roll:
                temp.name = name
                temp.marks = marks
                print("Record Updated")
                return
            temp = temp.next
        print("Student Not Found")

    # Sort records
    def sort(self, key, reverse=False):
        records = []
        temp = self.head
        while temp:
            records.append(temp)
            temp = temp.next

        records.sort(
            key=lambda x: x.marks if key == "marks" else x.roll,
            reverse=reverse
        )

        for s in records:
            print(s.roll, s.name, s.marks)


# Main program
s = StudentList()

s.add(1, "Amit", 85)
s.add(2, "Rahul", 90)
s.add(3, "Priya", 75)

print("Student Records:")
s.display()

s.search(2)

s.update(1, "Amit", 95)

s.delete(3)

print("Sorted by Marks (Ascending):")
s.sort("marks")

print("Sorted by Roll No (Descending):")
s.sort("roll", True)
