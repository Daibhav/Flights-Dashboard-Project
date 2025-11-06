# importing flights.csv to precreated database on mysql
# database se related saara code yaha likha hua hoga

# import pandas as pd
# import pymysql
# from sqlalchemy import create_engine
# df = pd.read_csv('flights.csv')

# engine = create_engine("mysql+pymysql://root:My#721#sql@127.0.0.1/flights")
# df.to_sql('flights_table',con = engine, if_exists = 'replace',index = False)

# print('upload complete')


# now we will connect to our database

import mysql.connector
class DB:

    # we will make a constructor

    def __init__(self):
        # connect to the database
        try:
            self.conn = mysql.connector.connect(
                host = '127.0.0.1',
                user = 'root',
                password = 'My#721#sql',
                database = 'flights'
            )
            self.mycursor = self.conn.cursor()
            print('connection established')
        except:
            print('connection error')
    
    # Airline piechart(no. of flights of which company)
    def fetch_city_names(self):

        city = []
        self.mycursor.execute("""
        select distinct(Source) from flights.flights_table
        union
        select distinct(Destination) from flights.flights_table;
        """)

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
        
        return city
    
    # showcasing in dataframe
    def fetch_all_flights(self,source,destination):
        self.mycursor.execute("""
        select Airline,Route,Dep_Time,Duration,Price from flights.flights_table
        where Source = '{}' and Destination = '{}';
        """.format(source,destination))

        data = self.mycursor.fetchall()
        return data

    # number of flights line chart
    def fetch_flights_frequency(self):

        airline = []
        frequency = []

        self.mycursor.execute("""
        select Airline, count(*) from flights_table
        group by Airline 
        """)

        data = self.mycursor.fetchall() # our data has two items, one is the name of the airline and other is its frequency
        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline,frequency   
    
    # busy airport bar chart
    def busy_airport(self):

        city = []
        frequency = []
        self.mycursor.execute("""
        select Source, count(*) 
        from (select Source from flights.flights_table
        union all 
        select Destination from flights.flights_table) t1
        group by Source
        order by count(*) desc
        """)

        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city,frequency   


    # Daily number of flights 
    def daily_frequency(self):
        date = []
        frequency = []

        self.mycursor.execute("""
        select Date_of_Journey, count(*) from flights_table
        group by Date_of_Journey
        """) 
        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])
        return date,frequency    

        