import requests
from bs4 import BeautifulSoup
import re
import csv

csv_file_path = "MathCourseOfferings.csv"
url = 'https://www.math.ucla.edu/ugrad/tentschedule-lower' #change to upper or pic if needed

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'lxml')

view_groupings = soup.find_all('div', class_='view-grouping')

# Write course data to CSV file
with open(csv_file_path, 'a', newline='') as csvfile:
    fieldnames = ["Course_ID", "Quarters_Offered"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Loop through each 'view-grouping' element and navigate to 'view-grouping-content'
    for view_grouping in view_groupings:
        # Navigate to 'view-grouping-content' within each 'view-grouping'
        view_grouping_content = view_grouping.find('div', class_='view-grouping-content')

        # Extract the course title 
        course_title = view_grouping.find('div', class_='view-grouping-header').get_text(strip=True)
        if course_title:
            hyphen_index = course_title.find('-')
            if hyphen_index!=-1:
                course_digits = course_title[5:hyphen_index].strip() #change to 4 for pic
            else:
                None
            course_id = "PIC " + course_digits
            #change to PIC for pic

        quarters_offered = []
        # Loop through 'views-table' elements within 'view-grouping-content'
        tables = view_grouping_content.find_all('table', class_='views-table')
        for table in tables:
            # Extract the caption text (e.g., "23F" or "24S")
            caption_text = table.find('caption').get_text(strip=True)

            # Loop through 'views-field' elements within 'views-table'
            views_fields = table.find_all('td', class_='views-field')
            for views_field in views_fields:
                # Extract the text within 'views-field'
                views_field_text = views_field.get_text(strip=True)
                if not views_field_text.startswith("Cancelled"):
                    if (caption_text[2]=='F'):
                        caption_text = "Fall"
                    elif (caption_text[2]=='W'):
                        caption_text = "Winter"
                    elif (caption_text[2]=='S'):
                        caption_text = "Spring"
                        
            if caption_text=="Fall" or caption_text=="Winter" or caption_text=="Spring" :
                quarters_offered.append(caption_text)
                continue
            
        # # Print the results
        # print("Course ID:", course_id)
        # print("Quarters Offered:", quarters_offered)
        # print("")

        # Write course data for the current course
        writer.writerow({"Course_ID": course_id, "Quarters_Offered": quarters_offered})

