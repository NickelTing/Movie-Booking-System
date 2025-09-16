## 
# @file Seat.py
#
# @brief Seat Model
# 
# @section description_cinema Description
# Maintains infomation of seats
#
# @section notes_cinema Notes
# (additional notes)
# 
# @section author_cinema Author
# Created by Nicholas Ting on 28/09/2023


# Imports
from typing import List

class Seat:
    """! The Seat class maintains Seat objects and methods"""
    nextID = 1
    def __init__(self, sname: str, sprice: float):
        """! The class initialiser
        @param sname The seat's name
        @param sprice The seat's price
        """
        # The seat's id
        self.__seatId: int = Seat.nextID
        # The seat's name
        self.__seatName = sname
        # The seat's name
        self.__seatPrice = sprice
        Seat.nextID += 1

    @property
    def seatId(self) -> int:
        """! Getter method for id
        @return The seat's id as a string
        """
        return int(self.__seatId)
    
    @property
    def seatName(self) -> str:
        """! Getter method for name
        @return The seat's name as a string
        """
        return self.__seatName
    
    @property
    def seatPrice(self) -> float:
        """! Getter method for price
        @return The seat's price as an float
        """
        return self.__seatPrice

    @seatPrice.setter
    def seatPrice(self, price: float) -> bool:
        """! Setter method for seat's price 
        @return A boolean to indicate whether the assignment is successful
        """
        self.__seatPrice = price
        pass

    def __str__(self) -> str:
        """! __str__ method for Seat object
        @return The seat id and name in a string
        """
        return self.seatName