from bs4 import BeautifulSoup
import requests
import re
import csv

csv_file_path = "CSCourseOfferings.csv"
response = requests.get('https://www.seasoasa.ucla.edu/cs-tentative-offerings/')
soup = BeautifulSoup(response.content, 'lxml')

# Use a regular expression to find div elements with the specified class pattern
pattern = re.compile(r"et_pb_with_border et_pb_row et_pb_row_\d+")
courses = soup.find_all("div", class_=pattern)

# Write course data to CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ["Course_ID", "Quarters_Offered"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    for course in courses:
        # Extract Course ID
        course_title_element = course.select_one(".et_pb_column_1_2 .et_pb_module.et_pb_text p strong")
        course_title = course_title_element.get_text(strip=True) if course_title_element else None
        if course_title:
            digits_match = re.search(r'\d+', course_title)
            if digits_match:
                course_digits = digits_match.group() 
                end_index = digits_match.end()
                if course_title[end_index]!=" ":
                    course_digits = course_title[:end_index+1]
            else:
                None
            course_id = "COM SCI " + course_digits
        # Extract Quarters Offered
        quarters_elements = course.select(".et_pb_column_1_6 .et_pb_module.et_pb_text p")
        quarters_offered = []
        for element in quarters_elements:
            element_text = element.get_text(strip=True)
            if (element_text[:4]=="Fall"): 
                element_text="Fall"
            elif (element_text[:6]=="Winter"): 
                element_text="Winter"
            elif (element_text[:6]=="Spring"): 
                element_text="Spring"
            quarters_offered.append(element_text)

        # # Print the results
        # print("Course ID:", course_id)
        # print("Quarters Offered:", quarters_offered)
        # print("")

        # Write course data for the current course
        writer.writerow({"Course_ID": course_id, "Quarters_Offered": quarters_offered})

