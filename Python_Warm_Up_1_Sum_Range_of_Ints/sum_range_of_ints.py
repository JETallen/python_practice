# Practice problem 1 Outlined in realpython.com
# - Write a function, add_it_up(), that takes a single integer as 
# - input and returns the sum of the integers from zero to the input parameter.
# - The function should return 0 if a non-integer is passed in.
def add_it_up(last_num):
    try:
        i = 0
        sumedup = 0
        if not(isinstance(last_num,int)):
            return sumedup
        while i<last_num+1:
            sumedup = sumedup + i
            i += 1
        return sumedup
    except:
        return "An Error Occured"+sys.exc_info()[0]
print(add_it_up("a"))
print(add_it_up("5"))
print(add_it_up(5))
print(add_it_up(100))