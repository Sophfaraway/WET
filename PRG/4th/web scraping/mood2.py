from bs4 import BeautifulSoup
import requests


def main():

    url = "https://www.arsenal.com/results"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    arsenal = soup.find(class_="scores__score--arsenal").text
    all_scores = soup.find_all(class_="scores__score")
    score1 = int(arsenal)
    score2 = int(all_scores[1].text)

    # print(arsenal.text)
    # print(all_scores[2].text)

    if score1 > score2 :
        print("yay")
    elif score1 < score2 :
        print(":(")
    elif score1 == score2 :
        print("-_-")

    # all_p = soup.find_all("p")

    # for p in all_p:
    #     print(p.text)

    # gym = soup.find(id="favimagehover-title4")
    # print(f"Název oboru je {gym.text}")
    # gym2 = soup.select("#favimagehover-title4")

if __name__ == "__main__":
    main()