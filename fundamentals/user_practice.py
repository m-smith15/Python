class createUser:
    def __init__(self, first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
    
    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points += 200
            print(f"It is {self.is_rewards_member}, you are a member with {self.gold_card_points} in your balance")
        else:
            print("User is already a member")
        return self

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("What do you think this is, Enron? -- not enough points in balance")
            
        else:
            self.gold_card_points -= amount
            print(f"You have {self.gold_card_points} gold card points remaining")
        return self

# Create user Timmy Shrimp, email timmytheshrimp@ocean.gov, age 1050
print("------1--------")
user1 = createUser("timmy","shrimp","timmytheshrimp@ocean.gov","1050")
# Create display_info method, have it print each attributes on new line
print("------2---------")
print(user1.display_info())
# Create enroll to update member status to True and add 200 points
print("------3---------")
print(user1.enroll(), user1.is_rewards_member, user1.gold_card_points)
# Create spend_points have it increase/decrease users gold point total by amount specified
print("------4---------")
user1.spend_points(100) # expecting 100 back, 200 from member creation - 100 here
print(user1.gold_card_points)
# Bonus - if member already print messaging.
print("------5---------")
user1.enroll() #should get messaging back, setting member earlier in code
# Bonus 2 - add logic in spend points to make sure they have enough points, if not print message
print("------6---------")
user1.spend_points(200) #should only have balance of 100, so should see error messaging
print("-------------Assignment Parameters ------------")

# --------- Assignment Parameters ---------
# --------- Updating for chaining assignment --------
print("----Assignment user 1----")
assignment_user1 = createUser("Tester","One","testerone@email.edu",50).display_info().enroll().spend_points(50).display_info().enroll()
# assignment_user1.display_info()
# assignment_user1.enroll()
print("----Assignment user 2----")
assignment_user2 = createUser("Nottester","Two","notatest@email.edu",40).enroll().spend_points(80).display_info()
# assignment_user2.display_info() 
print("----Assignment user 3----")
assignment_user3 = createUser("Yepitsatest","Three","jkistest@email.edu",30).display_info().spend_points(40)
# assignment_user3.display_info()

# assignment_user1.spend_points(50)
# assignment_user2.enroll()
# assignment_user2.spend_points(80)
# assignment_user1.display_info() 
# assignment_user2.display_info()
# assignment_user3.display_info()

# assignment_user1.enroll() #bonus 1

# assignment_user3.spend_points(40) # bonus 2
