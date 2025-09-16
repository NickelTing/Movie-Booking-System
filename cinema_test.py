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
from CinemaCon import Cinema

cinema = Cinema()

##### Login #####
aUser = User("Nicholas Ting", "nickyting222@gmail.com", "nickyting", "nicky777")
# return True to indicate the login is successful
def test_login():
    assert aUser.login("nickyting", "nicky777") == True
# return False to indicate the inputs are invalid
def test_login_with_uppercase_inputs():
    assert aUser.login("nickyting", "Nicky777") == False
    assert aUser.login("Nickyting", "nicky777") == False

##### Register #####
# return error message to indicate the name contains numbers and symbols
def test_register_on_name():
    inputList[0] = "n!ck ting"
    assert cinema.validateRegister(inputList) ==  'Name should contain alphabets and whitespace only'
    inputList[0] = "n1ck ting"
    assert cinema.validateRegister(inputList) ==  'Name should contain alphabets and whitespace only'
    inputList[0] = "Nicholas Ting"
# return error message to indicate the phone number contains alphabets or symbols or whitespace, or is too short or too long
def test_register_on_phone():
    inputList[1] = "abc 12345678"
    assert cinema.validateRegister(inputList) ==  "Phone number should contain numbers only"
    inputList[1] = "1234"
    assert cinema.validateRegister(inputList) ==  "Phone number should contain 7 to 12 numbers only"
    inputList[1] = "12345678901234"
    assert cinema.validateRegister(inputList) ==  "Phone number should contain 7 to 12 numbers only"
    inputList[1] = "021526533"
# return error message to indicate the home address contains special symbols
def test_register_on_address():
    inputList[2] = "123 h@me street"
    assert cinema.validateRegister(inputList) ==  "Home address should contain alphabets, numbers and whitespace only"
    inputList[2] = "211 Wainoni Road"
# return error message to indicate the email address format is invalid
def test_register_on_email():
    inputList[3] = "nick123email.com"
    assert cinema.validateRegister(inputList) ==  "Please enter a valid email address (eg. nick123@email.com)"
    inputList[3] = "nickyting222@gmail.com"
# return error message to indicate the username contains whitespace and special symbols
def test_register_on_username():
    inputList[4] = "nick!23"
    assert cinema.validateRegister(inputList) ==  "Username should contain alphabet and numbers only (no whitespace)"
    inputList[4] = "nick 123"
    assert cinema.validateRegister(inputList) ==  "Username should contain alphabet and numbers only (no whitespace)"
    inputList[4] = "nickyting"
# return error message to indicate the password is too short, or the new password and the confirm password do not match
def test_register_on_password():
    inputList[5] = "1234"
    assert cinema.validateRegister(inputList) ==  "Password should contain at least 8 characters (no whitespace)"
    inputList[6] = "1234"
    assert cinema.validateRegister(inputList) ==  "Password should contain at least 8 characters (no whitespace)"
    inputList[5] = "nicky777"
    inputList[6] = "12345678"
    assert cinema.validateRegister(inputList) ==  "New password should the same as confirm password"
    inputList[6] = "nicky777"
# return error message to indicate the name, phone number, email address and username must be unique
def test_register_unique():
    assert cinema.validateRegister(inputList) ==  "The name has been registered" # error message is still displayed despite that the name is lowercased
    inputList[0] = "Nicky Ting"
    assert cinema.validateRegister(inputList) ==  "The phone number has been registered" # phone number is the same as aCustomer
    inputList[1] = "021526333"
    assert cinema.validateRegister(inputList) ==  "The email address has been registered" # email address is the same as aCustomer
    inputList[3] = "nick123@email.com"
    assert cinema.validateRegister(inputList) ==  "The username has been registered" # username is the same as aCustomer
    inputList[4] = "nick123"
    assert cinema.validateRegister(inputList) ==  True # returns True, means the registration is successful

##### Guests ######
def test_guests():
    # Guests navigate to the online movie ticket booking system.
    assert isinstance(cinema.currentUser, Guest) == True # This means the default user is always guest before login, and therefore able to access the system
    # Guests browse/search movies based on title, language, genre, and release date. (for example, guest search by movie title)
    assert cinema.currentUser.searchMovieTitle(search,cinema.movieList) == [aMovie] # the model method which returns a list of movies that matches the result
    assert cinema.searchMovie(search, type) == [aMovie] # the controller method which returns the list of movies
    # Guests view selected movie.
    assert cinema.currentUser.viewMovieDetails(aMovie) == details # the model method which return details of the movie
    assert cinema.getMovieDetails(aMovie) == details # the controller method which return details of the movie
    # To book a movie, guests must register as a new member
    assert cinema.checkScreeningSeats(aScreening) == False # False means that the guest is unable to check the seats for the screening. Encourages the guest to login or register

##### Customer booking movie tickets #####
def test_customer_booking():
    # Customers navigate to the online movie ticket booking system.
    assert isinstance(cinema.currentUser, Guest) == True # True means the default user is always guest before login, and therefore able to access the system
    # Customers log in to the system.
    assert aCustomer.login(uname,pw) == True # True means that the login is successful
    cinema.currentUser = aCustomer
    # Customers browse/search movies based on title, language, genre, and release date.
    assert cinema.currentUser.searchMovieTitle(search,cinema.movieList) == [aMovie] # the model method which returns a list of movies that matches the result
    assert cinema.searchMovie(search, type) == [aMovie] # the controller method which returns the list of movies
    # Customers view selected movie.
    assert cinema.currentUser.viewMovieDetails(aMovie) == details # the model method which return details of the movie
    assert cinema.getMovieDetails(aMovie) == details # the controller method which return details of the movie
    # Customers view the selected movie schedules.
    assert aMovie.movieScreeningList == [aScreening] # the view needs to get the list of screening of the movie object
    # Customers select the date and time for the selected movie screening.
    assert str(aScreening) == aScreening.screenDate.strftime("%d/%m/%Y") + "," + aScreening.screenTime.strftime("%H:%M") + "-" + aScreening.endTime.strftime("%H:%M") + "," + str(aScreening.screenHall) 
        # the string form of the Screening object shows the screen date, screen time, end time and hall for the screening, so that the customer can choose a screening based on date and time
    # Customers select one or more available seats, according to their preferred seat location.
    for i in range(0,len(seatObjs)-1):
        cinema.cartAddSeat(seatObjs[i],aScreening)
    assert cinema.cartAddSeat(seatObjs[-1],aScreening) == (aMovie, aScreening, seatObjs, aCustomer.customerCart.calcTotal()) 
    cinema.currentUser.customerCart.screening = aScreening
    cinema.currentUser.customerCart.seatList = seatObjs
    cinema.currentUser.customerCart.coupon = aCoupon
        # return the movie, screening, seats and total price of the shopping cart if seat is added successfully
    # Customers add discount coupon if any
    assert cinema.cartAddCoupon('discount10') == 10 # return integer 10 to show the coupon is applied successfully
    # Customers pay for the movie tickets using cash, credit card or debit card (pay by credit card in this example)
    aPayment = cinema.makePayment('Credit Card', aCustomer, '1234123412341234','N C TING','Visa', 11, 24)
    assert isinstance(aCustomer.makePayment('Credit Card',30.00,'1234123412341234','N C TING','Visa',date(2024, 11, 1)), Payment) == True
    assert isinstance(aPayment, Payment) == True
        # a Payment object is created o show the payment is made successfully.
    tickets = cinema.createTickets(cinema.currentUser)
    # Customers make a booking
    aBooking = cinema.currentUser.addBooking(currentDate,tickets,aPayment,aMovie,aScreening,aCoupon)
    assert isinstance(aBooking, Booking) == True
    assert isinstance(cinema.createBooking(aPayment)[1], Booking) == True
        # a Booking object is created to show the booking is made successfully.
    # Customers get a notification of the booking.
    assert isinstance(cinema.createBooking(aPayment)[0], Notification) == True
        # a Notification object is created to show the booking is made successfully.

##### customer cancel movie tickets #####
def test_customer_cancelling():
    cinema.currentUser = aGuest
    # Customers navigate to the online movie ticket booking system.
    assert isinstance(cinema.currentUser, Guest) == True # This means the default user is always guest before login, and therefore able to access the system
    # Customers log in to the system.
    assert aCustomer.login(uname,pw) == True # True means that the login is successful
    cinema.currentUser = aCustomer
    cinema.currentUser.customerCart.screening = aScreening
    cinema.currentUser.customerCart.seatList = seatObjs
    cinema.currentUser.customerCart.coupon = aCoupon
    aPayment = cinema.makePayment('Credit Card', aCustomer, '1234123412341234','N C TING','Visa', 11, 24)
    tickets = cinema.createTickets(cinema.currentUser)
    aBooking = cinema.currentUser.addBooking(currentDate,tickets,aPayment,aMovie,aScreening,aCoupon)
    # Customers click on the booking tab.
    # Customers click on the selected booking to cancel.
    assert isinstance(cinema.currentUser.deleteBooking(aBooking,currentDate)[1], Payment) == True
    aBooking = cinema.currentUser.addBooking(currentDate,tickets,aPayment,aMovie,aScreening,aCoupon)
    assert cinema.currentUser.deleteBooking(aBooking,currentDate)[1].paymentAmt < 0 
        # a Payment (with negative amount) is created to indicate that the booking is cancelled and the payment is refunded
    aBooking = cinema.currentUser.addBooking(currentDate,tickets,aPayment,aMovie,aScreening,aCoupon)
        # return the movie, screening, seats and total price of the shopping cart if seat is added successfully
    # Customers get a notification of the cancellation
    assert isinstance(cinema.deleteBooking(aBooking)[0], Notification) == True
        # a Notification object is created to show the booking is made successfully.

##### staff book movie tickets #####
def test_staff_booking():
    cinema.currentUser = aGuest
    # Staff member navigates to the online movie ticket booking system.
    assert isinstance(cinema.currentUser, Guest) == True # This means the default user is always guest before login, and therefore able to access the system
    # Staff member logs in to the system.
    uname = 'jennywong'
    pw = 'jenny524'
    assert aStaff.login(uname,pw) == True # True means that the login is successful
    cinema.currentUser = aStaff
    # Staff member selects the movie screening.
    assert str(aScreening) == aScreening.screenDate.strftime("%d/%m/%Y") + "," + aScreening.screenTime.strftime("%H:%M") + "-" + aScreening.endTime.strftime("%H:%M") + "," + str(aScreening.screenHall) 
        # the string form of the Screening object shows the screen date, screen time, end time and hall for the screening, so that the customer can choose a screening based on date and time
    # Staff member selects one or more available seats, according to the customer’s preferred seat location.
    for i in range(0,len(seatObjs)-1):
        cinema.cartAddSeat(seatObjs[i],aScreening, aCustomer)
    assert cinema.cartAddSeat(seatObjs[-1],aScreening, aCustomer) == (aMovie, aScreening, seatObjs, aCustomer.customerCart.calcTotal()) 
    # Staff member adds discount coupon if any.
    assert cinema.cartAddCoupon('discount10', aCustomer) == 10 # return integer 10 to show the coupon is applied successfully
    # Staff member receives payment from the customer in cash, credit card, or debit card.
    assert isinstance(aCustomer.makePayment('Credit Card',30.00,'1234123412341234','N C TING','Visa',date(2024, 11, 1)), Payment) == True
    aPayment = cinema.makePayment('Credit Card', aCustomer, '1234123412341234','N C TING','Visa', 11, 24)
    assert isinstance(aPayment, Payment) == True
        # a Payment object is created o show the payment is made successfully.
    # Staff member makes a booking
    aCustomer.customerCart.screening = aScreening
    aCustomer.customerCart.seatList = seatObjs
    aCustomer.customerCart.coupon = aCoupon
    tickets = cinema.createTickets(aCustomer)
    aBooking = cinema.currentUser.addBooking(currentDate,tickets,aPayment,aMovie,aScreening,aCoupon, aCustomer) 
        # staff add booking on behalf of the customer
    assert isinstance(aBooking, Booking) == True
    assert isinstance(cinema.createBooking(aPayment,aCustomer)[1], Booking, ) == True
        # a Booking object is created to show the booking is made successfully.

##### staff cancel movie tickets #####
def test_staff_cancelling():
    cinema.currentUser = aGuest
    # Staff member navigates to the online movie ticket booking system.
    assert isinstance(cinema.currentUser, Guest) == True # This means the default user is always guest before login, and therefore able to access the system
    # Staff member logs in to the system.
    uname = 'jennywong'
    pw = 'jenny524'
    assert aStaff.login(uname,pw) == True # True means that the login is successful
    cinema.currentUser = aStaff
    aCustomer.customerCart.screening = aScreening
    aCustomer.customerCart.seatList = seatObjs
    aCustomer.customerCart.coupon = aCoupon
    aPayment = cinema.makePayment('Credit Card', aCustomer, '1234123412341234','N C TING','Visa', 11, 24)
    tickets = cinema.createTickets(aCustomer)
    aBooking = cinema.currentUser.addBooking(currentDate,tickets,aPayment,aMovie,aScreening,aCoupon,aCustomer)
    # Staff clicks on the booking tab.
    # Staff member selects booking to cancel.
    assert isinstance(cinema.currentUser.deleteBooking(aBooking,currentDate,aCustomer)[1], Payment) == True 
        # staff cancel the movie on behalf of the customer
    aBooking = cinema.currentUser.addBooking(currentDate,tickets,aPayment,aMovie,aScreening,aCoupon,aCustomer)
    assert cinema.currentUser.deleteBooking(aBooking,currentDate,aCustomer)[1].paymentAmt < 0 
        # a Payment (with negative amount) is created to indicate that the booking is cancelled and the payment is refunded
    # Staff member provides refund to the customer

##### admin add movie #####
def test_admin_adding_movie():
    cinema.currentUser = aGuest
    # Admin navigates to the online movie ticket booking system.
    assert isinstance(cinema.currentUser, Guest) == True # This means the default user is always guest before login, and therefore able to access the system
    # Admin logs in to the system.
    uname = 'alexting'
    pw = 'alex0614'
    assert aAdmin.login(uname,pw) == True # True means that the login is successful
    cinema.currentUser = aAdmin
    # Admin clicks on add new movie.
    # Admin enters the relevant details for the new movie.
    title = "A Silent Voice"
    language = "English"
    genre = "Romance"
    releaseDate = '10/11/23'
    # Admin confirms adding the new movie
    assert isinstance(cinema.currentUser.addMovie(title, language, genre, releaseDate), Movie) == True
    assert isinstance(cinema.createMovie(title, language, genre, releaseDate), Movie) ==  True
        # True means that a movie object is created successfully

##### admin cancel movie #####
    cinema.currentUser = aGuest
    # Admin navigates to the online movie ticket booking system.
    assert isinstance(cinema.currentUser, Guest) == True # This means the default user is always guest before login, and therefore able to access the system
    # Admin logs in to the system.
    uname = 'alexting'
    pw = 'alex0614'
    assert aAdmin.login(uname,pw) == True # True means that the login is successful
    cinema.currentUser = aAdmin
    # Admin clicks on cancel a movie.
    # Admin selects the movie to cancel.
    aMovie =  cinema.findMovie('Jujutsu Kaisen 0')
    aCustomer.customerCart.screening = aScreening
    aCustomer.customerCart.seatList = seatObjs
    aCustomer.customerCart.coupon = aCoupon
    aPayment = cinema.makePayment('Credit Card', aCustomer, '1234123412341234','N C TING','Visa', 11, 24)
    tickets = cinema.createTickets(aCustomer)
    aBooking = aCustomer.addBooking(currentDate,tickets,aPayment,aMovie,aScreening,aCoupon,aCustomer)
    # Admin confirms cancelling the selected movie (and issue refund to those who has made bookings with the movie)
    assert aAdmin.deleteMovie(aMovie) == True
    assert cinema.deleteMovie(aMovie) == True
    assert aCustomer.notificationList != []
        # True indicates that the movie has been removed from the movie list and will not be selected for booking.
        # Notification is also generated to the Customer's notification list that the booking for the movie is cancelled

##### admin add screening #####
    cinema.currentUser = aGuest
    # Admin navigates to the online movie ticket booking system.
    assert isinstance(cinema.currentUser, Guest) == True # This means the default user is always guest before login, and therefore able to access the system
    # Admin logs in to the system.
    uname = 'alexting'
    pw = 'alex0614'
    assert aAdmin.login(uname,pw) == True # True means that the login is successful
    cinema.currentUser = aAdmin
    # Admin selects a movie.
    scnMovie = str(aMovie)
    # Admin adds a screening to that movie.
    scnDate = '11/20/23'
    scnHall = 'Hall 1'
    scnTime = '10:00'
    endTime = '12:00'
    cinema.movieList = [aMovie]
    assert isinstance(cinema.currentUser.addScreening(date(2023, 11, 20), aHall, time(10, 0), time(12, 0)), Screening) == True
    assert cinema.createScreening(scnMovie, scnDate, scnHall, scnTime, endTime) == True
        # True indicates that a Screening object has been created. 
    # Admin confirms adding that screening.

##### admin cancel screening #####
    cinema.currentUser = aGuest
    # Admin navigates to the online movie ticket booking system.
    assert isinstance(cinema.currentUser, Guest) == True # This means the default user is always guest before login, and therefore able to access the system
    # Admin logs in to the system.
    uname = 'alexting'
    pw = 'alex0614'
    assert aAdmin.login(uname,pw) == True # True means that the login is successful
    cinema.currentUser = aAdmin
    # Admin selects a movie.
    scnMovie = str(aMovie)
    cinema.movieList = [aMovie]
    aMovie.movieScreeningList = [aScreening]
    # Admin selects the screening for that movie to cancel.
    aCustomer.customerCart.screening = aScreening
    aCustomer.customerCart.seatList = seatObjs
    aCustomer.customerCart.coupon = aCoupon
    aPayment = cinema.makePayment('Credit Card', aCustomer, '1234123412341234','N C TING','Visa', 11, 24)
    tickets = cinema.createTickets(aCustomer)
    aBooking = aCustomer.addBooking(currentDate,tickets,aPayment,aMovie,aScreening,aCoupon,aCustomer)
    # Admin confirms cancelling the selected screening for the selected movie and issues a refund to those customers who have booked the screening.
    assert aAdmin.deleteScreening(aScreening, aMovie) == True
        # True indicates the screening is deleted successfully
    assert aCustomer.notificationList != []
        # Notification is also generated to the Customer's notification list that the screening for the movie is cancelled and refund will be provided


# get the current date variable
currentDate = date.today()
# create a Guest object
aGuest = Guest('guest')
# registration inputs sample
name = "Nicholas Ting"
phone = "021526533"
home = "211 Wainoni Road"
email = "nickyting222@gmail.com"
uname = "nickyting"
pw = "nicky777"
confirmpw = "nicky777"
inputList = [name, phone, home, email, uname, pw, confirmpw]
# create a customer sample
aCustomer = cinema.createCustomer("Nicholas Ting","nickyting","nicky777","nickyting222@gmail.com","211 Wainoni Road","021526533")
# create a movie sample
aMovie = cinema.generateMovie('Jujutsu Kaisen 0','Japanese','Action','10/23/23')
# create a hall sample
aHall = cinema.createHall("Hall 1",120) 
# create a screening sample
aScreening = cinema.generateScreening('Jujutsu Kaisen 0','12/23/23','Hall 1','11:00','13:00')
# variables for searching a movie
search = "0"
type = "title"
# string variable that displays the movie details
details = "Movie ID: " + aMovie.movieId
details += "\nTitle: " + aMovie.movieTitle
details += "\nLanguage: " + aMovie.movieLanguage
details += "\nGenre: " + aMovie.movieGenre
details += "\nRelease Date: " + aMovie.movieReleaseDate.strftime('%d/%m/%Y')
details += "\nNo. of Screenings: " + str(len(aMovie.movieScreeningList))
# create seat variables
seatList = ['A1','A2','A3']
seatObjs = []
for seat in seatList:
    seatobj = cinema.findSeat(seat)
    seatObjs.append(seatobj)
# create a coupon sample
aCoupon = cinema.createCoupon('discount10',10)
# create a staff sample
aStaff = cinema.createStaff('Jenny Wong','jennywong','jenny524','jennywong@email.com')
# create an admin sample
aAdmin = cinema.createAdmin('Alex Ting','alexting','alex0614','alexting@email.com')