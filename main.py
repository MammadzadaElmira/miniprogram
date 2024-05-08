import os
import datetime
import time


HELP = "HELP"
HISTORY = "HISTORY"
OPERATION = "OPERATION"

def get_calculate(operation):
    try:
        calculate = eval(operation)
        rounded_result = round(calculate, 1)
        return f"The result is '{rounded_result}'"
    except ZeroDivisionError:
        return "ERROR. DIVIDING BY '0' IS PROHIBITED❌"


def get_instructions():
    print("***📜 INSTRUCTIONS***:\nIT IS A BASIC CALCULATOR PROGRAM. YOU CAN ONLY USE"
          "📝 \033[93m +, -, /, *, **.\033[0m ")
    print("Additionally, You Can Get Information About 'History Of Operation', And 'Help'")

def get_history():
    #history = [ ]
    now = datetime.datetime.now()
    current = now.strftime("%d %b  %H:%M:%S")

    """with open("file.txt", "w+") as file:
        for x in history:
            file.writelines(x)
       """
    result = f"Operation⏱:\n{current}. Operation - "
    return result

        
def choose():
    data = {
        HELP: get_instructions,
        HISTORY: get_history
    }
    if ask_user in data:
        result = data[ask_user]
        return result()
    return get_calculate(ask_user)

print("HELLO😊 IT IS A CALCULATE PROGRAM 📱Pls, CALCULATE")
while True:
    ask_user = input("You Can Choose 'HELP' or 'HISTORY To Get Additional Information\n").strip().upper()
    os.system("cls")
    print(choose())
    ask_again = input("Do You Want Exit or Continue?👉 Choose 1(exit) or 2(continue) \n")
    if ask_again == "1":
        break
    else:
        print("\033[95mLETS'GO...\033[0m")
        time.sleep(1)
print("\033[92mTHE ENDED...🙂\033[0m")    