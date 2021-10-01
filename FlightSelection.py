from Agnos.Booking import Selection_Of_Distance_Fare

class Flight:

    def __init__(self):
        self.Traveller_Name = str(input("Enter Traveller Name: "))

        self.Baggage = int(input("Enter Baggage in Kgs: "))

        self.PromoCode = str(input("PromoCode Available (yes/y): ")).lower()

        self.Frequent_Traveller = str(input("Frequent Traveller (yes/y): ")).lower()


    def Flight_Route(self):
        try:
            min_distance_fare = Selection_Of_Distance_Fare().Minimum_Distance_Fare()
            min_distance = min_distance_fare[0]
            min_fare = min_distance_fare[1]

            if (self.Baggage>40 and (self.PromoCode in ('yes','y'))):
                f = ((self.Baggage-40)*0.1)+(min_fare-(min_fare*0.05))


            elif (self.Baggage<=40 and (self.PromoCode in ('yes','y'))):
                f = (min_fare-(min_fare*0.05))


            elif (self.Baggage>40 and (self.PromoCode in ('no','n'))):
                f = min_fare+((self.Baggage-40)*0.1)

            elif (self.Baggage<=40 and (self.PromoCode in ('no','n'))):
                f = min_fare

            else:
                print("Enter Proper values")

            if (self.Frequent_Traveller in ('yes','y')):
                print("Mr/Ms/Mrs {} can travel with fare ${} of {} km distance and he can wait at special lounge".format(self.Traveller_Name,f,min_distance))
            elif (self.Frequent_Traveller in ('no','n')):
                print("Mr/Ms/Mrs {} can travel with fare ${} of {} km distance".format(self.Traveller_Name,f,min_distance))
            else:
                print("Enter Proper values")
        except ValueError:
            print("Value Error")

f = Flight()
f.Flight_Route()
