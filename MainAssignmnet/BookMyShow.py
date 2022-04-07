import sys
import openpyxl

def workbook(filename,sheetname):
    wb = openpyxl.load_workbook(filename)
    sh1 = wb[sheetname]
    row = sh1.max_row
    col = sh1.max_column
    return row, col, sh1,wb


class AdminOfBookMyShow():

    def __init__(self,adminName,adminPassword):
        self.adminName=adminName
        self.adminPassword=adminPassword
        print("******WelcomeAdmin*******\n1.Add New Movie Info\n2.Edit Movie\n3.Delete Movie\n4.Logout")

    def adminOperations(self,choice):
        while(True):
            row, col, sh1, wb = workbook("MoviesInfo.xlsx", "Sheet1")
            if(choice==1):
                # wb = openpyxl.load_workbook("MoviesInfo.xlsx")
                # sh1 = wb['Sheet1']
                # row = sh1.max_row
                # col = sh1.max_column
                # print(row, col)
                print("enter the details of the movie")
                row1 = 1
                column1 = 1
                for c in range(1,col+1):
                    m=(sh1.cell(row1,column1).value)
                    sh1.cell(row + 1, c, value=input(f"Enter the {m}: "))
                    column1 += 1
                wb.save("updated.xlsx")
                break
            elif(choice==2):
                movieNameToBeEdited=input("enter the movie name that you want to edit: ")
                # wb = openpyxl.load_workbook("MoviesInfo.xlsx")
                # sh1 = wb['Sheet1']
                # row = sh1.max_row
                # col = sh1.max_column
                #column1 = 1
                #newName= sh1.cell(row=1, column=1).value
                for i in range(2,row+1):
                    name = sh1.cell(i, column=1).value
                    if(movieNameToBeEdited==name):
                        for j in range(1,col+1):
                            for m in range(1,col+1):
                                newName = sh1.cell(1,m).value
                                sh1.cell(i, j, value=input(f"Enter the {newName} to change: "))
                        #column1 += 1
                wb.save("MoviesInfo.xlsx")
                break
            elif(choice==3):
                movieToBeDeleted=input("Enter the movie name you want to Delete: ")
                # wb = openpyxl.load_workbook("MoviesInfo.xlsx")
                # sh1 = wb['Sheet1']
                # row = sh1.max_row
                # col = sh1.max_column
                for i in range(2,row+1):
                    name=sh1.cell(i,column=1).value
                    if(name==movieToBeDeleted):
                        sh1.delete_rows(i, True)
                wb.save("updated2.xlsx")
                break
            elif(choice==4):
                print("You have Successfully Logged out")
                sys.exit()


class UserDetails(AdminOfBookMyShow):

    def __init__(self,userName,userPassword):
        self.userName=userName
        self.userPassword=userPassword
        print(f"*****Hello {self.userName},you have Logged in Successfully*****")
    # def workbook(self):
    #     wb = openpyxl.load_workbook("MoviesInfo.xlsx")
    #     sh1 = wb['Sheet1']
    #     row = sh1.max_row
    #     col = sh1.max_column
    #     return row ,col,sh1

    def userActions(self):
        # wb = openpyxl.load_workbook("MoviesInfo.xlsx")
        # sh1 = wb['Sheet1']
        # row = sh1.max_row
        # col = sh1.max_column
        row, col, sh1, wb = workbook("MoviesInfo.xlsx", "Sheet1")
        m = 1
        for i in range(2,row+1):
            print(m,end='.')
            print(sh1.cell(i,1).value)
            m+=1

        choiceByUser=int(input("Enter the choice you want to choose"))
        if(choiceByUser==1):
            print("***** Welcome User *****")
            # wb = openpyxl.load_workbook("MoviesInfo.xlsx")
            # sh1 = wb['Sheet1']
            # row = sh1.max_row
            # col = sh1.max_column

            for i in range(1, col + 1):
                print(sh1.cell(1, i).value, end=": ")
                print(sh1.cell(choiceByUser + 1, i).value)
            print("1.Book Tickets\n2. Cancel Ticket \n3. Give User Rating ")
            userTicketChoice=int(input("Enter the choice from above: "))
            if(userTicketChoice==1):
                print("***** Welcome User *****")
                for i in range(7,9):
                    print(f"Timing : {sh1.cell(choiceByUser + 1, i).value}")
                timing=int(input("enter the timing you want to choose: "))
                print(f"selected timing {timing}")
                print(f"Remaining Seats is {sh1.cell(choiceByUser + 1,13).value}")
                totalTicketsToBeBooked=int(input("Enter the number of tickets to be Booked:"))
                #sh1.cell(choiceByUser + 1,13,value=)










print("******Welcome to BookMyShow*******\n1.Login\n2.Register new account\n3.Exit")
user_input=int(input("Enter your choice: "))
while(True):
    if(user_input==1):
        print("Welcome\n1.AdminLogin\n2.UserLogin")
        loginType=int(input("enter your choice"))
        if(loginType==1):
            name = input("enter you name")
            password = input("enter your password")
            admin=AdminOfBookMyShow(name,password)
            admin.adminOperations(int(input("Enter your choice to perform: ")))
        if(loginType==2):
            userName=input("enter your UserName: ")
            UserPassword=input("enter the password: ")
            user=UserDetails(userName,UserPassword)
            user.userActions()

        break
    elif(user_input==2):
        userName=input("Enter Your Name")
        userEmail=input("Enter Your Email")
        userPhoneNumber = int(input("Enter Your PhoneNumber"))
        userAge = input("Enter Your Age")
        userPassword = input("Enter Your Password")
        keshav=UserDetails(userName,userPassword)



        break
    else:
        sys.exit()