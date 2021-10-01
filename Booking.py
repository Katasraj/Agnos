import pandas as pd

class Selection_Of_Distance_Fare:

    def Minimum_Distance_Fare(self):
        df_flight_distance = pd.read_excel('FlightInfo.xlsx',sheet_name="Sheet1",index_col=None,usecols="C")

        df_flight_fare = pd.read_excel('FlightInfo.xlsx',sheet_name="Sheet1",index_col=None,usecols="D")

        Distance = df_flight_distance['Distance(Miles)'].to_list()

        Fare = df_flight_fare['Fare(Dollars)'].to_list()

        min_distance = Distance[0]

        for distance_val in Distance:
            if distance_val < min_distance:
                min_distance = distance_val

        fare_list = []
        for idx_distance in range(len(Distance)):
            if Distance[idx_distance] == min_distance:
                fare_list.append(Fare[idx_distance])


        min_fare = fare_list[0]

        for fare_val in fare_list:
            if fare_val < min_fare:
                min_fare = fare_val

        return [min_distance,min_fare]





