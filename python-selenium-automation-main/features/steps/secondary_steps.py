from behave import given, when, then
from pages_for_secondary import LoginPage, Sidebar, SecondaryPage

BASE_URL = "https://soft.reelly.io"
USERNAME = "dwebb8210@gmail.com"   # change to yours
PASSWORD = "AWDFlylikeag6@"   # change to yours


@given("I open the site")
def open_site(ctx):
    ctx.login = LoginPage(ctx.driver, ctx.wait)
    ctx.login.open(BASE_URL)

@when("I log in")
def do_login(ctx):
    ctx.login.login(USERNAME, PASSWORD)
    ctx.login.wait_until_logged_in()

@when("I open the Secondary page")
def open_secondary(ctx):
    ctx.sidebar = Sidebar(ctx.driver, ctx.wait)
    ctx.sidebar.click_secondary()
    ctx.secondary = SecondaryPage(ctx.driver, ctx.wait)
    ctx.secondary.assert_loaded()

@when("I go to the final page")
def last_page(ctx):
    ctx.secondary.go_last()

@then("I go back to the first page")
def first_page(ctx):
    ctx.secondary.go_first()


