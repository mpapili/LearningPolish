import json

with open("introductions.json", "r") as myfile:
    phrases = json.load(myfile)
print(phrases)

for p in phrases["phrases"]:
    print(f'\n{p["english"]}\n')
    answer = input("What is this in polish?\n").rstrip()
    if answer == p["polish"]:
        print("Very good!")
    else:
        print("bledny (bwednih)")
        print(f"To jest {p['polish']}")
