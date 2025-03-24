from bs4 import BeautifulSoup
import requests
import json


def main():

    url = "https://www.trebesin.cz/"

    response = requests.get(url)
    #pythonovina

    soup = BeautifulSoup(response.content, "html.parser")
    #hrnec

    all_p = soup.find_all("p")

    print(all_p)

    list_p = []

    for p in all_p:
        list_p.append(p.text)

    with open("datatrebe.json", mode="w") as file:
        json.dump(list_p, file, indent=4, ensure_ascii=False)
    
if __name__ == "__main__":
    main()