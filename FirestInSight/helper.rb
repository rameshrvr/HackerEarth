require 'watir'
# Helper module for all execution
module Helper
  # Initialize objects for sections containers
  @home_page = b.div(class: 'responsive-page homepage')
  @top_header = @home_page.header(class: 'navbar-header header-top')
  @login_popup = b.div(id: 'login-modal')
  # container object for new window (Facebook)
  @facebook_page = b.div(id: 'booklet')
  # container object for new window (Google)
  @google_page = b.div(id: 'view_container')
  # After login container
  @container = b.div(id: 'general-settings')

  # Method to login by formal way
  def _formal_login(
      username:,
      password:
  )
    @login_popup.text_field(id: 'id_login').set(username)
    @login_popup.text_field(id: 'id_password').set(password)
    @login_popup.button(type: 'submit').click
  end

  # Method to login/signup using specific option
  #
  # @param method [String] Mostly 'Facebook'/'Google'
  def _login_into_app(
      method:
  )
    @top_header.link(text: 'Login').fire_event('click')
    @login_popup.link(title: method).fire_event('click')
  end

  # Method to login via facebook
  def _login_via_facebook(
      email:,
      password:
  )
    b.window(title: /Facebook/).use do
      @facebook_page.text_field(id: 'email').set(email)
      @facebook_page.text_field(id: 'pass').set(password)
      @facebook_page.button(name: 'login').fire_event('click')
    end
  end

  # Method to login via google
  def _login_via_google(
      email:,
      password:
  )
    b.window(title: /Google Accounts/).use do
      @google_page.text_field(type: 'email').set(email)
      @google_page.span(text: 'Next').click
      @google_page.text_field(type: 'password').set(password)
      @google_page.span(text: 'Next').click
    end
  end

  # Method to fille form after login
  def _fill_form_after_login(**args)
    @container.text_field(id: 'id_dob').set(args[:dob])
    @container.select_list(id: 'id_locale').select(args[:locale])
    @container.select_list(id: 'id_timezone').select(1)
    @container.select_list(id: 'id_country').select(args[:country])
    @container.select_list(id: 'id_gender').select(args[:gender])
    @container.select_list(id: 'id_marital_status').select(args[:status])
  end
end
