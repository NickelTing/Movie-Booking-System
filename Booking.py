## 
# @file Booking.py
#
# @brief Booking model
# 
# @section description_cinema Description
# Maintains infomation of bookings
#
# @section notes_cinema Notes
# (additional notes)
# 
# @section author_cinema Author
# Created by Nicholas Ting on 28/09/2023

# Imports
from typing import List
from datetime import date

from Payment import *
from Ticket import Ticket
from Movie import Movie
from Screening import Screening
from Coupon import Coupon

class Booking:
    """! The Booking class maintains Booking objects and methods"""
    nextID = 100
    def __init__(self, bkdate: date, bktotal: float, payment: Payment, movie: Movie, screening: Screening, coupon: Coupon = None):
        """! The class initialiser
        @param bkdate The booking's date
        @param bktotal The booking's total price
        @param payment The Payment Object
        @param screening The Screening Object
        @param coupon The Coupon Object (default None)
        """
        # The booking's id
        self.__bookingId: int = Booking.nextID
        # The booking's date
        self.__bookingDate = bkdate
        # The booking's total price
        self.__bookingTotal = bktotal
        # The booking's payment information
        self.__paymentDetails = payment
        # The booking's tickets
        self.__bookingTickets: List[Ticket] = []
        # The booking's movie
        self.__bookingMovie = movie
        # The booking's screening
        self.__bookingScreening = screening
        # The booking's coupon
        self.__bookingCoupon = coupon
        Booking.nextID += 1

    @property
    def bookingId(self) -> str:
        """! Getter method for id
        @return The booking's id as a string
        """
        return str(self.__bookingId)
    
    @property
    def bookingDate(self) -> date:
        """! Getter method for date
        @return The booking's date as a date
        """
        return self.__bookingDate
    
    @property
    def bookingTotal(self) -> float:
        """! Getter method for total price
        @return The booking's total price as a float
        """
        return self.__bookingTotal
    
    @property
    def paymentDetails(self) -> Payment:
        """! Getter method for payment details
        @return The booking's payment details as a Payment object
        """
        return self.__paymentDetails
         
    @property
    def bookingTickets(self) -> List[Ticket]:
        """! Getter method for tickets
        @return The booking's tickets as a list of Ticket object
        """
        return self.__bookingTickets
    
    @property
    def bookingMovie(self) -> Movie:
        """! Getter method for movie
        @return The booking's movie as a Movie object
        """
        return self.__bookingMovie
    
    @property
    def bookingScreening(self) -> Screening:
        """! Getter method for screening
        @return The booking's screening as a Screening object
        """
        return self.__bookingScreening
    
    @property
    def bookingCoupon(self) -> Coupon:
        """! Getter method for coupon
        @return The booking's coupon as a Coupon object
        """
        return self.__bookingCoupon
    
    @paymentDetails.setter
    def paymentDetails(self, pay: Payment) -> bool:
        """! Setter method for booking payment 
        @return A boolean to indicate whether the assignment is successful
        """
        self.__paymentDetails = pay
        pass

    def __str__(self) -> str:
        """! __str__ method for Booking object
        @return The booking id and screening in a string
        """
        return str(self.bookingId) + "," + str(self.bookingMovie) + "," + str(self.bookingScreening)