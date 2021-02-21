import json


def read_file():
    """
    """
    with open("friends_list_Obama.json", "r") as f:
        data = json.load(f)
    return data


def something(data):
    """
    """
    if isinstance(data, dict):
        print("This object is dictionary")
        print(data.keys())
        users_input = str(input("Please choose what key do you want to see: "))
        for key in data:
            if users_input == key:
                key_data = data[key]
                return something(key_data)
    elif isinstance(data, list):
        print("This object is list")
        print(len(data))
        users_input = int(input("Please choose what number of list do you want to see: "))
        for els in data:
            if els == data[users_input]:
                list_data = data[users_input]
                return something(list_data)
    elif isinstance(data, str):
        print(data)
    elif isinstance(data, int):
        print(data)


def main():
    """
    """
    something(read_file())
    cicle = input("Do you want to do it again? (Yes or No):  ")
    if cicle == "Yes":
        main()
    else:
        pass



if __name__ == "__main__":
    main()