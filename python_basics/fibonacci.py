
def fibonacci_function_module(n): # how to define a function
    '''Putting this is very important, because it is a string that acts as documentation of the function.
    In it you can detail inputs, parameters and outputs.
    This way people when typing the function and pressing shift+tab can read this and know how it works (try it).'''
    if n==0:
        return(1) # Functions always return something even if it is an empty element or a 'None'.
    elif n==1:
        return(1) # If it is a procedure, then something is not returned.
    else:
        return(fibonacci_function_module(n-1)+fibonacci_function_module(n-2))

def print_name():
    print(__name__)

# Main program
def main():
    
    print_name()
    
    for i in range(10):
        print(fibonacci_function_module(i)) 
        
print("I'm outside the execution scope")    

int = "overridden"

if __name__ == "__main__":
    
    main()
