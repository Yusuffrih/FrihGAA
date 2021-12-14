# Testing

## Validator Testing 
### HTML Validator

### CSS Validator
CSS Validator showed no errors.

## Lighthouse Testing
Lighthouse testing was carried out on all pages on both [desktop](testing/lighthouse/desktop) and [mobile](testing/lighthouse/mobile)

## Compatability & Responsiveness Testing
To test the compality of the site across different devices and screen sizes, I used the [dev tools](https://developer.chrome.com/docs/devtools/) that comes with [Google Chrome](https://www.google.com/chrome/?brand=FHFK&gclid=Cj0KCQiAnuGNBhCPARIsACbnLzqcMJxCHBH-BSjGpuwc1I8L4clEMk1vlfWm_VanpbS6tX1knC2AkNkaAgSkEALw_wcB&gclsrc=aw.ds). This is a really handy tool as it allows you to see what you site would look and act like on different screen sizes with the click of a button.

I was satisfied with the look and feel of the site across **all** devices that I tested this on. They were as follows:
* Moto G4
* Iphone 4
* Galaxy s5
* Pixel 2
* Pixel 2 XL
* Iphone 5/SE
* Iphone 6/7/8
* Iphone 6/7/8 plus
* Iphone X
* Ipad
* Ipad Pro
* Surface Duo

## User Story & Feature Testing
### Navbar
![navbar screenshot](testing/feature_testing/navbar.png)
<hr>

![navbar screenshot](testing/feature_testing/navbar-dropdown-menu.png)
<hr>

![navbar screenshot](testing/feature_testing/navbar-responsive-dropdown.png)
<hr>

The navbar links all work perfectly and all have the same hover and click state. When the navbar dropdown menu is displayed, all the links in this all work perfectly as well and all have the same font size, hover and click state as well. The user is able to navigate to all areas of the site. In particular, the user is able to navigate to the basket from the navbar and is also able to see the grand total cost of what they have placed into their basket which should make for a positive User Experience. 

Conclusion:
The site's navbar works as expected and is responsive on all screens as noted above. All the links look well and behave in the desired manner. All aspects of the site are navigable from the navbar which allows the user to quickly and easily find their way from feature to feature and this provides them with a positive user experience.

User story satisified: 
* Site navigation to be easy and very intuitive
* be able to view the items in my basket from anywhere in the site

### User Authentication - Allauth

There are various steps to users registering to the site:
1) The clicks the account icon in the navbar. They will see that they can either login or register.
![allauth account icon in navbar](testing/feature_testing/registration.png)

2) When they click to register, the will be directed to the registration page where they will be prompted to input their details including username, email address and password.
![allauth signup page](testing/feature_testing/sign-up.png)
3) The user will then be directed to a page with a message to let them know that they need to verify their email address.
![allauth email verification page](testing/feature_testing/email-verification.png)

4) An email is then sent to the user's given email address with a link to follow which will verify their email address when clicked. Once the user verifies their email, they will be automatically signed in and redirected to the homepage where they would have started out. 
![allauth confirmation email page](testing/feature_testing/confirm-email.png)

Conclusion:
The user authentication on the site works exactly as it's supposed to with a user being able to easily navigate to where they can login or sign up. Once they sign up, they are then sent an email with a link to follow in order to cofirm their own email address provided is actually theirs. This then completes the user authentication process and the user is automatically signed in. Read the profile testing to see how the user can update their details. If the user wants to delete their profile entirely, they can easily contact the site owners through the contact form and ask for this to be done.

User story satisified: 
* To be able to log in and out easily
* To be able to recover my password if I no longer remember it
* to receive confirmation emails throughout the registration process

### Club Shop
#### Display Products
![all products display page](testing/feature_testing/products-page.png)
As this feature suggests, this page is used to display all the products for sale on this site. The users can come here to view any products. When the site owner adds a product via the admin site or in the product management page, it will come up here on this page. The products are all displaying correctly on this page in the desired format with the desired details attached to them such as product categories, prices, names, images. When a product does not have an image attached to it, the product will have a placeholder image instead that signifies that there is no image attached to that product. 

Also, on each product, if the user signed in is a site owner, they will see the edit and delete buttons on each product. The edit button takes the user to the edit product form as seen below.
![edit product page](testing/feature_testing/edit-product.png)

When the site owner goes to delete the specific product that they want to delete, they are given a warning to make sure that they want to delete the item from the database. This warning is in the form of a modal and is when they click on the delete button again, only then is the product deleted.

conclusion:
To conclude this piece of testing, all the products are displaying in the products page exactly as they are supposed to be displaying, with all the details that are needed to make this a rich and enticing page for the user to have a positive experience while on the site.

User story satisfied:
* be able to view all the products available to purchase
* To be able to add, edit and delete delete products to and from the database

#### Search bar

The search bar that is positioned in the `base template` is available to the users across the entire site meaning that at any point, the user can type in a product's name or in the product description. Through testing this, from all pages on the site, the conclusion is that this feature is fully functional works as expexted.

Once the user has searched for a item through the search bar, it renders the products page with the relevant criteria being searched for. The number of products returned and the search criteria is also noted at the top of the list of items returned.
![search bar screenshot](testing/feature_testing/searchbar.png)

conclusion:
The conclusion from this piece of testing is that the search bar allows the user to search for products using the key words that target the name and description fields of the products.

User story satisfied:
* be able to search the site for products using keywords in the search bar

#### Sort Products



User story satisfied:
* be able to sort products by Category/Price/Name

### Product Details

User story satisfied:
* be able to see a more detailed page about a particular product
* be able to easily add products to my basket

### Shopping Basket

User story satisfied:
* be able to view the items in my basket from anywhere in the site
* be able to adjust the quantity of products in the basket, from the basket
* be able to checkout from the basket page


### Online Payments & Checkout

User story satisfied:
* be able to easily enter my payment details and make payments
* be able to hava my delivery and payment details autofill in checkout once I have a profile
* recieve an order confirmation email directly after checkout


### Profile

User story satisfied:
* To be able to register a profile on the site with all my details
* To be able to view my profile details and past orders

### Contact Form

User story satisfied:
* be able to contact the site owners easily through a contact form on the site
* receive an acknowledgement email to let me know my contact form has been submitted


### FAQs

User story satisfied:
* Be able to view a list of FAQs on the site to find out more information about the club

### Footer

User story satisfied:
* Be a able to view some basic details about the site owners in the site footer
* Be able to navigate to the site owners social media pages from links in the footer to be able to discover more about the club


## Bugs

1. 
**Issue:** When deploying to Heroku, I managed to push my postgres database url to Github. 

**Fix:** I luckily did not have any data in the database so I decided to delete the database and create a new one with a new url which fixed the threat to the security of the site.

2. 
**Issue:** I put the heroku app name into my Procfile instead of the django app name. This was causing a H14 Heroku error (No web services running).

**Fix:** I changed the app name to the name of the project level app in the django virtual environment instead of Heroku and this got rid of the error that was being thrown.

3. 
**Issue:**  I made a syntax error when wiring up the production database to the settings file - 'default': dj_database_url.parse('DATABASE_URL'). This was causing the live site to not be working correctly.

**Fix:** Changed the above mistake to: 
‘default': dj_database_url.parse(os.environ.get(’DATABASE_URL’)). Once this change was made, the live site was functioning correctly.

4. 
**Issue:** Stripe API Keys not working white the user would try and make a payment. There was an error message showing on screen for this.

**Fix:** The stripe public API key was not registering correctly. I could not figure this out for a long time and decided to try and change the API keys in Stripe and in my environment variable to try and fix the issue. This created another issue where the workspace was still picking up the expired API key. I had a to restart the workspace to register the new variable. In the end, the fix was simply that the context variable in the view was wrapped as a string rather than just being a variable.

5. 
**Issue:** On placing an order and making payment for the order, I would check the user profile and see that the order placed had been duplicated in the database. 

**Fix:** I spent ages looking for the cause of the issue, but in the end it was as simple as a typo in the checkout view’s original_basket variable. This caused the webhook in stripe to search for the incorrect viariable. When it couldn't find the order with this key attached to it, it would the create the order again.  

6. 
**Issue:** When I deployed to Heroku and more specifically when I had set up real emails to be sent from Django, sign-up and email verification process would break. 

**Fix:** For a long time, I did not understand where the issue was coming from. But after a lot of examination, I decided to try and turn off email verification for new users. This fixed the issue. As Email verification is not assessed in the MS4 I decided to leave email verification off. I later found out that this was an issue with Google and not with how I set it up. The email verification was working when in Development.

7. 
**Issue:** The above bug 6 did not actually fix the overall issue that was the real emails being sent to the users was not working. This bug had me stumped for a while and I couldn't understand why the emails were being sent in development but not in production.

**Fix:** Once I figured out that the issue was to do with the setup of the real emial being sent out, the fix was again, as simple as locating a typo in the Heroku environment variables. This was causing the code to not be able to locate the value for the email host password. 