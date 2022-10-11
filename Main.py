class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:
  def __init__(self):
    self.head = None
    self.last = None

  def enqueue(self, data) -> None:
    # Write your code here
    if self.last is None:
      self.head = Node(data)
      self.last = self.head
    else:
      self.last.next = Node(data)
      self.last = self.last.next

  def dequeue(self) -> None:
    # Write your code here
    if self.head is None:
      return None
    else:
      removed_data = self.head.data
      self.head = self.head.next
    
  def status(self) -> None:
    # Write your code here
    curr = self.head
    display = []
    while (curr):
      display.append(curr.data)
      curr = curr.next
    for ele in display:
      print(ele, end="=>")
    print(None)


# Do not change the following code
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()
