import random
from tkinter import N

destinations = ['St.Louis', 'Chicago', 'Milwaukee', 'Detroit']

restuarants = ['Taco_Bell', 'Burger_King', 'Weber_Grill', 'Burrito_King']

mode_of_transportation = ['uber', 'train', 'limosine', 'rental_car']

entertainment = ['dancing', 'theatre', 'play', 'opera']


def select_dest():
    dest = random.choice(destinations)
    dest_choice = input(f'We have selected {dest} for your destination! Does this sound good? Enter y/n:')
    if dest_choice == 'y': 
        print('Awesome! Glad that you approve of this destination. Let\'s continue')
        return dest
    else:
        print('Oh, my apologies, you don\'t approve of this destination. No problem at all, we can try something else.')
        select_dest() 

def select_rest():
    eatery1 = random.choice(restuarants)
    rest_choice = input(f'We have selected {eatery1} for your dining pleasure. Doesn\'t that sound tantilizing? Enter y/n:')
    if rest_choice == 'y':
        print('Awesome! Glad that you approve of this restaurant. Let\'s continue')
        return eatery1
    else:
        print('Oh, my apologies, you don\'t approve of this restaurant. No problem at all, we can try another place to eat.')
        select_rest()

def select_transport():
    transport1 = random.choice(mode_of_transportation) 
    transpo_choice = input(f'We have selected {transport1} for your mode of transportation. Doesn\'t that sound relaxing? Enter y/n:')
    if transpo_choice =='y':
        print('Awesome! Glad that you approve of this mode of transportation. Let\'s continue')
        return transport1
    else:        
        print('Oh, my apologies, you don\'t approve of this type of transportation. No problem at all, we can try different one.')
        select_transport()

def select_activity():
    activity1 = random.choice(entertainment)
    activity_choice = input(f'We have selected {activity1} for your entertainment. Doesn\'t that sound exciting? Enter y/n:')
    if activity_choice == 'y':
        print('Awesome! Glad that you approve of the entertainment chosen. Let\'s summarize')
        return activity1





def main_itinerary():
    print("Welcome to the Day Trip Generator! If you aren't sure what you want to do for your vacation, you have come to the right place!")
    dest = select_dest()
    eatery1 = select_rest()
    transport1 = select_transport()
    activity1 = select_activity()

    print('Congratulations! We have completed generating the itinerary for your Day trip. Now let\'s just confirm this is the trip you wanted.')

    print('The trip we have generated for you is as follows: ')

    print(f'Trip Destination: {dest} ')
    print(f'Restaurant: {eatery1}')
    print(f'Mode of Transporation: {transport1}')
    print(f'Entertainment: {activity1}')



main_itinerary()
    










