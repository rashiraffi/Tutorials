import requests
import json
response = requests.get("https://coronacache.home-assistant.io/corona.json")
result = response.json()
country = result["features"]
#print(country[0]["attributes"]["Country_Region"])
class countryDetails:
    def __init__(self,item):
        self.item=item
    def searchCountry(self,country):
        for x in self.item:
            if(country.lower()==x["attributes"]["Country_Region"].lower()):
                r=x["attributes"]
                print("\nCountry: "+r["Country_Region"]+"\nConfirmed: "+str(r["Confirmed"])+"\nDeaths: "+str(r["Deaths"])+"\nRecovered :"+str(r["Recovered"])+"\nActive :"+str(r["Active"]))
    def allCountries(self):
        resldict={}
        for x in self.item:
            resldict[x["attributes"]["Country_Region"]]=x["attributes"]["Confirmed"]
        return(resldict)
ctry=countryDetails(country)

while(True):
    print("\n\n1.Search by Country\n2.Active case of all countries\n9.Exit")
    ch=int(input("Enter any option: "))
    if(ch==1):
        ctry.searchCountry(input("Enter the country: "))
    elif(ch==2):
        rests=ctry.allCountries()
        for x in rests.keys():
            print(x,":",rests[x])
    elif(ch==9):
        break
    else:
        print("Invalid Input...!")