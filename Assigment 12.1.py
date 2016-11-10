from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

base_url = "https://scrapebook22.appspot.com"

response = urlopen(base_url).read()

soup = BeautifulSoup(response)

email_seznam = []
seznam_mest =[]
seznam_imen = []

for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = base_url + link["href"]
        person_html =urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html)
        email = person_soup.find("span", attrs={"class": "email"})
        city = person_soup.find("span", attrs={"data-city": True})
        name_surname = person_soup.find("div", attrs={"class": "col-md-8"}).h1

        email_seznam.append(str(email.string))#tu dodamo v seznam
        seznam_mest.append(str(city.string))
        seznam_imen.append(str(name_surname.string))


csv_file = open("data_scraper.csv", "w")
csv_file.write(str(email_seznam) + ", " + "\n")
csv_file.write(str(seznam_mest) + ", " + "\n")
csv_file.write(str(seznam_imen) + ", " + "\n")


csv_file.close()





