from behave import *
import time
from nose import tools as assertion
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import ipdb


@given('the page "{url}" is loaded')
def load_page(context, url):
	context.browser.get(url)
	time.sleep(3) 

@when('I type "{text}" in "{input_id}" input')
def fill_username(context, text, input_id):
	input_field = context.browser.find_element_by_xpath(
		'//input[@id="{input_id_xp}"]'.format(input_id_xp=input_id))
	input_field.send_keys(text)
	time.sleep(3)

@when('I click "{button_id}" button')
def click_button(context, button_id):
	btn = context.browser.find_element_by_xpath(
		'//button[@id="{button_id}"]'.format(button_id=button_id))
	btn.click()
	time.sleep(3)

@then('the home page is displayed')
def home_page(context):
	context.browser.find_element_by_xpath(
		'//table[@id="customers"]')

@when('I select "{value}" from "{select_id}" select')
def select_car(context, value, select_id):
	sel = context.browser.find_element_by_xpath(
'//select[@id="{select_id}"]/option[text()="{value}"]'.format(
			select_id=select_id, value=value)
	)
	sel.click()

@when('I click Zapisz')
def zapisz(context):
	zapisz_button = context.browser.find_element_by_xpath(
		'//button[text()="Zapisz"]'
	)
	zapisz_button.click()
	WebDriverWait(context.browser, 5).until(
		EC.presence_of_element_located((By.XPATH, '//table[@id="customers"]')))

@then('in column "{column}" are values "{values}"')
def column_values(context, column, values):
	expected_values = [value.strip() for value in values.split(',')]
	element_on_page = context.browser.find_element_by_xpath(
	'//table[@id="customers"]//td[@class="{column}"]'.format(column=column))
		value_on_page = element_on_page.text
		assertions.assert_equals(values, value_on_page)
		ipdb.set_trace()


@then('there is a car: brand "{brand}", model "{model}", year "{year}"')
def car_model(context, brand, model, year):
	context.browser.find_element_by_xpath(
		'//table[@id="customers"]'
		'//tr[td[@class="brand"][text()="{brand}"]]'
		'[td[@class="model"][text()="{model}"]]'
		'[td[@class="year"][text()="{year}"]]'.format(
		  brand=brand, model=model, year=year)
	)
	
@when('I clear all data')
def clear_data(context):
	while True:
		try:
			context.browser.find_element_by_xpath('//a[contains(text(),"Usuń")]').click()
		except NoSuchElementException:
			break

@then('the table is empty')
def empty_table(context):
	try:
		context.browser.find_element_by_xpath('//a[contains(text(), "Usuń")]')
	except NoSuchElementException:
		pass
	else:
		raise Exception('Table is not empty.')	





