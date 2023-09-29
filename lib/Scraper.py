from bs4 import BeautifulSoup
import requests
from Course import Course 
import json
import ipdb

class Scraper:
    def __init__(self):
        self.courses = []

    def get_page(self):
        try:
            response = requests.get("http://learn-co-curriculum.github.io/site-for-scraping/courses")
            response.raise_for_status()  # Raise an exception for any HTTP error
            doc = BeautifulSoup(response.text, 'html.parser')

            for course in doc.select('.post'):
                title = course.select("h2")[0].text if course.select("h2") else ''
                date = course.select(".date")[0].text if course.select(".date") else ''
                description = course.select("p")[0].text  if course.select("p") else ''

                new_course = Course(title, date, description)
                self.courses.append(new_course)

        except requests.exceptions.RequestException as e:
            print("Error making an HTTP request:", e)
        except (IndexError, AttributeError) as e:
            print("Error extracting data from the web page:", e)

    def print_courses(self):
        for course in self.courses:
            print(course)

scraper_instance = Scraper()

scraper_instance.get_page()

scraper_instance.print_courses()
ipdb.set_trace()