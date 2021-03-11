from selenium import webdriver
import time
import pandas as pd
import urllib

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')

chromedriver = 'C:\driver\chromedriver.exe'

driver = webdriver.Chrome(chromedriver, options=options)

keywords = input().split()

encoded = "?"
for i,keyword in enumerate(keywords) :
        encoded += "keywords="+urllib.parse.quote(keyword) + "&"

# 로켓펀치 채용 공고 JPA, 신입
driver.get('https://www.rocketpunch.com/jobs'+encoded+'page=1')


print(driver.title)
print('현재 URL : ',driver.current_url)

class Job :
    name = 'job name'
    stat = 'job stat info'
    date = 'job date'
    link = 'job link'
    def __init__(self,name,stat,date,link):
        self.name = name
        self.stat = stat
        self.date = date
        self.link = link
    def __str__(self):
        return "name : {}, stat : {}, date : {}, link : {}".format(self.name,self.stat,self.date,self.link)

class Company :
    name = "company name"
    logo = "company logo"
    link = "company link"
    detail = "company detail"
    jobs = []
    def __init__(self,name,logo,link,detail,jobs):
        self.name = name
        self.logo = logo
        self.link = link
        self.detail = detail
        self.jobs = jobs
    def __str__(self):

        jobStr = "["
        for job in self.jobs :
            jobStr += "{"
            jobStr += job.__str__()
            jobStr += "}"
        jobStr += "]"
        return "name : {}, logo : {}, link : {}, detail : {}, jobs : {}".format(self.name,self.logo,self.link,self.detail,jobStr)

driver.implicitly_wait(time_to_wait=5)

pageList = driver.find_elements_by_css_selector(".pagination.menu .computer.large.screen a.item")

str = str(pageList[len(pageList)-1].get_attribute("data-query-add"))

strs = str.split('=')

total = int(strs[1])

# 회사 리스트
clist = []

# 채용 공고 개수
count = 0

for i in range(1,total) :

    driver.implicitly_wait(time_to_wait=3)

    print("====================================현재 ",i,"번째 페이지를 작업중입니다.====================================")

    driver.get('https://www.rocketpunch.com/jobs'+encoded+'page=' + i.__str__())

    items = driver.find_elements_by_css_selector('.company.item')

    for item in items :
        logo = item.find_element_by_css_selector('.ui.logo').find_element_by_tag_name('img').get_attribute('src')
        title = item.find_element_by_class_name('company-name').find_element_by_tag_name('strong').text
        companyLink = item.find_element_by_class_name('company-name').find_element_by_tag_name('a').get_attribute('href')
        companyDetail = item.find_element_by_class_name('description').text
        jobs = []
        jlist = item.find_elements_by_class_name('company-jobs-detail')
        for job in jlist :
            count += 1
            jobs.append(Job(job.find_element_by_class_name('job-title').text,
                            job.find_element_by_class_name('job-stat-info').text,
                            job.find_element_by_class_name('job-dates').text,
                            job.find_element_by_class_name('job-title').get_attribute('href')))
        clist.append(Company(title,logo,companyLink,companyDetail,jobs))


print('총 회사 개수 : ',len(clist))
print('총 채용 공고 개수 : ', count)

for c in clist :
    print(c)


driver.quit()