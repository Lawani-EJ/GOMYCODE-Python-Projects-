import requests
import string
from bs4 import BeautifulSoup

Enter_input = input("Search: ")
u_i = string.capwords(Enter_input)  
lists = u_i.split()  
word = "_".join(lists)  


url = "https://en.wikipedia.org/wiki/" + word

def WikiBot(url):
    try:
        url_open = requests.get(url)
        soup = BeautifulSoup(url_open.content, 'html.parser')
        

        details = soup.find_all('table', {'class': 'infobox'})
        

        if details:
            for i in details:
                h = i.find_all('tr') 
                for j in h:
                    heading = j.find('th') 
                    detail = j.find('td') 
                    if heading is not None and detail is not None:
                        print("{} :: {}".format(heading.text.strip(), detail.text.strip()))
                        print("-------------------------")
        else:
            print("No infobox found for this entry.")

        paragraphs = soup.find_all('p')
        for i in range(1, 3):
            print(paragraphs[i].text.strip())
            print("-------------------------")

    except Exception as e:
        print(f"An error occurred: {e}")

WikiBot(url)
