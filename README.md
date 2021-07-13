# Instagram-Replica
## Author
Nicholas Ngetich
*****
### Description
This is a Django web application replica website for the popular photo app Instagram.It requires users to sign in to the application to start using and upload pictures to the application.A user can follow other users and see their pictures on my timeline and also like a picture or leave a comment on it.

### Prerequisites
* Python 3
* Text editor eg Visual Studio Code
* You need to have git installed. You can install it with the following command in your terminal
`$ sudo apt install git-all`
*****
## Setup Instruction
To access this project on your local files, you can clone it using these steps
1. Open your terminal
1. Use this command to clone $ git clone https://github.com/ngetichnicholas/Instagram-Replica.git
1. This will clone the repositoty into your local folder
*****
### Admin Site
There is an admin site to manage the application entities,that is,  users, images and profiles
![alt text](https://res.cloudinary.com/dbos9xidr/image/upload/v1626157955/Screenshot_from_2021-07-13_09-31-59_mdnl20.png)
### User Profile and Timeline posts
After a user successfully sign up and login, they will be redirected to profile page showing user information and posts by other users
![alt text](https://res.cloudinary.com/dbos9xidr/image/upload/v1626157017/screencapture-nick-instagram-herokuapp-accounts-profile-2021-07-13-09_09_20_rhwfbf.png)
*****
### View Photo details
A user can click on any image and a page will be displayed containing the photo information like image name, caption, number of comments and likes and also date posted.  
A user can only see a delete button if they are the owner of the post so they cannot delete a post belonging to another user
*****
![alt text](https://res.cloudinary.com/dbos9xidr/image/upload/v1626157362/screencapture-nick-instagram-herokuapp-photo-10-2021-07-13-09_10_58_ktsjzu.png)
*****
### Search Function
A user can search other users and it will return users found or display "Found 0 results if no match found by the search function.
*****
![alt text](https://res.cloudinary.com/dbos9xidr/image/upload/v1626157535/screencapture-127-0-0-1-8000-search-2021-07-13-09_25_11_d1wgdy.png)
*****
## Behaviour Driven Development
1. Show user profile 
   - INPUT: Account option profile clicked
   - OUTPUT: Profile page with user information and other users posts displayed
1. Provides a search form
   - INPUT: Search term entered in the search field
   - OUTPUT: Number of matched user results displayed in the page
1. Show photo details
   - INPUT: Image is clicked
   - OUTPUT: A new page loaded with image details
1. Provides a delete function for image
   - INPUT: Delete button clicked
   - OUTPUT: Image deleted
## Dependencies
* django-bootstrap
* Pillow
* psycopg2
* python-decouple
* Python Venv
* whitenoise
* gunicorn
*****
## Technologies Used
* HTML
* Python 3
* JavaScript
* CSS
******
### Live Link
Or you can access the web application directly via this [LIVE LINK]().
*****
### License
This project is under:  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](/LICENSE)
*****
### Questions?
Twitter: **[@ngetichnichoh](https://twitter.com/ngetichnichoh)**  
Email: **[nicholas.ngetich@student.moringaschool.com](mailto:nicholas.ngetich@student.moringaschool.com)**