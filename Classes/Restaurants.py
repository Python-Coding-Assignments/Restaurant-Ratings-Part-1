from Classes import Rating

class Restaurant:
    """Class definition for Restaurant."""

    def __init__(self, *arguments):
        """This is a constructor the defines the public member attributes (instance variables) of the class: name, ratings, and website."""

        #conditional statement which checks if the number of arguments within the method's call is equal to zero
        if len(arguments) == 0:
            self.name = "null"
            self.ratings = "null"
            self.website = "null"

        #conditional statement which checks if the number of arguments within the method's call is equal to three    
        elif len(arguments) == 3:
            self.name = arguments[0]

            #declaration and initialization of local variables
            rating = Rating()
            ratings = []

            #for loop which runs through each iteration of the list contained in index one of the tuple
            for i in range(len(arguments[1])):
                #initializing rating and appending it to a list of ratings
                rating = (arguments[1][i])
                ratings.append(rating)

            self.ratings = ratings    
            self.website = arguments[2]

    def setName(self, name):
        """This method is a setter that sets the public instance variable name.""" 

        self.name = name

    def getName(self):
        """This method is a getter that returns the public instance variable name."""

        return self.name

    def setRatings(self, rating):
        """This method is a setter that appends a new rating to the instance variable containing all of the restaurant's ratings."""

        #creating instance of Rating, and then appending this new instance to the instance variable called ratings
        rating = Rating(rating.user, rating.ratingValue, rating.comment)
        self.ratings.append(rating)

    def getRatings(self, index):
        """This method is a getter that returns a rating from a restaurant at a defined index."""

        return self.ratings[index]
    
    def getRatingsSize(self):
        """This method returns the total number of ratings that a restaurant has."""
        
        return len(self.ratings)

    def setWebsite(self, website):
        """This method is a setter which sets the name of the restaurant's website."""

        return self.website 

    def getWebsite(self):
        """This method is a getter which returns the name of the restaurant's website."""

        return self.website           