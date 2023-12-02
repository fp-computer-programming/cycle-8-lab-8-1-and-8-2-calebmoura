# Author: Caleb Moura

# Defining element and settign parameters.
def generate_invitations(names):
    """
    Generates and prints party invitations for each name in the given list.

    - names (list): A list of names to invite to the party.
    """
    for name in names:
        # Generating the invitation for each name.
        invitation = f"Hi {name}, You're invited to my party on Friday!"
        # Printing the invitation.
        print(invitation)

# Prompting user for 3 names.
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
name3 = input("Enter the third name: ")

# Creating list of the entered names.
guest_list = [name1, name2, name3]

# Calling function with the user inputs.
generate_invitations(guest_list)