import copy
import time
from queue import PriorityQueue
from random import randint

#Khởi tạo trạng thái cho bài toán
class State:
  def __init__(self, data = None, par = None, g = 0, h = 0, op = None):
    self.data = data
    self.par = par
    self.g = g
    self.h = h
    self.op = op

  def Clone(self):
    ns = copy.deepcopy(self)
    return ns

  def Prints(self):
    size = 3 
    for i in range(size):
      for j in range(size):
        print(self.data[i * size + j], end = ' ')
      print()
    print()

  def Keys(self):
    if self.data == None:
      return None
    res = ''
    for x in self.data:
      res += (str)(x)
    return res

  def __lt__(self, other):
    if other == None:
      return False
    return self.g + self.h < other.g + other.h

  def __eq__(self, other):
    if other == None:
      return False
    return self.Keys() == other.Keys()

#Lớp các toán tử
class Operator:
  def __init__(self, i):
    self.i = i

  def CheckState(self, s):
    return s.data == None

  def FindPos(self, s):
    size = 3
    for i in range(size):
      for j in range(size):
        if s.data[i * size + j] == 0:
          return i, j
    return None

  def Up(self, s):
    if self.CheckState(s) == True:
      return None
    row, col = self.FindPos(s)
    if row == 0:
      return None
    return self.Swap(s, row, col, self.i)
  def Down(self, s):
    if self.CheckState(s) == True:
      return None
    row, col = self.FindPos(s)
    if row == 2:
      return None
    return self.Swap(s, row, col, self.i)      
  def Left(self, s):
    if self.CheckState(s) == True:
      return None
    row, col = self.FindPos(s)
    if col == 0:
      return None
    return self.Swap(s, row, col, self.i)
  def Right(self, s):
    if self.CheckState(s) == True:
      return None
    row, col = self.FindPos(s)
    if col == 2:
      return None
    return self.Swap(s, row, col, self.i)   

  def Move(self, s):
    if self.i == 0:
      return self.Up(s)
    if self.i == 1:
      return self.Down(s)
    if self.i == 2:
      return self.Left(s)
    if self.i == 3:
      return self.Right(s)
    return None

  def Swap(self, s, row, col, i):
    size = 3
    ns = s.Clone()
    row_new = row
    col_new = col
  
    if i == 0:
      row_new = row - 1
      col_new = col
    if i == 1:
      row_new = row + 1
      col_new = col
    if i == 2:
      row_new = row 
      col_new = col - 1
    if i == 3:
      row_new = row
      col_new = col + 1
    ns.data[row * size + col] = ns.data[row_new * size + col_new]
    ns.data[row_new * size + col_new] = 0
    return ns

#Hàm hỗ trợ
def CheckInPriority(Open, temp):
  if temp == None:
    return False
  return (temp in Open.queue)

def Equal(O, G):
  if O == None:
    return False
  return O.Keys() == G.Keys()

def Path(O):
  if O.par != None:
    Path(O.par)
    if (O.op.i==0):
      print("Up")
    elif (O.op.i==1):
      print("Down")
    elif (O.op.i==2):
      print("Left")
    elif (O.op.i==3):
      print("Right")
    print("-----")
    O.Prints()

def Hx(S, G):
  size = 3
  res = 0
  for i in range(size):
    for j in range(size):
      if S.data[i * size + j] != G.data[i * size + j]:
        res += 1
  return res

def Run():
  Open = PriorityQueue()
  Close = PriorityQueue()
  S.g = 0
  S.h = Hx(S, G)
  Open.put(S)

  while True:
    if Open.empty() == True:
      print("--Tìm kiếm thất bại--")
      return
    O = Open.get()
    Close.put(O)
    if Equal(O, G) == True:
      print("--Tìm kiếm thành công--")
      print(' ')
      Path(O)
      return
# Tim cac trang thai con
    for i in range(4):
      op = Operator(i)
      sub = op.Move(O)
      if sub == None:
        continue
      sub1 = CheckInPriority(Open, sub)
      sub2 = CheckInPriority(Close, sub)
                
      if not sub1 and not sub2:
        sub.par = O
        sub.op = op
        sub.g = O.g +1    
        sub.h = Hx(sub, G)
        Open.put(sub)

def random(num):
  G = State()
  size = 3
  G.data = []
  for i in range(size):
    for j in range(size):
      G.data.append((i * size + j + 1) % 9)
  S = G.Clone()
  for i in range(num):
    op = Operator(randint(0, 3))
    temp = op.Move(S)      
    if temp != None:
      S = temp
  return S, G

t1 = time.time()
S, G = random(30)
print("Đầu")
S.Prints()
print("Đích")
G.Prints()
Run()
t2 = time.time()

print("time: ", (t2-t1),"s")
