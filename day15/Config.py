"""
3 hot drinks:
Espresso
    price: 1.50$
    50ml of hot water
    18g of coffee
Latte
    price: 2.50$
    200ml of hot water
    24g of coffee
    150ml of milk
Cappuccino
    price: 3.00$
    250ml of hot water
    24g of coffee
    100ml of milk
"""


class Config:

    INITIAL_MONEY = 0

    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "milk": 0,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 2000,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
