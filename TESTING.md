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

## User Story Testing
* the site navigation to be easy and very intuitive
The site navbar
* be able to register a profile on the site with all my details
* be able to log in and out easily
* be able to recover my password if I no longer remember it
* receive confirmation emails throughout the registration process
* be able to view my profile details and past orders
* be able to view all the products available to purchase
* be able to sort products by Category/Price/Name
* be able to see a more detailed page about a particular product
* be able to easily add products to my basket
* be able to view the items in my basket from anywhere in the site
* be able to adjust the quantity of products in the basket, from the basket
* be able to checkout from the basket page
* be able to easily enter my payment details and make payments
* be able to hava my delivery and payment details autofill in checkout once I have a profile
* recieve an order confirmation email directly after checkout
* be able to search the site for products or membership types using keywords in the search bar
* be able to contact the site owners easily through a contact form on the site
* receive an acknowledgement email to let me know my contact form has been submitted
* be able to view a list of FAQs on the site to find out more information about the club

## Feature Testing


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