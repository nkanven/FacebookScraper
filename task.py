"""Facebook Surfer Robot."""
from Facebook.Actions.login import Login

if __name__ == "__main__":
    login = Login()
    if login.connect():
        print("Successfully login")
