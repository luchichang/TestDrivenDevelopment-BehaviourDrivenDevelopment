# declaring the function

# here ":float" near the parameter doesn't enforces the float value but act as indicator that function expects  float value
def area_of_a_triangle( base: float , height: float) -> float :
    """calculate the area of the triangle"""

    """
    below method works great for smaller list but for larger list it will takes more time since it do linear search so time complexity is O(n)
    """
    # if type(base) in [int , float]:
    #     print(base)
    
    # another way which compares in c interpreter level
    if not isinstance(base , (int,float)):
        raise TypeError("Base must be a number")
    
    # here (int, float) is passed as tuple single parameter
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")
    
    if base < 0 or base < 0.0 :
        raise ValueError("base must be a positive number")
    
    if height < 0 :
        raise ValueError("Height must be a positive number")
    
    # return 0.5*base*height
    return (base/2)*height



