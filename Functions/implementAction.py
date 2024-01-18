from Functions import displayRestaurants, displayRestRatings, validRestIndex, addRating

def implementAction(restaurants, action):
    """This function determines who the flow of the program will run based on the user's menu selection.  This function takes in two arguments into its parameter list: restaurants and action."""

    #declaration and initialization of variable
    index = 0

    #conditional statement which checks if user's input is either "a" or "A"
    if action == "a" or action == "A":
        #calling displayRestaurants function to display all the restaurant's in the system
        displayRestaurants.displayRestaurants(restaurants)

    #conditional statement which checks if user's input is either "b" or "B"    
    elif action == "b" or action == "B":
        print("\nDisplay all ratings for a restaurant...")
        #getting a valid restaurant index from user by calling validRestIndex function
        index = validRestIndex.validRestIndex(restaurants)   
        #calling displayRestaurants function to display all the restaurant's in the system          
        displayRestRatings.displayRestRatings(restaurants[index])  

    #conditional statement which checks if user's input is either "c" or "C"
    elif action == "c" or action == "C":
        print("\nAdd a rating to a restaurant...")
        #getting a valid restaurant index from user by calling validRestIndex function
        index = validRestIndex.validRestIndex(restaurants)
        #calling addRating function to add a rating to the specified restaurant
        addRating.addRating(restaurants[index])