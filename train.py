import random

# Class for Train Booking System
class Train_booking:

    # Static method to greet the user
    @staticmethod
    def greet():
        msg = "Welcome Indian Railways, Good Morning!"
        print(msg)
        return msg

    # Method to generate and return a random train number
    def Train_no(self):
        trainno = f"Your train no. is: {random.randint(10000, 100000)}"
        print(trainno)
        return trainno

    # Method to return source and destination information
    def location(self, fro, to):
        loc = f"From: {fro} To: {to}"
        print(loc)
        return loc

    # Method to return ticket price information
    def price(self, fro, to):
        pri = f"Cost of your train ride from: {fro} To: {to} is: {random.randint(400, 500)}"
        print(pri)
        return pri

# Collecting user input
name = input("Enter your name: ")
fro = input("Enter where you want to board the train: ")
to = input("Enter where is your destination the train: ")

# Creating an object of the Train_booking class
name = Train_booking()

# Calling methods and storing their returned values
a = name.greet()
b = name.Train_no()
c = name.location(fro, to)
d = name.price(fro, to)

# Writing ticket details to a file
with open("Ticket_details.txt", "w") as f:
    f.write(a + "\n")
    f.write(b + "\n")
    f.write(c + "\n")
    f.write(d + "\n")
