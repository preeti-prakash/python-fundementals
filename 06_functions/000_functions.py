def print_hello_world_once():           #function declaration
    print("Hello World")        

print_hello_world_once() #function call


def print_hello_world_twice():
    print("Hello World 1")
    print("Hello World 2")

print_hello_world_twice()

def print_hello_world_thrice():
    print("Hello World 1")
    print("Hello World 2")
    print("Hello World 3")

print_hello_world_thrice()

# add a value to the function - parameters
def print_hello_world(no_of_times):
    for i in range(no_of_times):
        print("Hello World")

print_hello_world(3)  #printing hello world based on the parameter passed to the function


