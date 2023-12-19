import csv

def main():  
    BadIceCream = {
        "Vanilla": 1,
        "Strawberry": 3,
        "Chocolate": 2,
        "Sorbet": 1
    }
    
    save_data(BadIceCream)
    load_data(BadIceCream)

def save_data(BadIceCream):
    with open("C:\\Users\\sopmo\\Documents\\WET\\Python\\ukazky z hodin\\icecream.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for flavor, points in BadIceCream.items():
            writer.writerow([flavor, points])

def load_data(BadIceCream):
    with open("C:\\Users\\sopmo\\Documents\\WET\\Python\\ukazky z hodin\\icecream.csv", "r") as file:
        reader = csv.reader(file)
        for addKeys in reader:
            BadIceCream[addKeys[0]] = int(addKeys[1])
    print(BadIceCream)

if __name__=="__main__":
    main()