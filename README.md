# 🚗 CRAMS
Welcome to the **Car Rental Management System**! This is the final project we developed as part of our **Software Engineering** course. This web application is designed to streamline the process for both **car dealers** and **customers**. It allows car dealers to easily manage their vehicles and rental orders, while providing customers with a simple and secure way to search for, rent, and track their car rentals – all in one convenient platform!

## 🎥 [Click for Video Demo](URL HERE)

## 🚗 Features
- **User Authentication**: Register and log in as a customer or car dealer. Each role has access to specific functionalities such as managing vehicles or renting cars.
- **Car Search**: Easily search for available cars based on various criteria like VIN and location.
- **Vehicle Management**: Car dealers can add and remove vehicles from the system, including uploading photos and specifying features.
- **Car Rental**: Customers can rent cars directly through the platform with a simple, secure booking process. Payment can be made via debit/credit card or PayPal.
- **Order Tracking**: Keep track of car rental orders and their statuses, including pending and completed rentals.
- **Reports**: Generate detailed reports on vehicle availability, rental orders, and earnings for car dealers.
- **Contact Form**: Guests can contact the platform through a contact form for inquiries or support.

## 🛠 Tech Stack
- **Frontend**:
  - [jQuery](https://jquery.com/) simplifies DOM manipulation, event handling, and Ajax requests on the front-end.
  - [Popper.js](https://popper.js.org/docs/v2/) manages poppers (elements that pop up, like tooltips or dropdowns), often used with Bootstrap.
  - [Bootstrap JS](https://getbootstrap.com/) is used for front-end functionality.
  - [W3.css](https://www.w3schools.com/w3css/defaulT.asp)
- **Backend**:
  - [Django](https://www.djangoproject.com/) is the core back-end framework used to build web applications.
  - [MySQL](https://www.mysql.com/) stores data like user info, vehicles details, orders, and contacts.
  - [Flask](https://flask.palletsprojects.com/en/stable/) is used for lightweight applications (though in this case, Django is the main framework).

## 🤝 Collaborators
[@Anahita0712](https://github.com/Anahita0712)
[@Karan-Goel10](https://github.com/Karan-Goel10)
[@Mahad10569](https://github.com/Mahad10569)
[@SahibjotSB](https://github.com/SahibjotSB)

### 🚀 Install Requirements
```bash
pip install -r requirements.txt
```
- **Make migrations**
```
python manage.py makemigrations
python manage.py migrate
```
- **Run app on website**
```
python manage.py runserver
```
- **Create admin account**
```
python manage.py createsuperuser
```
### 🧑‍💻 Accounts for Testing
- **Admin Account**
```
username: admin
password: cp317
```
- **Client Account**
```
username: client1
password: cp317
```
- **Dealer Account**
```
username: dealer1
password: cp317
```
### 💳 Payment Testing
- **PayPal Test Account**
```
firstname: John
lastname: Doe
email: sb-icssv33269733@business.example.com
password: ,t8/L&Tq
address: 1 Maire-Victorin, Toronto ON M5A 1E1
phone: 6136270192
```
- **Credit Card Test**
```
card number: 4214023128717093
expiry date: 02/2029
cvc code: 848
```
### 🛠 Database Management
[localhost:8000/admin](http://127.0.0.1:8000/)

