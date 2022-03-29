import random


destinations = ['St.Louis', 'Chicago', 'Milwaukee', 'Detroit']

location1 = random.choice(destinations)


print("Welcome to the Day Trip Generator! If you aren't sure what you want to do for your vacation, you have come to the right place!")

response = input(f'We have selected {location1} for your destination! Does this sound good? Enter y/n:')

if response == 'y': 
    # move forward to next category
    pass
else:
    location1 = random.choice(destinations)
    










