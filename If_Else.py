answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return False        # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return False        # Make sure this returns False
print black_knight()
print french_soldier()


# Complete the if and elif statements!
def grade_converter(grade):
    if grade > 89:
        return "A"
    elif grade > 79 and grade < 90:
        return "B"
    elif grade > 69 and grade < 80:
        return "C"
    elif grade > 64 and grade < 70:
        return "D"
    else:
        return "F"
      
# This should print an "A"      
print grade_converter(92)

# This should print a "C"
print grade_converter(70)

# This should print an "F"
print grade_converter(61)


print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word: ")
if len(original) > 0:
  print original
  
else:
  print "empty"
  


print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word: ")
if len(original) > 0 and original.isalpha():
  print original
  
else:
  print "empty"
