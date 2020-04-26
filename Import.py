#import math # Imports the math module
#everything = dir(math) # Sets everything to a list of things from math
#print everything # Prints 'em all!

#ფუნქციები და მოდულების იმპორტი

def biggest_number(*args):
  print (max(args))
  return max(args)
    
def smallest_number(*args):
  print (min(args))
  return min(args)

def distance_from_zero(arg):
  print (abs(arg))
  return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)


# მაგალითი Set maximum to the max value of any set of numbers on line 3!

maximum = max(5,7,9)

print (maximum)

#კიდევ ერთი მაგალითი

print (type(42))
print (type(23.5))
print (type('String'))


from math import sqrt
print (sqrt(13689))

