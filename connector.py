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
    
    __headers_default = { 
            "Content-Type"                  : "application/json; charset=UTF-8",
            "Accept"                        : "application/json, text/plain, */*",
            "Accept-Encoding"               : "gzip, deflate, br",
            "Access-Control-Allow-Origin"   : "*",
            "Accept-Language"               : "de-DE,de;q=0.8,en-US;q=0.6,en;q=0.4",
            "Content-Encoding"              : "gzip",
            "Connection"                    : "keep-alive",            
    }

    def __init__(self,username,password,apiurl = 'https://manage.smartadserverapis.com/'):
        self.__username     = username
        self.__password     = password
        self.__api_url      = apiurl
        self.__headers      = self.__headers_default
    
    def get(self):
        return {
            "username"  : self.__username,
            "password"  : self.__password,
            "api_url"   : self.__api_url,
            "headers"   : self.__headers
        }

    def add_to_headers(self,headers):
        self.__headers.update(headers)
    
    
    def set_headers(self,headers):
        self.__headers = headers
    
    def reset_headers(self):
        self.__headers = self.__headers_default

class Advertiser():
            
    def __init__(self,connector,networkID):
        self.__connector    = connector
        self.__username     = connector.get()['username']
        self.__password     = connector.get()['password']
        self.__headers      = connector.get()['headers']
        self.__api_url      = connector.get()['api_url']
        self.__networkID    = networkID
        self.__type         = '/advertisers/'        
        self.__finalUrl     = self.__api_url+str(self.__networkID)+self.__type
    
    def set_network_id(self,networkID):
        self.__networkID = networkID
        self.__finalUrl  = self.__api_url+str(self.__networkID)+self.__type
    
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
            self.__finalUrl,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            params  = params
            )
        print("API URL: '"+r.url+"'")
        return r.json()
    
    '''
    id : Int32
        Id of the advertiser
    '''
    def get(self,id,subAction = ''):
        r = requests.get(
            self.__finalUrl+str(id)+'/'+subAction,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password)
            )
        print("API URL: '"+r.url+"'")
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
            self.__finalUrl,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = advertiser
            )
        print("API URL: '"+r.url+"'")
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
            self.__finalUrl+str(id)+'/'+subAction,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            )
        print("API URL: '"+r.url+"'")
        return r.json()
    '''
    same as create
    '''
    def update(self,advertiser):
        r = requests.put(
            self.__finalUrl,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = advertiser
            )
        print("API URL: '"+r.url+"'")
        return r.json()
    '''
    id
        id of the resource you want to delete
    '''
    def delete(self,id):
        r = requests.delete(
            self.__finalUrl+str(id),
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            )
        print("API URL: '"+r.url+"'")
        return r.json()

    '''
    id: Int32
        Id of the advertiser
    subAction: String
        Allowed sub-actions: * "domainLists" to remove the domain list of the advertiser from its targeting
    '''
    def delete_domain_blacklist(self,id,subAction):
        r = requests.delete(
            self.__finalUrl+str(id)+'/'+subAction,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            )
        print("API URL: '"+r.url+"'")
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
        self.__finalUrl     = self.__api_url+str(self.__networkID)+self.__type

    
    def set_network_id(self,networkID):
        self.__networkID = networkID
        self.__finalUrl  = self.__api_url+str(self.__networkID)+self.__type

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
    def get_all(self,params={}):
        r = requests.get(
            self.__finalUrl,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            params  = params
            )
        print("API URL: '"+r.url+"'")
        return r.json()

    '''
    id: int32
        id of the Agency
    '''
    def get(self,id,subAction = ''):
        r = requests.get(
            self.__finalUrl+str(id)+'/'+subAction,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password)
            )
        print("API URL: '"+r.url+"'")
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
            self.__finalUrl,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = agency
            )
        print("API URL: '"+r.url+"'")
        return r.json()
  
    ''' Updates a agency
    same as create
    '''
    def update(self,agency):
        r = requests.put(
            self.__finalUrl,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = agency
            )
        print "API URL: '"+r.url+"'"
        return r.json()

    ''' deletes an agency
    id: int32
    '''
    def delete(self,id):
        r = requests.delete(
            self.__finalUrl+str(id),
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            )
        print("API URL: '"+r.url+"'")
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
        self.__finalUrl     = self.__api_url+str(self.__networkID)+self.__type
        self.__state        = '/campaignstatus/'
    
    def set_network_id(self,networkID):
        self.__networkID = networkID
        self.__finalUrl  = self.__api_url+str(self.__networkID)+self.__type
    
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
                    self.__finalUrl,
                    headers = self.__headers,
                    auth    = HTTPBasicAuth(self.__username, self.__password),
                    params  = params
                    )
        print("API URL: '"+r.url+"'")
        return r.json()

    '''
    id: int32
        id of the Campaign
    '''
    def get(self,id,subAction = ''):
        r = requests.get(
            self.__finalUrl+str(id)+'/'+subAction,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password)
            )
        print("API URL: '"+r.url+"'")
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
            self.__finalUrl,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = campaign
            )
        print("API URL: '"+r.url+"'")
        return r.json()
    
    ''' updates a given campaign
    same as create
    '''
    def update(self,campaign):
        r = requests.put(
            self.__finalUrl,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = campaign
            )
        print("API URL: '"+r.url+"'")
        return r.json()

    ''' deletes a campaign with given id
    id: int32
    '''
    def delete(self,id):
        r = requests.delete(
            self.__finalUrl+str(id),
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            )
        print("API URL: '"+r.url+"'")
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
        print("API URL: '"+r.url+"'")
        return r.json()
    
    ''' Returns the campaign status with the given id
    id:int32
        The unique ID of the resource you want to retrieve
    '''
    def get_status(self,id):
        r = requests.get(
                    self.__api_url+str(self.__networkID)+self.__state+str(id),
                    headers = self.__headers,
                    auth    = HTTPBasicAuth(self.__username, self.__password),
                    )
        print("API URL: '"+r.url+"'")
        return r.json()

''' ====================================================== Class CreativeSize ======================================================

'''
class CreativeSize():
    
    def __init__(self,connector,networkID):
        self.__connector    = connector
        self.__username     = connector.get()['username']
        self.__password     = connector.get()['password']
        self.__headers      = connector.get()['headers']
        self.__api_url      = connector.get()['api_url']
        self.__networkID    = networkID
        self.__type         = '/creativesizes/'
        self.__finalUrl     = self.__api_url+str(self.__networkID)+self.__type
    
    def set_network_id(self,networkID):
        self.__networkID = networkID
        self.__finalUrl  = self.__api_url+str(self.__networkID)+self.__type
    
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
                    self.__finalUrl,
                    headers = self.__headers,
                    auth    = HTTPBasicAuth(self.__username, self.__password),
                    params  = params
                    )
        print("API URL: '"+r.url+"'")
        return r.json()

    '''
    id: int32
        id of the CreativeSize
    '''
    def get(self,id):
        r = requests.get(
            self.__finalUrl+str(id),
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password)
            )
        print("API URL: '"+r.url+"'")
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
            self.__finalUrl,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = size
            )
        print("API URL: '"+r.url+"'")
        return r.json()

''' ====================================================== Class CreativeType ======================================================

'''
class CreativeType():

    def __init__(self,connector,networkID):
        self.__connector    = connector
        self.__username     = connector.get()['username']
        self.__password     = connector.get()['password']
        self.__headers      = connector.get()['headers']
        self.__api_url      = connector.get()['api_url']
        self.__networkID    = networkID
        self.__type         = '/creativetypes/'
        self.__finalUrl     = self.__api_url+str(self.__networkID)+self.__type
    
    def set_network_id(self,networkID):
        self.__networkID = networkID
        self.__finalUrl  = self.__api_url+str(self.__networkID)+self.__type
    
    ''' Returns all the creatives sizes
    params: {
        ids IntList 
            Filters the results according to the given ids
    } 
    '''
    def get_all(self,params):
        r = requests.get(
                    self.__finalUrl,
                    headers = self.__headers,
                    auth    = HTTPBasicAuth(self.__username, self.__password),
                    params  = params
                    )
        print("API URL: '"+r.url+"'")
        return r.json()

    '''
    id: int32
        id of the CreativeType
    '''
    def get(self,id):
        r = requests.get(
            self.__finalUrl+str(id),
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password)
            )
        print("API URL: '"+r.url+"'")
        return r.json()

''' ====================================================== Class platforms ======================================================

'''

class Keyword:
    
    def __init__(self,connector,networkID):
        self.__connector    = connector
        self.__username     = connector.get()['username']
        self.__password     = connector.get()['password']
        self.__headers      = connector.get()['headers']
        self.__api_url      = connector.get()['api_url']
        self.__networkID    = networkID
        self.__type         = '/keywords/'
        self.__finalUrl     = self.__api_url+str(self.__networkID)+self.__type
    
    def set_network_id(self,networkID):
        self.__networkID = networkID
        self.__finalUrl  = self.__api_url+str(self.__networkID)+self.__type
    
    ''' Returns all the keywords
    params: {
        ids IntList 
            Filters the results according to the given ids
    } 
    '''
    def get_all(self,params):
        r = requests.get(
                    self.__finalUrl,
                    headers = self.__headers,
                    auth    = HTTPBasicAuth(self.__username, self.__password),
                    params  = params
                    )
        print("API URL: '"+r.url+"'")
        return r.json()

    '''
    id: int32
        id of the keyword
    '''
    def get(self,id):
        r = requests.get(
            self.__finalUrl+str(id),
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password)
            )
        print("API URL: '"+r.url+"'")
        return r.json()
    
    '''
    keyword : object : {
        id:
        name:
        applicationId:
        deliveryTargetingValue:
        keywordGroupId:
    }
    '''
    def create(self,keyword):
        r = requests.post(
            self.__finalUrl,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = keyword
            )
        print("API URL: '"+r.url+"'")
        return r.json()

''' ====================================================== Class Platform ======================================================

'''

class Platform:
    def __init__(self,connector,networkID):
        self.__connector    = connector
        self.__username     = connector.get()['username']
        self.__password     = connector.get()['password']
        self.__headers      = connector.get()['headers']
        self.__api_url      = connector.get()['api_url']
        self.__networkID    = networkID
        self.__type         = '/platforms/'
        self.__finalUrl     = self.__api_url+str(self.__networkID)+self.__type
    
    def set_network_id(self,networkID):
        self.__networkID = networkID
        self.__finalUrl  = self.__api_url+str(self.__networkID)+self.__type
    
    ''' Returns all the platforms
    params: {
        ids IntList 
            Filters the results according to the given ids
    } 
    '''
    def get_all(self,params={}):
        r = requests.get(
                    self.__finalUrl,
                    headers = self.__headers,
                    auth    = HTTPBasicAuth(self.__username, self.__password),
                    params  = params
                    )
        print("API URL: '"+r.url+"'")
        return r.json()

    '''
    id: int32
        id of the platform
    '''
    def get(self,id):
        r = requests.get(
            self.__finalUrl+str(id),
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password)
            )
        print("API URL: '"+r.url+"'")
        return r.json()

''' ====================================================== Class Page ======================================================

'''
class Site:
    def __init__(self,connector,networkID):
        self.__connector    = connector
        self.__username     = connector.get()['username']
        self.__password     = connector.get()['password']
        self.__headers      = connector.get()['headers']
        self.__api_url      = connector.get()['api_url']
        self.__networkID    = networkID
        self.__type         = '/sites/'
        self.__finalUrl     = self.__api_url+str(self.__networkID)+self.__type
    
    def set_network_id(self,networkID):
        self.__networkID = networkID
        self.__finalUrl  = self.__api_url+str(self.__networkID)+self.__type
    
    ''' Returns all the sites
    site: {    
         ids IntList 
            Filters the results according to the given ids
        name String 
            Filters the results according to their name
        externalId String 
            Filters the results according to their externalId
        isArchived OptionalBool 
            State if this item can be used (not deprecated neither removed neither...)
        formatIds IntList 
            If not null, returns only sites which have a page group supporting at least one of the provided formats
    }
    '''
    def get_all(self,site):
        r = requests.get(
                    self.__finalUrl,
                    headers = self.__headers,
                    auth    = HTTPBasicAuth(self.__username, self.__password),
                    params  = site
                    )
        print("API URL: '"+r.url+"'")
        return r.json()

    '''
    id: int32
        id of the Site
    '''
    def get(self,id):
        r = requests.get(
            self.__finalUrl+str(id),
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password)
            )
        print("API URL: '"+r.url+"'")
        return r.json()
    
    ''' Creates a new site
    site : {
        id  
            Site's unique ID
        externalId  
            External id, you can write what you want up to 50 characters
        name  
            Site's name declared in Smart
        userGroupId  
            Group's id of the user
        url  
            Site's url as declared in Smart
        languageId  
            Language's id of the site
        isArchived  
            False if this site can be used as parameter in other methods. True if deprecated / removed / deactivated... so archived
        updatedAt  
            Last modification date
        iABCategoryIds  
            List of IAB category ids accepted on this site

    }
    
    '''
    def create(self,site):
        r = requests.post(
            self.__finalUrl,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = site
            )
        print("API URL: '"+r.url+"'")
        return r.json()
    
    ''' updates a given site
    same as create
    '''
    def update(self,site):
        r = requests.put(
            self.__finalUrl,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = site
            )
        print("API URL: '"+r.url+"'")
        return r.json()

    ''' deletes a site with given id
    id: int32
    '''
    def delete(self,id):
        r = requests.delete(
            self.__finalUrl+str(id),
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            )
        print("API URL: '"+r.url+"'")
        return r.json()
   
''' ====================================================== Class Page ======================================================

'''
class Page:
    def __init__(self,connector,networkID):
        self.__connector    = connector
        self.__username     = connector.get()['username']
        self.__password     = connector.get()['password']
        self.__headers      = connector.get()['headers']
        self.__api_url      = connector.get()['api_url']
        self.__networkID    = networkID
        self.__type         = '/pages/'
        self.__finalUrl     = self.__api_url+str(self.__networkID)+self.__type
    
    def set_network_id(self,networkID):
        self.__networkID = networkID
        self.__finalUrl  = self.__api_url+str(self.__networkID)+self.__type
    
    ''' Returns all the pages
    page: {    
        ids IntList 
            If not null, returns only pages specified in this parameter.
        pageGroupIds IntList 
            If not null, returns only pages that belong to one of pageGroups specified in this parameter.
        name String 
            If not null, returns only pages having this parameter in their name.
        externalId String 
            If not null, returns only pages having this parameter in their externalId.
        isArchived OptionalBool 
            Allowed: false, or both.
    }
    '''
    def get_all(self,site):
        r = requests.get(
                    self.__finalUrl,
                    headers = self.__headers,
                    auth    = HTTPBasicAuth(self.__username, self.__password),
                    params  = site
                    )
        print("API URL: '"+r.url+"'")
        return r.json()

    '''
    id: int32
        id of the Page
    '''
    def get(self,id):
        r = requests.get(
            self.__finalUrl+str(id),
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password)
            )
        print("API URL: '"+r.url+"'")
        return r.json()
    
    ''' Creates a new page
    page : {
        id  
            Page's unique Id
        externalId  
            External id, you can write what you want up to 50 characters
        name  
            Page's name with parent pages            For example: "Page/SubPage/PageName"            If the page has no parent page: "PageName"
        fullName  
            Page's name with site and parent pages            For example: "Site/Page/SubPage/PageName"
        url  
            URL of the page
        pageGroupId  
            Page group's Id
        parentPageId  
            Parent page's Id
        isArchived  
            False if this page can be used as parameter in other methods. True if deprecated / removed / deactivated... so archived
        updatedAt  
            Last modification date

    }
    
    '''
    def create(self,site):
        r = requests.post(
            self.__finalUrl,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = site
            )
        print("API URL: '"+r.url+"'")
        return r.json()
    
    ''' updates a given page
    same as create
    '''
    def update(self,site):
        r = requests.put(
            self.__finalUrl,
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            data    = site
            )
        print("API URL: '"+r.url+"'")
        return r.json()

    ''' deletes a page with given id
    id: int32
    '''
    def delete(self,id):
        r = requests.delete(
            self.__finalUrl+str(id),
            headers = self.__headers,
            auth    = HTTPBasicAuth(self.__username, self.__password),
            )
        print("API URL: '"+r.url+"'")
        return r.json()

''' ====================================================== Class UserGroup ======================================================

'''

class UserGroup:
    def __init__(self,connector,networkID):
        self.__connector    = connector
        self.__username     = connector.get()['username']
        self.__password     = connector.get()['password']
        self.__headers      = connector.get()['headers']
        self.__api_url      = connector.get()['api_url']
        self.__networkID    = networkID
        self.__type         = '/usergroups/'
        self.__finalUrl     = self.__api_url+str(self.__networkID)+self.__type
    
    def set_network_id(self,networkID):
        self.__networkID = networkID
        self.__finalUrl  = self.__api_url+str(self.__networkID)+self.__type
    
    ''' Returns all the user groups of your network '''
    def get(self):
        r = requests.get(
                    self.__finalUrl,
                    headers = self.__headers,
                    auth    = HTTPBasicAuth(self.__username, self.__password),
                    )
        print("API URL: '"+r.url+"'")
        return r.json()


''' ====================================================== Class User ======================================================

'''
class User:
    def __init__(self,connector,networkID):
        self.__connector    = connector
        self.__username     = connector.get()['username']
        self.__password     = connector.get()['password']
        self.__headers      = connector.get()['headers']
        self.__api_url      = connector.get()['api_url']
        self.__networkID    = networkID
        self.__type         = '/users/'
        self.__finalUrl     = self.__api_url+str(self.__networkID)+self.__type
    
    def set_network_id(self,networkID):
        self.__networkID = networkID
        self.__finalUrl  = self.__api_url+str(self.__networkID)+self.__type
    
    ''' Returns all the user groups of your network '''
    def get(self,userIDs=''):
        r = requests.get(
                    self.__finalUrl,
                    headers = self.__headers,
                    auth    = HTTPBasicAuth(self.__username, self.__password),
                    params = userIDs
                    )
        print("API URL: '"+r.url+"'")
        return r.json()