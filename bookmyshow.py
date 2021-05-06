import numpy as np
import pandas as pd

class Bookmy_Tickets:
    print('Welcome to StarkCinemas')

    def __init__(self):
        self.display()

    def display(self):
        print('******************************************')
        print('PLEASE ENTER YOUR CHOICE : ')
        print('******************************************')
        print('1. Show the screens')
        print('2. Buy a Tickets')
        print('3. Statistics')
        print('4. Show booked Tickets User Info')
        print('5. Exit')
        choice = int(input('Enter your choice'))
        if choice == 5:
            exit()
        if choice == 1:
            self.show_screens()
        if choice == 2:
            self.Buy_tickets()
        if choice == 3:
            self.ticket_price()
        if choice == 4:
            self.ticket_info()



    def show_screens(self):

        print('Type of screen you want enjoy watching movie')
        print('1 . IMAX 4K Dual Digital Projecter')
        print('2 . Min_screen with Stellar Surround Sound')

        choice=int(input('Enter your screen Type you want'))

        if choice == 1:
            print("Total Seats in Imax_screen:")
            self.row = 6
            self.col = 6
            self.details = {}
            self.matrix = []
            self.pricing = {}
            for i in range(self.row):
                a = []
                for j in range(self.col):
                    a.append("S")

                self.matrix.append(a)
            print(end="  ")
            for j in range(self.col):
                print(j + 1, end=" ")
            print()
            for i in range(self.row):
                print(i + 1, end=" ")
                for j in range(6):
                    print(self.matrix[i][j], end=" ")
                print()

        buy = input('To Procced with Booking Tickets Press "Yes" or "No" ')
        if buy in ['Yes', 'yes', 'YES']:
            self.Buy_tickets()
        elif buy in ['No', 'NO', 'no']:
            self.display()
            # arr = np.array(self.matrix)
            # df = pd.DataFrame(arr)
            # df.iloc[2, 3] = 'b'
            # print(df)


        elif choice == 2:

            print("Total Seats in MinScreen :")
            self.row = 8
            self.col = 8
            self.details = {}
            self.matrix = []
            self.pricing={}

            self.pricing = {}
            for i in range(self.row):
                a = []
                for j in range(self.col):
                    a.append("S")

                self.matrix.append(a)
            print(end="  ")
            for j in range(self.col):
                print(j + 1, end=" ")
            print()
            for i in range(self.row):
                print(i + 1, end=" ")
                for j in range(8):
                    print(self.matrix[i][j], end=" ")
                print()
            # arr = np.array(self.matrix)
            #
            # # print(arr)
            #
            # df = pd.DataFrame(arr)
            # df.iloc[2,3] = 'b'
            # print(df)

        # print('To Procced with Booking Tickets Press "Yes" or "No" ')
        buy=input('To Procced with Booking Tickets Press "Yes" or "No" ')
        if buy in ['Yes' , 'yes' , 'YES']:
            self.Buy_tickets()
        if buy in ['No' , 'NO' , 'no']:
            self.display()


    def Buy_tickets(self):
        self.row = int(input("Enter the Row "))
        self.col=int(input("Enter the column"))
        print("Enter Row and Column Number for your desired Place")
        print(self.matrix)
        arr = np.array(self.matrix)
        df = pd.DataFrame(arr)
        df.iloc[self.row,self.col] = 'b'
        print(df)
        booking_details={}
        customer_name,customer_gender,customer_age,customer_phone=input("Enter your Name Gender Age Phone_Number: \n").split()

        booking_details[int(self.row),self.col]=[(customer_name),(customer_gender),int(customer_age),int(customer_phone)]
        self.details.update(booking_details)
        print(self.details)
        print(self.details.values())

        # if int(customer_age) > 17 and len(customer_phone) == 10:
        #     booking_details[int(self.row,self.col)]=list[((customer_name),(customer_gender),int(customer_age),int(customer_phone))]
        #     self.details.update(booking_details)
        #     print(booking_details)

    def ticket_info(self):

        self.getrow=int(input("Enter your row number"))
        self.getcol=int(input("Enter your column number"))
        print("Name: ", self.details[int(self.getrow) , int(self.getcol) ])
        print("Gender: ", self.details[int(self.getrow) , int(self.getcol)][1])
        print("Age: ", self.details[int(self.getrow) , int(self.getcol) ][2])
        print("Phone Number: ", self.details[int(self.getrow) , int(self.getcol) ][3])
       # print("Ticket Price: ", self.details[int(self.getrow) , int(self.getcol) ][4])
        buy = input('To Procced with Main_Menu Press 1')
        if buy=='1':
            self.display()

    def ticket_price(self):
        if self.row * self.col <= 60:
            for i in range(0, self.row + 1):
                for j in range(0, self.col + 1):
                    a = {}
                    a[i, j] = 10
                    self.pricing.update(a)

        elif self.row * self.col > 60:

            c = self.row // 2
            b = self.col // 2
            for i in range(0, self.row + 1):
                for j in range(0, self.col + 1):
                    a = {}
                    a[i, j] = 8
                    self.pricing.update(a)
            for i in range((c + 1), self.row + 1):
                for j in range(0, self.col + 1):
                    a = {}
                    a[i, j] = 10
                    self.pricing.update(a)

movie = Bookmy_Tickets()
movie.Buy_tickets()
