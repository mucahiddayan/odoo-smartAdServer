''' 
    Odoo - Smart AdServer Connector
    Wenn einen neuen Auftrag im Odoo angelegt wird,
    soll der Connector den Auftrag automatisch im SmartAdServer erstellen
'''

''' 
r = requests.post(URL, data = {'key':'value'})
r = requests.put('http://httpbin.org/put', data = {'key':'value'})
r = requests.delete(URL)
r = requests.head(URL)
r = requests.options(URL)

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)

'''

import requests
from requests.auth import HTTPBasicAuth
import json

class Connector():
    
    def __init__(self,username,password):
        self.__username     = username
        self.__password     = password
        self.__api_url      = 'https://manage.smartadserverapis.com/'
        self.__headers      = { "Content-Type": "application/json; charset=utf-8" }
    
    def get(self):
        return {
            "username"  : self.__username,
            "password"  : self.__password,
            "api_url"   : self.__api_url,
            "headers"   : self.__headers
        }
    
    def set_headers(headers):
        self.__headers = headers

class Advertiser():
            
    def __init__(self,connector,networkID):
        self.__connector    = connector
        self.__username     = connector.get()['username']
        self.__password     = connector.get()['password']
        self.__headers      = connector.get()['headers']
        self.__api_url      = connector.get()['api_url']
        self.__networkID    = networkID
    
    def set_networkID(self,networkID):
        self.__networkID = networkID

    def get_all(self,params):
        r = requests.get(
            self.__api_url+str(self.__networkID)+'/advertisers',
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            params  = params
            )
        print(r.url)
        return r.json()

    def get(self,advertiserID):
        r = requests.get(
            self.__api_url+str(self.__networkID)+'/advertisers/'+str(advertiserID),
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password)
            )
        print(r.url)
        return r.json()

    def create(self,params):
        r = requests.post(
            self.__api_url+str(self.__networkID)+'/advertisers/',
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = params
            )
        print(r.url)
        return r.json()
    
    def create_domain_blacklist(self,advertiserID,subAction):
        r = requests.post(
            self.__api_url+str(self.__networkID)+'/advertisers/'+str(advertiserID)+'/'+subAction,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            )
        print(r.url)
        return r.json()

    def update(self,params):
        r = requests.put(
            self.__api_url+str(self.__networkID)+'/advertisers/',
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = params
            )
        print(r.url)
        return r.json()

    def delete(self,advertiserID):
        r = requests.delete(
            self.__api_url+str(self.__networkID)+'/advertisers/'+str(advertiserID),
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            )
        print(r.url)
        return r.json()

    def delete_domain_blacklist(self,advertiserID,subAction):
        r = requests.delete(
            self.__api_url+str(self.__networkID)+'/advertisers/'+str(advertiserID)+'/'+subAction,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            )
        print(r.url)
        return r.json()

connector = {
    "username" : 'root',
    "password" : 12323,    
}

create_update_advertiser = {
    "id"                : 21,
    "name"              : 'name',
    "description"       : "desc",
    "isDirectAdvertiser": "true",
    "isHouseAds"        : "true",
    "address"           : "address",
    "contactName"       : "contactName",
    "contactEmail"      : "contactEmail",
    "contactPhoneNumber": "contactPhoneNumber",
    "isArchived"        : "true",
    "userGroupId"       : 22,
    "agencyIds"         : 23,
    "domainListId"      : 24,
    }

get_advertisers = {
    "userGroupIDs"      : 30,
    "ids"               : "31,32,33",
    "name"              : "Name",
    "isArchived"        : "false"
}

my_connector = Connector(**connector);
my_advertiser= Advertiser(my_connector,1563);

print my_advertiser.get_all(get_advertisers)['message']
print my_advertiser.get(2)['message']
print my_advertiser.create(create_update_advertiser)['message']
print my_advertiser.update(create_update_advertiser)['message']
print my_advertiser.create_domain_blacklist(1,"domainList")['message']
print my_advertiser.delete(1)['message']
print my_advertiser.delete_domain_blacklist(1,"domainList")['message']