from urllib.parse import urlparse, urljoin

import requests
from bs4 import BeautifulSoup
from googlesearch import search

class LinkCrawler:

    def crawl_results(self):
        # Durchsuche Google nach den gewünschten Ergebnissen
        suchergebnisse = search(f"Deutschland Campingplatz", num_results=10)  # Nummer der Ergebnisse, die du erhalten möchtest
        resuslts = []
        for link in suchergebnisse:
            print(link)
            resuslts.append(link)

        return resuslts

    def get_filtered_suburls(self, base_url, filter_prefix, exclude_links):
        # Send an HTTP GET request to the base URL
        response = requests.get(base_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Get the base domain of the URL
            base_domain = urlparse(base_url).netloc

            # Create an empty set to store unique sub-URLs
            unique_suburls = set()

            # Find all anchor tags (links) in the HTML
            for anchor_tag in soup.find_all('a', href=True):
                # Get the href attribute of the anchor tag
                href = anchor_tag['href']

                # Join the href with the base URL to get the absolute URL
                absolute_url = urljoin(base_url, href)

                # Parse the absolute URL to extract the domain
                parsed_url = urlparse(absolute_url)

                # Check if the domain matches the base domain (same site)
                if parsed_url.netloc == base_domain:
                    # Check if the URL starts with the specified filter_prefix
                    if absolute_url.startswith(filter_prefix):
                        # Check if the URL is not in the exclude_links list
                        if absolute_url not in exclude_links:
                            # Check if the URL ends with "#Kontakt"
                            if absolute_url.endswith("#Kontakt"):
                                unique_suburls.add(absolute_url)

            # Convert the set back to a list if needed
            unique_suburls_list = list(unique_suburls)

            return unique_suburls_list

        else:
            print("Failed to retrieve the webpage. Status code:", response.status_code)
            return []
