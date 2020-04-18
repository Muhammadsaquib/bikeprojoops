
#@author: Saqib Shaikh
# Bike Rental System

import random

total_av_bike = 20

class B_rental_s:
    cs_info = {}
    cs_record ={}
    cs_cod = {}
    global total_av_bike
    total_av_bike = 20
    
    def __init__(self):
        self.a = 0
        self.b = 0
        
        
    def show_d(self):
        print('''
* Rent bikes on hourly basis $5 per hour.-->Press "1"
* Rent bikes on daily basis $20 per day.-->Press "2"
* Rent bikes on weekly basis $60 per week.-->Press "3"''')
        self.user_in()
        
    def total_bikes(self):
       print(f"* Right now have" , total_av_bike , " bikes available!")
        
        
    
    def user_in(self):
        global total_av_bike
        self.a = 0 
        self.a = int(input("Enter the period of time (e.g 1,2,3) = "))
        if self.a == 1 or self.a == 3 or self.a == 2:
            self.b = int(input("No: of Bike you want :"))
            while 0 < self.b <= total_av_bike:    
                if self.a == 1:
                    self.cus_hrs= float(input("How many hours :"))
                    self.cost_T= self.cus_hrs * 5
                    break
                if self.a == 3:
                    self.cus_week = int(input("How many weeks :"))
                    self.cost_T = self.cus_week * 60
                    break
                if self.a == 2:
                    self.cus_days = int(input("How many days :"))
                    self.cost_T= self.cus_days*20

                    break
            else:
                print(f"Right now have" ,total_av_bike , " bikes available! Sorry" )
                self.user_in()    
            self.cs_nam = input("Please enter you first name :")
            self.cod_gen = str(random.randint(10000,99999))
            print("Your Customer Code", self.cod_gen)
            print("Have a nice & safe  Ride")
            self.calcu()
                    
        else :
            print("Invalid Entry\nPlease try again")
            self.user_in()
                
    def retun_b(self):
        global total_av_bike
        self.cus_naam = str(input("Please Enter your first name :"))
        if self.cus_naam in self.cs_record:
            self.u_ver_cod = input("Please enter the generated Code :")
            if self.u_ver_cod in self.cs_cod and self.cs_info[self.u_ver_cod] == self.cus_naam :
                self.u_in_ret = int(input("How many bikes you want to return :"))
                total_av_bike += self.u_in_ret
                self.cs_record[self.cus_naam] -= self.u_in_ret 
                self.cs_bil = input("You want Bill? Y/N")
                if self.cs_bil == "Y" or self.cs_bil == "y":
                    self.invent()
                else:
                    print("You have",self.cs_record[self.cus_naam] ,"Bikes after this" )
            else:
                print("Wrong Code Please try again!")
                self.retun_b()
        else:
            print("Your Name is not found!")
            self.retun_b()
                
    def calcu(self):
        global total_av_bike
        self.cs_info[self.cod_gen] = self.cs_nam
        self.cs_record[self.cs_nam] = self.b
        self.cs_cod[self.cod_gen] = self.b
        total_av_bike -= self.b
        print(self.cs_cod)
        print(self.cs_record)
        print(self.cs_info)
        return self.cs_cod,self.cs_record,self.cs_info,total_av_bike

        
    def invent(self):
         global total_av_bike
         print("Total Bill = ",self.cost_T,"$")
         print("Total Bikes available =", total_av_bike)
         print("You have",self.cs_record[self.cus_naam] )



print(" *Press =1 for Take new bikes\n*Press =2 for Return bikes\n*Press =3 for Total bikes Available")
     
op = input("Please enter the choice :")
def case_userIn(op):
    cus_1 = B_rental_s()
    switcher = {'1' : cus_1.show_d(),
                '2' : cus_1.retun_b(),
                '3' : cus_1.total_bikes()}
    ex = switcher.get(op, "Invalid Entry")


case_userIn(op)
    
    


