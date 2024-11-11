from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Set up the WebDriver (make sure the path to ChromeDriver is correct)
service = Service('C:\\Users\\VivoBook\\OneDrive\\Desktop\\rename\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')  # Update this with the actual path

# Create a WebDriver instance using the Service object
driver = webdriver.Chrome(service=service)

# Open the URL
driver.get('https://collegedunia.com/btech/private-colleges')

# Allow time for the page to load dynamically
time.sleep(5)

# Find all the college names (using the class from the original request)
college_elements = driver.find_elements(By.XPATH, "//h3[@class='jsx-3230181281 font-weight-medium text-lg mb-0']")

# Extract text from each element
colleges = [college.text for college in college_elements]

# Create a DataFrame with Serial No and College Name
df = pd.DataFrame(colleges, columns=['College Name'])
df['Serial No'] = df.index + 1

# Reorder columns: Serial No first
df = df[['Serial No', 'College Name']]

# Save to CSV
df.to_csv('colleges_list.csv', index=False)

print("Data saved to 'colleges_list.csv'")

# Close the WebDriver
driver.quit()
