## 
# @file ShoppingCart.py
#
# @brief ShoppingCart Model
# 
# @section description_cinema Description
# Maintains infomation of shopping carts
#
# @section notes_cinema Notes
# (additional notes)
# 
# @section author_cinema Author
# Created by Nicholas Ting on 28/09/2023

# Imports
from typing import List
from decimal import Decimal

from Screening import Screening
from Coupon import Coupon
from Seat import Seat

class ShoppingCart:
    """! The ShoppingCart class maintains ShoppingCart objects and methods"""
    nextID = 1
    def __init__(self, cpn: Coupon = None, screen: Screening = None):
        """! The class initialiser
        @param cpn The Coupon object (default value None)
        @param screen The Screening object (default value None)
        """
        # The shopping cart's id
        self.__shoppingCartId: int = ShoppingCart.nextID
        # The shopping cart's coupon
        self.__coupon = cpn
        # The shopping cart's screening
        self.__screening = screen
        # The shopping cart's seats
        self.__seatList: List[Seat] = []
        ShoppingCart.nextID += 1

    @property
    def shoppingCartId(self) -> str:
        """! Getter method for id
        @return The shopping cart's id as a string
        """
        return str(self.__shoppingCartId)

    @property
    def coupon(self) -> Coupon:
        """! Getter method for coupon
        @return The shopping cart's coupon as a Coupon object
        """
        return self.__coupon
    
    @property
    def screening(self) -> Screening:
        """! Getter method for screening
        @return The shopping cart's screening as Screening object
        """
        return self.__screening
    
    @property
    def seatList(self) -> List[Seat]:
        """! Getter method for seat list
        @return The shopping cart's seat list as a list of Seat objects
        """
        return self.__seatList
    
    @coupon.setter
    def coupon(self, cpn: Coupon) -> bool:
        """! Setter method for shopping cart's coupon
        @return A boolean to indicate whether the assignment is successful
        """
        self.__coupon = cpn

    @screening.setter
    def screening(self, scn: Coupon) -> bool:
        """! Setter method for shopping cart's screening
        @return A boolean to indicate whether the assignment is successful
        """
        self.__screening = scn

    @seatList.setter
    def seatList(self, seatlist: List) -> bool:
        """! Setter method for shopping cart's seat list
        @return A boolean to indicate whether the assignment is successful
        """
        self.__seatList = seatlist

    def __str__(self) -> str:
        """! __str__ method for Shopping Cart
        @return The string representation of the Customer object in a string
        """
        return "Shopping cart " + str(self.shoppingCartId)

    def calcTotal(self) -> float:
        """! Calculate total price of the seats in the seatList
        @return The total price as a float
        """
        total = 0
        for seat in self.seatList:
            total += seat.seatPrice
        # If a coupon is applied, calculate the discounted price
        if self.coupon != None:
            total = float(total) * (1 - (self.coupon.discountRate / 100))
        return Decimal("{:.2f}".format(total))