''' 
    Odoo - Smart AdServer Connector
    Wenn einen neuen Auftrag im Odoo angelegt wird,
    soll der Connector den Auftrag automatisch in SmartAdServer einpflegen
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
        self.__type         = '/advertisers/'
    
    def set_networkID(self,networkID):
        self.__networkID = networkID
    
    '''
    userGroupIDs : intList
        Filters the results according to the given user group ids
    ids : intList
        Filters the results according to the given ids 
    name : String
        Filters the results according to the fact they contain the name you gave
    isArchived : OptionalBool
        State if this item can be used (not deprecated neither removed neither...)
    '''
    def get_all(self,params):
        r = requests.get(
            self.__api_url+str(self.__networkID)+self.__type,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            params  = params
            )
        print(r.url)
        return r.json()
    
    '''
    id : Int32
        Id of the advertiser
    '''
    def get(self,id,subAction = ''):
        r = requests.get(
            self.__api_url+str(self.__networkID)+self.__type+str(id)+'/'+subAction,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password)
            )
        print(r.url)
        return r.json()

    '''
    id: string
        id of advertiser                  
    name: string
        name of advertiser              
    description: string
        description of advertiser        
    isDirectAdvertiser: string
        isDirectAdvertiser of advertiser
    isHouseAds: string
        isHouseAds of advertiser        
    address: string
        address of advertiser            
    contactName: string
        contactName of advertiser        
    contactEmail: string
        contactEmail of advertiser        
    contactPhoneNumber: string
        contactPhoneNumber of advertiser
    isArchived: OptionalBool
        isArchived of advertiser        
    userGroupId: intList
        userGroupId of advertiser        
    agencyIds: intList
        agencyIds of advertiser            
    domainListId: string
        domainListId of advertiser        
    '''
    def create(self,params):
        r = requests.post(
            self.__api_url+str(self.__networkID)+self.__type,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = params
            )
        print(r.url)
        return r.json()
    
    '''
    id: Int32
        Id of the insertion
    subAction: String
        Allowed sub-actions: "domainLists" to add or replace the advertiser's domain list.
    file: FileAndIsBlacklist
        A generic model to wrap fileName, fileContent and isBlacklist
    '''
    def create_domain_blacklist(self,id,subAction):
        r = requests.post(
            self.__api_url+str(self.__networkID)+self.__type+str(id)+'/'+subAction,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            )
        print(r.url)
        return r.json()
    '''
    same as create
    '''
    def update(self,params):
        r = requests.put(
            self.__api_url+str(self.__networkID)+self.__type,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = params
            )
        print(r.url)
        return r.json()
    '''
    id
        id of the resource you want to delete
    '''
    def delete(self,id):
        r = requests.delete(
            self.__api_url+str(self.__networkID)+self.__type+str(id),
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            )
        print(r.url)
        return r.json()

    '''
    id: Int32
        Id of the advertiser
    subAction: String
        Allowed sub-actions: * "domainLists" to remove the domain list of the advertiser from its targeting
    '''
    def delete_domain_blacklist(self,id,subAction):
        r = requests.delete(
            self.__api_url+str(self.__networkID)+self.__type+str(id)+'/'+subAction,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            )
        print(r.url)
        return r.json()


'''
Class Agencies.
You can manage agencies by creating an instance of the class
'''
class Agencies():
    def __init__(self,connector,networkID):
        self.__connector    = connector
        self.__username     = connector.get()['username']
        self.__password     = connector.get()['password']
        self.__headers      = connector.get()['headers']
        self.__api_url      = connector.get()['api_url']
        self.__networkID    = networkID
        self.__type         = '/agencies/'
    
    def set_networkID(self,networkID):
        self.__networkID = networkID

    '''
    userGroupIDs: intList
        Filters the results according to the given user group ids
    ids: String
        Ids of a set of agencies to return
    name
        Filters the results according to the fact they contain the name you gave
    isArchived
        Allowed: False, or Both
    '''
    def get_all(self,params):
        r = requests.get(
            self.__api_url+str(self.__networkID)+self.__type,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            params  = params
            )
        print(r.url)
        return r.json()

    '''
    id: int32
        id of the Agency
    '''
    def get(self,id,subAction = ''):
        r = requests.get(
            self.__api_url+str(self.__networkID)+self.__type+str(id)+'/'+subAction,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password)
            )
        print(r.url)
        return r.json()
    
    
    ''' Creates a new agency
    id: int32    
        Agency's Id
    name:
        Agency's name
    address
        Agency's address
    description
        Agency's description
    contactName
        Agency's contact name
    contactEmail
        Agency's contact email
    contactPhoneNumber
        Agency's contact phone number
    isArchived
        False if this agency can be used as parameter in other methods. True if deprecated / removed / deactivated... so archived

    '''
    def create(self,params):
        r = requests.post(
            self.__api_url+str(self.__networkID)+self.__type,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = params
            )
        print(r.url)
        return r.json()
  
    ''' Updates a agency
    same as create
    '''
    def update(self,params):
        r = requests.put(
            self.__api_url+str(self.__networkID)+self.__type,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = params
            )
        print(r.url)
        return r.json()

    def delete(self,id):
        r = requests.delete(
            self.__api_url+str(self.__networkID)+self.__type+str(id),
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            )
        print(r.url)
        return r.json()

    def delete_domain_blacklist(self,id,subAction):
        r = requests.delete(
            self.__api_url+str(self.__networkID)+self.__type+str(id)+'/'+subAction,
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