from selenium import webdriver

url = r"https://classroom.google.com/u/1/a/not-turned-in/all"
path = r"C:\browserdriver\msedgedriver.exe"

driver = webdriver.Edge(path)

driver.get(url)