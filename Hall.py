## 
# @file Hall.py
#
# @brief Hall model
# 
# @section description_cinema Description
# Maintains infomation of halls
#
# @section notes_cinema Notes
# (additional notes)
# 
# @section author_cinema Author
# Created by Nicholas Ting on 28/09/2023

# Imports
from typing import List

from Seat import Seat

class Hall:
    """! The Hall class maintains Hall objects and methods"""
    nextID = 1
    def __init__(self, hname: str, cap: int):
        """! The class initialiser
        @param hname The hall's name
        @param cap The hall's capacity
        """
        # The hall's id
        self.__hallId: int = Hall.nextID
        # The hall's name
        self.__hallName = hname
        # The hall's capacity
        self.__capacity =  cap
        # The hall's seat list
        self.__seatList: List[Seat] = []
        Hall.nextID += 1

    @property
    def hallId(self) -> str:
        """! Getter method for id
        @return The hall's id as a string
        """
        return str(self.__hallId)

    @property
    def hallName(self) -> str:
        """! Getter method for name
        @return The hall's name as a string
        """
        return self.__hallName
    
    @property
    def hallCapacity(self) -> int:
        """! Getter method for capacity
        @return The hall's capacity as an integer
        """
        return self.__capacity
    
    @property
    def seatList(self) -> List[Seat]:
        """! Getter method for seat list
        @return The hall's seat list as a list of Seat objects
        """
        return self.__seatList

    @hallCapacity.setter
    def hallCapacity(self, cap: int) -> bool:
        """! Setter method for hall's capacity 
        @return A boolean to indicate whether the assignment is successful
        """
        self.__capacity = cap
        pass

    def __str__(self) -> str:
        """! __str__ method for Hall object
        @return The hall name in a string
        """
        return self.hallName
    
    def addSeat(self, seat: Seat) -> bool:
        """! add a seat to the seat list
        @param seat A Seat object
        @return A boolean
        """
        self.seatList.append(seat)
        return

