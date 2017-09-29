require_relative 'helper.rb'

include Helper

# Initialize object for browser
b = Watir::Browser.new :chrome
# Maximize window
b.driver.manage.window.maximize
# Navigate to the target URL
b.goto('https://www.hackerearth.com/')

#################### EXECUTION ########################

# Login into app
@top_header.link(text: 'Login').click
ogin_into_app(method: 'Google')
# Replace 'sample' with original email and password
_login_via_google(email: 'sample', password: 'sample')

nav_bar = b.header(class: 'header new-layout-header')
# Click the caret icon
nav_bar.div(class: 'caret-icon').fire_event('click')
# Click the setting link
b.ul(class: 'no-margin').link(text: 'Settings').fire_event('click')
#######################################################
