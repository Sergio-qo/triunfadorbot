from selenium import webdriver

#WebDriver path
browser = webdriver.Chrome('E:/Sistema/Downloads/chromedriver')

browser.get('http://triunfador.net')

#C1 is the box which select all the lower line
def getC1():
    try:
        return browser.find_element_by_name('c1')
    except:
        return "error"

#It stops until you log in
c1 = getC1()
while c1 == "error":
    c1 = getC1()

#Then this part is going to be the automation
c1.click()