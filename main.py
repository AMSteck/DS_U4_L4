#Alannah Steck
#U4L4
#balancing brackets
#૮꒰ ˶• ༝ •˶꒱ა  Good Luck Bunny
from StackClass import ArrayStack

def balancedTest(testStr): #must check to see if all brackets/parenthesis are closed inside other brackets and parenthesis ex : test4
  theStack = ArrayStack()
  for item in testStr:
    if item == "(" or item == "[" or item == "{":
      theStack.push(item)
    else:
      try:
        prev = theStack.top()
      except:
        prev = None
      if item == ")" and prev != "(":
        return "Unbalanced"
      elif item == "]" and prev != "[":
        return "Unbalanced"
      elif item == "}" and prev != "{":
        return "Unbalanced"
      else:
        theStack.pop()
  if len(theStack) == 0:
    return "Balanced"
  else:
    return "Unbalanced"
  


def main():
  test1 = "()(()){([()])}"
  test2 = "((()(()){([()])}))"
  test3 = ")(()){([()])]"
  test4 = "({[])}"
  test5 = "("

  for test in [test1, test2, test3, test4, test5]:
    status = balancedTest(test)
    print(f"{test} - {status}\n")

if __name__ == "__main__":
  main()