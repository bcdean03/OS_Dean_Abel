__author__ = 'abelamadou Dean Bailey'

from random import choice


# Create a dictionary of recipes and there ingredient list
def create_recipe_dictionary():
    goodies_dictionary = {
    "Banana Bread":["Banana","Eggs","Salt","Flour","Sugar","Baking Soda","Butter","Yeast","Water"],
    "Apple Bread":["Apple","Baking Soda","Salt","Flour","Eggs","Sugar","Butter","Yeast","Water"],
    "Raisin Bread":["Raisin","Sugar","Salt","Flour","Eggs","Baking Soda","Butter","Yeast","Water"],
    "Pumpkin Bread":["Pumpkin","Butter","Salt","Flour","Eggs","Sugar","Baking Soda","Yeast","Water"],
    "Wheat Bread":["Wheat Flour","Yeast","Salt","Eggs","Sugar","Baking Soda","Butter","Water"],
    "Honey Bread":["Honey","Salt","Flour","Eggs","Sugar","Baking Soda","Butter","Yeast","Water"],
    "Chocolate Chip Bread":["Chocolate Chips","Eggs","Salt","Flour","Sugar","Baking Soda","Butter","Yeast","Water"],
    "Cinnamon Bread":["Cinnamon","Water","Salt","Flour","Eggs","Sugar","Baking Soda","Butter","Yeast"],
    "Pizza":["Pepperoni","Salt","Flour","Eggs","Yeast","Water","Oil","Sauce","Cheese"],
    "Mac and Cheese":["Cheese","Noodles","Milk","Water"],
    "Cheese Burger":["Hamburger","Cheese","Lettuce"],
    "Spaghetti":["Noodles","Cheese","Hamburger","Sauce"]}
    return goodies_dictionary


# Get a random food item to get the ingredients
def get_food_and_recipe(goodies):
    food = choice(goodies.keys())
    recipe_list = goodies[food]
    return food, recipe_list
