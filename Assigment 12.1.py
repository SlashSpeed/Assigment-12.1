from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

base_url = "https://scrapebook22.appspot.com"

response = urlopen(base_url).read()

soup = BeautifulSoup(response)

email_seznam = []#ko smo izvozili emaile jih dodamo v seznam z append
seznam_mest =[]
seznam_imen = []

for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = base_url + link["href"]
        person_html =urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html)
        email = person_soup.find("span", attrs={"class": "email"})
        city = person_soup.find("span", attrs={"data-city": True})

        #print (email.string)
        email_seznam.append(str(email.string))#tu dodamo v seznam
        seznam_mest.append(str(city.string))

print (email_seznam)
print (seznam_mest)



#shranitev datoteke v txt datoteke(ali bilokatero vrsto)
"""in_file = open("emails.txt", "w")"""
with open("emails", "w") as in_file: #s tem ukazom lahko ukinemo zgornjo vrstico in spodnjo in_file.close, ker avtomatsko zapre datoteko
    for email in email_seznam:                      #kar sem dal v trojni narekovaj lahko ukines s tem ukazom zgoraj
         in_file.write(email + "; "  + "\n")

"""in_file.close()#ne pozabi te funkcije za zaprtje programa"""

