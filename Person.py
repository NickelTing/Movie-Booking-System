## 
# @file Person.py
#
# @brief Person model
# 
# @section description_cinema Description
# Maintains infomation of the users and guests
#
# @section notes_cinema Notes
# (additional notes)
# 
# @section author_cinema Author
# Created by Nicholas Ting on 28/09/2023

#  Imports
from abc import ABC, abstractmethod
from typing import List
from datetime import date, time

from ShoppingCart import ShoppingCart
from Booking import Booking
from Payment import *
from Seat import Seat
from Ticket import Ticket
from Hall import Hall
from Screening import Screening
from Movie import Movie
from Notification import Notification
from Coupon import Coupon


class Person(ABC):
    """! The Person class is an abstract class for users and guests"""
    def __init__(self, pname: str = "None"):
        """! The class initialiser
        @param pname The person's name (default value None)"""
        # The person's real name
        self._personName = pname

    @property
    @abstractmethod
    def givenName(self):
        """! An abstract method which gets the person's name"""
        pass

    def searchMovieTitle(self, title: str, movieList: List[Movie]) -> List[Movie]:
        """! Search movie by title
        @param title The movie's title
        @param movieList The movie's list
        @return A list of Movie objects
        """
        resultList = []
        for movie in movieList:
            if title in movie.movieTitle.lower():
                resultList.append(movie)
        return resultList

    def searchMovieLang(self, lang: str, movieList: List[Movie]) -> List[Movie]:
        """! Search movie by language
        @param lang The movie's language
        @param movieList The movie's list
        @return A list of Movie objects
        """
        resultList = []
        for movie in movieList:
            if lang in movie.movieLanguage.lower():
                resultList.append(movie)
        return resultList

    def searchMovieGenre(self, genre: str, movieList: List[Movie]) -> List[Movie]:
        """! Search movie by genre
        @param genre The movie's genre
        @param movieList The movie's list
        @return A list of Movie objects
        """
        resultList = []
        for movie in movieList:
            if genre in movie.movieGenre.lower():
                resultList.append(movie)
        return resultList

    def searchMovieDate(self, rDate: date, movieList: List[Movie]) -> List[Movie]:
        """! Search movie by release date
        @param rDate The movie's release date
        @param movieList The movie's list
        @return A list of Movie objects
        """
        resultList = []
        for movie in movieList:
            if rDate == movie.movieReleaseDate:
                resultList.append(movie)
        return resultList

    def viewMovieDetails(self, aMovie: Movie) -> str:
        """! View details of a movie
        @param aMovie A Movie object
        @return A string
        """
        return aMovie.getMovieDetails()
    
    def viewScreeningDetails(self, aScreening: Screening) -> str:
        """! Get details of a screening
        @param scn The Screening Object
        @return A string
        """
        return aScreening.getScreeningDetails()


class Guest(Person):
    """! The Guest class inherits from the Person class and maintains Guest objects and methods"""
    def __init__(self,pname):
        """! The class initialiser
        @param pname The guest's name
        """
        # The guest's real name
        super().__init__(pname)

    def register(self, name: str, uname: str, pw: str, email: str, address: str, phone: str) -> None:
        """! Register an account
        @param name The given name
        @param uname The username
        @param pw The password
        @param email The email address
        @param address The home address
        @param email The phone number
        @return A Customer object
        """
        aCustomer = Customer(name, uname, pw, email, address, phone)
        return aCustomer

    @property
    def givenName(self) -> str:
        """! Getter method for name
        @return The guest's name as a string"""
        return self._personName

    def __str__(self) -> str:
        """! __str__ method for Guest object
        @return The guest's name as a string"""
        return self.givenName

class User(Person):
    """! The User class inherits from the Person class and maintains User objects and methods"""
    def __init__(self, pname: str, email: str, uname: str, pw: str):
        """! The class initialiser
        @param pname The user's name
        @param email The user's email address
        @param uname The user's username 
        @param pw The user's password
        """
        # The user's email address
        self._userEmail = email
        # The user's username
        self._userName = uname
        # The user's password
        self._userPassword = pw
        # The user's real name
        super().__init__(pname)

    @property
    def givenName(self) -> str:
        """! Getter method for name
        @return The user's name as a string
        """
        return self._personName

    @property
    def userEmail(self) -> str:
        """! Getter method for email address
        @return The user's email address as a string
        """
        return self._userEmail

    @property
    def userName(self) -> str:
        """! Getter method for username
        @return The user's username as a string
        """
        return self._userName
    
    @property
    def userPassword(self) -> str:
        """! Getter method for password
        @return The user's password as a string
        """
        return self._userPassword

    def __str__(self) -> str:
        """! __str__ method for User object
        @return The user's username as a string
        """
        return self._userName

    def login(self, uname: str, pw: str) -> bool:
        """! Log in an account (abstract method)
        @param uname The user's username
        @param pw The user's password
        @return A boolean to indicate whether the login is successful
        """
        if uname == self.userName and pw == self.userPassword:
            return True
        else: 
            return False
    
    def logout(self) -> bool:
        """! Log out the account (abstract method)
        @return A boolean to indicate whether the logout is successful
        """
        return True

    @userPassword.setter
    def userPassword(self, pw: str) -> bool:
        """! Reset password of the user
        @return A boolean to indicate whether the reset is successful
        """
        self._userPassword = pw

class Customer(User):
    """! The Customer class inherits from the User class and maintains Customer objects and methods"""
    nextID = 1000
    def __init__(self, pname: str, email: str, uname: str, pw: str, cusadr: str, cusphone: str, cart: ShoppingCart = None):
        """! The class initialiser
        @param pname The customer's name
        @param email The customer's email address
        @param uname The customer's username
        @param pw The customer's password
        @param cusadr The customer's home address
        @param cusphone The customer's phone number
        @param cart The customer's ShoppingCart (class variable, default None)
        """
        # The customer's id
        self.__customerId: int = Customer.nextID
        # The customer's home address
        self.__customerAddress =  cusadr
        # The customer's phone number
        self.__customerPhone = cusphone
        # The customer's shopping cart
        self.__customerCart = cart
        # The customer's real name, email address, username and password
        User.__init__(self,pname,email,uname,pw)
        # The customer's booking list
        self.__bookingList: List[Booking] = []
        # The customer's notification list
        self.__notificationList: List[Notification] = []
        Customer.nextID += 1

    @property
    def customerId(self) -> str:
        """! Getter method for id
        @return The customer's id as a string
        """
        return str(self.__customerId)
    
    @property
    def customerAddress(self) -> str:
        """! Getter method for home address
        @return The customer's home address as a string
        """
        return self.__customerAddress
    
    @property
    def customerPhone(self) -> str:
        """! Getter method for phone number
        @return The customer's phone number as a string
        """
        return self.__customerPhone
    
    @property
    def customerCart(self) -> ShoppingCart:
        """! Getter method for shopping cart
        @return The customer's cart as a ShoppingCart object
        """
        return self.__customerCart
    
    @property
    def bookingList(self) -> List[Booking]:
        """! Getter method for booking list
        @return The customer's booking list as a list of Booking objects
        """
        return self.__bookingList
    
    @property
    def notificationList(self) -> List[Notification]:
        """! Getter method for notification list
        @return The customer's notification list as a list of Notification objects
        """
        return self.__notificationList

    @notificationList.setter
    def notificationList(self, noteList: List[Notification]) -> None:
        """! Setter method for notification list
        @return A boolean to indicate whether the assignment is successful
        """
        self.__notificationList = noteList
        pass
    
    @customerCart.setter
    def customerCart(self, cart: ShoppingCart) -> None:
        """! Setter method for shopping cart
        @return A boolean to indicate whether the assignment is successful
        """
        self.__customerCart = cart
        pass
    
    def __str__(self) -> str:
        """! __str__ method for Customer object
        @return The customer's id and name in a string
        """
        return self.customerId + " " + self.givenName

    def addCartItem(self, screen: Screening, seat: Seat) -> bool:
        """! Add a item to the shopping cart
        @param screen The Screening Object
        @param seat The Seat object
        @return A boolean to indicate whether the seat is added successfully.
        """
        self.customerCart.screening = screen
        self.customerCart.seatList.append(seat)
        return True

    def deleteCartItem(self, seat: Seat) -> bool:
        """! Delete a item from the shopping cart
        @param seat the Seat object
        @return A boolean to indicate whether the item is deleted successfully.
        """
        self.customerCart.seatList.remove(seat)
        return True
    
    def emptyCart(self) -> None:
        """! Clear the shopping cart"""
        self.customerCart.seatList = []
        self.customerCart.screening = None

    def viewCart(self) -> tuple:
        """! View the shopping cart"""
        screen = self.customerCart.screening
        seatList = self.customerCart.seatList
        price = self.customerCart.calcTotal()
        return (screen, seatList, price)

    def makePayment(self, option: str, amount: float, paymentDate: date, cardNum: str = None, cardName: str = None, banktype: str = None, expiryDate: date = None) -> bool:
        """! Make a payment
        @param option The payment's option
        @param amount The payment's amount
        @param cardNum The payment's card number
        @param cardName The payment's name on card
        @param banktype The payment's bank or card type
        @param month The payment's month
        @param year The payment's year
        @return A boolean to indicate whether the payment is successful
        """
        if option == "Credit Card":
            aPayment = CreditCard(amount,paymentDate,cardNum,banktype,expiryDate,cardName)
        elif option == "Debit Card":
            aPayment = DebitCard(amount,paymentDate,cardNum,banktype,cardName)
        else:
            aPayment = Cash(amount,paymentDate)
        return aPayment

    def addBooking(self, bkdate: date, bktickets: List[Ticket], pay: Payment, mv: Movie, scn: Screening, cpn: Coupon, cus = None) -> Booking:
        """! Make a booking
        @param bkdate The booking's date
        @param bktickets A list of the Ticket objects
        @param pay The Payment object
        @param scn The Screening object
        @param cus (overloading)
        @return A Booking object
        """
        aBooking = Booking(bkdate, pay.paymentAmt, pay, mv, scn, cpn)
        bktickets = sorted(bktickets, key=lambda x: x.ticketSeat.seatName)
        for ticket in bktickets:
            aBooking.bookingTickets.append(ticket)
            aBooking.bookingScreening.bookedSeats.append(ticket.ticketSeat)
        self.bookingList.append(aBooking)
        return aBooking

    def viewBooking(self, book: Booking) -> str:
        """! Display information of a booking
        @param book A Booking object
        @return A string
        """
        seats = ''
        count = len(book.bookingTickets) - 1
        for i in range(0,len(book.bookingTickets),1):
            seats += book.bookingTickets[i].ticketSeat.seatName
            if i != count:
                seats += ", "
        msg = "Movie Name: " + str(book.bookingMovie) + "\n"
        msg += "Screen Info: " + str(book.bookingScreening) + "\n"
        msg += "Number of Tickets: " + str(len(book.bookingTickets)) + "\n"
        msg += "Seats: " + seats + "\n"
        msg += "Payment Total: $" + str(book.bookingTotal) + "\n"
        if isinstance(book.paymentDetails, CreditCard):
            msg += "Payment Type: Credit Card\n"
        elif isinstance(book.paymentDetails, DebitCard):
            msg += "Payment Type: Debit Card\n"
        else:
            msg += "Payment Type: Cash\n"
        return msg

    def deleteBooking(self, book: Booking, cdate: date, cus = None) -> str:
        """! Delete a booking
        @param bk The Booking object
        @param cdate The cancellation date
        @param cus The Customer object (overloading)
        @return A string
        """
        # remove booking from list
        self.bookingList.remove(book)
        msg = "Booking for " + str(book.bookingMovie) + " " + str(book.bookingScreening) + " is cancelled\n\n"
        msg += "Payment of $" + str(book.bookingTotal) + " will be refunded"
        # create a payment with negative balance to show the payment is refunded to the customer (in the form of cash)
        refundAmt = book.paymentDetails.paymentAmt * -1
        aPayment = Cash(refundAmt, cdate)
        return msg, aPayment

    def viewNotifications(self) -> None:
        """! View the notifications"""
        pass


class Staff(User):
    """! The Staff class inherits from the User class and maintains Staff objects and methods"""
    nextID = 2000
    def __init__(self, pname: str, email: str, uname: str, pw: str):
        """! The class initialiser
        @param pname The staff's name
        @param email The staff's email address
        @param uname The staff's username
        @param pw The staff's password
        """
        # The staff's id
        self.__staffId: int = Staff.nextID
        # The staff's booking list
        self.__bookingList: List[Booking] = []
        # The staff's real name, email address, username and password
        User.__init__(self,pname,email,uname,pw)
        Staff.nextID += 1

    @property
    def staffId(self) -> str:
        """! Getter method for id
        @return The staff's id as a string
        """
        return str(self.__staffId)
    
    @property
    def bookingList(self) -> List[Booking]:
        """! Getter method for booking list
        @return The staff's booking list as a list of Booking objects
        """
        return self.__bookingList
    
    def __str__(self) -> str:
        """! __str__ method for Staff object
        @return The staff's id and name in a string
        """
        return self.staffId + " " + self.givenName

    def addBooking(self, bkdate: date, bktickets: List[Ticket], pay: Payment, mv: Movie, scn: Screening, cpn: Coupon, cus: Customer) -> Booking:
        """! Add a booking for a particular customer
        @param cus The Customer Object
        @param bkdate The booking's date
        @param bktickets A list of the Ticket objects
        @param pay The Payment object
        @param mv The Movie object
        @param scn The Screening object
        @param cpn The Coupon object
        @return A Booking object
        """
        aBooking = Booking(bkdate, pay.paymentAmt, pay, mv, scn, cpn)
        for ticket in bktickets:
            aBooking.bookingTickets.append(ticket)
            aBooking.bookingScreening.bookedSeats.append(ticket.ticketSeat)
        cus.bookingList.append(aBooking)
        return aBooking

    def deleteBooking(self, book: Booking, cdate: date, cus: Customer) -> str:
        """Delete a booking
        @param bk The Booking Object
        @param cdate The cancellation date
        @param cus The Customer Object
        @return A string
        """
        # remove booking from the customer's booking list
        cus.bookingList.remove(book)
        msg = "Booking for " + str(book.bookingMovie) + " " + str(book.bookingScreening) + " is cancelled\n\n"
        msg += "Payment of $" + str(book.bookingTotal) + " will be refunded"
        # create a payment with negative balance to show the payment is refunded to the customer (in the form of cash)
        refundAmt = book.paymentDetails.paymentAmt * -1
        aPayment = Cash(refundAmt, cdate)
        return msg, aPayment       

class Admin(User):
    """! The Admin class inherits from the User class and maintains Admin objects and methods"""
    nextID = 3000
    def __init__(self, pname: str, email: str, uname: str, pw: str):
        """! The class initialiser
        @param pname The admin's name
        @param email The admin's email address
        @param uname The admin's username
        @param pw The admin's password
        """
        # The admin's id
        self.__adminId: int = Admin.nextID
        # The admin's movie list
        self.__movieList: List[Movie] = []
        # The admin's screening list
        self.__screeningList: List[Screening] = []
        User.__init__(self,pname,email,uname,pw)
        Admin.nextID += 1

    @property
    def adminId(self) -> str:
        """! Getter method for id
        @return The admin's id as a string
        """
        return str(self.__adminId)
    
    @property
    def movieList(self) -> List[Movie]:
        """! Getter method for movie list
        @return The admin's movie list as a list of Movie objects
        """
        return self.__movieList
    
    @property
    def screeningList(self) -> List[Screening]:
        """! Getter method for screening list
        @return The admin's screening list as a list of Screening objects
        """
        return self.__screeningList
    
    def __str__(self) -> str:
        """! __str__ method for Admin object
        @return The admin's id and name in a string
        """
        return self.adminId + " " + self.givenName

    def addMovie(self, title: str, lan: str, gnr: str, redate: date) -> Movie:
        """! Add a new movie
        @param title The movie's title
        @param lan The movie's language
        @param gnr The movie's genre
        @param redate The movie's release date 
        @return A Movie object
        """
        return Movie(title,lan,gnr,redate)

    def deleteMovie(self, mv: Movie) -> bool:
        """! Delete a movie
        @param mv The Movie object
        @return A boolean to indicate whether the movie is deleted successfully 
        """
        # clear the screeninglist of the movie
        mv.movieScreeningList = []
        return True

    def addScreening(self, scndate: date, scnhall: Hall, scntime: time, endtime: time) -> Screening:
        """! Add a new screening
        @param scndate The Screening's date
        @param scnhall The Screening's hall
        @param scntime The Screening's start time
        @param endtime The Screening's end time
        @return A Acreening object
        """
        aScreening = Screening(scndate,scnhall,scntime,endtime)
        return aScreening

    def deleteScreening(self, scn: Screening, mv: Movie) -> bool:
        """! Delete a screening
        @param scn The Screening object
        @return A boolean to indiciate whether the screening is deleted successfully
        """
        # remove the screening from the movie's screening list
        mv.movieScreeningList.remove(scn)
        return True