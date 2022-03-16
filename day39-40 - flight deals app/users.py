import requests
import re


class UserManager:
    def __init__(self, token):
        self.token = token

    def get_users_addresses(self):
        endpoint = "https://api.sheety.co/5d68b1baa7b33d460a3afb95a8197651/flightDeals/users"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url=endpoint, headers=headers)
        response.raise_for_status()
        emails = [user["emailAddress"] for user in response.json()["users"]]
        return emails

    def new_user(self):
        name, address = self.user_input()
        self.add_user_to_database(name, address)

    @staticmethod
    def user_input():
        print("Setting up new account")
        name = input("What is your name?: ")
        print(f"Hi {name}.")
        while True:
            email1 = input("What is your email address?: ")
            email2 = input(f"Confirm your email address: ")
            if email1 == email2:
                if re.search(r"[^@]+@[^@]+\.[^@]+", email1):
                    return name, email1
                else:
                    print("Email address not correct.")
            else:
                print("Addresses are not the same. Try again...")

    def add_user_to_database(self, name, email):
        endpoint = "https://api.sheety.co/5d68b1baa7b33d460a3afb95a8197651/flightDeals/users"
        headers = {"Authorization": f"Bearer {self.token}"}
        body = {"user": {"name": name, "emailAddress": email}}
        response = requests.post(url=endpoint, headers=headers, json=body)
        response.raise_for_status()
        print("user added successfully.")
        return response.json()
