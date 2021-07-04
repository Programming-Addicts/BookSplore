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
2. For some books, the Google Book API also provides a webreader for you to read the book through. This can be used through BookSplore.
3. BookSplore allows you to publish reviews about books, and rate them, which is then stored in our databases.
4. On BookSplore, you can follow other users to see what books they read, and be notified whenever they publish a review.

Please note that we use the Google Books API to obtain some information about books and to allow users to read them, so these features alone may not be available for all books. Needless to say, every other feature would be available regardless of the book, as they are completely implemented by us.

## 💻 Usage

To get started, head over to our website - [booksplore.tech](https://booksplore.tech). Once you register yourself, you will be redirected to your dashboard.

To explore our collection of books, ratings, reviews, and users, head over to the [Explore page](https://booksplore.tech), and search for a book, or user you want to view! When searching for books, you can search by name, by subject, and by its ISBN - International Standard Book Number.

Once you provide your search query, BookSplore will fetch data from the Google Books API, and our own databases for a wide collection of books, and users. You can browse these, at your leisure!

## ️️🛠️ Tools Used

This project was written in `Python3`, and primarily, `Javascript` for the frontend.

The backend made use of `FastAPI`, which is a fast, asynchronous API framework for Python, and `Postgres` for the database. `Asyncpg` was used to establish connections to the database.

The frontend was written with a popular javascript framework called `Vue.js`

We used the Google API for books to obtain data about books published by authors.

## ⛏️  Local Setup

To locally run BookSplore, first fork, and clone this git repository to your machine.

### Setting up the Frontend

Setting up the frontend is very easy -
1. `cd` into the `frontend` directory
2. Run `npm install` or `yarn install` to install the packages required
3. Next, run `./build.sh` to build the project, and move it to the backend directory, so that the backend can serve the html files. If you are on windows, you will need to make some changes to the shell script to suit your operating system.

### Setting up the Backend

## 📃 Terms of Service

Please read this short, yet important passage. By using our website, registering for an account, you agree to these guidelines.

- Please do not abuse the website, or API in any way, like spamming it, or posting irrelevant content.
- BookSplore requires you to have a Google account to register with. Please note, that we do not access a lot of your information, and keep most of the little information that we do use, private. Once you register, your name as it appears in your Google account will be your username on the site, and your email will be kept private. To prevent people from accessing it, the email is not even sent to the frontend. It is only used as a means of differentiating accounts. By registering on BookSplore, you agree to this policy.
- Please refrain from creating multiple accounts (alt accounts) on the site.
- Please do not attempt anything malicious with the API, like trying to obtain information about other users.
- All services of BookSplore are completely free, and open-source. Some of our content may not be available evenly for all books, since we use the Google API to obtain information about books. So by using BookSplore, you agree not to market any of the code, or claim it to be any of your own.
- All rights are reserved by the admins of BookSplore, namely [Milind](https://github.com/milindmadhukar), [class PythonAddict](https://github.com/classPythonAddike/) and [devnull](https://github.com/devnull03). If they find any content to be irrelevant or users to be misusing the site, they reserve the rights to remove the content, or disable the user's account


