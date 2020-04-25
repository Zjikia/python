def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print ("%d squared is %d." % (n, squared)) ## გიო: შეცდომას აგდებდა სანამ ფრჩხილებში არ ჩავსვი
  return squared
  
# Call the square function on line 10! Make sure to
# include the number 10 between the parentheses.

my_number_squared = square(10)
print (my_number_squared)  # Prints 100 ## გიო: იგივე აქაც, ფრჩხილები print-ს
#print square(10)  # Also prints 100!
#ფუნქცია ამუშავებს ცალკე პროგრამას, მისი დაძახება ხდება გარედან და მნიშვნელობა შეაქვს დაძახებისას


#აქ ძირი და ხარისხი პირდაპირ ფუნქციაშია მოცემული, ხოლო არგუმენტების შეყვანა ხდება ბოლოს ფუქციის დაძახებისას
def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print ("%d to the power of %d is %d." % (base, exponent, result))

power(10, 4)  # Add your arguments here!


def one_good_turn(n):
  return n + 1
    
def deserves_another(n):
  return one_good_turn(n) + 2
result = deserves_another(4)
print (result)


def cube(number):
  return number*number*number
#print number
def by_three(number):
  if number % 3 == 0:
    return number*number*number

  else:
    return False


# ეს რაც ვერ გავიგე წესიერად   ## რა ვერ გაიგე აქ?
def shut_down(s):
  if s == "yes":
    return "Shutting down"
    print ("Shutting down")
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry"
#shut_down('yes')
print (shut_down)


def hotel_cost(nights):
  return 140 * nights
def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
  else:
    print ("Wrong city")
	
## ორჯერ რატომ გაქვს ერთიდაიგივე ფუნქციები?	
def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost
def trip_cost(city, days, spending_money):
  return hotel_cost(days -1) + plane_ride_cost(city) + rental_car_cost(days) + spending_money
 
print (trip_cost("Los Angeles", 5, 800)) #აქ ვიძახებთ trip_cost-ს და მნიშვნელობები შემოდის რიგითობით და შეესებამება 
## აქ IndentationError: unindent does not match any outer indentation level ამ შეცდომას აგდებდა. 
## იმიტომ, რომ print ერთი პრაბელით იყო გაწეული. ხომ იცი python-ში intendation-ის დიდი მნიშვნელობა აქვს. ზედმეტი space ცვლის ყველაფერს.
## ჰოდა კიდე პრინტი ფრჩხილებში.
## მთლიანად ეს კოდი აბრუნებს შემდეგს:
""" 
10 squared is 100.
100
10 to the power of 4 is 10000.
7
<function shut_down at 0x000002D5935E8D08>
2015
"""