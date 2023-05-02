# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#   4. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of each of the following:
#       - It must be longer than 7 characters (8 is fine)
#       - It must contain at least one of the following special characters:
#         `!`, `@`, `$`, `%` or `&`
#
# We recommend that you store the passwords in a dictionary, where the keys are
# the service names and the values are the passwords.
#
# Example usage:
#   > password_manager = PasswordManager()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.get_for_service('not_real')
#   None
#   > password_manager.get_for_service('twitter')
#   None
#   > password_manager.list_services()
#   ['gmail', 'facebook']
#

# == YOUR CODE ==

class PasswordManager():
    
    #Create init file
    def __init__(self):
        #Create blank dictionary to store all services and passwords
        self.password_dict = {}
        print("#################################")
        print("Welcome to Ian's password manager")
        print("#################################")


    #method to validate the password
    def is_valid(self, password):
        #Define special characters
        sc = ["!", "@", "$", "%", "&"]
        #Validate the password length and check for any special characters
        if len(password) > 7 and any([x in password for x in sc]):
            print(f" {password} is Valid!")
            return True
        else:
            print (f" {password} is invalid! Either the password length is too short or the password doesn't contain a special characters")
            return False


    #Create a method to 'add' a new service and password to a dictionary
    #Note - need to validate the password before it is added
    def add(self, service, password):
        if self.is_valid(password) == True:
            print(f"New service will be added called {service}")
            #create key value pairs
            kvp = {service:password} 
            #add password to a dictionary
            self.password_dict.update((kvp))
        else:
            print(f"New service called #{service}# will NOT be added!")

    #Create a method to list services
    def list_services(self):       
        print(f"The valid keys in the dictionary are : {self.password_dict.keys()}")
        return self.password_dict.keys()
    
    #Create a method to request a password for a given service
    def get_for_service(self, service):
        print(f"the password for service #{service}# = {self.password_dict.get(service)}")
        return self.password_dict.get(service)



password_manager = PasswordManager()
password_manager.add('gmail', '12ab5!678')#pass
password_manager.add('facebook', '$abc1234')#pass
password_manager.add('twitter', '12345678')#fail
password_manager.get_for_service('gmail')#pass
password_manager.get_for_service('facebook')#pass
password_manager.get_for_service('not_real')#fail
password_manager.get_for_service('twitter')#fail
password_manager.list_services()#'gmail', 'facebook'