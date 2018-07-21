# Routes
- [x] Have login page display the login form
- [x] Have login page route to the sign up form
- [x] Have logout route redirect to the login page
- [x] Redirect to the login page if not logged in, otherwise redirect to the index page
- [ ] Have login page display over secure HTTP
- [x] Route to reset password form on login page
- [x] Redirect to settings page with a dropdown menu via navigation bar
- [ ] Ensure that settings/user prefs only works if logged in

# Views
- [x] Get sidebar to show up on all pages
- [x] Set up basic dashboard at index page
- [ ] Implement fancy bootstrap password reset link
- [ ] Attach user preferences page to the user's name
- [x] Get all links working on index page such that they all switch between tabs
- [x] Get a modal working
- [x] Populate password entries as a grid in the dashboard view and make entries clickable w/ modal
- [x] Populate credit card entries as a grid in the dashboard view and make entries clickable w/ modal
- [x] Populate notes/files entries as a grid in the dashboard view and make entries clickable w/ modal
- [ ] Create and implement working password item popup modal
- [ ] Create and implement working credit card item popup modal (with bootstrapped credit card form)
- [ ] Create and implement working file and note uploading modals
- [ ] Get the trusted users view and table working
- [ ] Get the search form working
- [ ] Get a filterer / organizer button module working on each tab
- [ ] Get the Starred view to filter out non-starred records
- [ ] Get the Flagged view to filter out non-flagged records
- [ ] Get the Identification view to filter out non-Identification-themed notes

# Forms
- [ ] Implement CSRF protection in all forms
- [x] Add working 'verify password' option to registration form
- [x] Make working login form
- [ ] Make login and register forms work with config's password limit size
- [x] Make working registration form
- [x] Make a form for adding records
- [x] Make a form for editing records
- [x] Make a form for uploading files
- [x] Make a search form
- [ ] Set up custom validators with existing forms
- [ ] Have the share-based forms actually send messages via email

# Models
- [x] Remove password from User model, replace with password hash
- [x] Add a model for user preferences
- [ ] Add description and notes max length from config to Record models
- [x] Finish SiteRecord model
- [x] Finish WalletRecord model
- [ ] Finish Device model
- [x] Make a model for encrypted documents
- [ ] After making password generation utility, add it to user model
- [x] Finish the encrypted file model
- [x] Determine all intended note types and their fields
- [x] Finish NoteRecord model
- [ ] Implement blank note
- [x] Add a Tag model
- [x] Add a Flag model
- [x] Make Record mixin
- [x] Finish TrustedUser model
- [ ] Finish Service model for websites
- [ ] Add a Vault model (only if its useful) and then implement a KeySet class for the vault
- [ ] Create caches for each of these models

# Managers
- [x] Make a basic user manager template
- [ ] Make a basic record manager template
- [ ] Put in a tag manager somewhere (?)

# Security
- [ ] Implement Argon for salting
- [ ] Set up SSL
- [ ] Add middleware?
- [ ] Add a password hint
- [x] Enable encryption and decryption of documents
- [ ] Add IP whitelisting?

# Templates
- [x] Fill out the login template
- [x] Fill out the signup template
- [x] Fill out navigation bar
- [x] Fill out the layout/base template
- [x] Fill out the error templates
- [x] Fill out the form template
- [x] Fill out the basic settings template
- [ ] Fill out the advanced settings template
- [x] Fill out the user preferences template
- [ ] Fill out the about page template
- [ ] Fill out the help page template
- [ ] Add tags to the dashboard
- [ ] Fill out the search template in the macros folder and add it to index.html
- [ ] Give base.html a facelift that is consistent with the app's layout

# Static
- [x] Fill out index CSS
- [x] Fill out tabs CSS
- [ ] Fill out search CSS
- [ ] Fill out modals CSS
- [ ] Fill out auth/base CSS
- [ ] Change names of CSS tags on index page to be more relevant

# Utilities
- [ ] Add template filters
- [ ] Add password generation utility
- [x] Add password strength indicator utility
- [x] Add permissions
- [x] Add fake notes
- [ ] Add fake files
- [ ] Add fake tags to test the tagging functionality

# Mail
- [ ] Make throwaway email account to test email functionality
- [ ] Set up async tasking with Celery
- [x] Set up password reset functionality
- [ ] Use Celery to send registration email and password reset emails

# Database
- [x] Implement migration in initialization of app
- [x] Add some fake user data
- [x] Add some fake records data
- [ ] Add all database relationships

# CLI
- [x] Load database with flask shell
- [x] Load user model with flask shell
- [ ] Get 'add record' command to work with proper responses
- [ ] Get manual 'add record' functionality to work with the database

# Configuration
- [x] Order the configuration options by groups
- [ ] Ensure the instance folder exists
- [ ] If not testing, don't load instance config
- [ ] Set up MAIL_FROM_EMAIL to fit throwaway email address used for testing
- [ ] Replace BaseConfig with app_config
- [ ] Generate Vault token
- [ ] Update last seen for User upon app initialization

# File Structure
- [ ] Add proper CLI folder
- [x] Move extensions to a features folder
- [x] Add logging functionality to a features folder
- [ ] Figure out where to add exceptions (and add them)!
- [ ] List out all the flags somewhere
- [x] Put all modals into proper folder
- [x] Put all tabs into proper subfolder in the app folder
- [x] Reorganize templates folder s.t. app holds tabs/ and modals/ and add in index
- [x] Put settings/ folder as a subfolder in app/tabs and implement in index
- [x] Add add/ and view/ subfolders to app/modals folder, create appropriate modals, and add in index

# Functionality
- [ ] Add ability to star/favorite a record
- [ ] Implement search functionality
- [ ] Implement tagging
- [ ] Add ability to share records/notes

# Extensions
- [ ] Consider using Flask-User
- [ ] Consider using Flask-Security
- [ ] Implement Flask-CORS

# Testing / Logging
- [x] Get Flask debug toolbar working
- [ ] Set up Redis caching
- [ ] Add signals script
- [ ] Log invites, user actions, etc.
- [x] Add log file for non-debug mode
- [ ] Set up email error catching for non-debug mode

# Future Features
- Import / export / backup info
- Tagging --> working on
- Password generator --> working on
- Filtering and sorting
- Share passwords --> working on
- Demand security question if not updated in a while
- Multifactor authentication
- Emergency access settings/trusted users --> working on
- Functionality for detecting / removing expired credit cards
- Pyperclip (for copying)
- Equiv. domains for websites on entries
- Sync with external apps (social media, phone, etc.)
- Internationalization with Babel
- Mobile support
- Trusted devices
- Secure notes --> working on
- Encrypted documents --> working on
- Autofill and autosave functionality
- Custom fields
- Support for importing from multiple password managers
- Password alerts in settings
- Clear clipboard after a certain time
- Automatic vault locking after certain amount of time inactive