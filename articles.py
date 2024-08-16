import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

BASE_URL = "https://sea.mashable.com"

def get_articles():
    home_page = requests.get(BASE_URL)
    soup = BeautifulSoup(home_page.content, "html.parser")
    nav_links = soup.find("nav").find(id="topmenu").find_all("a")
    
    article_collections = {}

    for nav_link in nav_links:
        url = BASE_URL + nav_link["href"]

        current_page = requests.get(url)
        soup = BeautifulSoup(current_page.content, "html.parser")
        articleContainers = soup.find_all(id="new")

        current_articles = []
        for container in articleContainers:
            article_els = container.find_all("li")
            for article_el in article_els:
                article_name = article_el.find("div", class_="caption").text
                article_link = article_el.find("a")["href"]
                article_date = article_el.find("time").text
                current_articles.append({
                    "title": article_name,
                    "url": article_link,
                    "date": article_date
                })
        article_collections[nav_link.text] = current_articles
    
    return article_collections

def write_articles_to_file(articleCollections):
    with open("test.txt", "w") as f:
        for category, articles in articleCollections.items():
            f.write(category)
            f.write("\n")
            for article in articles:
                f.write(article["title"] + ": " + article["url"] + "\n")
            f.write("\n")

# driver = webdriver.Chrome()
# for url in urls:
#     driver.get(url)
    
    # load_btn = driver.find_element_by_id("showmore")

    # page_num = 1
    # try:
    #     while load_btn.is_displayed():
    #         article_pages = driver.find_elements_by_id("wn")
    #         last_page = article_pages[-1]
    #         last_article = last_page.find_elements_by_class_name("blogroll")[-1]
    #         last_article_date = last_article.find_element_by_tag("time").text
    #         last_article_date.strip()
    #         last_article_year = int(last_article_date[-4:-1])

    #         if (last_article_year < 2022):
    #             break

    #         load_btn.click()
    #         time.sleep(3)
    #         page_num += 1
    # except:
    #     pass