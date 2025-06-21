# user inputs the email to be slicing.

email = input("Enter your E-mail: ")

# indexing the E-mail for starting and ending index.

index = email.index("@")

# indexing to extracting username.

username = email[:index]

# indexing for the domain

domain = email[index:]

# output for username and domain after indexing.

print(f"Your E-mail username is {username} and domain is {domain}")