<img align="left" width=70px height=70px src="https://booksplore.tech/favicon.ico" alt="Booksplore logo">

<h1>BookSplore - A Place to Enjoy Books</h1>

This project was made for a [Tech-With-Tim](https://discord.gg/twt) CodeJam, by the **Programming Addicts**.

<br>

<p align="center">

<a href="https://github.com/milindmadhukar/">
	<img src="https://images.weserv.nl/?url=avatars.githubusercontent.com/u/68477234?v=4&h=100&w=100&fit=cover&mask=circle&maxage=7d">
</a>
 
 
<a href="https://github.com/classPythonAddike/">
	<img src="https://images.weserv.nl/?url=avatars.githubusercontent.com/u/72556571?v=4&h=100&w=100&fit=cover&mask=circle&maxage=7d">
</a>
 
 
<a href="https://github.com/devnull03/">
	<img src="https://images.weserv.nl/?url=avatars.githubusercontent.com/u/56480041?v=4&h=100&w=100&fit=cover&mask=circle&maxage=7d">
</a>

</p>

## 🏁 Introduction

Booksplore is a website where you can enjoy, and explore the world of books - with your friends, and in the comfort of your browser! It offers a safe online environment for you to engross yourself in the world of books with your friends.

BookSplore is a social platform, as well as a site dedicated to books, in accordance with our tagline - `Explore the world of books, with your friends`. So BookSplore offers you the following delights -

1. Searching for books by title, subject, and isbn, and viewing information associated with them, such as a short description, similar books, published versions, etc. Note: This information is provided by the Google Book API.
2. BookSplore allows you to publish reviews about books, and rate them, which is then stored in our own databases.
3. On BookSplore, you can follow other users to see what books they read, and be notified whenever they publish a review.

Please note that we use the Google Books API to obtain some information about books and to allow users to read them, so these features alone may not be available for all books. Needless to say, every other feature would be available regardless of the book, as they are completely implemented by us.

## 💻 Usage

To get started, head over to our website - [booksplore.tech](https://booksplore.tech). Once you register yourself, you will be redirected to your dashboard.

To explore our collection of books, ratings, reviews, and users, head over to the [Explore page](https://booksplore.tech), and search for a book, or user you want to view! When searching for books, you can search by name, by subject, and by its ISBN - International Standard Book Number.

Once you provide your search query, BookSplore will fetch data from the Google Books API, and our own databases for a wide collection of books, and users. You can browse these, at your leisure!

## ️️🛠️ Tools Used

This project was written in `Python3`, and primarily, `Javascript` for the frontend.

The backend made use of `FastAPI`, which is a fast, asynchronous API framework for Python, and `Postgres` for the database. `Asyncpg` was used to establish connections to the database.

The frontend was written with a popular javascript framework - `Vue.js`

We used the Google API for books to obtain data about books published by authors.

## ⛏️  Local Setup

To locally run BookSplore, first fork, and clone this git repository to your machine.

### Setting up the Frontend

Setting up the frontend is very easy -
1. `cd` into the `frontend` directory.
2. Run `npm install` to install the packages required.
3. Next, run `npm run serve` to build the project, and move it into the required directory. If you are on Windows, you will need to run this in git bash.

### Setting up the Backend
1.  `cd` into the `backend` directory.
2.  You may create a virtualenv for the project and then run `pip install -r requirements.txt` to install the dependency modules.
3.  Create a `.env` file in the same directory as the `example.env` and copy the format as shown in the example file.
4.  Set the `SECRET_KEY` for JWT tokens.
5.  Create a postgres database and fill out the `DB_URI` in the `.env`
6.  To set up the Google authentication, go to [Google Cloud Console](https://console.cloud.google.com/), login with your google account and create a project. 
7.  Go to `APIs & Services` section and click on `+ Add Credentials` and create an Oauth Client ID
8.  Select `Web Application` for Application type and add the following entries:
`http://127.0.0.1:8000` for `Authorized JavaScript origins` and `http://127.0.0.1:8000/api/auth` for `Authorized redirect URIs`
Click `Create`
9.  Go ahead and fill out `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` in the `.env`
10. Click on `+ Add Credentials` and click on `API key` to create an API key for Google Books API. Make sure you enable the Google Books API from the Google API libraries. Fill out the `GOOGLE_API_KEY` in the `.env` file.
11. Run the command `uvicorn main:app`. If all steps were followed correctly and dependencies were installed, it will start the FastAPI server and initialize all the tables for you in the database.

## ⬅️ Contributing

To contribute to BookSplore, first fork this repository, clone it, and switch to another branch which describes your contribution.

Once you finish your changes, make sure to lint the files with a linter like prettier, or black. Then push your changes, and open a Pull Request!

## 📃 Terms of Service

Please read this short, yet important passage. By using our website, registering for an account, you agree to these guidelines.

- Please do not abuse the website, or API in any way, like spamming it, or posting irrelevant content.
- BookSplore requires you to have a Google account to register with. Please note, that we do not access a lot of your information, and keep most of the little information that we do use, private. Once you register, your name as it appears in your Google account will be your username on the site, and your email will be kept private. To prevent people from accessing it, the email is not even sent to the frontend. It is only used as a means of differentiating accounts. By registering on BookSplore, you agree to this policy.
- Please refrain from creating multiple accounts (alt accounts) on the site.
- Please do not attempt anything malicious with the API, like trying to obtain information about other users.
- All services of BookSplore are completely free, and open-source. Some of our content may not be available evenly for all books, since we use the Google API to obtain information about books. So by using BookSplore, you agree not to market any of the code, or claim it to be any of your own.
- All rights are reserved by the admins of BookSplore, namely [Milind](https://booksplore.tech/user/2), [class PythonAddict](https://booksplore.tech/user/4) and [devnull](https://booksplore.tech/user/3). If they find any content to be irrelevant or users to be misusing the site, they reserve the rights to remove the content, or disable the user's account.

<h3 align="center">BookSplore - Explore the world of books, with your friends! </h3>
