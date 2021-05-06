import numpy as np
import pandas as pd
import  sys

class Bookmy_Tickets:
    print('Welcome to StarkCinemas')

    def __init__(self):
        self.details = {}
        self.matrix = []
        self.pricing = {}
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
        if choice == 1:
            self.show_screens()
        if choice == 2:
            self.Buy_tickets()
        if choice == 3:
            self.Statistics()
        if choice == 4:
            self.ticket_info()
        if choice == 5:
            sys.exit()




    def show_screens(self):
        print("*******************************************************")
        print('Type of screen you want enjoy watching movie')
        print('1 . IMAX 4K Dual Digital Projecter')
        print('2 . Min_screen with Stellar Surround Sound')

        choice=int(input('Enter your screen Type you want'))

        if choice == 1:
            print("Total Seats in Imax_screen:")
            self.row = 6
            self.col = 6

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
            # self.details = {}
            # self.matrix = []
            # self.pricing={}

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
        print("*******************************************************")
        self.row  = int(input("Enter the Row "))
        self.col  =int(input("Enter the column"))
        self.row=self.row-1
        self.col=self.col-1
        print("Enter Row and Column for your desired Place")
        # print(self.matrix)
        self.arr = np.array(self.matrix)
        self.df = pd.DataFrame(self.arr)
        self.df.index = np.arange(1,len(self.df)+1)
        self.df.columns = np.arange(1,len(self.df)+1)
        self.df.iloc[self.row,self.col] = 'b'
        print(self.df)
        # self.matrix[self.row][self.col] = 'b'
        # print(self.matrix)
        print("SUCESSFULLY YOUR TICKET HAVE BEEN BOOKED cost is 10$ ")

        booking_details={}
        customer_name,customer_gender,customer_age,customer_phone=input("Enter your Name Gender Age Phone_Number: \n").split()

        booking_details[int(self.row),self.col]=[(customer_name),(customer_gender),int(customer_age),int(customer_phone)]
        self.details.update(booking_details)
        # print(self.details)
        # print(self.details.values())

        # if int(customer_age) > 17 and len(customer_phone) == 10:
        #     booking_details[int(self.row,self.col)]=list[((customer_name),(customer_gender),int(customer_age),int(customer_phone))]
        #     self.details.update(booking_details)
        #     print(booking_details)
        print("SUCESSFULLY YOUR TICKET HAVE BEEN BOOKED PLEASE PROVIDE US FURTHER INFROMATION ")
    def Statistics(self):

        # if self.df.shape[1] * self.df.shape[0]>=30:
        print(self.df)


        count1 = 1
        count2 = 1
        for i in self.matrix:
            for j in i:
                if j == 'b':
                    count1 = count1 + 1
                else:
                    count2 = count2 + 1
        print("number of ticket purchased", count1)
        print("number of ticket percentage",(count1 * count2)/100)
        print("current income")
        if self.row * self.col >= 30:
            print("total income",(self.row * self.col)*8)
        if self.row * self.col <= 60:
            print("total income",(self.row * self.col)*10)
        else:
            #totalseats = self.row * self.col
            a = self.row // 2
            c = 1
            d = 1
            for i in range(0, a):
                c = a * self.col * 10
            for j in range(a, self.row):
                d = a * self.col * 8
            print("total income", c + d)
            #return self.total_income
        buy = input('To Procced with Main_Menu Press 1')
        if buy == '1':
            self.display()

    def ticket_info(self):
        print("*******************************************************")
        self.getrow=int(input("Enter your row number"))
        self.getcol=int(input("Enter your column number"))
        self.getrow = self.getrow - 1
        self.getcol = self.getcol - 1
        print("Name: ", self.details[int(self.getrow) , int(self.getcol) ])
        print("Gender: ", self.details[int(self.getrow) , int(self.getcol)][1])
        print("Age: ", self.details[int(self.getrow) , int(self.getcol) ][2])
        print("Phone Number: ", self.details[int(self.getrow) , int(self.getcol) ][3])
        print("Please Check you exact seat loction in Theater")
        print(self.df)
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
        buy = input('To Procced with Main_Menu Press 1')
        if buy == '1':
            self.display()



movie = Bookmy_Tickets()
movie.Buy_tickets()
