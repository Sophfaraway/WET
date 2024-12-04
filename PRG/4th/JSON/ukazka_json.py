import json

filmy = {
    "komedie":"Tropická bouře",
    "horror":["Sinister", "To"],
    "animák":["Spongebob", "Na vlásku", "Lví král"],
    "muzikál":"Hamilton"
}

with open("data.json", mode="w") as file:
    json.dump(filmy, file, indent=4, ensure_ascii=False)

with open("data.json", mode="r") as file:
    loaded_data = json.load(file)

print(loaded_data)