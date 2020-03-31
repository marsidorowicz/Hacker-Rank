name = input("Podaj swoje imię: ")
def inputNumber(message) :
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Podaj liczbę")
            continue
        else:
            return userInput
            break
age = inputNumber("Ile masz lat?: ")
x = 100 - age
import datetime
now = datetime.datetime.now()
year = int(now.year)+x
if age < 100:

    print("Masz na imię "+str(name) +" i za " + str(x) + " lat będziesz mieć 100 lat, czyli w roku "+str(year)+ " ponieważ mamy obecnie rok " + str(now.year))

if age == 100:
    print("Masz sto lat!")

else:
    print("Twój wiek musi być liczbą")
