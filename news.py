from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')
news = 'https://news.google.com/?hl=zh-TW&gl=TW&ceid=TW:zh-Hant'
driver.get(news)
art = driver.find_element_by_css_selector('article')
#標題
news_title = art.find_element_by_css_selector('h3').text
#來源
news_from = art.find_element_by_class_name('SVJrMe').find_element_by_css_selector('a').text
#時間
news_time = art.find_element_by_class_name('SVJrMe').find_element_by_css_selector('time').get_attribute('datetime')
#網址
news_url = art.find_element_by_css_selector('h3').find_element_by_css_selector('a').get_attribute('href')
print(news_title)
print(news_from)
print(news_time)
print(news_url)
driver.quit()