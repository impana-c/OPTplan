from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import csv

csv_file_path = "MathPrereqs.csv"


driver = webdriver.Chrome()
driver.get('https://registrar.ucla.edu/academics/course-descriptions?search=Mathematics')

# Wait for the 'body-content' element to be present
body_content_element = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'body-content'))
)
# Wait for the 'Loading course browser...' message to disappear
WebDriverWait(driver, 30).until_not(
    EC.text_to_be_present_in_element((By.CLASS_NAME, 'body-content'), 'Loading course browser...')
)

html_content = driver.page_source

soup = BeautifulSoup(html_content, 'lxml')
courses = soup.select('.body-content .course-record')

with open(csv_file_path, 'a', newline='') as csvfile:
    fieldnames = ["Course_ID", "Course_Name", "Units", "Prerequisites"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for course in courses:
        course_title_element = course.find('h3')
        course_title = course_title_element.get_text(strip=True)
        if course_title:
            dot_index = course_title.find('.')
            if dot_index!=-1:
                course_digits = course_title[:dot_index].strip() 
                if (int((re.search(r'\d+', course_digits)).group()) >= 200):
                    break
            else:
                None
            course_id = "MATH " + course_digits
            course_name = course_title[dot_index+2:]

        course_units_string = course.find('p', string=re.compile(r'Units:')).text.strip()[7:]
        course_units = []
        course_units.append(float(course_units_string[:3]))
        if (len(course_units_string)>3):
            course_units.append(float(course_units_string[7:]))

        requisites_paragraph = course.find_all('p')[1]
        requisites_sentence = requisites_paragraph.find(text=re.compile(r'requisite', flags=re.IGNORECASE))
        if requisites_sentence:
            matches = re.findall(r'requisites?[^.]*\s*:\s*([^\.]+)\.', requisites_sentence, flags=re.IGNORECASE)
            if matches:
                requisites_list = [item.strip() for item in matches[0].split(',')]

        print(course_id)
        print(course_name)
        print(course_units)
        print("Requisites List:", requisites_list)
        print("")

        writer.writerow({"Course_ID": course_id, "Course_Name": course_name, "Units": course_units, "Prerequisites": requisites_list})

driver.quit()
