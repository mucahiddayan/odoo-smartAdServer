from connector import Connector,Agency,Advertiser,Campaign 

# ====================================================== MAIN ======================================================

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