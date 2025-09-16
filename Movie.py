## 
# @file Movie.py
#
# @brief Movie model
# 
# @section description_cinema Description
# Maintains infomation of movies
#
# @section notes_cinema Notes
# (additional notes)
# 
# @section author_cinema Author
# Created by Nicholas Ting on 28/09/2023

# Imports
from typing import List
from datetime import date

from Screening import Screening

class Movie:
    """! The Movie class maintains Movie objects and methods"""
    nextID = 1
    def __init__(self, title: str, lan: str, gnr: str, redate: date):
        """! The class initialiser
        @param title The movie's title
        @param lan The movie's language
        @param gnr The booking's genre
        @param redate The booking's release date
        """
        # The movie's id
        self.__movieId: int = Movie.nextID
        # The movie's title
        self.__movieTitle = title
        # The movie's language
        self.__language = lan
        # The movie's genre
        self.__genre = gnr
        # The movie's release date
        self.__releaseDate = redate
        # The movie's screening list
        self.__screeningList: List[Screening] = []
        Movie.nextID += 1

    @property
    def movieId(self) -> str:
        """! Getter method for id
        @return The movie's id as a string
        """
        return str(self.__movieId)
    
    @property
    def movieTitle(self) -> str:
        """! Getter method for title
        @return The movie's title as a string
        """
        return self.__movieTitle
    
    @property
    def movieLanguage(self) -> str:
        """! Getter method for language
        @return The movie's language as a string
        """
        return self.__language
    
    @property
    def movieGenre(self) -> str:
        """! Getter method for genre
        @return The movie's genre as a string
        """
        return self.__genre

    @property
    def movieReleaseDate(self) -> date:
        """! Getter method for release date
        @return The movie's release date as a date
        """
        return self.__releaseDate
    
    @property
    def movieScreeningList(self) -> List[Screening]:
        """! Getter method for screening list
        @return The movie's screening list as a list of Screening objects
        """
        return self.__screeningList
    
    @movieScreeningList.setter
    def movieScreeningList(self, scns: List) -> bool:
        """! Setter method for screening list
        @return A boolean to indicate whether the assignment is successful
        """
        self.__screeningList = scns
    
    def __str__(self) -> str:
        """! __str__ method for Movie object
        @return The movie title in a string
        """
        return self.movieTitle
    
    def getMovieDetails(self) -> str:
        """! Get details of a movie
        @return A string of movie title, language, genre and release date
        """
        details = "Movie ID: " + self.movieId
        details += "\nTitle: " + self.movieTitle
        details += "\nLanguage: " + self.movieLanguage
        details += "\nGenre: " + self.movieGenre
        details += "\nRelease Date: " + self.movieReleaseDate.strftime('%d/%m/%Y')
        details += "\nNo. of Screenings: " + str(len(self.movieScreeningList))
        return details
    
    def addScreening(self, screen: Screening) -> bool:
        """! add a screening to the screening list
        @param screen A Screening object
        @return A boolean
        """
        self.movieScreeningList.append(screen)
        return True