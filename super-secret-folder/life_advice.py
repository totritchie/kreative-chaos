

import sys

def life_advice():
    if len(sys.argv) < 2:
        print("You need to pass in your favorite programming language as an argument!")
        return

    favorite_language = sys.argv[1]

    if favorite_language == "Python":
        print("You are cool")
    elif favorite_language == "Java":
        print("Inherit deez nuts ")
    elif favorite_language == "C++":
        print("I'm so sorry for your pain :(")
    elif favorite_language == "Go":
        print("Holy based")
    elif favorite_language == "Rust":
        print("You are a chad")
    elif favorite_language == "JavaScript":
        print("Object object is not a function")
    elif favorite_language == "C":
        print("You are a masochist")
    elif favorite_language == "Haskell":
        print("You are a genius")
    elif favorite_language == "Ruby":
        print("You are a hipster")
    elif favorite_language == "PHP":
        print("You are a SQL injection") 
    elif favorite_language == "Assembly":
        print("You are a god")
    elif favorite_language == "Swift":
        print("You are a hipster but more hipster than Ruby")
    else:
        print("You are a funny person!")

life_advice()