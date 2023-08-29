
import json


with open('me-capitals.json', 'r') as f:
    data = json.load(f)
    total = len(data["cards"])
    score = 0
    
    for i in data["cards"] :
      guess = input (i["q"] + ">")  
    
    if guess == i ["a"]:
        score += 1
        print(f"correct! Current Score: {score}/{total}")
    else:
            print("Incorrect! The correct answer was" , i ["a"])
            print (f"current score: {score}/ {total}")


