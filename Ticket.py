## 
# @file Ticket.py
#
# @brief Ticket Model
# 
# @section description_cinema Description
# Maintains infomation of tickets
#
# @section notes_cinema Notes
# (additional notes)
# 
# @section author_cinema Author
# Created by Nicholas Ting on 28/09/2023

# Imports
from Seat import Seat
from Screening import Screening

class Ticket:
    """! The Ticket class maintains Ticket objects and methods"""
    nextID = 500000
    def __init__(self, screen: Screening, seat: Seat):
        """! The class initialiser
        @param screen The Screening object
        @param seat The Seat object
        """
        # The ticket's id
        self.__ticketId: int = Ticket.nextID
        # The ticket's screening
        self.__ticketScreening = screen
        # The ticket's seat
        self.__ticketSeat = seat
        Ticket.nextID += 1

    @property
    def ticketId(self) -> str:
        """! Getter method for id
        @return The ticket's id as a string
        """
        return str(self.__ticketId)
    
    @property
    def ticketScreening(self) -> Screening:
        """! Getter method for screening
        @return The ticket's screening as a Screening object
        """
        return self.__ticketScreening
    
    @property
    def ticketSeat(self) -> Seat:
        """! Getter method for seat
        @return The ticket's seat as a Seat object
        """
        return self.__ticketSeat
    
    @ticketSeat.setter
    def ticketSeat(self, seat: Seat) -> bool:
        """! Setter method for ticket's seat
        @return A boolean to indicate whether the assignment is successful
        """
        self.__ticketSeat = seat
        pass
    
    def __str__(self) -> str:
        """! __str__ method for Ticket object
        @return The ticket id, screening's movie and seat name in a string
        """
        return self.ticketId + " "  + self.ticketScreening.screenMovie + " " + self.ticketSeat.seatName