# Python turtle driver/demo
# Python 3.7
# Using 4 spaces for indents as per:
#   https://www.python.org/dev/peps/pep-0008/#id17

# Import the module of drawing functions.
import Drawings

# When you add a function to Drawings, add a description here.
descriptions = ["Star drawing",     # 0
                "Rainbow Spiral"]   # 1

# Main menu:
while True:
    # Get the length of the current description index.
    l = len(descriptions)

    # Tell users what drawings we have.
    print("\n Turtle Drawings ")
    for i in range(l):
        print("", i, ") ", descriptions[i])

    # Ask which drawing they want to see. 
    print("\n Which one do you want to see? (q to quit)")
    instr = input(" > ")
    print("")
    
    # Check if it's the exit condition.
    if (instr == "q"):
        exit()

    # Now try to parse the int out of the user input.
    # Continue the loop if they don't give us a valid number.
    try:
        d = int(instr)
        if (d < 0 or d >= l):
            print(" !!! Please give us a number in between 0 and", str(l) + ".")
            input() # Pause to allow users to read the error message.
            continue
    except ValueError:
        print(" !!! Please give us an integer.")
        input() # Pause to allow users to read the error message.
        continue

    # Launch the right function based on what number they selected.
    if (d == 0):
        Drawings.star()
    elif (d == 1):
        Drawings.rainbow_spiral()

    # When we're done with the drawing, just loop around to the menu.