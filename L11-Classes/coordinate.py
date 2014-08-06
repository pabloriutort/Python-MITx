class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
       
    def __eq__(c1, c2):
        return c1.getX() == c2.getX() and c1.getY() == c2.getY()
    
    def __repr__(c1):
        return 'Coordinate('+ str(c1.getX()) + ', ' + str(c1.getY())+')'

