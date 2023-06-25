import os


if __name__ == "__main__":
    print("wellcome to RoboSpeaker 1.1 Created by Ajit")
    while True:
        speach = input("enter what you want to speak: ")
        if speach == "a":
            os.system("say 'Bye bye friends'")
            break
        command = f"say {speach}"
        os.system(command)
    