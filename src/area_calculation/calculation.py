def rectangle_area(l, w):
        '''
        Caculates the area of a rectangle. If the length and width are the same,
        it returns length**2, else length * width

        :param l float: The length of the rectangle
        :param w float: The width of the rectangle
        '''
        if l == w:
                return l * l 
        return l * w

'''
        Caculates the area of a triangle. 

        :param b float: base of the triangle
        :param h float: height of the triangle
        '''

def triangle_area(b, h): 
        return b * h * 0.5

def circle_area(b, h): 
        pass 
