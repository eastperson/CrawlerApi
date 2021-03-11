from flask_restful import Resource
from flask_restful import reqparse
from flask import Flask
from selenium import webdriver
from flask import jsonify
import json
from json import JSONEncoder

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

class JobEncoder(JSONEncoder) :
    def default(self, o) :
        return o.__dict__

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

class CompanyEncoder(JSONEncoder) :
    def default(self, o) :
        return o.__dict__

object = {'name' : 'kim', 'age' : 9}
job = Job('이름','스탯','데이트','링크')
company = Company("name","logo","link","detail",[job])
clist = [company,company,company]
rs_json = json.dumps(object)

companyJSONData = json.dumps(company,indent=4, cls=CompanyEncoder)
company_json = json.loads(companyJSONData)

companyListJSONData = json.dumps(clist,indent=4, cls=CompanyEncoder)
companyList_json = json.loads(companyListJSONData)

print("result company : ", company_json)
print("result company list : ",companyList_json)
print(json.dumps({'companyCnt' : len(clist), 'compnayList' : companyList_json},ensure_ascii=False))