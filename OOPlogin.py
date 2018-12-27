"""brushing up on that OOP programming
imports a csv with fake login:password combo"""

import csv

class AccountClass:
    def __init__(self, profilename, username, password):
        self.profilename = profilename
        self.username = username
        self.password = password
        self.session = ''
    
    def login(self):
        print('logging in for {} with {} and {}'.format(self.profilename, self.username, self.password))
        print('setting self.session')
        self.session = 'sessioncookie'
    
    def logout(self):
        print('logging out')

    def post_comment(self, comment):
        self.comment = comment
        print('posting comment on forum')
        print(comment)

def main():
    with open('ooplogin.csv') as login_file:
        reader = csv.reader(login_file)
        reader = list(reader)
    first_account = AccountClass(reader[0][0], reader[0][1], reader[0][2])
    first_account.login()

main()