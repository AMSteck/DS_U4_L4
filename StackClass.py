#Alannah Steck
#U4L1
#StackClass
#૮꒰ ˶• ༝ •˶꒱ა  Good Luck Bunny

class ArrayStack:
  def __init__(self):
    """Initalizes class"""
    self.__stack = []
    self.__size = 0

  def __str__(self):
    """Display contents of stack"""
    out = ""
    for ele in self.__stack:
        out += str(ele) + ' '

    out += "<TOP"
    return out

  def __len__(self):
    """returns the length of the stack"""
    return self.__size

  def __is_empty(self):
    """Determines if stack is empty"""
    if self.__size == 0:
      return True
    else:
      return False

  def push(self, newElement):
    """adds element to the top of stack"""
    self.__stack.append(newElement)
    self.__size += 1

  def top(self):
    """returns top of stack"""
    value = self.__is_empty()
    if value == False:
      return self.__stack[-1]
    else:
      raise IndexError("list index out of range")

  def pop(self):
    """gets rid of the top element of the stack"""
    value = self.__is_empty()
    if value == False:
      topVal = self.top()
      del self.__stack[-1]
      self.__size -= 1
      return topVal
    else:
      raise IndexError("list index out of range")
