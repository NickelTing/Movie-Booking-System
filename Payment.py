## 
# @file Payment.py
#
# @brief Payment model
# 
# @section description_cinema Description
# Maintains infomation of payments
#
# @section notes_cinema Notes
# (additional notes)
# 
# @section author_cinema Author
# Created by Nicholas Ting on 28/09/2023

#  Imports
from abc import ABC, abstractmethod
from datetime import date, time, datetime

class Payment(ABC):
    """! The Payment class maintains Payment objects and methods"""
    nextID = 1
    def __init__(self,amt: float, pdate: datetime):
        """! The class initialiser
        @param amt The payment's amount
        """
        # The payment's id
        self._paymentID: int = Payment.nextID
        # The payment's amount
        self._paymentAmt = amt
        # The payment's amount
        self._paymentDate = pdate
        Payment.nextID += 1

    @property
    @abstractmethod
    def paymentID(self) -> str:
        """! Abstract getter method for payment ID
        @return The ID as a str
        """
        return str(self._paymentID)

    @property
    @abstractmethod
    def paymentAmt(self) -> float:
        """! Abstract getter method for payment amount
        @return The amount as a float
        """
        return self._paymentAmt
    
    @property
    @abstractmethod
    def paymentDate(self) -> datetime:
        """! Abstract getter method for payment Date
        @return The date as a datetime object
        """
        return self._paymentDate

class Cash(Payment):
    """! The Cash class inherits from the Payment class and maintains Cash objects and methods"""
    def __init__(self,amt: float,pdate: datetime):
        """! The class initialiser
        @param name The payment's type
        """
        # The cash's amount and payment date
        Payment.__init__(self,amt,pdate)

    @property
    def paymentID(self) -> str:
        """! Abstract getter method for payment ID
        @return The ID as a str
        """
        return str(self._paymentID)

    @property
    def paymentAmt(self) -> float:
        """! Abstract getter method for payment amount
        @return The amount as a float
        """
        return self._paymentAmt
    
    @property
    def paymentDate(self) -> datetime:
        """! Abstract getter method for payment Date
        @return The date as a datetime object
        """
        return self._paymentDate

    def __str__(self) -> str:
        """! __str__ method for Cash object
        @return The payment amount and type in a string
        """
        return "Cash $" + str(self.paymentAmt)


class CreditCard(Payment):
    """! The CreditCard class inherits from the Payment class and maintains CreditCard objects and methods"""
    def __init__(self,amt: float,pdate: datetime,cdnum: str,cdtype: str,edate: date,name: str):
        """! The class initialiser
        @param amt The credit card payment's amount
        @param cdnum The credit card number
        @param cdtype the credit card type
        """
        # The credit card's number
        self.__cardNumber = cdnum
        # The credit card's type
        self.__cardType = cdtype
        # The credit card's expiry date
        self.__cardExpiry = edate
        # The credit card's holder's name
        self.__cardName = name
        # The credit card payment's amount and payment date
        Payment.__init__(self,amt,pdate)

    @property
    def paymentID(self) -> str:
        """! Abstract getter method for payment ID
        @return The ID as a str
        """
        return str(self._paymentID)

    @property
    def paymentAmt(self) -> float:
        """! Abstract getter method for payment amount
        @return The amount as a float
        """
        return self._paymentAmt
    
    @property
    def paymentDate(self) -> datetime:
        """! Abstract getter method for payment Date
        @return The date as a datetime object
        """
        return self._paymentDate

    @property
    def cardNumber(self) -> str:
        """! Getter method for card number
        @return The card number as a string
        """
        return self.__cardNumber
    
    @property
    def cardType(self) -> str:
        """! Getter method for card type
        @return The card type as a string
        """
        return self.__cardType
    
    @property
    def cardExpiry(self) -> date:
        """! Getter method for expiry date
        @return The expiry date as a date object
        """
        return self.__cardExpiry
    
    @property
    def cardName(self) -> str:
        """! Getter method for card name
        @return The card name as a string
        """
        return self.__cardName

    def __str__(self) -> str:
        """! __str__ method for CreditCard object
        @return The payment amount and type as a string
        """
        return "Credit Card $" + str(self.paymentAmt)

    def getCreditCardDetails(self) -> str:
        """! Get details of a credit card
        @return The card number and card type of the credit card in a string"""
        pass

class DebitCard(Payment):
    """! The DeditCard class inherits from the Payment class and maintains DeditCard objects and methods"""
    def __init__(self,amt: float,pdate: datetime,cdnum: str,bank: str,name: str):
        """! The class initialiser
        @param amt The debit card payment's amount
        @param cdnum The debit card number
        @param cdtype the debit card type
        """
        # The debit card's number
        self.__cardNumber = cdnum
        # The debit card's bank issuer
        self.__cardBank = bank
        # The debit card's holder's name
        self.__cardName = name
        # The debit card payment's amount and payment date
        Payment.__init__(self,amt,pdate)

    @property
    def paymentID(self) -> str:
        """! Abstract getter method for payment ID
        @return The ID as a str
        """
        return str(self._paymentID)

    @property
    def paymentAmt(self) -> float:
        """! Abstract getter method for payment amount
        @return The amount as a float
        """
        return self._paymentAmt
    
    @property
    def paymentDate(self) -> datetime:
        """! Abstract getter method for payment Date
        @return The date as a datetime object
        """
        return self._paymentDate

    @property
    def cardNumber(self) -> str:
        """! Getter method for card number
        @return The payment amount and type as a string
        """
        return self.__cardNumber
    
    @property
    def cardBank(self) -> str:
        """! Getter method for card bank
        @return The card bank as a string
        """
        return self.__cardBank
    
    @property
    def cardName(self) -> str:
        """! Getter method for card name
        @return The card name as a string
        """
        return self.__cardName

    def __str__(self) -> str:
        """! __str__ method for DebitCard object
        @return The card number and type in a string
        """
        return "Debit Card $" + str(self.paymentAmt)
    
    def getDebitCardDetails(self) -> str:
        """! Get details of a debit card
        @return The card number and card type of the debit card in a string"""
        pass