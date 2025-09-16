## 
# @file Coupon.py
#
# @brief Coupon Model
# 
# @section description_cinema Description
# Maintains infomation of coupons
#
# @section notes_cinema Notes
# (additional notes)
# 
# @section author_cinema Author
# Created by Nicholas Ting on 28/09/2023


class Coupon:
    """! The Coupon class maintains Coupon objects and methods"""
    nextID = 111111
    def __init__(self,ccode: str, rate: int):
        """! The class initialiser
        @param ccode The coupon's code
        @param rate The coupon's discount rate
        """
        # The coupon's id
        self.__couponId: int = Coupon.nextID
        # The coupon's code
        self.__couponCode = ccode
        # The coupon's discount rate
        self.__discountRate = rate
        Coupon.nextID += 1

    @property
    def couponId(self) -> str:
        """! Getter method for id
        @return The coupon's id as a string
        """
        return str(self.__couponId)

    @property
    def couponCode(self) -> str:
        """! Getter method for code
        @return The coupon's code as a string
        """
        return self.__couponCode
    
    @property
    def discountRate(self) -> int:
        """! Getter method for discount rate
        @return The coupon's discount rate as a float
        """
        return self.__discountRate
    
    @discountRate.setter
    def discountRate(self, rate: float) -> None:
        """! Setter method for discount rate
        @return A boolean to indicate whether the assignment is successful
        """
        self.__discountRate = rate

    def __str__(self) -> str:
        """! __str__ method for Coupon object
        @return The coupon id and code in a string
        """
        return self.couponId + " " + self.couponCode