# Routes
- [x] Have login page display the login form
- [x] Have login page route to the sign up form
- [ ] Have logout page redirect to the login page
- [x] Redirect to the login page if not logged in, otherwise redirect to the index page
- [ ] Have login page display over secure HTTP

# Views

# Forms
- [ ] Implement CSRF protection in all forms
- [x] Add working 'verify password' option to registration form
- [x] Make working login form
- [ ] Make login and register forms work with config's password limit size
- [x] Make working registration form
- [ ] Get the forms to work with BaseForm

# Models
- [ ] Remove password from User model, replace with password hash
- [ ] Update User database relationships
- [ ] Add a model for user preferences
- [ ] Finish Record model
- [ ] Finish Device model

# API
- [x] Make a basic user manager template
- [ ] Make a basic record manager template

# Security
- [ ] Implement Argon for salting
- [ ] Set up SSL

# Templates
- [ ] Fill out the login template
- [ ] Fill out the signup template
- [x] Fill out navigation bar
- [ ] Fill out the header and footer templates
- [ ] Fill out the layout template
- [ ] Fill out the error templates
- [ ] Fill out the form template
- [ ] Put the navigation bar on the bottom of the page
- [ ] Create a settings page and add it to the navigation bar
- [ ] Create an about page and add it to the navigation bar
- [ ] Create and add a sidebar for viewing the entries

# Static
- [ ] Fill out CSS
- [ ] Get Flask-Assets working for assets

# Utilities
- [ ] Add template filters

# Mail
- [ ] Set up async tasking with Celery

# Database
- [ ] Update database schema
- [ ] Implement migration in initialization of app

# CLI
- [x] Load database with flask shell
- [x] Load user model with flask shell

# Configuration
- [x] Order the configuration options by groups
- [ ] Ensure the instance folder exists
- [ ] If not testing, don't load instance config

# Testing / Logging
- [ ] Get Flask debug toolbar working
- [ ] Set up Redis caching
- [ ] Log invites, user actions, etc.

# Future Features
- Import / export / backup info
- Demand security question if not updated in a while
- Multifactor authentication
- Emergency access settings
- Functionality for detecting / removing expired credit cards
- Pyperclip (for copying)
- Equiv. domains for websites on entries