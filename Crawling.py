from selenium import webdriver
import bs4
import time
import csv

driver = webdriver.Chrome(executable_path='./chromedriver')

driver.get("https://github.com/ksundong/backend-interview-question#%EC%96%B8%EC%96%B4-%EA%B4%80%EB%A0%A8")
time.sleep(1)
soup = bs4.BeautifulSoup(driver.page_source, 'lxml')
titles = soup.find_all('h3')
li = soup.find_all('details')
list = soup.find_all('summary')
list2 = soup.find_all('p')
    
fields = ['문제', '답안']    
rows = []

for item in li[0:]:
    rows.append(item.text.split('\n\n'))
    
with open('result.csv', 'w', newline='') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(rows)