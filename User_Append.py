#    Initialize a List: Create a list named database to store user inputs.
#    Input Loop: Set up a loop that continuously prompts the user for input.
#    Input Limit Condition: Implement a condition inside the loop that checks if the length of database has reached 5. If true, exit the loop.
#    Limit Reached Message: When the limit is reached, print a message informing the user that they have reached the maximum input limit.
#    Timer Implementation: Look up how to use a timer in your programming language and set a timer for a specific duration.
#    Wait for Timer: After reaching the input limit, wait for the timer to finish.
#    Timer Completion Message: Once the timer ends, display a message letting the user know they can continue to input messages.
#    Resume Input: After the timer message, prompt the user again to continue adding inputs to database.

import time 
#       Initialize a List: Create a list named database to store user inputs.

database = []

user_message = input('Add a comment: ')
#       Input Loop: Set up a loop that continuously prompts the user for input.

while len(database) < 5: 
    user_message = input('Add a comment: ')
    database.append(user_message)
    if len(database) == 5:
        print("\tSorry your last comment was not posted.")
        print("\tYou've reached the max amount of comments for now, please wait.")
        time.sleep(5)
        database.clear()
        print("You may comment again now")
