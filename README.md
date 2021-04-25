# DevClub IITD Recruitment Assignment 2021

## Backend Project: Library Management Website


### About
A library website for users to get information about the books in the library and borrow/return/renew books.

Website hosted on Heroku: [Booklib: Your Own Library](https://polar-chamber-13872.herokuapp.com/)


### Features
All the minimum features prescribed in the assignment are implemented.

1. A registration system to allow users to register themselves with the library using email id, username and password.
2. Access level system implemented: three levels of access to different types of users. Admins: with all access to the site, Librarians: with access to book management only and
members/users with access to only view and borrow books.
    Note: 
    1. Website hosted contains default admin account with the prescribed username and password.
    2. Website contains a Librarian level account with credentials mentioned in form submitted.
    3. Website contains dummy user accounts with credentials mentioned in form submitted.
3. Separate pages for each book containing details about the book, and also included, details about each copy of the book (Yes, multiple copy system for each book implemented)
4. System for Librarians to add and edit book info under the admin site, which is linked with the Librarian Dashboard site.
5. Admins can assign Librarian role in the admin site under group property of each user.
6. Search bar for books and author search.
7. System to borrow book, the link to borrow a book becomes visible in the book's detail page only if the user viewing is logged in.
8. Librarians can accept or reject requests for borrowing a book under dashboard as well as in admin site. Database is automatically updated after Librarian approves or rejects 
request.
9. System to renew/return book in user's dashboard.

Preferred Requirements implemented:

1. Homepage displays recently added books. (Also added complete library stats in the home page)


### Technologies used:
Django Python Framework

Heroku (for hosting)

### How to run locally
Requirements: 

1. Python 3.6+ (I used 3.8.x)
2. Django 2.2+ (I used the latest version available 3.2)

Steps:
1. Clone or download the zip file of the repo in your local machine.
2. Go into the outer booklib directory (which contains manage.py file) and run the command: `python manage.py runserver`

The server should be up and running on the default port. Go to the url shown in your terminal (Generally: `127.0.0.1:8000`)


### Website Overview
*/* : base url redirects to /books/

*/books/* : de-facto home page. Displays library stats and recently added books. Contains links to all other pages of website (except admin site)

*/books/all/* : Displays all books availablae in the library

*/books/authors/all/* : Displays all the authors whose books are available in the library

*/books/<book_pk>/* : Specific page of book with primary key <book_pk>, displays that book's complete information.

*/books/authors/<author_pk>/<author_name>/* : Specific page of author with name <author_name>, displaying all the books of that author present in the library.

*/books/<book_pk>/<book_instance_uuid>/borrow/* : Borrow/renew request page for a copy of book with primary key <book_pk> and the copy's UUID <book_instance_uuid>

*Serach bar* for books and authors (both separately) are displayed in each page with url /books/

*/accounts/dashboard/* : The 'dashboard' or 'profile page' of the user. It shows all books borrowed currently by the user and pending requests of books requested by the 
user to borrow. In case of Librarians, it shows all books currently borrowed from the library and all pending borrow requests. For both librarians and admins, this page 
also contains link to admin page.

*/accounts/register/* : Page for registeration for new users

*/accounts/login/* : Page for logging in for existing users

*/admin/* : The admin page. This is the default admin page implementation of Django. Site Admins can add, edit or remove any user or book from the library. Librarians can only add,
edit or remove books, authors and specific copies of books (named under Book Instances class) from the library. Librarians can also approve or reject book borrow requests
by selecting the requests and choosing the respective command from dropdown and selecting 'Go' option next to it.

Note: since this is the default Django admin implementation, and I have not changed much, so there are no hyperlinks to go back to main library website from here. One has to 
manually replace the '/admin/*' url to '/' in the browser to go to home page.


### Proposed plans not implemented (due to time or other constraints)
1. Prevent user to request multiple times for same book, or to multiple available copies of same book.
2. Prevent user to make borrow request if they already have borrowed a fixed number of books.
3. Password change, forgot password system.
4. Email validation.
5. Email notifications about due dates to users.
6. Google sign in.

## Research Assignment
PDF file included in my repo as well for the Research Assignment.
