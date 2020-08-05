from selenium import webdriver

driver =  webdriver.Chrome()
driver.get('https://youtube.com')
driver.maximize_window()

searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
driver.implicitly_wait(10)
searchbox.send_keys('Nora Fatehi')

searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchbutton.click()

videoplayer = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[5]/div[1]/div/div[1]/div/h3/a');
videoplayer.click()

# fullscreen = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[30]/div[2]/div[3]/button[9]')
# driver.implicitly_wait(10)
# fullscreen.click()



driver.implicitly_wait(10)
url = driver.current_url
print(url)