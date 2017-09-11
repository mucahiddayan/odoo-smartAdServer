from connector import Connector,Agency,Advertiser,Campaign 
import config

# ====================================================== MAIN ======================================================

connector = {
    "username" : config.USERNAME,
    "password" : config.PASSWORD,    
    "apiurl"   : config.API_URL
}

new_advertiser = {
    "id"                : 1,
    "name"              : 'name',
    "description"       : "desc",
    "isDirectAdvertiser": "True",
    "isHouseAds"        : "True",
    "address"           : "address",
    "contactName"       : "contactName",
    "contactEmail"      : "contactEmail",
    "contactPhoneNumber": "contactPhoneNumber",
    "isArchived"        : "True",
    "userGroupId"       : 2,
    "agencyIds"         : [1],
    "domainListId"      : 1,
    }

new_campaign = {
    "id"                : 1,
    "name"              : "Test Campaign",
    "advertiserId"      : 2,
    "campaignStatusId"  : 1,
    "startDate"         : 1,
}

new_agency = {
    "id"                : 1000006778,
    "name"              : "Test Agency",
    "address"           : "Koepenickerstr. 178-179",
    "description"       : "Test Agency to test API Access",
    "concactName"       : "Dayan",
    "contactEmail"      : "it@pmedia.de",
    "contactPhoneNumber": 33,
    "isArchived"        : 'False'
}

get_advertisers = {
    "userGroupIDs"      : 2,
    #"ids"               : "31,32,33",
    "name"              : "Name",
    "isArchived"        : "false"
}

my_connector = Connector(**connector);
my_advertiser= Advertiser(my_connector,config.NETWORK_ID);
my_campaign  = Campaign(my_connector,config.NETWORK_ID)


#camStat = my_campaign.get_status(2)["name"]
#print camStat
#print type(camStat)
#print my_campaign.get_statuses({"ids":"1,2"})
#print my_campaign.get_statuses()
#print my_campaign.get_status(2)
#print my_agency.create(new_agency)
# my_connector.set_headers({
#     "cache-control":"no-cache",
#     "content-type":"text/plain; charset=utf-8",
#     "expires":"-1",
#     "pragma":"no-cache"
# })

my_agency    = Agency(my_connector,config.NETWORK_ID)
print my_agency.update(new_agency)
#print my_agency.get_all()