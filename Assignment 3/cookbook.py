'''
 Manages a collection of Dish objects using a Cookbook class.
'''
class Dish:
    def __init__(self, dish_id, dish_name, ingredients, instructions):
        self.dish_id = dish_id
        self.dish_name = dish_name
        self.ingredients = ingredients
        self.instructions = instructions

class Cookbook:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def show_all(self):
        for d in self.dishes:
            print(f"ID: {d.dish_id} | Name: {d.dish_name}")
            print(f"Ingredients: {d.ingredients}")
            print(f"Instructions: {d.instructions}\n")

# Example Usage
if __name__ == "__main__":
    my_cb = Cookbook()
    d1 = Dish(101, "Pasta", "Water, Flour, Salt", "Boil and mix.")
    my_cb.add_dish(d1)
    my_cb.show_all()