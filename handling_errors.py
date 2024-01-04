def party_planner(cookies, people):
    # TODO: Add a try-except block here to
    try:
        num_each = cookies // people
        leftovers = cookies % people
    #       make sure no ZeroDivisionError occurs.
    except ZeroDivisionError:
        print("Warning!, please input a different number of people")
        return None
              
    return(num_each, leftovers)

# The main code block is below; do not edit this
lets_party = 'y'
while lets_party == 'y':

    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = input("\nWould you like to party more? (y or n) ")