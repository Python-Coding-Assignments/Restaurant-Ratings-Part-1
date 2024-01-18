class Rating:
    """Class definition for Rating"""

    def __init__(self, *arguments):
        """This is a constructor which defines three instance variables: user, ratingValue, and comment."""

        #conditional statement which checks if the number of arguments within the method's call is equal to zero
        if len(arguments) == 0:
            self.user = "null"
            self.ratingValue = "null"
            self.comment = "null"

        #conditional statement which checks if the number of arguments within the method's call is equal to three    
        elif len(arguments) == 3:    
            self.user = arguments[0]
            self.ratingValue = arguments[1]
            self.comment = arguments[2]

    def setUser(self, user):
        """This method is a setter which sets the instance variable user."""

        self.user = user

    def getUser(self):
        """This method is a getter which returns the instance variable user."""

        return self.user

    def setRatingValue(self, value):
        """This method is a setter which sets the instance variable ratingValue."""

        self.ratingValue = value

    def getRatingValue(self):
        """This method is a getter which returns the instance variable ratingValue."""

        return self.ratingValue

    def setComment(self, comment):
        """This method is a setter which sets the instance variable comment."""

        self.comment = comment

    def getComment(self):
        """This method is a getter which returns the instance variable comment."""

        return self.comment                