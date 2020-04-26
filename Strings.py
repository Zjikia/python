name = input("What is your name? ")
quest = input("What is your quest? ")
color = input("What is your favorite color? ")

print ("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))


# Write your code below, starting on line 3!

my_string = "My name is Zurab"
print (len(my_string))
print (my_string .upper())


from datetime import datetime
now = datetime.now()

print ('%02d/%02d/%04d' %(now.month, now.day, now.year))

from datetime import datetime
now = datetime.now()

print ('%02d:%02d:%02d' % (now.hour, now.minute, now.second))

from datetime import datetime
now = datetime.now()

print ('%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second))

def clinic():
    print ("You've just entered the clinic!")
    print ("Do you take the door on the left or the right?")
    answer = input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print ("This is the Verbal Abuse Room, you heap of parrot droppings!")
    elif answer == "right" or answer == "r":
        print ("Of course this is the Argument Room, I've told you that already!")
    else:
        print ("You didn't pick left or right! Try again.")
        clinic()

clinic()


# Create comparative statements as appropriate on the lines below!

# Make me true!
bool_one = 3 < 5  # We already did this one for you!

# Make me false!
bool_two = 7 == 9
print (bool_two)
# Make me true!
bool_three = 8!=5
print (bool_three)
# Make me false!
bool_four = 5>9
print (bool_four)
# Make me true!
bool_five = 3<7
print (bool_five)