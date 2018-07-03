# Routes
- [x] Have login page display the login form
- [x] Have login page route to the sign up form
- [ ] Have logout route redirect to the login page
- [x] Redirect to the login page if not logged in, otherwise redirect to the index page
- [ ] Have login page display over secure HTTP
- [x] Route to reset password form on login page
- [x] Redirect to settings page with a dropdown menu via navigation bar

# Views
- [ ] Get sidebar to show up on all pages
- [ ] Set up basic dashboard at index page
- [x] Add settings page (basic)
- [x] Add settings page (advanced)
- [x] Add user preferences page
- [ ] Add an about page to the navigation bar

# Forms
- [ ] Implement CSRF protection in all forms
- [x] Add working 'verify password' option to registration form
- [x] Make working login form
- [ ] Make login and register forms work with config's password limit size
- [x] Make working registration form
- [ ] Get the forms to work with BaseForm

# Models
- [x] Remove password from User model, replace with password hash
- [ ] Update User database relationships
- [ ] Add getters and setters to User model
- [ ] Add a model for user preferences
- [ ] Add description and notes max length from config to Record model
- [ ] Finish Record model
- [ ] Finish Device model
- [ ] Make a model for encrypted documents
- [ ] After making password generation utility, add it to user model

# API
- [x] Make a basic user handler template
- [ ] Make a basic record handler template

# Security
- [ ] Implement Argon for salting
- [ ] Set up SSL
- [ ] Add middleware
- [ ] Add a security question
- [ ] Enable encryption and decryption of documents

# Templates
- [x] Fill out the login template
- [x] Fill out the signup template
- [x] Fill out navigation bar
- [ ] Fill out the header and footer templates
- [ ] Fill out the layout template
- [x] Fill out the error templates
- [ ] Fill out the form template
- [ ] Fill out the basic settings template
- [ ] Fill out the advanced settings template
- [ ] Fill out the user preferences template
- [ ] Fill out the about page template

# Static
- [ ] Fill out CSS
- [ ] Get AngularJS running with Flask backend
- [ ] Get Flask-Assets working for assets

# Utilities
- [ ] Add template filters
- [ ] Add password generation utility

# Mail
- [ ] Make throwaway email account to test email functionality
- [ ] Set up async tasking with Celery
- [x] Set up password reset functionality

# Database
- [x] Implement migration in initialization of app
- [ ] Add some fake user data
- [ ] Add some fake records data

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

# Functionality
- [ ] Add ability to star/favorite a record

# Testing / Logging
- [x] Get Flask debug toolbar working
- [ ] Set up Redis caching
- [ ] Log invites, user actions, etc.
- [ ] Add log file for non-debug mode
- [ ] Set up email error catching for non-debug mode

# Future Features
- Import / export / backup info
- Tagging
- Password generator
- Filtering and sorting
- Folders
- Share passwords
- Demand security question if not updated in a while
- Multifactor authentication
- Emergency access settings
- Functionality for detecting / removing expired credit cards
- Pyperclip (for copying)
- Equiv. domains for websites on entries
- Sync with external apps (social media, phone, etc.)
- Internationalization with Babel
- Mobile support
- Secure notes
- Encrypted documents
- Autofill and autosave functionality
- Custom fields
- Support for multiple password managers