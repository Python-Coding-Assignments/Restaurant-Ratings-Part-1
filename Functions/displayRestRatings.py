def displayRestRatings(restaurant):
    """This function prints each rating for a specified restaurant.  This function takes in one mutable argument which is a list, more specifically, a list or restaurants."""

    print("Ratings for " + restaurant.name)
    #for loop which iterates over each restaurant rating
    for i in range(0, restaurant.getRatingsSize()):
        #printing each restaurant rating to the user
        print("Rating Index: " + str(i))
        print("User: " + restaurant.getRatings(i).getUser())
        print("Rating Value: " + str(restaurant.getRatings(i).getRatingValue()))
        print("Comment: " + restaurant.getRatings(i).getComment())
        print("******************\n")