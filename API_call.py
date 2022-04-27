import json
import requests
#this is a function with whole working
def somthing():
    try:
        url = "the API url"
        user= "username"
        pwd= "password"
        global snow_getresponse_json
        myrequst= requests.get(url,auth=(user,pwd))
        snow_getresponse_json = json.loads(myrequst.content)
        print(type(snow_getresponse_json))
        response_result_list = snow_getresponse_json["result"]
        return response_result_list
    except:
        print("Something went wrong")
        
a= somthing()
print(a)
print('this is a demo.')
#print(a[0]["variables.pg_itsm_other"])


        
