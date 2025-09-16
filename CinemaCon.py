##
# @mainpage Cinema Application Project
#
# @section description_main Description 
# This project aims to develop an online movie ticket system that can facilitate the purchase of movie tickets by its customers.
# The e-ticketing system will allow customers to browse through the movies currently playing and book seats for screenings, anywhere and anytime.
#
# @section notes_main Notes
# Project is in the design phase
# 

## 
# @file CinemaCon.py
#
# @brief Controller of the system
# 
# @section description_cinema Description
# Implementation for Cinema
#
# @section notes_cinema Notes
# (additional notes)
# 
# @section author_cinema Author
# Created by Nicholas Ting on 28/09/2023

# Imports
from datetime import date, time, datetime
import re
from decimal import Decimal, getcontext

from Person import *
from ShoppingCart import ShoppingCart
from Booking import Booking
from Payment import *
from Coupon import Coupon
from Ticket import Ticket
from Seat import Seat
from Hall import Hall
from Screening import Screening
from Movie import Movie
from Notification import Notification

currentDate = date.today()

class Cinema:
    """! The Cinema Class defines all the methods for the controller"""
    def __init__(self):
        """! The class initialiser
        @param user The User object (default None)"""
        # Guest variable
        self.guest = Guest('guest')
        # The list of users
        self.userList = []
        # The list of customers
        self.customerList = []
        # The list of staffs
        self.staffList = []
        # The list of admins
        self.adminList = []
        # The list of bookings
        self.bookingList = []
        # The list of payments
        self.paymentList = []
        # The list of coupons
        self.couponList = []
        # The list of movies
        self.movieList = []
        # The list of screenings
        self.screeningList = []
        # The list of halls
        self.hallList = []
        # The list of seats
        self.seatList = []
        # The list of tickets
        self.ticketList = []
        # The list of notifications
        self.notificationList = []
        # The current user (default Guest)
        self.currentUser = self.guest

    def generateMovie(self, mvName, mvLanguage, mvGenre, releaseDate):
        """! Generate a movie from txt file
        @param mvName The movie's name
        @param mvLanguage The movie's language
        @param mvGenre The movie's genre
        @param releaseDate The movie's release date
        @return A Movie object
        """
        releaseDate = datetime.strptime(releaseDate, "%m/%d/%y").date()
        aMovie = Movie(mvName,mvLanguage,mvGenre,releaseDate)
        self.movieList.append(aMovie)
        return aMovie

    def generateScreening(self, title, scnDate, scnHall, scnTime, endTime):
        """! Generate a screening from txt file
        @param title The screening's movie title
        @param scnDate The screening's date
        @param scnTime The screening's start time
        @param endTime The screening's end time
        @param scnHall A Hall object
        @return A Screening object
        """
        # convert format
        scnDate = datetime.strptime(scnDate, "%m/%d/%y")
        scnDate = scnDate.strftime("%d/%m/%Y")
        scnDate = datetime.strptime(scnDate, "%d/%m/%Y").date()
        scnTime = datetime.strptime(scnTime, "%H:%M").time()
        endTime = datetime.strptime(endTime, "%H:%M").time()
        # create an identical hall object for the particular screening
        hallSample = self.findHall(scnHall)
        hall = self.createHall(hallSample.hallName,hallSample.hallCapacity)
        self.hallList.append(hall)
        aScreening = Screening(scnDate,scnTime,endTime,hall)
        # find a movie and hall object
        scnMovie = self.findMovie(title)
        # append to screening lists
        scnMovie.movieScreeningList.append(aScreening)
        self.screeningList.append(aScreening)
        return aScreening
    
    def returnCustomer(self, cus: str = None) -> Customer:
        """ Return a Customer object if the current user is not customer
        @param cus The customer ID and name (overloading)
        @return A Customer object
        """
        if self.checkUser() != "customer":
            user = self.findCustomer(str(cus))
        else:
            user = self.currentUser
        return user
    
    def returnCartCoupon(self, cus = None) -> int:
        """ Display the discount rate of the coupon applied in the shopping cart
        @param cus The customer ID and name (overloading)
        @return An integer
        """
        # return a Customer object
        user = self.returnCustomer(cus)
        # display discount rate if there is already a coupon applied
        if user.customerCart.coupon:
            return int(user.customerCart.coupon.discountRate)
        return None

    def createCustomer(self, customerName: str, username: str, password: str, email: str, cusAddress: str, cusPhone: str) -> None:
        """! Creates an instance of Customer
        @param customerName The customer's name
        @param username The customer's username
        @param password The customer's password
        @param email The customer's email address
        @param cusAddress The customer's home address
        @param cusPhone The customer's phone number
        """
        # generate a shopping cart for the customer
        aShoppingCart = ShoppingCart()
        # create an instance of customerf
        aCustomer = Customer(customerName,email,username,password,cusAddress,cusPhone,aShoppingCart)
        # append to the customer list and user list
        self.customerList.append(aCustomer)
        self.userList.append(aCustomer)
        return aCustomer

    def findCustomer(self, cus: str) -> Customer:
        """! Search for a customer
        @param customer The customer's id and username
        @return A Customer object
        """
        for customer in self.customerList:
            if str(customer) == cus:
                return customer
        return None

    def createStaff(self, staffName: str, username: str, password: str, email: str) -> None:
        """! Creates an instance of Staff
        @param staffName The staff's name
        @param username The staff's username
        @param password The staff's password
        @param email The staff's email
        """
        # create an instance of staff
        aStaff = Staff(staffName,email,username,password)
        # append to the staff list
        self.staffList.append(aStaff)
        self.userList.append(aStaff)
        return aStaff

    def findStaff(self, uname: str) -> Staff:
        """! Search for a staff
        @param uname The staff's username
        @return A Staff object
        """
        for staff in self.staffList:
            if staff.userName == uname:
                return staff
        return None
    
    def createAdmin(self, adminName: str, username: str, password: str, email: str) -> None:
        """! Creates an instance of Admin
        @param adminName The admin's name
        @param username The admin's username
        @param password The admin's password
        @param email The admin's email
        """
        # create an instance of admin
        aAdmin = Admin(adminName,email,username,password)
        # append to the admin list
        self.adminList.append(aAdmin)
        self.userList.append(aAdmin)
        return aAdmin

    def findAdmin(self, uname: str) -> Admin:
        """! Search for a admin
        @param uname The admin's username
        @return An Admin object
        """
        for admin in self.adminList:
            if admin.userName == uname:
                return admin
        return None

    def createHall(self, name: str, cap: int) -> None:
        """! Creates an instance of Hall
        @param name The hall's name
        @param cap The hall's capacity
        """
        aHall = Hall(name,cap)
        # create seats for the hall
        self.createSeats(aHall)
        # append the hall to the overall hall list
        self.hallList.append(aHall)
        return aHall


    def createSeats(self, hall: Hall) -> None:
        """! Creates multiple instances of Seat based on the capacity of each Hall.
        @param hall The Hall object
        """
        # calculate number of rows 
        row = hall.hallCapacity // 10
        remainder = hall.hallCapacity % 10
        # generate full rows of seats
        for i in range(row):
            for j in range(1,11):
                name = chr(65 + i) + str(j)
                aSeat = Seat(name,Decimal('15.00'))
                # append seat to the hall's seat list
                hall.addSeat(aSeat)
                self.seatList.append(aSeat)
        # if there is remainder, add an extra row with the remanining seats
        if remainder:
            for j in range(1,remainder + 1):
                name = chr(65 + row) + str(j)
                aSeat = Seat(name,Decimal('15.00'))
                # append seat to the hall's seat list
                hall.addSeat(aSeat)
                self.seatList.append(aSeat)

    def createCoupon(self, code: str, rate: int) -> None:
        """! Create a Coupon instance
        @param code The coupon's code
        @param rate The coupon's discount rate
        """
        aCoupon = Coupon(code, rate)
        self.couponList.append(aCoupon)

    def validateRegister(self, inputList: List) -> str:
        """! Validate registration inputs
        @param inputList A list of inputs
        @return A string
        """
        # get every input in the register frame and make sure they are not empty
        for input in inputList:
            if input == '':
                return "Input field(s) cannot be empty" 
        # validate given name
        if not re.match(r'^[a-zA-Z\s-]+$', inputList[0]):
            return "Name should contain alphabets and whitespace only"
        # validate phone number
        elif not re.match(r'^\d+$', inputList[1]):
            return "Phone number should contain numbers only"
        elif len(inputList[1]) < 7 or len(inputList[1]) > 12:
            return "Phone number should contain 7 to 12 numbers only"
        # validate home address
        elif not re.match(r'^[a-zA-Z0-9\s/-]+$', inputList[2]):
            return "Home address should contain alphabets, numbers and whitespace only"
        # validate email address
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', inputList[3]):
            return "Please enter a valid email address (eg. nick123@email.com)"
        # validate username
        elif not re.match(r'^[a-zA-Z0-9_]+$', inputList[4]):
            return "Username should contain alphabet and numbers only (no whitespace)"
        # validate new password and confirm password
        elif len(inputList[5].strip()) < 8 or len(inputList[6].strip()) < 8:
            return "Password should contain at least 8 characters (no whitespace)"
        elif inputList[5] != inputList[6]:
            return "New password should the same as confirm password"
        # check whether the name, phone number, email address and username is unique
        for customer in self.customerList:
            if customer.givenName.lower() == inputList[0].lower():
                return "The name has been registered"
            elif customer.customerPhone.strip() == inputList[1].strip():
                return "The phone number has been registered"
            elif customer.userEmail.lower()  == inputList[3].lower():
                return "The email address has been registered"
            elif customer.userName == inputList[4]:
                return "The username has been registered"
        return True
    
    def register(self, inputList: List) -> None:
        """! Register a customer
        @param inputList A list of inputs
        """
        # carry out registration
        aCustomer = self.currentUser.register(inputList[0],inputList[3],inputList[4],inputList[6],inputList[2],inputList[1])
        # create a shopping cart and assign it to the customer
        aShoppingCart = ShoppingCart()
        aCustomer.customerCart = aShoppingCart
        # append to the customer list
        self.customerList.append(aCustomer)
        self.userList.append(aCustomer)

    def validateReset(self, inputList: List) -> str:
        """! Validate registration inputs
        @param inputList A list of inputs
        @return A string
        """
        # get every input in the register frame and make sure they are not empty
        for input in inputList:
            if input == '':
                return "Input field(s) cannot be empty"    
        # validate email address
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', inputList[0]):
            return "Please enter a valid email address (eg. nick123@email.com)"
        # check if the email address exists
        for user in self.userList:
            if user.userEmail == inputList[0]:
                # if exists, validate new password and confirm password
                if len(inputList[1]) < 8 or len(inputList[2]) < 8:
                    return "Password should contain at least 8 characters"
                elif inputList[1] != inputList[2]:
                    return "New password should the same as confirm password"
                elif inputList[2] == user.userPassword:
                    return "New password should not be the same as the old password"
                return user
        return "Email address entered does not exists. Please try again"

    def resetPassword(self, user: User, pw: str) -> None:
        """! Reset
        @param user The account's holder
        @param pw The user's password
        """
        # set the password of the user to the new passwords
        user.userPassword = pw
        

    def login(self, username: str, password: str) -> str:
        """! Log in the system
        @param username The user's username
        @param password The user's password
        @return A boolean
        """
        # make sure the inputs fields are empty
        if username == "" or password == "":
            return "The input fields cannot be empty"
        # find user, check password if the username matches
        for user in self.userList:
            if user.login(username, password):
                return user
        return "Invalid username or password."

    def checkUser(self) -> str:
        """! Check the role of the user
        @param user The User object
        @return A string
        """
        if isinstance(self.currentUser, Guest):
            return "guest"
        elif isinstance(self.currentUser, Customer):
            return "customer"
        elif isinstance(self.currentUser, Staff):
            return "staff"
        elif isinstance(self.currentUser, Admin):
            return "admin"

    def logout(self) -> bool:
        """! Log out of the system
        """
        # log out the user if possible
        flag = False
        classList = [Customer, Staff, Admin]
        for cls in classList:
            if isinstance(self.currentUser, cls):
                flag = self.currentUser.logout()
        if flag:
            # set the current user as a guest 
            self.currentUser = self.guest
        return flag

    def findBooking(self, id: str) -> Booking:
        """! Search for a particular booking
        @param mv The Movie Object
        @param mv The Screening Object
        @return A Booking object
        """
        for book in self.bookingList:
            if book.bookingId == id:
                booking = book
        return booking

    def findMovie(self, mvName: str) -> Movie:
        """! Search for a particular movie based on the name
        @param mvName The movie's name
        @return A Movie object
        """
        for movie in self.movieList:
            if movie.movieTitle.lower() == mvName.lower():
                return movie
            
    def getMovieDetails(self, mv: Movie) -> str:
        """! Get details of a movie
        @param mv The Movie Object
        @return A string
        """
        return self.currentUser.viewMovieDetails(mv)
    
    def getScreeningDetails(self, scn: Screening) -> str:
        """! Get details of a screening
        @param scn The Screening Object
        @return A string
        """
        return self.currentUser.viewScreeningDetails(scn)

    def validateSearch(self, search: str, type: str) -> bool:
        """! Validate input from the search
        @param search The text input of the search
        @param type The type of search
        """
        # Check search has inputs
        if search == "":
            return "Input field cannot be empty"
        # if the search input is text-related
        if type != "release date":
            search = search.lower()
            if not re.match(r'^[a-zA-Z0-9\s-]+$', search):
                return "Plase enter alphabet, number and space only"
        return True

    def searchMovie(self, search: str, type: str) -> Movie:
        """! Search for a particular movie
        @param search The text input of the search
        @param type The type of search
        """
        returnList = []
        if type != 'release date':
            search = search.lower()
        # return a list of movies that match the requirement
        if type == 'title':
            returnList = self.currentUser.searchMovieTitle(search,self.movieList)
        elif type == 'language':
            returnList = self.currentUser.searchMovieLang(search,self.movieList)
        elif type == 'genre':
            returnList = self.currentUser.searchMovieGenre(search,self.movieList)
        elif type == 'release date':
            returnList = self.currentUser.searchMovieDate(search,self.movieList)
        return returnList

    def findScreening(self, scnName: str) -> Screening:
        """! Search for a particular screening
        @param scnName The screening's name
        @return A Screening object
        """
        for screening in self.screeningList:
            if scnName == str(screening):
                return screening
            
    def checkScreeningSeats(self, screen: Screening) -> List[Seat]:
        """! Search for available seats in a screening
        @param screen The Screening Object
        @return A list of Seat objects
        """
        # return False if self.currentUser is guest
        if self.checkUser() == "guest":
            return False
        # get every seat in the screening 
        allSeats = []
        for seat in screen.screenHall.seatList:
            allSeats.append(seat)
        # remove the seat which is already booked for the screening
        for booked in screen.bookedSeats:
            for seat in allSeats:
                if str(booked) == str(seat):
                    allSeats.remove(seat)
        # return all available seats
        return allSeats
    
    def checkCartSeats(self, cus = None) -> bool:
        """! Check if the seats in the shopping cart are still bookable
        @param cus The customer ID and name (overloading)
        @return A boolean
        """
        # return a Customer object
        user = self.returnCustomer(cus)
        screen = user.customerCart.screening
        # return error if the seat is one of the booked seats of the screening
        if screen:
            for seat in user.customerCart.seatList:
                if screen.bookedSeats:
                    for bookedSeat in screen.bookedSeats:
                        if bookedSeat == seat:
                            return "The seat(s) in your cart has already been booked. Please re-select the screening chosen and check available seats again"
        else:
            return "Please select a movie and screening first."
        return True

    def findHall(self, name: str) -> Hall:
        """! Search for a particular Hall
        @param name The hall's name
        @return A Hall object
        """
        for hall in self.hallList:
            if name == str(hall):
                return hall
        return None

    def findSeat(self, seatName: str) -> Seat:
        """! Search for a particular seat
        @param seatName The seat's name
        @return A Seat object
        """
        for seat in self.seatList:
            if seatName == seat.seatName:
                return seat
        return None


    def displayScreening(self, movie: Movie) -> List[Screening]:
        """! Display all available screenings of a movie
        @param movie The Movie object
        @return A list of screenings
        """
        pass

    def displaySeat(self, screening: Screening) -> List[Seat]:
        """! Display all available seats for a screening
        @param screening The Screening Object 
        @return A list of seats
        """
        pass

    def cartDisplaySeat(self, cus = None) -> tuple:
        """! Display every seat in the shopping cart
        @return A tuple 
        """
        # return a Customer object
        user = self.returnCustomer(cus)
        # assign variables
        price = 0
        movie = None
        # get screening, seatlist and total price
        screening = user.viewCart()[0]
        seatlist = user.viewCart()[1]
        price = user.viewCart()[2]
        # get movie name
        for mv in self.movieList:
            if screening in mv.movieScreeningList:
                movie = mv
        return (movie, screening, seatlist, price)
    
    def cartAddSeat(self, seat: Seat, screen: Screening, cus = None) -> tuple:
        """! Add a seat to the shopping cart
        @param seat The Seat object
        @param screen The Screening object
        @param cus The customer ID and name (overloading)
        @return A boolean to indicate whether the seat is added successfully 
        """
        # return a Customer object
        user = self.returnCustomer(cus)
        # add seat of a particular screening to the shopping cart
        user.addCartItem(screen, seat)
        # get a tuple of details
        aTuple = self.cartDisplaySeat(user)
        # return movie, screening and list of seats in a tuple
        return aTuple
    
    def cartCheckSeat(self, seatName: Seat, cus = None) -> bool:
        """! Check whether a seat already exists in the shopping cart
        @param seat The Seat object
        @param cus The customer ID and name (overloading)
        @return A boolean
        """
        # return a Customer object
        user = self.returnCustomer(cus)
        for seat in user.customerCart.seatList:
            if seat == seatName:
                return True
        return False
    
    def clearCart(self, cus = None) -> str:
        """! Clear the shopping cart
        @param cus The customer ID and name (overloading)
        @return A string
        """
        # return a Customer object
        user = self.returnCustomer(cus)
        # clear the shopping cart
        user.emptyCart()
        return 'The shopping cart has been cleared'

    def cartDeleteSeat(self, seatName: str, cus = None) -> tuple:
        """! Add a seat to the shopping cart
        @param seat The seat's name
        @param cus The customer ID and name (overloading)
        @return A tuple 
        """
        # return a Customer object
        user = self.returnCustomer(cus)
        # remove the seat in the shopping cart
        for seat in user.customerCart.seatList:
            if seatName == seat.seatName:
                # remove the seat from the cart
                user.deleteCartItem(seat)
        # get a tuple of details
        aTuple = self.cartDisplaySeat(user)
        # return movie, screening and list of seats in a tuple
        return aTuple


    def cartAddCoupon(self, code: str, cus = None) -> str:
        """! Add a coupon to the shopping cart
        @param code The coupon code
        @param cus The customer ID and name (overloading)
        @return A boolean to indicate whether the coupon is added successfully
        """
        # return a Customer object
        user = self.returnCustomer(cus)
        # validate coupon
        if code == '':
            return "Cannot apply discount without code"
        for coupon in self.couponList:
            if coupon.couponCode == code:
                # add coupon to the shopping
                user.customerCart.coupon = coupon
                return coupon.discountRate
        return "Invalid coupon code"
    
    def calculateTotal(self, cus = None) -> float:
        """! Calculate total price of the seats in the shopping cart
        @param cus The customer ID and name (overloading)
        return A float
        """
        # return a Customer object
        user = self.returnCustomer(cus)
        return user.customerCart.calcTotal()
    
    def validateCard(self,cardNum: str,cardName: str,month: str = None,year: str = None) -> bool:
        """! Validate inputs for credit card payment
        @param cardNum The credit card number
        @param cardName The name on credit card
        @param month The month
        @param year The year
        return A boolean
        """
        # make sure inputs are not empty
        if cardNum == '' or cardName == '':
            return 'Input field(s) cannot be empty'
        # validate credit card number
        if not re.match(r'^\d+$', cardNum):
            return "Credit card number should contain numbers only"
        elif len(cardNum.strip()) < 8 or len(cardNum.strip()) > 19:
            return "Credit Card number should contain 8 to 19 numbers"
        # validate name on card
        if not re.match(r'^[a-zA-Z\s-]+$', cardName):
            return "Name should contain alphabets and whitespace only"
        # validate expiry date (if any)
        if month and year:
            expiryDate = date(int('20' + year), month, 1)
            if expiryDate <= currentDate:
                return "Expiry date cannot be in the present or in the past"
        return True

    def makePayment(self, option: str, cus: str = None, cardNum: str = None, cardName: str = None, banktype: str = None,  month: int = None,year: int = None) -> Payment:
        """! Make a payment for the tickets
        @param option The payment's option
        @param cus The customer ID and name (overloading)
        @param amount The payment's amount
        @param cardNum The payment's card number
        @param cardName The payment's name on card
        @param banktype The payment's bank or card type
        @param month The payment's month
        @param year The payment's year
        @return A boolean to indicate whether the payment is successful
        """
        # return a Customer object
        user = self.returnCustomer(cus)
        amount = user.customerCart.calcTotal()
        if month and year:
            expiryDate = date(int('20' + str(year)), month, 1)
        else:
            expiryDate = None
        # make payment
        aPayment = user.makePayment(option, amount, currentDate, cardNum, cardName, banktype, expiryDate)
        # append new payment
        self.paymentList.append(aPayment)
        return aPayment
    
    def createTickets(self, cus: Customer) -> None:
        """! Create tickets based on the items in the shopping cart"""
        tempList = []
        for seat in cus.customerCart.seatList:
            aTicket = Ticket(cus.customerCart.screening, seat)
            tempList.append(aTicket)
            self.ticketList.append(aTicket)
        return tempList

    def createBooking(self, pay: Payment, cus: str = None) -> str:
        """! Create a booking
        @param pay A Payment object
        @param cus The customer ID and name (overloading)
        @return A boolean to indivate whether the booking is created successfully
        """
        # return a Customer object
        user = self.returnCustomer(cus)
        bkSeats = self.createTickets(user)
        payment = pay
        screen = user.customerCart.screening
        movie = ''
        # get movie name
        for mv in self.movieList:
            if screen in mv.movieScreeningList:
                movie = mv
        coupon = user.customerCart.coupon
        # create a booking and add to the Customer's booking list (self.currentUser.addBooking can be Customer or Staff method, depends on the self.currentUser)
        aBooking = self.currentUser.addBooking(currentDate,bkSeats,payment,movie,screen,coupon,user)
        # clear the shopping cart
        user.emptyCart()
        user.customerCart.coupon = None
        user.customerCart.screening = None
        # display information of the booking
        msg = "Booking made Successful\n\n"
        msg += user.viewBooking(aBooking)
        self.bookingList.append(aBooking)
        # generate a notification
        note = self.createNotification(msg, None)
        return (note, aBooking)
    
    def displayBookings(self, cus = None) -> List[Booking]:
        """! Check the bookings of the currentUser
        @return A list of Booking objects
        """
        # return a Customer object
        user = self.returnCustomer(cus)
        return user.bookingList

    def displayBooking(self, book: Booking, cus: str = None) -> str:
        """! Display information of a particular booking
        @param book The Booking object
        @param cus The customer ID and name (overloading)
        @return A string
        """
        # return a Customer object
        user = self.returnCustomer(cus)
        info = user.viewBooking(book)
        return info

    def deleteBooking(self, book: Booking, cus = None, status: str = None) -> bool:
        """! Delete a booking
        @param book A Booking object
        @param cus The customer ID and name (overloading)
        @param status The status of delete (overloading)
        @return A boolean to indicate whether the booking is deleted successfully
        """
        # return a Customer object
        user = self.returnCustomer(cus)
        if self.checkUser() == "admin":
            operator = cus
        else:
            operator = self.currentUser
        # delete the booking from the customer's booking list (self.currentUser.deletebooking can be Customer or Staff method, depends on the self.currentUser)
        msg, aPayment = operator.deleteBooking(book,currentDate,user)
        # get booked tickets from the booking
        seats = []
        for ticket in book.bookingTickets:
            seats.append(ticket.ticketSeat)
        # delete booked tickets from the screening
        book.bookingScreening.deleteTickets(seats)
        bookings = user.bookingList
        # add the refund record to the payment list
        self.paymentList.append(aPayment)
        # generate a notification
        note = self.createNotification(msg, None)
        return (note, bookings, status)
    
    def createMovie(self, mvName: str, mvLanguage: str, mvGenre: str, releaseDate: str) -> str:
        """! Create a movie
        @param mvName The movie's name
        @param mvLanguage The movie's language
        @param mvGenre The movie's genre
        @param releaseDate The movie's release date
        @return A boolean to indicate whether the movie is created successfully
        """
        # validate inputs
        # convert the date format
        releaseDate = datetime.strptime(releaseDate, "%m/%d/%y")
        releaseDate = releaseDate.strftime("%d/%m/%Y")
        releaseDate = datetime.strptime(releaseDate, "%d/%m/%Y").date()
        if mvName == '' or mvLanguage == '' or mvGenre == '':
            return "Input field(s) cannot be empty"  
        elif not re.match(r"[\w\d\s&':,-]+", mvName):
            return "Invalid movie name"
        elif not re.match(r"[\w\d\s&':,-]+", mvLanguage):
            return "Invalid movie language"
        elif not re.match(r"[\w\s-]+", mvGenre):
            return "Invalid movie genre"
        elif self.findMovie(mvName):
            return "Movie name must be unique"
        aMovie = self.currentUser.addMovie(mvName.capitalize(),mvLanguage,mvGenre,releaseDate)
        # send a notification to every customer (existing movies, which are created from txt files, are not notified to the customers)
        note = "New movie " + aMovie.movieTitle + " is available for booking!"
        self.createNotification(note,'add movie')
        self.movieList.append(aMovie)
        return aMovie

    def deleteMovie(self, movie: Movie) -> bool:
        """! Delete a movie
        @param movie A Movie object
        @return A boolean to indicate whether the movie is deleted successfully
        """
        # delete every booking associated to the movie, and provide refund to them
        for book in self.bookingList:
            for customer in self.customerList:
                if book.bookingMovie == movie and book in customer.bookingList:
                    aTuple = self.deleteBooking(book, customer, "admindeletemovie")
                    self.createNotification(aTuple[0], aTuple[2], customer)
        # remove from the movie list
        if self.currentUser.deleteMovie(movie):
            self.movieList.remove(movie)
            return True
        return False

    def createScreening(self, scnMovie: str, scnDate: str, scnHall: str, scnTime: str, endTime: str) -> bool:
        """! Create a screening
        @param scnMovie The screening's movie title
        @param scnDate The screening's date
        @param scnTime The screening's start time
        @param endTime The screening's end time
        @param scnHall A Hall object
        @return A boolean to indicate whether the screening is created successfully
        """
        # validate inputs
        if scnMovie == "(select a movie)":
            return "Please select a movie before submitting"
        elif scnHall == "(select a hall)":
            return "Please select a hall before submitting"
        elif int(scnTime[:-3]) < 10 or int(scnTime[:-3]) > 23:
            return "Invalid start time. Please make sure the screening start time is not earlier than 10:00am"
        elif int(endTime[:-3]) > 23:
            return "Invalid end time. Please make sure the end time entered is valid"
        elif int(scnTime[-2:]) % 10 != 0 or int(endTime[-2:]) % 10 != 0:
            return "Please make sure the minutes part of the start time and end time is divisble by 10 (e.g. 10:30, 14:20)"
        # create an identical hall object for the particular screening
        hallSample = self.findHall(scnHall)
        hall = self.createHall(hallSample.hallName,hallSample.hallCapacity)
        self.hallList.append(hall)
        # find a movie and hall object
        movie = self.findMovie(scnMovie)
        # convert formats
        scnDate = datetime.strptime(scnDate, "%m/%d/%y")
        scnDate = scnDate.strftime("%d/%m/%Y")
        scnDate = datetime.strptime(scnDate, "%d/%m/%Y").date()
        scnTime = datetime.strptime(scnTime, "%H:%M").time()
        endTime = datetime.strptime(endTime, "%H:%M").time()
        # ensure that the screening date must be on or later than the release date
        if scnDate < movie.movieReleaseDate:
            return "Invalid screening date. Please make sure the date entered is not earlier than the release date"
        # ensure the end time is always later than start time (an assumption is made that a movie will not run towards next day)
        if endTime < scnTime:
            return "Please make sure the end time is later than start time"
        startTimeMinutes = scnTime.hour * 60 + scnTime.minute
        endTimeMinutes = endTime.hour * 60 + endTime.minute
        difference = endTimeMinutes - startTimeMinutes
        # ensure the movie is at least 40 minutes long
        if difference < 40:
            return "Movie length is too short. Please make sure the difference between start time and end time is 40 minutes long."
        # validate the screening has no conflict with other screenings
        for scn in movie.movieScreeningList:
            if str(scn.screenHall) == scnHall and scn.screenDate == scnDate:
                end_time_minutes = scn.endTime.hour * 60 + scn.endTime.minute
                difference = startTimeMinutes - end_time_minutes
                if scn.screenTime <= scnTime and scn.endTime >= scnTime:
                    return "Conflict with existing screening found. Please consider changing hall or start time or end time"
                elif scn.screenTime <= endTime and scn.endTime >= endTime:
                    return "Conflict with existing screening found. Please consider changing hall or start time or end time"
                elif difference < 60:
                    return "Please make sure there is at least 1 hour gap between screenings for cleaning purposes"
        aScreening = self.currentUser.addScreening(scnDate,scnTime,endTime,hall)
        # append the screening to the respective movie's screening list
        movie.addScreening(aScreening)
        self.screeningList.append(aScreening)
        return True

    def deleteScreening(self, screen: Screening) -> bool:
        """! Delete a screening
        @param screen A Screening Object
        @return A boolean to indicate whether the screening is deleted successfully
        """
        movie = ''
        # find the movie associated to the screening
        for mv in self.movieList:
            for scn in mv.movieScreeningList:
                if scn == screen:
                    movie = mv
        # delete every booking associated to the screening, and provide refund to them
        for book in self.bookingList:
            for customer in self.customerList:
                if book.bookingScreening == screen and book in customer.bookingList:
                    aTuple = self.deleteBooking(book, customer, "admindeletescreening")
                    self.createNotification(aTuple[0], aTuple[2], customer)
        # delete the screening
        if self.currentUser.deleteScreening(screen, movie):
            self.screeningList.remove(screen)
            return True
        return False

    def createNotification(self, note: str, type: str, cus: Customer = None) -> str:
        """! Send a notification
        @param note An existing msg content
        @param type Status which helps identifying what kind of notification should be created
        @param cus A Customer object (overloading)
        @return A string which will be displayed in the view page
        """
        # add extra words in certain situations
        if type == "admindeletescreening":
            note = "Due to cancellation of the screening,\n" + str(note)
        if type == "admindeletemovie":
            note = "Due to cancellation of the movie,\n" + str(note)
        # generate notification
        aNotification = Notification(note,currentDate)
        # store the notification in a customer's notification list (only if is related to admin) and system's notification list
        if type:
            if cus:
                cus.notificationList.append(aNotification)
            else:
                for cus in self.customerList:
                    cus.notificationList.append(aNotification)
        self.notificationList.append(aNotification)
        return aNotification

    def displayNotification(self) -> str:
        """! Display a notification
        @return A string which will be displayed in the view page
        """
        # store every unseen notification in a list
        displayList = self.currentUser.notificationList
        # clear the notification list of the currentUser
        self.currentUser.notificationList = []
        return displayList