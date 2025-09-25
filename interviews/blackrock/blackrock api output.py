Skip to:

Header Navigation
Side Navigation
Main content
HackerRank
Fun with Anagrams
S
REST API: TV Shows Produced During a Period
Stefan
REST API: TV Shows Produced During a Period
Description
Use the HTTP GET method to fetch information about recent TV shows. Query the endpoint https://jsonmock.hackerrank.com/api/tvseries to retrieve all records. The results are paginated and can be accessed by appending ?page=num to the query string, where num is the page number.

 

The response is a JSON object containing the following fields:

page: current page of results (Number)
per_page: maximum number of results per page (Number)
total: total number of results (Number)
total_pages: total number of pages with results (Number)
data: an array of TV series records
 

Each TV series in the data array has the following structure:

    "name": "Game of Thrones",
    "runtime_of_series": "(2011–2019)",
    "certificate": "A",
    "runtime_of_episodes": "57 min",
    "genre": "Action, Adventure, Drama",
    "imdb_rating": 9.3,
    "overview": "Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns after being dormant for millennia.",
    "no_of_votes": 1773458,
    "id": 1
 

In data, each tv series has the following schema:

name: (String)

runtime_of_series: years the show is in production (String)

certificate: rating (String)

runtime_of_episodes: average length per episode in minutes (String).

genre: genre (String)

imdb_rating: average viewer rating (Number)

overview: short description (String)
no_of_votes: how many votes were cast on imdb (Number)
id: unique identifier (Number) 
 

There are 4 possible forms of runtime_of_series.

(2020-2021) - The first and last years of production are shown.
(2020- ) - The show is still in production.
(2020) - The show was only produced for one year.
Entries may have (I) or (II) followed by one of the above formats, e.g., '(II) (2006-2010)'. Ignore (I) or (II).
Given a start year and an end year, return a list of the names of all tv series that started production in startYear or later and ended production in endYear or earlier. If the endYear is -1, the shows should still be in production. Sort the list in alphabetical order.

 
Function Description

Complete the function showsInProduction in the editor with the following parameter(s):

    int startYear: the earliest year of production

    int endYear: the latest year of production or -1

 

Return

    string[]: the sorted list of names of shows in production during the time period

 

Note: Please review the header in the code stub to see available libraries for API requests in the selected language. Required libraries can be imported in order to solve the question. Check our full list of supported libraries at https://www.hackerrank.com/environment.

Input Format For Custom Testing
Sample Case 0
Sample Input For Custom Testing

2006
2011
Sample Output

Death Note: Desu nôto
Heroes
Terra Nova
The Inbetweeners
The Tudors
Explanation

Return a list of shows that started production in 2006 or later and ended production in 2011 or earlier.

 

The name runtime_of_series pairs that match the query are shown.

(2006-2007) - Death Note: Desu nôto

(II) (2006-2010) - Heroes

(2008-2010) - The Inbetweeners

(2011) - Terra Nova

(2007-2010) - The Tudors

Sample Case 1
Sample Input For Custom Testing

2019
-1
Sample Output

After Life
Love, Death & Robots
Paranormal
Russian Doll
Sex Education
The Boys
The Mandalorian
The Umbrella Academy
Explanation

Show all the series that began production in 2019 or later and are still in production.

 

These series meet the criteria.

(2019- ) - After Life

(2019- ) - Love, Death & Robots

(2020- ) - Paranormal

(2019- ) - Russian Doll

(2019- ) - Sex Education

(2019- ) - The Boys

(2019- ) - The Mandalorian

(2019- ) - The Umbrella Academy

Python 3
34353637333932282930313840414227252643444546474849505152
#!/bin/python3

import math
import os
import random
import re
import sys
import requests

#
# Complete the 'showsInProduction' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER startYear
#  2. INTEGER endYear
#
# Base url: https://jsonmock.hackerrank.com/api/tvseries
…            runtime = show.get("runtime_of_series")
            start, end_time = get_runtime(runtime)
            if start <= startYear and end_time >= endYear:
                res.append(show.get("name"))
    return res
            

if __name__ == '__main__':
23def get_runtime(runtime):
Line: 66 Col: 17

Input / Output

Test Cases

Console
Test case passed:

0/10

Select a test case
Test case 0
Input (stdin)
2015
2017
Your Output (stdout)
Game of Thrones
Sherlock
The Big Bang Theory
Dexter
Prison Break
House of Cards
Vikings
Arrow
Supernatural
Suits
Daredevil
Narcos
Modern Family
Mr. Robot
Better Call Saul
Homeland
The Vampire Diaries
Orange Is the New Black
Arrested Development
Brooklyn Nine-Nine
The 100
Parks and Recreation
Gotham
Once Upon a Time
Shameless
Agents of S.H.I.E.L.D.
Jessica Jones
New Girl
Pretty Little Liars
Bones
Sense8
How to Get Away with Murder
Teen Wolf
Silicon Valley
Luther
The Originals
BoJack Horseman
Supergirl
Grimm
Orphan Black
Elementary
Bates Motel
Broadchurch
Black Sails
2 Broke Girls
The Man in the High Castle
Making a Murderer
The Americans
Naruto: Shippûden
The Leftovers
Ray Donovan
Schitt's Creek
Expected Output
Agent Carter
Master of None
Narcos
Debug output
None
[{'name': 'Game of Thrones', 'runtime_of_series': '(2011-2019)', 'certificate': 'A', 'runtime_of_episodes': '57 min', 'genre': 'Action, Adventure, Drama', 'imdb_rating': 9.3, 'overview': 'Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns after being dormant for millennia.', 'no_of_votes': 1773458, 'id': 1}, {'name': 'Breaking Bad', 'runtime_of_series': '(2008-2013)', 'certificate': '18', 'runtime_of_episodes': '49 min', 'genre': 'Crime, Drama, Thriller', 'imdb_rating': 9.5, 'overview': "A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's future.", 'no_of_votes': 1468887, 'id': 2}, {'name': 'The Walking Dead', 'runtime_of_series': '(2010- )', 'certificate': '18+', 'runtime_of_episodes': '44 min', 'genre': 'Drama, Horror, Thriller', 'imdb_rating': 8.2, 'overview': 'Sheriff Deputy Rick Grimes wakes up from a coma to learn the world is in ruins and must lead a group of survivors to stay alive.', 'no_of_votes': 854698, 'id': 3}, {'name': 'Friends', 'runtime_of_series': '(1994-2004)', 'certificate': '13+', 'runtime_of_episodes': '22 min', 'genre': 'Comedy, Romance', 'imdb_rating': 8.9, 'overview': 'Follows the personal and professional lives of six twenty to thirty-something-year-old friends living in Manhattan.', 'no_of_votes': 829816, 'id': 4}, {'name': 'Stranger Things', 'runtime_of_series': '(2016- )', 'certificate': '15', 'runtime_of_episodes': '51 min', 'genre': 'Drama, Fantasy, Horror', 'imdb_rating': 8.7, 'overview': 'When a young boy disappears, his mother, a police chief and his friends must confront terrifying supernatural forces in order to get him back.', 'no_of_votes': 824966, 'id': 5}, {'name': 'Sherlock', 'runtime_of_series': '(2010-2017)', 'certificate': 'UA', 'runtime_of_episodes': '88 min', 'genre': 'Crime, Drama, Mystery', 'imdb_rating': 9.1, 'overview': 'A modern update finds the famous sleuth and his doctor partner solving crime in 21st century London.', 'no_of_votes': 808717, 'id': 6}, {'name': 'The Big Bang Theory', 'runtime_of_series': '(2007-2019)', 'certificate': 'U', 'runtime_of_episodes': '22 min', 'genre': 'Comedy, Romance', 'imdb_rating': 8.1, 'overview': 'A woman who moves into an apartment across the hall from two brilliant but socially awkward physicists shows them how little they know about life outside of the laboratory.', 'no_of_votes': 724187, 'id': 7}, {'name': 'Dexter', 'runtime_of_series': '(2006-2021)', 'certificate': 'A', 'runtime_of_episodes': '53 min', 'genre': 'Crime, Drama, Mystery', 'imdb_rating': 8.6, 'overview': 'By day, mild-mannered Dexter is a blood-spatter analyst for the Miami police. But at night, he is a serial killer who only targets other murderers.', 'no_of_votes': 647136, 'id': 8}, {'name': 'How I Met Your Mother', 'runtime_of_series': '(2005-2014)', 'certificate': '15+', 'runtime_of_episodes': '22 min', 'genre': 'Comedy, Romance', 'imdb_rating': 8.3, 'overview': 'A father recounts to his children - through a series of flashbacks - the journey he and his four best friends took leading up to him meeting their mother.', 'no_of_votes': 603824, 'id': 9}, {'name': 'True Detective', 'runtime_of_series': '(2014- )', 'certificate': 'A', 'runtime_of_episodes': '55 min', 'genre': 'Crime, Drama, Mystery', 'imdb_rating': 9, 'overview': 'Seasonal anthology series in which police investigations unearth the personal and professional secrets of those involved, both within and outside the law.', 'no_of_votes': 500194, 'id': 10}]
[{'name': 'Lost', 'runtime_of_series': '(2004-2010)', 'certificate': 'A', 'runtime_of_episodes': '44 min', 'genre': 'Adventure, Drama, Fantasy', 'imdb_rating': 8.3, 'overview': 'The survivors of a plane crash are forced to work together in order to survive on a seemingly deserted tropical island.', 'no_of_votes': 496290, 'id': 11}, {'name': 'Prison Break', 'runtime_of_series': '(2005-2017)', 'certificate': 'UA', 'runtime_of_episodes': '44 min', 'genre': 'Action, Crime, Drama', 'imdb_rating': 8.3, 'overview': 'Due to a political conspiracy, an innocent man is sent to death row and his only hope is his brother, who makes it his mission to deliberately get himself sent to the same prison in order to break the both of them out, from the inside.', 'no_of_votes': 477157, 'id': 12}, {'name': 'House of Cards', 'runtime_of_series': '(2013-2018)', 'certificate': '16+', 'runtime_of_episodes': '51 min', 'genre': 'Drama', 'imdb_rating': 8.7, 'overview': 'A Congressman works with his equally conniving wife to exact revenge on the people who betrayed him.', 'no_of_votes': 467371, 'id': 13}, {'name': 'Black Mirror', 'runtime_of_series': '(2011- )', 'certificate': 'A', 'runtime_of_episodes': '60 min', 'genre': 'Drama, Sci-Fi, Thriller', 'imdb_rating': 8.8, 'overview': "An anthology series exploring a twisted, high-tech multiverse where humanity's greatest innovations and darkest instincts collide.", 'no_of_votes': 445745, 'id': 14}, {'name': 'Vikings', 'runtime_of_series': '(2013-2020)', 'certificate': 'A', 'runtime_of_episodes': {-truncated-}
values, ``` ``` , Prints the values to a stream, or to sys.stdout by default. sep   string inserted between values, default a space. end   string appended after the last value, default a newline. file   a file-like object (stream); defaults to the current sys.stdout. flush   whether to forcibly flush the stream., hint
Loading...
