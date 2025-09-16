import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.messagebox import showinfo
from tkcalendar import DateEntry, Calendar
from CinemaCon import Cinema
from datetime import date, time, datetime, timedelta
from decimal import Decimal

# get cinema controller
cinema = Cinema()
# get today's date
current_date = date.today()
current_year = current_date.year % 100
# unpacking persons.txt
with open("persons.txt", "r") as f:
    info = f.readlines()
    for e in info:
        infoList = e.strip().split(",")
        if len(infoList) == 7:
            identity, name, phone, address, email, uname, pw = infoList
            cinema.createCustomer(name,uname,pw,email,address,phone)
        else:
            identity, name, email, uname, pw = infoList
            if identity == "staff":
                cinema.createStaff(name,uname,pw,email)
            else:
                cinema.createAdmin(name,uname,pw,email)
# unpacking movies.txt
with open("movies.txt", "r") as f:
    info = f.readlines()
    for e in info:
        title, language, genre, releaseDate = e.strip().split(",")
        cinema.generateMovie(title,language,genre,releaseDate)
# unpacking halls.txt
with open("halls.txt", "r") as f:
    info = f.readlines()
    for e in info:
        name, capacity = e.strip().split(",")
        cinema.createHall(name,int(capacity))
# unpacking screenings.txt
with open("screenings.txt", "r") as f:
    info = f.readlines()
    for e in info:
        title, screenDate, hallname, screenTime, endTime = e.strip().split(",")
        cinema.generateScreening(title,screenDate,hallname,screenTime,endTime)
# unpacking coupons.txt
with open("coupons.txt", "r") as f:
    info = f.readlines()
    for e in info:
        code, rate = e.strip().split(",")
        cinema.createCoupon(code,int(rate))

### Login Frame ###
class Login(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)

        # validate username and password before login
        def verify():
            response = cinema.login(T1.get(),T2.get())
            if type(response) is not str:
                messagebox.showinfo("Alert", "Login Successful")
                cinema.currentUser = response
                refreshHomePage()
            else:
                messagebox.showinfo("Error", response)

        border = tk.LabelFrame(self, text="Login")
        border.pack(fill="both", expand="yes", padx= 200, pady=150)

        L1 = tk.Label(border, text="Username: ")
        L1.place(x=50, y=21)
        T1 = tk.Entry(border, width=34, bd=5)
        T1.place(x=130, y=20)

        L2 = tk.Label(border, text="Password: ")
        L2.place(x=50, y=61)
        T2 = tk.Entry(border, width=34, show='*', bd=5)
        T2.place(x=130, y=60)
                
        B1 = tk.Button(border, text="Login", command=verify)
        B1.place(x=130, y=100)

        B2 = tk.Button(border, text="Register", command = lambda:controller.show_frame(Register))
        B2.place(x=180, y=100)

        B3 = tk.Button(border, text="Reset Password", command = lambda:controller.show_frame(Reset))
        B3.place(x=240, y=100)

        B4 = tk.Button(border, text="Home", command = lambda:controller.show_frame(HomePage))
        B4.place(x=130, y=130)

### Register Frame ###
class Register(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        # validate registration entries
        def Register():
            inputList = [T1.get(),T2.get(),T3.get(),T4.get(),T5.get(),T6.get(),T7.get()]
            response = cinema.validateRegister(inputList)
            # if the validation is successful
            if type(response) is bool:
                # register the guest as a customer
                cinema.register(inputList)
                # display a success message
                messagebox.showinfo("Alert", "You have been registered")
                # shows login frame
                controller.show_frame(Login)   
            else:
                messagebox.showinfo("Error", response)
        border = tk.LabelFrame(self, text="Register")
        border.pack(fill="both", expand="yes", padx= 200, pady=50)
        L1 = tk.Label(border, text="Given Name: ")
        L1.place(x=50, y=21)
        T1 = tk.Entry(border, width=30, bd=5)
        T1.place(x=160, y=20)
        L2 = tk.Label(border, text="Phone Number: ")
        L2.place(x=50, y=61)
        T2 = tk.Entry(border, width=30, bd=5)
        T2.place(x=160, y=60)
        L3 = tk.Label(border, text="Home Address: ")
        L3.place(x=50, y=101)
        T3 = tk.Entry(border, width=30, bd=5)
        T3.place(x=160, y=100)
        L4 = tk.Label(border, text="Email Address: ")
        L4.place(x=50, y=141)
        T4 = tk.Entry(border, width=30, bd=5)
        T4.place(x=160, y=140)
        L5 = tk.Label(border, text="Username: ")
        L5.place(x=50, y=181)
        T5 = tk.Entry(border, width=30, bd=5)
        T5.place(x=160, y=180)
        L6 = tk.Label(border, text="New Password: ")
        L6.place(x=50, y=221)
        T6 = tk.Entry(border, width=30, show='*', bd=5)
        T6.place(x=160, y=220)
        L7 = tk.Label(border, text="Confirm Password: ")
        L7.place(x=50, y=261)
        T7 = tk.Entry(border, width=30, show='*', bd=5)
        T7.place(x=160, y=260)     
        B1 = tk.Button(border, text="Register", command=Register)
        B1.place(x=160, y=310)
        B2 = tk.Button(border, text="Home", command = lambda:controller.show_frame(HomePage))
        B2.place(x=305, y=310)

### Reset Password Frame ###
class Reset(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        # validate registration entries
        def validateEntries():
            inputList = [T1.get(),T2.get(),T3.get()]
            response = cinema.validateReset(inputList)
            # if the validation is successful
            if type(response) is not str:
                # reset the password based on email address
                cinema.resetPassword(response, inputList[2])
                # display a success message
                messagebox.showinfo("Success", "Password have been reset")
                # clear the entries
                # shows login frame
                controller.show_frame(Login)
            else:
                messagebox.showinfo("Error", response)
        border = tk.LabelFrame(self, text="Reset Password")
        border.pack(fill="both", expand="yes", padx= 200, pady=150)
        L1 = tk.Label(border, text="Account's Email: ")
        L1.place(x=50, y=21)
        T1 = tk.Entry(border, width=30, bd=5)
        T1.place(x=160, y=20)
        L2 = tk.Label(border, text="New Password: ")
        L2.place(x=50, y=61)
        T2 = tk.Entry(border, width=30, show='*', bd=5)
        T2.place(x=160, y=60)
        L3 = tk.Label(border, text="Confirm Password: ")
        L3.place(x=50, y=101)
        T3 = tk.Entry(border, width=30, show='*', bd=5)
        T3.place(x=160, y=100)   
        B1 = tk.Button(border, text="Reset", command=validateEntries)
        B1.place(x=160, y=140)
        B2 = tk.Button(border, text="Back", command = lambda:controller.show_frame(Login))
        B2.place(x=310, y=140)

### Home Page Frame ###
class HomePage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        ### HomePage functions ### 
        # command for replacing entries while certain value is selected in the combobox
        def comboSelection(event):
            searchOption = combo.get()
            if searchOption == "release date":
                search_entry.place_forget()
                cal.place(x=50, y=15)
            else:
                cal.place_forget()
                search_entry.place(x=50, y=15)
        # command for searching a movie
        def searchMovie():
            # clear the list box
            searchList.delete(0, tk.END)
            # get the text entered
            searchOption = combo.get()
            if searchOption == "release date":
                searchInput = cal.get()
                # convert the date format
                searchInput = datetime.strptime(searchInput, "%m/%d/%y")
                searchInput = searchInput.strftime("%d/%m/%Y")
                searchInput = datetime.strptime(searchInput, "%d/%m/%Y").date()
            else:
                searchInput = search_entry.get()
            # validate the search inputs
            response = cinema.validateSearch(searchInput,searchOption)
            if type(response) is bool:
                # get movie
                for movie in sorted(cinema.searchMovie(searchInput, searchOption), key=lambda x: x.movieTitle):
                    searchList.insert(tk.END,movie)
            else:
                messagebox.showinfo("Error", response)
        # select a movie function 
        def selectMovie():
            # get selected movie
            movieIndex = searchList.curselection()
            # If a movie is chosen
            if movieIndex:
                return [searchList.get(idx) for idx in movieIndex][0]
            else:
                return False
        # command for displaying movie info
        def movieInfo():
            selection = selectMovie()
            if selection:
                selectedMovie = cinema.findMovie(selection)
                # get details of the movie object
                messagebox.showinfo("Information", cinema.getMovieDetails(selectedMovie))
        # command for displaying screenings
        def displayScreenings():
            screeningList.delete(0, tk.END)
            selection = selectMovie()
            if selection:
                selectedMovie = cinema.findMovie(selection)
                # get every screening in a movie
                for screening in sorted(selectedMovie.movieScreeningList, key=lambda x: x.screenDate):
                    screeningList.insert(tk.END,screening)
        # select a screening function 
        def selectScreening():
            # get selected screening
            screenIndex = screeningList.curselection()
            # If a screening is chosen
            if screenIndex:
                return [screeningList.get(idx) for idx in screenIndex][0]
            else:
                return False
        # command that get available seats of a certain row
        def checkAvailableRowSeat(event, row = None):
            # works only if the user selects something
            if selectScreening():
                # if a different screening is selected
                if row != None:
                    # shows row A seats first
                    rowType = "A"
                    rowCombo.set(rowType)
                else:
                    # get the value of rowCombo
                    rowType = rowCombo.get()
                # clear the list box
                seatListBox.delete(0, tk.END)
                # get a Screening object
                screenObject = cinema.findScreening(selectScreening())
                # get a list of available seats in a screening
                if cinema.checkScreeningSeats(screenObject):
                    seatList = cinema.checkScreeningSeats(screenObject)
                else:
                    messagebox.showinfo("Error", "Please login first before make a booking")
                    controller.show_frame(Login)
                    return
                # insert the seats which matches the rowCombo
                count = 0
                for seat in seatList:
                    if seat.seatName[0] == rowType:
                        seatListBox.insert(tk.END,seat.seatName)
                        count = 1
                if count == 0:
                    seatListBox.insert(tk.END,"(No available seat for this row)")
            else:
                messagebox.showinfo("Error", "Please select a screening before selecting a seat")
        # command that get available seats when switched to a new screening
        def checkAvailableSeat():
            if cartListBox.size() > 0:
                messagebox.showinfo("Error", "Please clear your shopping cart before switching to a new movie screening")
            else:
                checkAvailableRowSeat('A','A') 
        # select a seat function 
        def selectSeat():
            # get selected seat
            seatIndex = seatListBox.curselection()
            # If a screening is chosen
            if seatIndex:
                return [seatListBox.get(idx) for idx in seatIndex][0]
            else:
                return False
        # draw seating plan for the customer to view
        def drawSeatingPlan():
            draw_seating_plan()
        # command that clear cartListBox and reinsert values
        def fillCartBox(customer):
            cartListBox.delete(0, tk.END)
            aTuple = cinema.cartDisplaySeat(customer)
            for seat in sorted(aTuple[2], key=lambda x: x.seatId):
                text = str(aTuple[0]) + ',' + seat.seatName
                cartListBox.insert(tk.END,text)
            total_price = aTuple[3]
            total_label.config(text=total_price)
        # command that add seat to the shopping cart
        def addSeat():
            if selectSeat():
                # check the user's role
                customer = checkCustomer()
                if not customer:
                    return 
                # get the Seat object
                theSeat = cinema.findSeat(selectSeat())
                # get the Screening object
                theScreening = cinema.findScreening(selectScreening())
                # insert the screening and seat information to the shopping cart, and insert details into the listbox
                if cinema.cartCheckSeat(theSeat,customer):
                    messagebox.showinfo("Error", "Seat already added to the shopping cart")
                    cinema.cartDisplaySeat(customer)
                else:
                    cinema.cartAddSeat(theSeat,theScreening,customer)
                # reinsert the values
                fillCartBox(customer)
            else:
                messagebox.showinfo("Error", "Please select a seat before adding to the shopping cart")
        # command for selecting a cart item 
        def selectCart():
            # get selected seat
            cartIndex = cartListBox.curselection()
            # If a screening is chosen
            if cartIndex:
                return [cartListBox.get(idx) for idx in cartIndex][0]
            else:
                return False
        # command for clearing the shopping cart
        def clearSeat():
            # check the user's role
            customer = checkCustomer()
            if not customer:
                return
            # clear cart list box, remove total price and discount 
            cartListBox.delete(0, tk.END)
            total_label.config(text=Decimal('0.00'))
            messagebox.showinfo("Error",cinema.clearCart(customer))
        # command that delete seat from the shopping cart
        def deleteSeat():
            if selectCart():
                # check the user's role
                customer = checkCustomer()
                if not customer:
                    return 
                # select a cart item
                cartItem = selectCart()
                # delete the previous listbox records
                cartListBox.delete(0, tk.END)
                # get movie, screening and seat name
                movie, seat = cartItem.strip().split(",")
                # delete the cart item
                cinema.cartDeleteSeat(seat, customer)
                # reinsert the values
                fillCartBox(customer)
            else:
                messagebox.showinfo("Error", "Please select a seat before removing it from the shopping cart")
        # command for replacing entries while certain value is selected in the combobox
        def paymentSelection(event):
            # forget every widget
            bank.place_forget()
            bankCombo.place_forget()
            cardType.place_forget()
            cardTypeCombo.place_forget()
            expiryDate.place_forget()
            monthCombo.place_forget()
            dividelabel.place_forget()
            yearCombo.place_forget()
            cardNumber.place_forget()
            cardNumber_entry.place_forget()
            nameOnCard.place_forget()
            nameOnCard_entry.place_forget()
            bank.place_forget()
            bankCombo.place_forget()
            discountCode.place_forget()
            discountCode_entry.place_forget()
            bookButton.place_forget()
            # get value of the combobox
            paymentOption = payCombo.get()
            # insert necessary widgets based on the payment option
            if paymentOption != "Cash":
                cardNumber.place(x=5, y=41)
                cardNumber_entry.place(x=100, y=40)
                nameOnCard.place(x=5, y=71)
                nameOnCard_entry.place(x=100, y=70)
                if paymentOption == "Credit Card":
                    cardType.place(x=5, y=101)
                    cardTypeCombo.place(x=100, y=100)
                    expiryDate.place(x=5, y=131)
                    monthCombo.place(x=100, y=131)
                    dividelabel.place(x=141, y=131)
                    yearCombo.place(x=151, y=131)
                    discountCode.place(x=5, y=161)
                    discountCode_entry.place(x=100, y=160)
                    applyButton.place(x=5, y=190)
                    bookButton.place(x=100, y=190)
                else:
                    bank.place(x=5, y=101)
                    bankCombo.place(x=100, y=100)
                    discountCode.place(x=5, y=131)
                    discountCode_entry.place(x=100, y=130)
                    applyButton.place(x=5, y=160)
                    bookButton.place(x=100, y=160)
            # if user chooses cash
            else:
                discountCode.place(x=5, y=41)
                discountCode_entry.place(x=100, y=40)
                applyButton.place(x=5, y=70)
                bookButton.place(x=100, y=70)
        def applyCoupon():
            # check the user's role
            customer = checkCustomer()
            if not customer:
                return 
            codeInput = discountCode_entry.get()
            response = cinema.cartAddCoupon(codeInput,customer)
            if type(response) is not str: 
                total_price = cinema.calculateTotal(customer)
                total_label.config(text=total_price)
                msg =  '('+ str(response) + '% off)' 
                discount_label.config(text=msg)
                messagebox.showinfo("Alert", "Coupon Code applied successfully")
            else:
                messagebox.showinfo("Error", response)
        # command to make a payment and place a booking        
        def makePayment():
            # check the user's role
            customer = checkCustomer()
            if not customer:
                return 
            # make sure the cart combobox is not empty
            if cartListBox.size() != 0:
                result = cinema.checkCartSeats(customer)
                if type(result) is not str:
                    # get value of the combobox
                    paymentOption = payCombo.get() 
                    if paymentOption != 'Cash':
                        cardNumberInput = cardNumber_entry.get()
                        nameOnCardInput = nameOnCard_entry.get()
                        if paymentOption == "Credit Card":
                            cardTypeInput = cardTypeCombo.get()
                            monthInput = int(monthCombo.get())
                            yearInput = yearCombo.get()
                            # validate credit card inputs
                            response = cinema.validateCard(cardNumberInput,nameOnCardInput,monthInput,yearInput)
                            # if valid, make payment
                            if type(response) is bool:
                                payment = cinema.makePayment(paymentOption,customer,cardNumberInput,nameOnCardInput,cardTypeInput,monthInput,yearInput)
                            else:
                                messagebox.showinfo("Error", response)
                                return
                        else:
                            bankInput = bankCombo.get()
                            # validate debit card inputs
                            response = cinema.validateCard(cardNumberInput,nameOnCardInput)
                            # if valid, make payment
                            if type(response) is bool:
                                payment = cinema.makePayment(paymentOption,customer,cardNumberInput,nameOnCardInput,bankInput)
                            else:
                                messagebox.showinfo("Error", response)
                                return
                    else:
                        payment = cinema.makePayment(paymentOption,customer)
                else:
                    messagebox.showinfo("Error", result)
                    return
                aTuple = cinema.createBooking(payment,customer)
                messagebox.showinfo("Success", str(aTuple[0]))
                bookListBox.insert(tk.END,str(aTuple[1]))
                # clear seat list box and cart list box, remove total price and discount 
                cartListBox.delete(0, tk.END)
                seatListBox.delete(0, tk.END)
                total_label.config(text=Decimal('0.00'))
                discount_label.config(text='')
            else:
                messagebox.showinfo("Error", "Cannot make booking with no seat in the shopping cart.")
        # command for selecting a screening function 
        def selectBooking():
            # get selected screening
            bookingIndex = bookListBox.curselection()
            # If a screening is chosen
            if bookingIndex:
                return [bookListBox.get(idx) for idx in bookingIndex][0]
            else:
                return False
        # command for viewing a booking details
        def viewBooking():
            # check the user's role
            customer = checkCustomer()
            if not customer:
                return 
            if selectBooking():
                # select a booking item
                bookingItem = selectBooking()
                # get movie, screening and seat name
                id, movie, screening, times, hall  = bookingItem.strip().split(",")
                # find the booking object
                booking = cinema.findBooking(id)
                # return info string from the selected booking
                info = cinema.displayBooking(booking,customer)
                messagebox.showinfo("Info", info)
            else:
                messagebox.showinfo("Error", "Please select a booking first")
        # command for deleting a booking 
        def deleteBooking():
            # check the user's role
            customer = checkCustomer()
            if not customer:
                return 
            if selectBooking():
                confirm = messagebox.askyesno("Confirmation", "Are you sure to delete this booking?")
                if confirm:
                    # select a booking item
                    bookingItem = selectBooking()
                    # get movie, screening and seat name
                    id, movie, screening, times, hall = bookingItem.strip().split(",")
                    # find the booking object
                    booking = cinema.findBooking(id)
                    # refund the booking's payment and cancel the booking
                    aTuple = cinema.deleteBooking(booking,customer)
                    messagebox.showinfo("Info", str(aTuple[0]))
                    # delete the previous listbox records
                    bookListBox.delete(0, tk.END)
                    for booking in aTuple[1]:
                        bookListBox.insert(tk.END,booking)
                    seatListBox.delete(0, tk.END)
            else:
                messagebox.showinfo("Error", "Please select a booking first")
        # command that fills up the cart and booking list boxes when the staff selects a customer
        def fillListBox(event = None):
            # clear the list boxes
            discount_label.config(text='')
            cartListBox.delete(0, tk.END)
            bookListBox.delete(0, tk.END)
            # check the user's role
            customer = checkCustomer()
            if not customer:
                return 
            # reinsert the values
            fillCartBox(customer)
            for booking in cinema.displayBookings(customer):
                bookListBox.insert(tk.END,str(booking))
            # change the discount label if there is any active
            rate = cinema.returnCartCoupon(customer)
            if rate:
                msg =  '('+ str(rate) + '% off)' 
                discount_label.config(text=msg)
        # command that make sure the user is a customer object
        def checkCustomer():
            customer = None
            if cinema.checkUser() == 'staff':
                customer = customerCombo.get()
                # procced only if a customer is selected
                if customer == '(select a customer)':
                    messagebox.showinfo("Error", "Please select a customer in the top right corner first")
                    return None
            else:
                customer = cinema.currentUser
            return customer
        # function that fill movieListbox and screenListBox
        def fillMovieBox():
            # clear movie list box
            movieListBox.delete(0, tk.END)
            for movie in sorted(cinema.movieList, key=lambda x: x.movieTitle):
                # insert every movie, including the new ones
                movieListBox.insert(tk.END,str(movie))
        # command that adds a movie
        def addMovie():
            # get inputs
            title = movie_title_entry.get()
            lang = movie_lang_entry.get()
            genre = movie_gen_entry.get()
            redate = movie_redate_entry.get()
            # validate inputs and create a movie if successful
            confirm = messagebox.askyesno("Confirmation", "Are you sure to add this movie?")
            if confirm:
                response = cinema.createMovie(title,lang,genre,redate)
                fillMovieBox()
                if type(response) is not str:
                    movie_title_entry.delete(0, "end")
                    movie_lang_entry.delete(0, "end")
                    movie_gen_entry.delete(0, "end")
                    updateCombo()
                    messagebox.showinfo("Success", "New movie added successfully")
                else:
                    messagebox.showinfo("Error",response)
        # command that selects a movie
        def selectMv():
            # get selected movie
            movieIndex = movieListBox.curselection()
            # If a movie is chosen
            if movieIndex:
                return [movieListBox.get(idx) for idx in movieIndex][0]
            else:
                return False
        # command that views a movie information
        def viewMv():
            selection = selectMv()
            if selection:
                selectedMovie = cinema.findMovie(selection)
                # get details of the movie object
                messagebox.showinfo("Information", cinema.getMovieDetails(selectedMovie))
            else:
                messagebox.showinfo("Error","Please select a movie first")
        # command that deletes a movie 
        def deleteMv():
            selection = selectMv()
            if selection:
                confirm = messagebox.askyesno("Confirmation", "Are you sure to delete this movie?")
                if confirm:
                    response = cinema.deleteMovie(cinema.findMovie(selection))
                    if response:
                        fillMovieBox()
                        response = "Movie " + selection + " has been deleted"
                        # get details of the movie object
                        updateCombo()
                        messagebox.showinfo("Success",response)
                    else:
                        messagebox.showinfo("Error","Cannot delete this movie. Please make sure there is no booking for this movie first")
                else:
                    pass
            else:
                messagebox.showinfo("Error","Please select a movie first")
        # command that fills screening list box when a movie is selected
        def fillScreenBox(event = None):
            screenListBox.delete(0, tk.END)
            selection = movie_combo.get()
            if selection != "(select a movie)":
                selectedMovie = cinema.findMovie(selection)
                # get every screening in a movie
                for screening in sorted(selectedMovie.movieScreeningList, key=lambda x: x.screenDate):
                    screenListBox.insert(tk.END,screening)
        # command that add a screening
        def addScn():
            # get inputs and convert them to appropriate formats
            scnMovie = movie_combo.get()
            scnDate = screen_date_entry.get()
            scnHall = hall_combo.get()
            start_time = start_hour_spinbox.get() + ":" + start_minute_spinbox.get()
            end_time = end_hour_spinbox.get() + ":" + end_minute_spinbox.get()
            # validate inputs, and create screen if successful
            confirm = messagebox.askyesno("Confirmation", "Are you sure to add this screening?")
            if confirm:
                response = cinema.createScreening(scnMovie,scnDate,scnHall,start_time,end_time)
                if type(response) is not str:
                    fillScreenBox()
                    messagebox.showinfo("Success", "New screening added successfully")
                else:
                    messagebox.showinfo("Error",response)
        # command that selects a screening
        def selectScn():
            # get selected movie
            screenIndex = screenListBox.curselection()
            # If a movie is chosen
            if screenIndex:
                return [screenListBox.get(idx) for idx in screenIndex][0]
            else:
                return False
        # command that views a screening information
        def viewScn():
            selection = selectScn()
            if selection:
                selectedScreen = cinema.findScreening(selection)
                # get details of the movie object
                messagebox.showinfo("Information", cinema.getScreeningDetails(selectedScreen))
            else:
                messagebox.showinfo("Error","Please select a movie first")
        # command that deletes a screening 
        def deleteScn():
            selection = selectScn()
            if selection:
                confirm = messagebox.askyesno("Confirmation", "Are you sure to delete this screening?")
                if confirm:
                    response = cinema.deleteScreening(cinema.findScreening(selection))
                    if type(response) is not str:
                        fillScreenBox()
                        response = "Screening " + selection + " has been deleted"
                        # get details of the movie object
                        messagebox.showinfo("Success",response)
                    else:
                        messagebox.showinfo("Error",response)
                else:
                    pass
            else:
                messagebox.showinfo("Error","Please select a screening first")
        # command that updates movie_combo after adding or deleting a movie
        def updateCombo():
            options = ['(select a movie)']
            for movie in cinema.movieList:
                options.append(movie)
            movie_combo['values'] = options
            movie_combo.set('(select a movie)')
        # command that log outs
        def logout():
            # log out the user
            if cinema.logout():
                messagebox.showinfo("Alert", "Log out Successful")
                # refresh the HomePage
                refreshHomePage()
            else:
                messagebox.showinfo("Error", "Cannot log out at the moment")
        ### Homepage widgets ###
        # default variables and labels
        border2Text = "Manage Shopping Cart"
        border3Text = "Manage Bookings"
        msg = ''
        # three frames
        border1 = tk.LabelFrame(self, text="Search Movie/Screening")
        border1.pack(side=tk.LEFT, fill="both", expand="yes", padx= 10, pady=50)
        border2 = tk.LabelFrame(self, text=border2Text)
        border2.pack(side=tk.LEFT, fill="both", expand="yes", padx= 10, pady=50)
        border3 = tk.LabelFrame(self, text=border3Text)
        border3.pack(side=tk.LEFT, fill="both", expand="yes", padx= 10, pady=50)
        
        ### header
        Button1 = tk.Button(self, text="Logout", command=logout)
        Button1.place(x=390, y=20)
        Button2 = tk.Button(self, text="Login", command = lambda:controller.show_frame(Login))
        Button3 = tk.Button(self, text="Register", command = lambda:controller.show_frame(Register))
        # default function for checking seat
        checkSeatFunc = checkAvailableSeat
        # Welcome message varies depending on the role of the user
        user_label = tk.Label(self, text=msg)
        user_label.place(x=50, y=20)

        ### border 1 widgets
        # Search widgets
        search_label = tk.Label(border1, text="Search:")
        search_label.place(x=5, y=15)
        search_entry = tk.Entry(border1, width=30, bd=5)
        search_entry.place(x=50, y=15)
        filter_label = tk.Label(border1, text="Filter:")
        filter_label.place(x=5, y=50)
        cal=DateEntry(border1, selectmode='day', maxdate=current_date)
        options = ["title", "language", "genre", "release date"]
        combo = ttk.Combobox(border1, values=options, width=11)
        combo.set(options[0])
        combo.bind("<<ComboboxSelected>>", comboSelection)
        combo.place(x=50, y=50)
        search_button = tk.Button(border1, text="Submit", command=searchMovie)
        search_button.place(x=150, y=50)
        # List Box for search results
        searchList = tk.Listbox(master=border1, exportselection=0, selectmode=tk.BROWSE, height=7, width=38)
        searchList.place(x=5, y=80)
        # display buttons   
        info_button = tk.Button(border1, text="Info", command=movieInfo)
        info_button.place(x=80, y=200)
        screen_button = tk.Button(border1, text="Screenings", command=displayScreenings)
        screen_button.place(x=120, y=200)
        # List Box for screenings
        screeningList = tk.Listbox(master=border1, exportselection=0, selectmode=tk.BROWSE, height=7, width=38)
        screeningList.place(x=5, y=230)
        # check seat buttons
        check_seat_button = tk.Button(border1, text="Check Seats", command=checkSeatFunc)
        check_seat_button.place(x=90, y=350)

        ### border 2 widgets
        # search function for available seats
        search_label = tk.Label(border2, text="Select Seats By Row:")
        options = [chr(65 + i) for i in range(12)]
        rowCombo = ttk.Combobox(border2, values=options, width=11)
        rowCombo.set(options[0])
        rowCombo.bind("<<ComboboxSelected>>", checkAvailableRowSeat)
        seatListBox = tk.Listbox(master=border2, exportselection=0, selectmode=tk.BROWSE, height=10, width=38)
        show_button = tk.Button(border2, text="Seating Plan", command=drawSeatingPlan)
        add_button = tk.Button(border2, text="Add to Cart", command=addSeat)
        cartListBox = tk.Listbox(master=border2, exportselection=0, selectmode=tk.BROWSE, height=7, width=38)
        clear_button = tk.Button(border2, text="Clear Cart", command=clearSeat)
        delete_button = tk.Button(border2, text="Remove Seat", command=deleteSeat)

        ### border 3 widgets
        # price labels
        price_label = tk.Label(border3, text="Total Price: $")
        total_price = Decimal('0.00')
        total_label = tk.Label(border3, text=total_price)
        # discount label
        discount_label = tk.Label(border3, text='')
        # payment type combobox
        options = ['Cash','Credit Card','Debit Card']
        payCombo = ttk.Combobox(border3, values=options, width=10)
        payCombo.set(options[0])
        payCombo.bind("<<ComboboxSelected>>", paymentSelection)
        # card number AND name on card entries
        cardNumber = tk.Label(border3, text="Card Number: ")
        cardNumber_entry = tk.Entry(border3, width=20, bd=5)
        nameOnCard = tk.Label(border3, text="Name on Card: ")
        nameOnCard_entry = tk.Entry(border3, width=20, bd=5)
        # credit card required entries 
        cardType = tk.Label(border3, text="Card type: ")
        options = ['Mastercard', 'Visa', 'American Express', 'Union Pay','Discover']
        cardTypeCombo = ttk.Combobox(border3, values=options, width=15)
        cardTypeCombo.set(options[0])
        cardTypeCombo.bind("<<ComboboxSelected>>")
        expiryDate = tk.Label(border3, text="Expiry date: ")
        options = []
        for i in range(1,13,1):
            options.append(i)
        monthCombo = ttk.Combobox(border3, values=options, width=3)
        monthCombo.set(options[0])
        monthCombo.bind("<<ComboboxSelected>>")
        dividelabel = tk.Label(border3, text="/")
        options = []
        for i in range(current_year,current_year+6,1):
            options.append(i)
        yearCombo = ttk.Combobox(border3, values=options, width=3)
        yearCombo.set(options[0])
        yearCombo.bind("<<ComboboxSelected>>")
        # debit card entries 
        bank = tk.Label(border3, text="Bank: ")
        options = ['ANZ', 'ASB', 'BNZ', 'Westpac','Kiwibank']
        bankCombo = ttk.Combobox(border3, values=options, width=15)
        bankCombo.set(options[0])
        bankCombo.bind("<<ComboboxSelected>>")
        # discount coupon entry
        discountCode = tk.Label(border3, text="Discount Code: ")
        discountCode_entry = tk.Entry(border3, width=20, bd=5)
        # book button
        applyButton = tk.Button(border3, text="Apply Coupon", command=applyCoupon)
        bookButton = tk.Button(border3, text="Checkout and Book", command=makePayment)
        # booking listbox
        bookListBox = tk.Listbox(master=border3, exportselection=0, selectmode=tk.BROWSE, height=7, width=38)
        # booking related buttons
        viewButton = tk.Button(border3, text="Booking Info", command=viewBooking)
        deleteButton = tk.Button(border3, text="Cancel Booking", command=deleteBooking)

        ### Guest functions ###
        if cinema.checkUser() == "guest":
            # new texts
            msg = "Welcome guest. Please login or register"
            # update the new text
            user_label.config(text=msg)
            # remove logout button, place login and register buttons
            Button1.place_forget()
            Button2.place(x=370, y=20)
            Button3.place(x=420, y=20)
            # warning labels for border2 and border3
            warning_label = tk.Label(self, text="Login first to unlock these functions")
            warning_label.place(x=300, y=200)
            warning_label = tk.Label(self, text="Login first to unlock these functions")
            warning_label.place(x=565, y=200)
        ### Shared functions between staff and customer ###
        elif cinema.checkUser() == "customer" or cinema.checkUser() == "staff" :
            ## place the relevant labels
            # border 2 widgets placement
            search_label.place(x=5, y=8)
            rowCombo.place(x=145, y=8)
            seatListBox.place(x=5, y=35)
            show_button.place(x=40, y=200)
            add_button.place(x=120, y=200)
            cartListBox.place(x=5, y=230)
            clear_button.place(x=50, y=350)
            delete_button.place(x=120, y=350)
            # border 3 widgets placement
            price_label.place(x=5, y=8)
            total_label.place(x=75, y=8)
            discount_label.place(x=105, y=8)
            payCombo.place(x=160, y=8)
            discountCode.place(x=5, y=41)
            discountCode_entry.place(x=100, y=40)
            applyButton.place(x=5, y=70)
            bookButton.place(x=100, y=70)
            bookListBox.place(x=5, y=230)
            viewButton.place(x=45, y=350)
            deleteButton.place(x=125, y=350)
            ### Customer only functions ###
            if cinema.checkUser() == "customer":
                # msg for customer
                msg = "Welcome back, " + cinema.currentUser.givenName + "! (customer)"
                # update the new text
                user_label.config(text=msg)
                # load existing data
                fillListBox()
                # display any unseen notification
                for note in cinema.displayNotification():
                    messagebox.showinfo("Notification", str(note))
            ### Staff only functions ###
            else:
                # msg for staff
                msg = "Welcome back, " + cinema.currentUser.givenName + "! (staff)"
                # update the new text
                user_label.config(text=msg)
                # select a customer widgets
                select_label = tk.Label(self, text="Select Customer :")
                select_label.place(x=550, y=20)
                options = ['(select a customer)']
                for customer in cinema.customerList:
                    options.append(customer)
                customerCombo = ttk.Combobox(self, values=options, width=20)
                customerCombo.set(options[0])
                customerCombo.bind("<<ComboboxSelected>>", fillListBox)
                customerCombo.place(x=650, y=20)
        ### Admin functions ###
        else:
            msg = "Welcome back, " + cinema.currentUser.givenName + "! (admin)"
            user_label.config(text=msg)
            border2.config(text="Manage Movies")
            border3.config(text="Manage Screenings")
            # Manage Movies widgets
            check_seat_button.place_forget()
            movie_title_label = tk.Label(border2, text="Movie Title: ")
            movie_title_label.place(x=5, y=15)
            movie_title_entry = tk.Entry(border2, width=23, bd=5)
            movie_title_entry.place(x=90, y=15)
            movie_lang_label = tk.Label(border2, text="Movie Language: ")
            movie_lang_label.place(x=5, y=45)
            movie_lang_entry = tk.Entry(border2, width=20, bd=5)
            movie_lang_entry.place(x=110, y=45)
            movie_gen_label = tk.Label(border2, text="Movie Genre: ")
            movie_gen_label.place(x=5, y=75)
            movie_gen_entry = tk.Entry(border2, width=23, bd=5)
            movie_gen_entry.place(x=90, y=75)
            movie_redate_label = tk.Label(border2, text="Release Date: ")
            movie_redate_label.place(x=5, y=105)
            movie_redate_entry =DateEntry(border2, selectmode='day')
            movie_redate_entry.place(x=90, y=105)
            add_movie_button = tk.Button(border2, text="Add Movie", command=addMovie)
            add_movie_button.place(x=90, y=135)
            movieListBox = tk.Listbox(master=border2, exportselection=0, selectmode=tk.BROWSE, height=11, width=38)
            movieListBox.place(x=5, y=165)
            view_movie_button = tk.Button(border2, text="Movie Info", command=viewMv)
            view_movie_button.place(x=50, y=350)
            delete_movie_button = tk.Button(border2, text="Cancel Movie", command=deleteMv)
            delete_movie_button.place(x=120, y=350)
            # Manage Screenings widgets
            select_screen_label = tk.Label(border3, text="Select Movie: ")
            select_screen_label.place(x=5, y=15)
            options = []
            movie_combo = ttk.Combobox(border3, values=options, width=20)
            updateCombo()
            movie_combo.bind("<<ComboboxSelected>>", fillScreenBox)
            movie_combo.place(x=95, y=15)
            screen_date_label = tk.Label(border3, text="Screening Date: ")
            screen_date_label.place(x=5, y=45)
            screen_date_entry = DateEntry(border3, selectmode='day', mindate=current_date)
            screen_date_entry.place(x=95, y=45)
            hall_label = tk.Label(border3, text="Select a hall: ")
            hall_label.place(x=5, y=75)
            options = ['(select a hall)']
            for hall in cinema.hallList:
                options.append(hall)
            hall_combo = ttk.Combobox(border3, values=options, width=20)
            hall_combo.set(options[0])
            hall_combo.bind("<<ComboboxSelected>>")
            hall_combo.place(x=95, y=75)
            screen_start_label = tk.Label(border3, text="Start Time: ")
            screen_start_label.place(x=5, y=105)
            start_hour_spinbox = tk.Spinbox(border3, from_=10, to=22, width=2)
            start_hour_spinbox.place(x=95, y=105)
            start_label = tk.Label(border3, text=":")
            start_label.place(x=120, y=105)
            values = ["{:02d}".format(i) for i in range(0,51,10)]
            start_minute_spinbox = tk.Spinbox(border3, values=values, width=4)
            start_minute_spinbox.place(x=130, y=105)
            screen_start_label = tk.Label(border3, text="End Time: ")
            screen_start_label.place(x=5, y=135)
            end_hour_spinbox = tk.Spinbox(border3, from_=11, to=23, width=2)
            end_hour_spinbox.place(x=95, y=135)
            end_label = tk.Label(border3, text=":")
            end_label.place(x=120, y=135)
            values = ["{:02d}".format(i) for i in range(0,51,10)]
            end_minute_spinbox = tk.Spinbox(border3, values=values, width=4)
            end_minute_spinbox.place(x=130, y=135)
            add_screen_button = tk.Button(border3, text="Add Screen", command=addScn)
            add_screen_button.place(x=90, y=165)
            screenListBox = tk.Listbox(master=border3, exportselection=0, selectmode=tk.BROWSE, height=9, width=38)
            screenListBox.place(x=5, y=195)
            view_screen_button = tk.Button(border3, text="Screening Info", command=viewScn)
            view_screen_button.place(x=30, y=350)
            delete_screen_button = tk.Button(border3, text="Cancel Screening", command=deleteScn)
            delete_screen_button.place(x=120, y=350)
            # fill the movie list box with existing movies
            fillMovieBox()
            
### Application Controller ###
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.window = tk.Frame(self)
        self.window.pack()

        self.window.grid_rowconfigure(0, minsize=500)
        self.window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (Login,Register,Reset,HomePage):
            frame = F(self.window, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky='nsew')
        self.show_frame(HomePage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Cinema Application")
# Function which refreshes the home page after login or logout
def refreshHomePage():
    # Destroy the existing HomePage frame
    app.frames[HomePage].destroy()  
    # Create a new instance of HomePage
    app.frames[HomePage] = HomePage(app.window, app)
    # Relocate the frame to the right place
    app.frames[HomePage].grid(row=0, column = 0, sticky='nsew')
    # Show the recreated HomePage frame  
    app.show_frame(HomePage)
# Function which shows the seating plan of the hall
def draw_seating_plan():
    # Create the main window
    root = tk.Tk()
    root.title("Cinema Seating Plan")
    # Create a Canvas widget
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()
    x1 = 20
    y1 = 20
    x2 = 500
    y2 = 50
    # Draw the screen
    canvas.create_rectangle(x1, y1, x2, y2, fill="gray")
    # Calculate the center of the screen
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    # Text to display inside the screen
    text = "Screen"
    # Create the text inside the screen
    canvas.create_text(center_x, center_y, text=text, fill="white", font=("Arial", 12, "bold"))
    # Draw the seats
    y = 30
    for row in range(2, 14):
        for seat in range(1, 11):
            x1 = seat * 40
            y1 = row * y
            x2 = x1 + 30
            y2 = y1 + 25
            # Create seat
            canvas.create_rectangle(x1, y1, x2, y2, fill="gray")
            # Calculate the center of the seat
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2
            # Text to display inside the seat
            text = chr(63 + row) + str(seat)
            # Create the text inside the seat
            canvas.create_text(center_x, center_y, text=text, fill="white", font=("Arial", 12, "bold"))
    note_label = tk.Label(root, text="Note: some seats are not available for some screenings")
    note_label.place(x=40, y=450)

app = Application()
app.maxsize(800,500)
app.mainloop()