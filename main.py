import time

from ExcelInput import ExcelInput
from LinkCrawler import LinkCrawler
from SiteHarvester import SiteHarvester

if __name__ == "__main__":
    excelFileName = "C:/Users/xmadd/Desktop/Camping.xlsx"
    baseUrlNewSite = "https://www.camping-in-deutschland.de/deutschland/"

    linkCrawler = LinkCrawler()
    excel = ExcelInput()

    siteHarvest = SiteHarvester()
    # print(siteHarvest.harvest_site_save_to_xlxs("https://www.camping-in-deutschland.de/deutschland/naturcampingpark_isarhorn/#Kontakt", "", excelFileName))

    with open("urls.txt", "r") as file:
        for line in file:
            print(line)
            siteHarvest.harvest_site_save_to_xlxs(
                line, "",
                excelFileName)
            time.sleep(5)