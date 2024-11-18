from bs4 import BeautifulSoup
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')

movie_webpage = response.text

soup = BeautifulSoup(movie_webpage, 'html.parser')


List = soup.select(selector="h3.title")

movies = [item.getText() for item in List ]
movies.reverse()
print(movies)

with open('movies.txt', 'w') as mfile:
    for movie in movies:
        mfile.write(f"{movie}\n")


# article_text = item_css.getText()
# article_link = item_css.get("href")
# print(article_text)
# print(article_link)
# upvote = soup.find_all( class_='score')
# print(upvote.getText())






















# if html parser fails, this one should work
import lxml


# with open ("website.html") as file:
#     contents = file.read()
#
# #Object requires parameters
# # contents of the document you are trying to scrape, type of parser you want to use
# soup = BeautifulSoup(contents,'html.parser')
# ## these will get a hold of one of a type of tag
# # print(soup.title)
# # print(soup.a.string)
# # will find all of the tags with specified name
# all_tags = soup.find_all(name='h3')
# for tag in all_tags:
#     print(tag.getText())
#
# # lets you get more specific with how you want to find items in your html, lettting you search by tag type, class and id
# item = soup.find(name='', id='', class_='')
#
# # can also narrow down based on css selectors..select one will give us first matching item and select will give all
# item = soup.select_one(selector="tag, tag1 tag2, #id, .class")


