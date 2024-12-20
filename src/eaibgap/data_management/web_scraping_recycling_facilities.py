"Task for web scraping recycling and composting facilities"

import os
import json
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Setup Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Optional: headless mode for faster performance
driver = webdriver.Chrome(options=options)

# Define paths and data folder
data_folder = "data"
os.makedirs(data_folder, exist_ok=True)
json_path = os.path.join(data_folder, "facilities.json")
csv_path = os.path.join(data_folder, "facilities.csv")

# Open the target URL
url = "https://sipsn.menlhk.go.id/sipsn/public/home/peta"
driver.get(url)

try:
    # Step 1: Select TPS3R category
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dd_fasilitas")))
    select_facility = driver.find_element(By.ID, "dd_fasilitas")
    select_facility.click()
    
    tps3r_option = driver.find_element(By.CSS_SELECTOR, "option[value='tps3r']")
    tps3r_option.click()

    # Step 2: Refresh the map
    refresh_button = driver.find_element(By.ID, "btn_refresh_peta")
    refresh_button.click()

    # Wait for the map to load
    time.sleep(5)

    # Step 3: Collect all markers on the map
    markers = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".gm-style .gm-marker"))
    )
    print(f"Found {len(markers)} markers for TPS3R.")

    facilities_data = []

    for i, marker in enumerate(markers):
        try:
            # Step 4: Click each marker
            ActionChains(driver).move_to_element(marker).click(marker).perform()

            # Step 5: Wait for the #fdata element to appear
            fdata_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "fdata"))
            )

            # Extract data from #tbl-fasilitas
            tbl_fasilitas = fdata_element.find_element(By.ID, "tbl-fasilitas")
            table_html = tbl_fasilitas.get_attribute("outerHTML")

            # Parse the HTML and extract relevant data
            rows = tbl_fasilitas.find_elements(By.TAG_NAME, "tr")
            facility_info = {}
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                if len(cells) == 2:
                    facility_info[cells[0].text.strip()] = cells[1].text.strip()
                elif len(cells) == 1:
                    key = cells[0].text.strip()
                    facility_info[key] = None  # If there's no value for the key

            facilities_data.append(facility_info)
            print(f"Collected data for marker {i + 1}: {facility_info}")

            # Close the popup if necessary
            close_button = driver.find_element(By.ID, "hide-grafik")
            if close_button.is_displayed():
                close_button.click()
        
        except Exception as e:
            print(f"Error collecting data for marker {i + 1}: {e}")

    # Step 6: Save data to JSON
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(facilities_data, json_file, ensure_ascii=False, indent=4)
    print(f"Data saved to {json_path}")

    # Step 7: Save data to CSV
    with open(csv_path, "w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["Jenis", "Alamat", "Latitude, Longitude"])
        writer.writeheader()
        for facility in facilities_data:
            writer.writerow(facility)
    print(f"Data saved to {csv_path}")

finally:
    driver.quit()
