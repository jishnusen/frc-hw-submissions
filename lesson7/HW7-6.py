user_password = ""
user_login = ""
def id_finder():
    user_login = (raw_input("What is your new login?"))
    user_password = (raw_input("What is your new password?"))
    print(len(user_login))

def login(user, pw):
    
    for u in user_login:
        if user == u:
            while pw != user_password:
                print "Failure"
                pw = raw_input("password:")
            else:
                print "Success!"
        else:
            print "Failure"
    
confirm = raw_input("Do you have an account?")
if confirm == "yes":
    login(raw_input("login:"), raw_input("password)"))
else:
    id_finder()
    login(raw_input("login:"), raw_input("password)"))
