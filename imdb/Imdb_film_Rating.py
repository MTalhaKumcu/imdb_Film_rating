import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"
response = requests.get(url)

html = response.content

soup = BeautifulSoup(html,"html.parser")

a =float(input("enter Star:"))

heads = soup.find_all("td",{"class":"titleColumn"})
rating = soup.find_all("td",{"class":"ratingColumn imdbRating"})

for head, rating in zip(heads,rating):
    head = head.text
    rating = rating.text

    head = head.strip()
    head = head.replace("\n", "")

    ratng = rating.split()
    ratng = rating.replace("\n", "")

    if (float(rating) > a):
        print("Film name:{} Film star:{}".format(head,rating))
