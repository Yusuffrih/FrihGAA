# FrihGAA
![Am I responsive image to go here]()

FrihGAA is my final project for the Code Institute's Professional Diploma. It is a Web Application for a fictional GAA club that satisfies the requirements of this assessment. The brief provided for this project in the Assessment handbook was to 

*"build a full-stack site based around business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service."*

- [User Experience (UX)](#user-experience--ux-)
  * [Site Owner Goals](#site-owner-goals)
  * [User Stories](#user-stories)
  * [User Requirements](#user-requirements)
  * [User Expectations](#user-expectations)
- [Design Choices](#design-choices)
  * [Fonts](#fonts)
  * [Colours](#colours)
  * [Icons](#icons)
  * [Wireframes](#wireframes)
  * [Data Schema](#data-schema)
- [Features](#features)
- [Features Yet To Implement](#features-yet-to-implement)
- [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Frameworks & Libraries](#frameworks---libraries)
  * [Tools](#tools)
- [Testing](#testing)
  * [Validator Testing](#validator-testing)
    + [HTML Validator](#html-validator)
    + [CSS Validator](#css-validator)
  + [Feature Testing](#feature-testing)
  * [Lighthouse Testing](#lighthouse-testing)
  * [Compatability Testing](#compatability-testing)
  * [Bugs](#bugs)
- [Deployment](#deployment)
  * [Run Locally](#run-locally)
  * [Deploying in Heroku](#deploying-in-heroku)
- [Credits](#credits)
  
- [Final Comments](#final-comments)

## User Experience (UX)

### Site Owner Goals
**As the site owner, I would like:**
* Access the admin section of the site
* To Create, Read, Update and Delete items in the database from a centralised location through the admin app
* Club members to be able to easily purchase Membership via the site
* To sell club merchandise through the site
* Customers to be able to rate and review the merchandise so I know the popular items
* Give the club a professional look and feel to attract new members
* To provide information to club members and the public about matches the club will be involved in

### User Stories
**As a user, I want to:**  
* the site navigation to be easy and very intuitive
* be able to register a profile on the site with all my details
* be able to log in and out easily
* be able to recover my password if I no longer remember it
* receive confirmation emails throughout the registration process
* be able to view my profile details and past orders
* be able to view all the products and memberships available to purchase
* be able to sort products by Category/Price/Rating
* be able to see a more detailed page about a particular product or membership
* be able to easily add products to my bag
* be able to view the items in my bag from anywhere in the site
* be able to adjust the quantity of products or memberships in my bag
* be able to checkout from the bag page
* be able to see all products from a specific category
* be able to easily enter my payment details
* be able to hava my delivery and payment details autofill in checkout once I have a profile
* recieve an order confirmation directly after checkout
* be able to review a product and leave a rating
* be able to Edit a review or rating
* be able to Delete a review or rating
* be able to search the site for products or membership types using keywords in the search bar

### User Requirements

### User Expectations

## Design Choices
### Fonts
For the fonts on the site, I used [Google Fonts](https://fonts.google.com/?standard-styles=). This is a really fantatic service of [Google](https://google.com) which is great for getting nearly any kind of font you want. The fonts I chose for my page are *Lato* & *Roboto* with *sans-serif* as a backup font in the event that [Google Fonts](https://fonts.google.com/?standard-styles=) does not work. The reason I decided to use *Lato* & *Roboto* is that I found them to be quite sleek fonts which would almost represent a pair of football boots. 

### Colours
I used [Coolors](https://coolors.co/) to assist in generating a colour scheme for the site. This is a great site as it gives you the codes of the colours you want in any form you want ie. Hex codes for my site. 
The colour scheme I have chosen for the site is White (#FFFFFF) and Maroon (#800000). The reasons for this choice is that they are the same colours as my own GAA club.

### Icons 
I have gone to [Font Awesome](https://fontawesome.com/) for the icons that I have used in the site. The icons, I feel just add a little bit extra to the site in terms of style and make it a bit more visually appealing which ultimately provides a better User Experience.

### Wireframes
When creating my wireframes, I first drew some rough sketches on paper but then decided that [Balsamiq](https://balsamiq.com/) would be the most suitable technology to use to assist with the design of the site.

You will see from the wireframes that a lot has changed since the planning stage of the project as I learned a lot about what direction I wanted the project to go as I went through the development process.

I created mock ups for my page to fit into the main device types - Desktop, Tablet and Mobile. The mock-ups for the devices can be found here: 
* [Mobile]()
* [Tablet]()
* [Desktop]()


### Data Schema
Django is compatible with SQL databases by default and so I used SQLite in development and then used a PostgresQL database in the deployed site which is provided by [Heroku](https://id.heroku.com/login). 

**User model**

Django provides, via django.contrib.auth.models, a ready to use User model which is what is being utilised in this project.

#### Profiles App
**Profile model**

| Name | Database Key | Field Type | Type Validation |
| :-------------: |:----------------:| :--------------: | :---------: |
|User | user |	OneToOneField 'User'| on_delete=models.CASCADE
|Membership | membership |	BooleanField | default=False, null=True, blank=True
|Default Phone Number |	default_phone_number | CharField | max_length=20, null=True, blank=True
|Default Country | default_country | CountryField | blank_label='country', null=True, blank=True
|Default Postcode | default_postcode | CharField | max_length=20, null=True, blank=True
|Default Town or City | default_town_or_city | CharField | max_length=40, null=True, blank=True
|Default Street Address1 | default_street_address1 | CharField | max_length=80, null=True, blank=True
|Default Street Address2 | default_street_address2 | CharField | max_length=80, null=True, blank=True

### Products App
**Category model**

| Name | Database Key | Field Type | Type Validation |
| :-------------: |:----------------:| :--------------: | :---------: |
|Name | name | CharField | max_length=254
|Friendly Name | friendly_name | CharField | max_length=254, null=True, blank=True

**Product model**

| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Product id | id | primary_key=True | AutoField
|Name | name | default='', max_length=254 | CharField
|SKU | sku | max_length=254, null=True, blank=True | CharField
|Description | content | blank=False | TextField
|Has Sizes | has_sizes | BooleanField | default=False, null=True, blank=True
|Price | price | max_digits=6, decimal_places=2 | DecimalField
|Image| image| blank=False | ImageField
|Rating | rating | blank=True | DecimalField

### Membership App
**Membership model**
| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Membership id | id | primary_key=True | AutoField
|Name | name | default='', max_length=254 | CharField
|SKU | sku | max_length=254, null=True, blank=True | CharField
|Description | content | blank=False | TextField
|Has Sizes | has_sizes | BooleanField | default=False, null=True, blank=True
|Price | price | max_digits=6, decimal_places=2 | DecimalField
|Image| image| blank=False | ImageField



**Category model**

| Name | Database Key | Field Type | Type Validation |
| :-------------: |:----------------:| :--------------: | :---------: |
|Name | name | CharField | max_length=254
|Friendly Name | friendly_name | CharField | max_length=254, null=True, blank=True



## Features

### Features Implemented
* User Authentication using Allauth. This allows login, logout, email verifation and other features.
* The club shop, givin the users the ability to browse and purchase club merchandise
* Product categorisation giving the users the ability to quickly search for certain types of products they are looking for 
* Membership area of the site, giving the users the ability to browse and purchase different membership types
* For each product and membership, there is a product or membership details page which outlines the details of that particular product or membership
* Search bar functionality, giving the users the ability to search the site for products & memberships by name or category
* 'Sort by' feature giving the users the ability to sort the products list by price, size, category, and other criteria
* Online payments feature made available via Stripe
* Matches page on the site that allows the users to keep up to date with the club's match activity
* Different sections on the matches page for each of the different age groups in the club so that users can search the matches for the team that is of interest to them
* Gallery of pictures of the club's facilities to entice non-member site users to join the club
* A contact form for site users to contact the club administrator and provide feedback, suggest improvements or just ake queries


### Features Yet To Implement
* Club news page where members can keep up to date with the different club activities such as fundraisers
* Club gym booking form to be able to book a slot that you can use the gym facility


## Technologies Used
### Languages
### Frameworks & Libraries
### Tools

## Testing

### User Story Testing

### Validator Testing 
#### HTML Validator
#### CSS Validator

### Feature Testing

### Lighthouse Testing

### Compatability Testing

### Bugs

## Deployment

Note: When deploying my project initially, I pushed my database url to Github. Luckily, I had no data in my database and it was easy for me to delete my postgres database and create a new one. This nuetralised any threat that there may have been to the app.

### Run Locally

### Deploying in Heroku

## Credits

## Final Comments
