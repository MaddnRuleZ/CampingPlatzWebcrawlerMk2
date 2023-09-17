import os
import re
import pandas as pd  # Make sure to import pandas correctly

import requests
from bs4 import BeautifulSoup

from ExcelInput import ExcelInput
from LinkCrawler import LinkCrawler
from imageRecognition import ImageRecognition


class SiteHarvester():
    def harvest_site(self, url, save_directory):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            textbox = soup.find('h1', {'class': 'platzname'})
            button = soup.find('button', {'id': 'pohnenumber_page'})

            if button:
                onclick_value = button.get('onclick')
                phone_number = onclick_value.split("'")[1]
                print(phone_number)


            if textbox:
                # Extract and return the text from the textbox
                extracted_text = textbox.text
                print(extracted_text)
            else:
                extracted_text = None

            # Search for image source URLs with campid in the format you provided
            image_urls = re.findall(r'<img src="/email_platz.php\?campid=(\d+)"', response.text)

            # Save each image to a file
            for index, campid in enumerate(image_urls, start=1):
                image_url = f"https://www.camping-in-deutschland.de/email_platz.php?campid={campid}"
                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    with open(os.path.join(save_directory, f"campid_{campid}.jpg"), 'wb') as image_file:
                        image_file.write(image_response.content)
                    print(f"Saved campid_{campid}.jpg")

            return extracted_text

        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch data from {url}: {e}")
        return None

    def harvest_site_save_to_xlxs2(self, url, save_directory, output_excel_file):
        data = []
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            textbox = soup.find('h1', {'class': 'platzname'})
            button = soup.find('button', {'id': 'pohnenumber_page'})

            if button:
                onclick_value = button.get('onclick')
                phone_number = onclick_value.split("'")[1]
                print(phone_number)
            else:
                phone_number = None

            if textbox:
                # Extract and return the text from the textbox
                extracted_text = textbox.text
                print(extracted_text)
            else:
                extracted_text = None

            # Search for image source URLs with campid in the format you provided
            image_urls = re.findall(r'<img src="/email_platz.php\?campid=(\d+)"', response.text)
            emailText = ""


            # Save each image to a file
            for index, campid in enumerate(image_urls, start=1):
                image_url = f"https://www.camping-in-deutschland.de/email_platz.php?campid={campid}"
                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    image_filename = f"campmail.jpg"
                    with open(os.path.join(save_directory, image_filename), 'wb') as image_file:
                        image_file.write(image_response.content)
                    print(f"Saved {image_filename}")
                    imgRecog = ImageRecognition()
                    emailText = imgRecog.getImageText()

                # Append data to the list
                data.append({
                    'Name': extracted_text,
                    'URL': url,
                    'Picture': emailText,
                    'Phone Number': phone_number
                })

            # Create a DataFrame from the list of data
            df = pd.DataFrame(data)

            # Save the DataFrame to an Excel file
            df.to_excel(output_excel_file, index=False)

            return extracted_text
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def harvest_site_save_to_xlxs1(self, url, save_directory, output_excel_file):
        data = []
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            textbox = soup.find('h1', {'class': 'platzname'})
            button = soup.find('button', {'id': 'pohnenumber_page'})

            if button:
                onclick_value = button.get('onclick')
                phone_number = onclick_value.split("'")[1]
                print(phone_number)
            else:
                phone_number = None

            if textbox:
                # Extract and return the text from the textbox
                extracted_text = textbox.text
                print(extracted_text)
            else:
                extracted_text = None

            # Search for image source URLs with campid in the format you provided
            image_urls = re.findall(r'<img src="/email_platz.php\?campid=(\d+)"', response.text)
            emailText = ""

            # Save each image to a file
            for index, campid in enumerate(image_urls, start=1):
                image_url = f"https://www.camping-in-deutschland.de/email_platz.php?campid={campid}"
                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    image_filename = f"campmail.jpg"
                    with open(os.path.join(save_directory, image_filename), 'wb') as image_file:
                        image_file.write(image_response.content)
                    print(f"Saved {image_filename}")
                    img = ImageRecognition()
                    emailText = img.getImageText()

                # Append data to the list
                data.append({
                    'Name': extracted_text,
                    'URL': url,
                    'Picture': emailText,
                    'Phone Number': phone_number
                })

            # Create a DataFrame from the list of data
            df = pd.DataFrame(data)

            # Save the DataFrame to an Excel file
            df.to_excel(output_excel_file, index=False)

            return extracted_text
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def harvest_site_save_to_xlxs3(self, url, save_directory, output_excel_file):
        data = []
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            textbox = soup.find('h1', {'class': 'platzname'})
            button = soup.find('button', {'id': 'pohnenumber_page'})

            if button:
                onclick_value = button.get('onclick')
                phone_number = onclick_value.split("'")[1]
                print(phone_number)
            else:
                phone_number = None

            if textbox:
                # Extract and return the text from the textbox
                extracted_text = textbox.text
                print(extracted_text)
            else:
                extracted_text = None

            # Search for image source URLs with campid in the format you provided
            image_urls = re.findall(r'<img src="/email_platz.php\?campid=(\d+)"', response.text)
            emailText = ""

            # Save each image to a file
            for index, campid in enumerate(image_urls, start=1):
                image_url = f"https://www.camping-in-deutschland.de/email_platz.php?campid={campid}"
                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    image_filename = f"campmail.jpg"
                    with open(os.path.join(save_directory, image_filename), 'wb') as image_file:
                        image_file.write(image_response.content)
                    print(f"Saved {image_filename}")
                    img = ImageRecognition()
                    emailText = img.getImageText()

                # Append data to the list
                data.append({
                    'Name': extracted_text,
                    'URL': url,
                    'Picture': emailText,
                    'Phone Number': phone_number
                })

            # Create a DataFrame from the list of data
            df = pd.DataFrame(data)

            # Reset the index before saving to Excel
            df.reset_index(drop=True, inplace=True)

            # Save the DataFrame to an Excel file
            df.to_excel(output_excel_file, index=False)

            return extracted_text
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    '''
    def harvest_site_save_to_xlxs(self, url, save_directory, output_excel_file, index):
        data = []
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            textbox = soup.find('h1', {'class': 'platzname'})
            button = soup.find('button', {'id': 'pohnenumber_page'})

            if button:
                onclick_value = button.get('onclick')
                phone_number = onclick_value.split("'")[1]
                print(phone_number)
            else:
                phone_number = None
                print("no phone number")

            if textbox:
                # Extract and return the text from the textbox
                extracted_text = textbox.text
                print(extracted_text)
            else:
                extracted_text = None
                print("no platzname")


            # Search for image source URLs with campid in the format you provided
            image_urls = re.findall(r'<img src="/email_platz.php\?campid=(\d+)"', response.text)
            emailText = ""

            # Save each image to a file
            for campid in image_urls:
                image_url = f"https://www.camping-in-deutschland.de/email_platz.php?campid={campid}"
                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    image_filename = f"campmail.jpg"
                    with open(os.path.join(save_directory, image_filename), 'wb') as image_file:
                        image_file.write(image_response.content)
                    print(f"Saved {image_filename}")
                    img = ImageRecognition()
                    emailText = img.getImageText()

            # Append data to the list
            data.append({
                 'Name': extracted_text,
                 'URL': url,
                 'Picture': emailText,
                 'Phone Number': phone_number
            })

            # Create a DataFrame from the list of data
            df = pd.DataFrame(data)

            # If the index parameter is provided and is within the valid range, insert the data at the specified row index
            if index is not None and 0 <= index <= len(df):
                df = pd.concat([df.iloc[:index], pd.DataFrame([data[index]]), df.iloc[index:]]).reset_index(drop=True)

            # Reset the index before saving to Excel
            df.reset_index(drop=True, inplace=True)

            # Save the DataFrame to an Excel file
            df.to_excel(output_excel_file, index=False)
            return "sucess"

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None
    '''

    def harvest_site_save_to_xlxs(self, url, save_directory, output_excel_file):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            textbox = soup.find('h1', {'class': 'platzname'})
            button = soup.find('button', {'id': 'pohnenumber_page'})

            if button:
                onclick_value = button.get('onclick')
                phone_number = onclick_value.split("'")[1]
                print(phone_number)
            else:
                phone_number = None
                print("no phone number")

            if textbox:
                # Extract and return the text from the textbox
                extracted_text = textbox.text
                print(extracted_text)
            else:
                extracted_text = None
                print("no platzname")

            # Search for image source URLs with campid in the format you provided
            image_urls = re.findall(r'<img src="/email_platz.php\?campid=(\d+)"', response.text)
            emailText = ""

            # Save each image to a file
            for campid in image_urls:
                image_url = f"https://www.camping-in-deutschland.de/email_platz.php?campid={campid}"
                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    image_filename = f"campmail.jpg"
                    with open(os.path.join(save_directory, image_filename), 'wb') as image_file:
                        image_file.write(image_response.content)
                    print(f"Saved {image_filename}")
                    img = ImageRecognition()
                    emailText = img.getImageText()

            # Create a DataFrame for the single row of data
            data = {
                'Name': extracted_text,
                'URL': url,
                'Picture': emailText,
                'Phone Number': phone_number
            }
            df = pd.DataFrame([data])

            # Append the data to the existing Excel file (if it exists)
            if os.path.exists(output_excel_file):
                existing_df = pd.read_excel(output_excel_file)
                df = pd.concat([existing_df, df], ignore_index=True)

            # Save the DataFrame to an Excel file
            df.to_excel(output_excel_file, index=False)
            return "success"
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None


    def get_all_sublinks(self):
        baseUrlNewSite = "https://www.camping-in-deutschland.de/deutschland/"
        linkCrawler = LinkCrawler()
        excel = ExcelInput()

        links = linkCrawler.crawl_results()
        exclude_link_list = ["https://www.camping-in-deutschland.de/deutschland/bayern/",
                             "https://www.camping-in-deutschland.de/deutschland/hessen/",
                             "https://www.camping-in-deutschland.de/deutschland/bremen/",
                             "https://www.camping-in-deutschland.de/deutschland/baden-wuerttemberg/",
                             "https://www.camping-in-deutschland.de/deutschland/rheinland-pfalz/",
                             "https://www.camping-in-deutschland.de/deutschland/berlin/",
                             "https://www.camping-in-deutschland.de/deutschland/brandenburg/",
                             "https://www.camping-in-deutschland.de/deutschland/mecklenburg-vorpommern/",
                             "https://www.camping-in-deutschland.de/deutschland/sachsen/",
                             "https://www.camping-in-deutschland.de/deutschland/niedersachsen/",
                             "https://www.camping-in-deutschland.de/deutschland/thueringen/",
                             "https://www.camping-in-deutschland.de/deutschland/hamburg/",
                             "https://www.camping-in-deutschland.de/deutschland/saarland/",
                             "https://www.camping-in-deutschland.de/deutschland/nordrhein-westfalen/",
                             "https://www.camping-in-deutschland.de/deutschland/schleswig-holstein/",
                             "https://www.camping-in-deutschland.de/deutschland/sachsen-anhalt/",
                             "https://www.camping-in-deutschland.de/deutschland/miet-zelte/",
                             "https://www.camping-in-deutschland.de/deutschland/ferienhaeuser/",
                             "https://www.camping-in-deutschland.de/deutschland/dauerstellplaetze/"
                             "https://www.camping-in-deutschland.de/deutschland/zimmer/",
                             ]
        top_level_links = [
            "https://www.camping-in-deutschland.de/?pid=platzsucheliste&bundesland=W%FCrttemberg&seite=0&order=61"]

        bundesLandMap = {
            "https://www.camping-in-deutschland.de/?pid=platzliste&bundesland=Bayern&seite=0&order=61": 12,
            "https://www.camping-in-deutschland.de/?pid=platzliste&bundesland=Hessen&seite=0&order=61": 4,
            "https://www.camping-in-deutschland.de/?pid=platzliste&bundesland=Bremen&seite=0&order=61": 1,
            "https://www.camping-in-deutschland.de/?pid=platzliste&bundesland=ttemberg&seite=0&order=61": 7,
            "https://www.camping-in-deutschland.de/?pid=platzliste&bundesland=Pfalz&seite=0&order=61": 8,
            "https://www.camping-in-deutschland.de/?pid=platzliste&bundesland=Berlin&seite=0&order=61": 1,
            "https://www.camping-in-deutschland.de/?pid=platzliste&bundesland=Brandenburg&seite=0&order=61": 6,
            "https://www.camping-in-deutschland.de/?pid=platzliste&bundesland=Vorpommern&seite=0&order=61": 8,
            "https://www.camping-in-deutschland.de/?pid=platzliste&bundesland=Sachsen&seite=0&order=61": 3,
            "https://www.camping-in-deutschland.de/?pid=platzliste&bundesland=Niedersachsen&seite=0&order=61": 12,
            "https://www.camping-in-deutschland.de/?pid=platzliste&bundesland=ringen&seite=0&order=61": 3,
            "https://www.camping-in-deutschland.de/?pid=platzliste&bundesland=Hamburg&seite=0&order=61": 1,
            "https://www.camping-in-deutschland.de/?pid=platzliste&bundesland=Saarland&seite=0&order=61": 1,
            "https://www.camping-in-deutschland.de/?pid=platzliste&bundesland=Westfalen&seite=0&order=61": 11,
            "https://www.camping-in-deutschland.de/?pid=platzliste&bundesland=Holstein&seite=0&order=61": 14,
            "https://www.camping-in-deutschland.de/?pid=platzliste&bundesland=Anhalt&seite=0&order=61": 4,
        }

        list_all_links_each_CampingPlatz = []
        for link, number in bundesLandMap.items():
            for i in range(number):
                modified_link = link.replace('seite=0', f'seite={i}')
                print(modified_link)

                results = linkCrawler.get_filtered_suburls(modified_link, baseUrlNewSite, exclude_link_list)
                for res in results:
                    print(res)
                    list_all_links_each_CampingPlatz.append(res)

        file_path = "urls.txt"

        # Open the file in write mode and save the URLs line by line
        with open(file_path, "w") as file:
            for url in list_all_links_each_CampingPlatz:
                file.write(url + "\n")

        print("URLs have been saved to", file_path)



