#############################################################################################################
# Challenge 1 -> A Function to get a float from the user
prompt_string = "Enter a float:"
def get_float(prompt_string: str):
    """A function that gets a float from the user and returns it.

    Arguments:
        - prompt_string: A string that will be shown to the user when they are 
            prompted to input the number.

    Returns:
        - A float converted from the user's input
    """
    the_float_value = float(input({prompt_string}))

    return the_float_value

#############################################################################################################
# Challenge 2 -> A Function to convert miles to km
# NOTE: 1 mile is 1.60934km

distance_in_miles = float(input("Enter a distance in miles:"))

def miles_to_km(distance_in_miles: float):
    """A function to convert distance from miles to km

    Arguments: 
        - distance_in_miles: A float representing a distance in miles
    
    Returns
        - a float representing the distance in kilometers
    """

    multiplier = float(1.60934)
    distance_in_km = float(distance_in_miles * multiplier)
    
    return distance_in_km

#############################################################################################################
# Challenge 3 -> A function to calculate the total distance run in a relay

distance_per_runner = float(input("Enter distance per runner:"))
number_of_runners = float(input("Enter number of runners:"))

def relay_distance(distance_per_runner: float, number_of_runners: float):
    """A function to calculate the total distance run by a team of runners
    in a relay race.
    
    Arguments:
        - distance_per_runner: a float representing the amount each runner runs
            (in a relay race, all runners run the same distance!)
        - number_of_runners: a float representing the number of runners in a team
    
    Returns:
        - A float representing the total distance run.
    """
    total_relay_distance = float(distance_per_runner * number_of_runners)
    return total_relay_distance


#############################################################################################################
# Challenge 4 (extra tricky, no tests for this one!)
# 
# See if you can write a single function that USES all three of the functions 
# you wrote for the above challenges.
#
# It should:
# - prompt the user for the distance each runner in the relay race will run (in miles)
# - prompt the user for the number of runners in a team
# - print the total distance run by the team, in kilometers!
# 
# No need for this function to accept any arguments or return any values.

def challenge():
    test_value = get_float(prompt_string)
    print ({test_value})
    test_value2 = miles_to_km(distance_in_miles)
    print ({test_value2})
    test_value3 = relay_distance(distance_per_runner, number_of_runners)
    print ({test_value3})

challenge()