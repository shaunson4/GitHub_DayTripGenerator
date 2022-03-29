import random


destinations = ['St.Louis', 'Chicago', 'Milwaukee', 'Detroit']


restuarants = ['Taco_Bell', 'Burger_King', 'Weber_Grill', 'Burrito_King']


mode_of_transportation = ['uber', 'train', 'tour_bus', 'rental_car']
transport1 = mode_of_transportation[0]

entertainment = ['dancing', 'theatre', 'play', 'opera']
activity1 = entertainment[0]


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







print("Welcome to the Day Trip Generator! If you aren't sure what you want to do for your vacation, you have come to the right place!")

select_dest()
select_rest()
    










