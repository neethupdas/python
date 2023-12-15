class Rectangle():
    def __init__(self):
        self.__length = 1.0
        self.__width = 1.0
    def __str__(self):
        return "This is class Rectangle"
    def set_length(self,len=1.0): #len=1 --> default value
        self.__length = len
    def set_width(self,wid=1.0): #wid=1 --> default value
        self.__width = wid
    def get_length(self):
        return self.__length
    def get_width(self):
        return self.__width
    def get_area(self):
        return self.get_width() * self.get_length()
    def __lt__(self, other):
        if(self.get_area()<other.get_area()):
            return "1st Rectangle is Smaller."
        else:
            return "2nd Rectangle is Smaller."
my_rect1 = Rectangle()
my_rect1.set_length(4.0)
my_rect1.set_width(2.0)
print ("The length is ", my_rect1.get_length())
print ("The width is ", my_rect1.get_width())
print ("The area is ", my_rect1.get_area())
print (my_rect1)
my_rect2 = Rectangle()
my_rect2.set_length(5.0)
my_rect2.set_width(3.0)
print ("The length is ", my_rect2.get_length())
print ("The width is ", my_rect2.get_width())
print ("The area is ", my_rect2.get_area())
print (my_rect2)
print(my_rect1 < my_rect2)
