## 
# @file Notification.py
#
# @brief Notification Model
# 
# @section description_cinema Description
# Maintains infomation of notifications
#
# @section notes_cinema Notes
# (additional notes)
# 
# @section author_cinema Author
# Created by Nicholas Ting on 28/09/2023

from datetime import date, time, datetime

class Notification:
    """! The Notification class maintains Notification objects and methods"""
    nextID = 1
    def __init__(self, note: str, cdate: date):
        """! The class initialiser
        @param note The notification message
        """
        # The notification's id
        self.__notificationId= Notification.nextID
        # The notification's message
        self.__notificationMessage= note
        # The notification's creation date
        self.__notificationDate = date
        Notification.nextID += 1

    @property
    def notificationId(self) -> str:
        """! Getter method for id
        @return The notification's id as a string
        """
        return str(self.__notificationId)
    
    @property
    def notificationMessage(self) -> str:
        """! Getter method for message
        @return The notification's message as a string
        """
        return self.__notificationMessage
    
    @notificationMessage.setter
    def notificationMessage(self, note: str) -> bool:
        """! Setter method for seat's price 
        @return A boolean to indicate whether the assignment is successful
        """
        self.__notificationMessage = note
        pass

    @property
    def notificationDate(self) -> date:
        """! Getter method for creation date
        @return The notification's creation date as a date object
        """
        return self.__notificationDate

    def __str__(self) -> str:
        """! __str__ method for Notification object
        @return The notification id and name in a string
        """
        return self.notificationMessage