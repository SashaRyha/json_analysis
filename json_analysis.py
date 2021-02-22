import json


def read_file():
    """
    Reads json file 
    """
    with open("friends_list_Obama.json", "r") as f:
        data = json.load(f)
    return data


def json_analysis(data):
    """
    This fuction creates json navigator, where user can choose 
    what object or data he/she wants to see, by using recursion
    """
    if isinstance(data, dict):
        print("This object is dictionary")
        print(data.keys())
        users_input = str(input("Please choose what key do you want to see: "))
        for key in data:
            if users_input == key:
                key_data = data[key]
                return json_analysis(key_data)
    elif isinstance(data, list):
        print("This object is list")
        print("This list has ",len(data),"elements")
        users_input = int(input("Please choose what number of list do you want to see: "))
        for els in data:
            if els == data[users_input]:
                list_data = data[users_input]
                return json_analysis(list_data)
    elif isinstance(data, str):
        print(data)
    elif isinstance(data, int):
        print(data)


def main():
    """
    This fuction calls json_analysis and creates cycle
    if user wants to do it again
    """
    json_analysis(read_file())
    cicle = input("Do you want to do it again? (Yes or No):  ")
    if cicle == "Yes":
        main()
    else:
        pass



if __name__ == "__main__":
    main()