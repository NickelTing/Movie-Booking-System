## 
# @file Screening.py
#
# @brief Screening Model
# 
# @section description_cinema Description
# Maintains infomation of screenings
#
# @section notes_cinema Notes
# (additional notes)
# 
# @section author_cinema Author
# Created by Nicholas Ting on 28/09/2023

# Imports
from typing import List
from datetime import date, time

from Seat import Seat
from Hall import Hall

class Screening:
    """! The Screening class maintains Screening objects and methods"""
    nextID = 100
    def __init__(self, scndate: date, scntime: time, endtime: time, scnhall: Hall):
        """! The class initialiser
        @param scndate The screening's date
        @param scntime The screening's start time
        @param endtime The screening's end time
        @param scnhall The Hall Object
        """
        # The screening's id
        self.__screenId: int = Screening.nextID
        # The screening's date
        self.__screenDate = scndate
        # The screening's start time
        self.__screenTime = scntime
        # The screening's end time
        self.__endTime = endtime
        # The screening hall
        self.__screenHall = scnhall
        # The screening's booked seats
        self.__bookedSeats: List[Seat] = []
        Screening.nextID += 1

    @property
    def screenId(self) -> int:
        """! Getter method for id
        @return The screening's id as a string
        """
        return int(self.__screenId)

    
    @property
    def screenDate(self) -> date:
        """! Getter method for date
        @return The screening's date as a date
        """
        return self.__screenDate
    
    @property
    def screenTime(self) -> time:
        """! Getter method for start time
        @return The screening's start time as a time
        """
        return self.__screenTime
    
    @property
    def endTime(self) -> time:
        """! Getter method for  end time
        @return The screening's end time as a time
        """
        return self.__endTime
    
    @property
    def screenHall(self) -> Hall:
        """! Getter method for hall
        @return The screening hall as a Hall object
        """
        return self.__screenHall
    
    @property
    def bookedSeats(self) -> List[Seat]:
        """! Getter method for booked Seats
        @return The screening's booked seats as a list of Seat objects
        """
        return self.__bookedSeats

    def __str__(self) -> str:
        """! __str__ method for Booking object
        @return The screening date and time in a string
        """
        return self.screenDate.strftime("%d/%m/%Y") + "," + self.screenTime.strftime("%H:%M") + "-" + self.endTime.strftime("%H:%M") + "," + str(self.screenHall)

    def getScreeningDetails(self) -> str:
        """! Get details of a screening
        @return The movie, date, time, hall and available seats in a string
        """
        details = "Screening ID: " + str(self.screenId)
        details += "\nDate: " + str(self.screenDate)
        details += "\nStart Time: " + str(self.screenTime)
        details += "\nEnd Time: " + str(self.endTime)
        details += "\nHall: " + str(self.screenHall)
        details += "\nNo. of Tickets: " + str(len(self.bookedSeats))
        return details

    def deleteTickets(self, seats: List[Seat]) -> None:
        """! Delete seats from the Screening
        #param seats A list of Seat objects
        """
        for seat in seats:
            for booked in self.bookedSeats:
                if booked == seat:
                    self.bookedSeats.remove(seat)
