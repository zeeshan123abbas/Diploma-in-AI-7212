# variable_scope.py
# Local vs global variables

college = "Aptech North Nazimabad"     # GLOBAL: created outside any function

def show_info():
    batch = "Morning"                  # LOCAL: exists only inside this function
    print("Inside :", college, "-", batch)

show_info()
print("Outside:", college)
# print(batch)   # would cause NameError: batch is not defined outside

# Changing a global variable needs the 'global' keyword
visitors = 0

def add_visitor():
    global visitors
    visitors += 1

add_visitor()
add_visitor()
print("Visitors:", visitors)

# A local variable with the same name hides the global one
x = 10
def test():
    x = 99          # a NEW local x; the global x is not changed
    print("local x =", x)
test()
print("global x =", x)
