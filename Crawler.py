import sys
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
from CarPriceDataBase import addElement


def findElementsLinks(address):
    i = 1
    while True:
        site_url = address + "?page=" + str(i)
        try:
            open_site_url = urlopen(site_url).read()
        except TimeoutError:
            i = i - 1
            continue
        soup = BeautifulSoup(open_site_url, "html.parser")
        ctr = 1
        flag = False
        for link in soup.find_all('a', href=True):
            text = link['href']
            if text[5:12] == "details" and flag:
                ctr += 1
                file = open("LimitedLinks.txt", "a")
                file.write("https://bama.ir" + text + "\n")
                file.close()
            flag = not flag
        if ctr < 12:
            return
        for tt in soup.select("#content > div.leftpanel > div.paging-bottom-div.hidden-xs > h4"):
            text = tt.text
            splited = text.split(" ")
            if splited[5] == splited[7]:
                return
        i += 1


def findLimitElementsLinks(address):
    maxPage = 3
    for i in range(1, maxPage + 1):
        site_url = address + "?page=" + str(i)
        try:
            open_site_url = urlopen(site_url).read()
        except TimeoutError:
            i = i - 1
            continue
        soup = BeautifulSoup(open_site_url, "html.parser")
        ctr = 1
        flag = False
        for link in soup.find_all('a', href=True):
            text = link['href']
            if text[5:12] == "details" and flag:
                ctr += 1
                file = open("LimitedLinks.txt", "a")
                file.write("https://bama.ir" + text + "\n")
                file.close()
            flag = not flag
        if ctr < 12:
            return
        for tt in soup.select("#content > div.leftpanel > div.paging-bottom-div.hidden-xs > h4"):
            text = tt.text
            splited = text.split(" ")
            if splited[5] == splited[7]:
                return


def findModelsLinks():
    site_url = 'https://bama.ir/'
    open_site_url = urlopen(site_url).read()
    soup = BeautifulSoup(open_site_url, "html.parser")

    # Data is List of Brands
    Data = []
    for link in soup.find_all('a', href=True):
        text = link['href']
        if text[0:4] == "/car" and text[5:8] != "all" and text.count("/") > 2 and not Data.__contains__(
                                "https://bama.ir" + text + "\n"):
            Data.append("https://bama.ir" + text + "\n")

    file = open("Brands.txt", "w")
    file.write("")
    file.close()
    file = open("Brands.txt", "a")
    for data in Data:
        file.write(data)
    file.close()


def findMaxPage():
    i = 1
    while True:
        site_url = "https://bama.ir/car/bmw/320i?page={}".format(str(i))
        open_site_url = urlopen(site_url).read()
        soup = BeautifulSoup(open_site_url, "html.parser")

        for tt in soup.select("#content > div.leftpanel > div.paging-bottom-div.hidden-xs > h4"):
            text = tt.text
            splited = text.split(" ")
            if splited[5] == splited[7]:
                return i
        i += 1


def findDetails(url):
    open_site_url = urlopen(url).read()
    Color = "unknown"
    soup = BeautifulSoup(open_site_url, "html.parser")
    for item in soup.find_all("div", {"class": "inforight"}):
        text = item.text
        data = text.split("\n")
        # Ckeck is not installment
        if data[13] == "تعداد اقساط ":
            return None, None, None, None, None, None, None, None, None, None, None, None, None
        Price = data[8].replace(",", "").replace(" ", "").replace("تومان", "")
        Drived = data[19].replace(" ", "").replace("کیلومتر", "").replace(",", "")
        Gear = data[25].replace(" ", "")
        Fuel = data[31].replace(" ", "")
        Color = data[43]
        State = data[49].replace(" ", "")
    for year in soup.find_all("span", {"itemprop": "releaseDate"}):
        Year = year.text
    for perBrand in soup.find_all("span", {"itemprop": "brand"}):
        PerBrand = perBrand.text
    for perModel in soup.find_all("span", {"itemprop": "model"}):
        PerModel = perModel.text
    # Nationality = findNationality(Brand)
    Nationality = "F"
    EnBrand, EnModel = splitURL(url)
    if Price == "تماسبگيريد":
        Price = "-1"
    return PerBrand, PerModel, EnBrand, EnModel, Price, Drived, Year, Fuel, State, Color, Gear, url, Nationality


def splitURL(url):
    data = url.split("/")
    detail = data[-1]
    splitedDetail = detail.split("-")
    lenth = len(splitedDetail)
    BrandModel = splitedDetail[1]
    for i in range(2, lenth - 2):
        BrandModel += "-" + splitedDetail[i]
    # Data is List of Brands
    Brands = open("BrandsList.txt", "r")
    for brand in Brands:
        brand = brand.replace("\n", "")
        if BrandModel.__contains__(brand):
            Brand = brand.replace("-", "_")
            brandLen = len(Brand)
            Model = BrandModel[brandLen + 1:len(BrandModel)].replace("-", "_")
            return Brand, Model


def findBrandLists():
    site_url = 'https://bama.ir/'
    open_site_url = urlopen(site_url).read()
    soup = BeautifulSoup(open_site_url, "html.parser")

    # file is List of Brands
    file = open("BrandsList.txt", "w")
    file.write("")
    file.close()
    Data = []

    for link in soup.find_all('a', href=True):
        text = link['href']
        textLen = len(text)
        brand = text[5:textLen]
        if text[0:4] == "/car" and text[5:8] != "all" and text.count("/") == 2 and not Data.__contains__(
                        brand + "\n"):
            Data.append(brand + "\n")

    file = open("BrandsList.txt", "a")
    for data in Data:
        file.write(data)
    file.close()


def findNationality(Brand):
    pass  # TODO


def crawlAllData():
    # # file = open("Links.txt", "w")
    # # file.write("")
    # # file.close()
    # file = open("LimitedLinks.txt", "w")
    # file.write("")
    # file.close()
    # findBrandLists()
    # findModelsLinks()
    # reader = open("Brands.txt", "r")
    # for line in reader:
    #     # find all links
    #     # findElementsLinks(line.replace("\n",""))
    #
    #     # find only 3 first page
    #     findLimitElementsLinks(line.replace("\n", ""))
    # reader.close()

    reader = open("LimitedLinks.txt", "r")
    for line in reader:
        PerBrand, PerModel, EnBrand, EnModel, Price, Drived, Year, Fuel, State, Color, Gear, url, Nationality = findDetails(
            line.replace("\n", ""))
        if (PerBrand == None and PerModel == None and EnModel == None and EnModel == None):
            continue
        addElement(EnBrand,EnModel,Price,Drived,Year,Fuel,State,Color,Gear,url,Nationality, PerBrand, PerModel)
    reader.close()


crawlAllData()

