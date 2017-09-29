require_relative 'helper.rb'

include Helper

# Initialize object for browser
b = Watir::Browser.new :chrome
# Maximize window
b.driver.manage.window.maximize
# Navigate to the target URL
b.goto('https://www.hackerearth.com/')

#################### EXECUTION ########################

# Execte different types of login
@top_header.link(text: 'Login').click
_login_into_app(method: 'Facebook')
_login_via_facebook(email: 'sample', password: 'sample')
# It will throw error since credentials are not valid
# close that window
b.window(title: /Facebook/).close
_login_into_app(method: 'Google')
_login_via_google(email: 'sample', password: 'sample')
# Same here close this window too
b.window(title: /Google Accounts/).close

# Execute different types of signup
@top_header.link(text: 'Sign up').click
_login_into_app(method: 'Facebook')
_login_via_facebook(email: 'sample', password: 'sample')
# It will throw error since credentials are not valid
# close that window
b.window(title: /Facebook/).close
_login_into_app(method: 'Google')
_login_via_google(email: 'sample', password: 'sample')
# Same here close this window too
b.window(title: /Google Accounts/).close

# Execute normal login
_formal_login(username: 'Sample User', password: 'Sample password')
#######################################################
