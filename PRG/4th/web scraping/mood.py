from bs4 import BeautifulSoup
import requests


def main():

    url = "https://www.arsenal.com/results"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    arsenal = soup.find(class_="scores__score--arsenal").text
    all_scores = soup.find_all(class_="scores__score")
    all_teams = soup.find_all(class_="team-crest__name-value")

    score1 = int(arsenal)
    score2 = int(all_scores[1].text)

    # print(arsenal.text)
    # print(all_scores[3].text)
    # print(all_teams)

    score3 = int(all_scores[0].text)

    for i in range(8):
        if all_teams[i].text == "Tottenham Hotspur":
            tottenteam = int(all_scores[i].text)
            if i == 1 or i == 3 or i == 5 or i == 7:
                arsenal2 = int(all_scores[i-1].text)
                if tottenteam <  arsenal2:
                    print("Hell yeah")
                    break

            if i == 0 or i == 2 or i == 4 or i == 6:
                arsenal2 = int(all_scores[i+1].text)
                if tottenteam <  arsenal2:
                    print("Hell yeah")
                    break
        elif i == 7:
            if score3 == score1:
                if score1 > score2 :
                    print("yay")
                elif score1 < score2 :
                    print(":(")
                elif score1 == score2 :
                    print("-_-")
            else:
                if score1 < score2 :
                    print("yay")
                elif score1 > score2 :
                    print(":(")
                elif score1 == score2 :
                    print("-_-")

if __name__ == "__main__":
    main()