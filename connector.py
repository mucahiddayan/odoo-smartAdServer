#!/usr/bin/env python
''' connector.py: Description of what connector does.

    Odoo - Smart AdServer Connector
    Automatische Auftragsverwaltung fuer Smart AdServer ueber Odoo

requests module beispiele
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


__author__      = "Muecahid Dayan"
__copyright__   = "Copyright 2017"
__version__     = "1.0.0"
__maintainer__  = "Muecahid Dayan"
__email__       = "mucahid@dayan.one"
__status__      = "Development"

class Connector():
    
    def __init__(self,username,password,apiurl = 'https://manage.smartadserverapis.com/'):
        self.__username     = username
        self.__password     = password
        self.__api_url      = apiurl
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
    def get_all(self,params={}):
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
    advertiser: {    
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
     }      
    '''
    def create(self,advertiser):
        r = requests.post(
            self.__api_url+str(self.__networkID)+self.__type,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = advertiser
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
    def update(self,advertiser):
        r = requests.put(
            self.__api_url+str(self.__networkID)+self.__type,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = advertiser
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
====================================================== Class Agencies ======================================================
You can manage agencies by creating an instance of the class
'''
class Agency():
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
    agency: {
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
    }
    '''
    def create(self,agency):
        r = requests.post(
            self.__api_url+str(self.__networkID)+self.__type,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = agency
            )
        print(r.url)
        return r.json()
  
    ''' Updates a agency
    same as create
    '''
    def update(self,agency):
        r = requests.put(
            self.__api_url+str(self.__networkID)+self.__type,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = agency
            )
        print(r.url)
        return r.json()

    ''' deletes an agency
    id: int32
    '''
    def delete(self,id):
        r = requests.delete(
            self.__api_url+str(self.__networkID)+self.__type+str(id),
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            )
        print(r.url)
        return r.json()
    

''' ====================================================== Class Campaign ======================================================

'''
class Campaign():

    def __init__(self,connector,networkID):
        self.__connector    = connector
        self.__username     = connector.get()['username']
        self.__password     = connector.get()['password']
        self.__headers      = connector.get()['headers']
        self.__api_url      = connector.get()['api_url']
        self.__networkID    = networkID
        self.__type         = '/campaigns/'
        self.__state        = '/campaignstatus/'
    
    def set_networkID(self,networkID):
        self.__networkID = networkID
    
    ''' Returns all the campaigns
    campaign: {    
        ids: IntList
            Filters the results according to the given ids
        name: String
            Filters the results according to the fact they contain the name you gave
        advertiserIds: IntList
            Filters the results according to the given advertiser ids
        agencyIds: IntList
            Filters the results according to the given agency ids
        campaignStatusIds: IntList
            Filters the results according to their campaign status (see "campaignStatus" resource)
        isArchived: OptionalBool
            Allowed: False, or Both
    }
    '''
    def get_all(self,campaign):
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
        id of the Campaign
    '''
    def get(self,id,subAction = ''):
        r = requests.get(
            self.__api_url+str(self.__networkID)+self.__type+str(id)+'/'+subAction,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password)
            )
        print(r.url)
        return r.json()
    
    ''' Creates a new campaign
    campaign : {
        id  
            Campaign Id
        name  
            Campaign Name
        advertiserId  
            Advertiser Id
        agencyId  
            Id of the agency linked to the campaign (optional).
        campaignStatusId  
            Id of the campaign status
        startDate  
            Campaign start date
        endDate  
            Campaign end date
        globalCapping  
            Set the default global capping configuration for next created insertion
        visitCapping  
            Set the default capping per visit configuration for next created insertion
        isArchived  
            False if you can update the campaign, true otherwise
    }
    
    '''
    def create(self,campaign):
        r = requests.post(
            self.__api_url+str(self.__networkID)+self.__type,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = campaign
            )
        print(r.url)
        return r.json()
    
    ''' updates a given agency
    same as create
    '''
    def update(self,campaign):
        r = requests.put(
            self.__api_url+str(self.__networkID)+self.__type,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = campaign
            )
        print(r.url)
        return r.json()

    ''' deletes an agency
    id: int32
    '''
    def delete(self,id):
        r = requests.delete(
            self.__api_url+str(self.__networkID)+self.__type+str(id),
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            )
        print(r.url)
        return r.json()
    
    ''' Returns all the campaign status
    ids: intList
        Filters the results according to the given ids
    '''
    def get_statuses(self,ids=""):
        r = requests.get(
                    self.__api_url+str(self.__networkID)+self.__state,
                    headers = self.__headers,
                    auth    = HTTPBasicAuth(self.__username, self.__password),
                    params  = ids
                    )
        print(r.url)
        return r.json()
    
    ''' Returns the campaign status with the given id
    id:int32
        The unique ID of the resource you want to retrieve
    '''
    def get_status(self,id):
        r = requests.get(
                    self.__api_url+str(self.__networkID)+self.__state+'/'+str(id),
                    headers = self.__headers,
                    auth    = HTTPBasicAuth(self.__username, self.__password),
                    )
        print(r.url)
        return r.json()

''' ====================================================== Class CreativeSize ======================================================

'''
class CreativeSize():
    
    def __init__(self,connector):
        self.__connector    = connector
        self.__username     = connector.get()['username']
        self.__password     = connector.get()['password']
        self.__headers      = connector.get()['headers']
        self.__api_url      = connector.get()['api_url']
        self.__networkID    = networkID
        self.__type         = '/creativesizes/'
    
    def set_networkID(self,networkID):
        self.__networkID = networkID
    
    ''' Returns all the creatives sizes
    params: {
        ids: IntList 
            Filters the results according to the given ids
        width: Int32 
            Filters the results according to the given width
        height: Int32 
            Filters the results according to the given height
    } 
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
        id of the CreativeSize
    '''
    def get(self,id):
        r = requests.get(
            self.__api_url+str(self.__networkID)+self.__type+str(id),
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password)
            )
        print(r.url)
        return r.json()
    
    ''' Creates a new CreativeSize
    size : {
        id  
            Size's id
        width  
            Size's width (in pixels)
        height  
            Size's height (in pixels)
    }
    
    '''
    def create(self,size):
        r = requests.post(
            self.__api_url+str(self.__networkID)+self.__type,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = size
            )
        print(r.url)
        return r.json()

''' ====================================================== Class CreativeType ======================================================

'''
class CreativeType():

    def __init__(self,connector):
        self.__connector    = connector
        self.__username     = connector.get()['username']
        self.__password     = connector.get()['password']
        self.__headers      = connector.get()['headers']
        self.__api_url      = connector.get()['api_url']
        self.__networkID    = networkID
        self.__type         = '/creativetypes/'
    
    def set_networkID(self,networkID):
        self.__networkID = networkID
    
    ''' Returns all the creatives sizes
    params: {
        ids IntList 
            Filters the results according to the given ids
    } 
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
        id of the CreativeType
    '''
    def get(self,id):
        r = requests.get(
            self.__api_url+str(self.__networkID)+self.__type+str(id),
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password)
            )
        print(r.url)
        return r.json()
    
''' ====================================================== Class CustomFormats ======================================================

'''