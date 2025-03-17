from selenium import webdriver
import selenium
brower = webdriver.Chrome()
brower.get('http://localhost:8000')

assert 'Django' in brower.page_source
