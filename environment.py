from selenium import webdriver

def before_scenario(context, scenario):
	context.browser = webdriver.Chrome()

def after_scenario(context, scenario):
	context.browser.quit()

