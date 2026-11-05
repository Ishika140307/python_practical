undo_stack = []
redo_stack = []
document = ""

def make_change(text):
    global document
    undo_stack.append(document)
    document += text
    redo_stack.clear()
    print("Change Added:", document)

def undo():
    global document
    if undo_stack:
        redo_stack.append(document)
        document = undo_stack.pop()
        print("Undo:", document)
    else:
        print("Nothing to Undo")

def redo():
    global document
    if redo_stack:
        undo_stack.append(document)
        document = redo_stack.pop()
        print("Redo:", document)
    else:
        print("Nothing to Redo")

def display():
    print("Document:", document)

make_change("Hello ")
make_change("World")
undo()
redo()
display()
