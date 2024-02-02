from contents_quantity import recipes

def my_deepcopy(d: dict) -> dict:
    new_dict = {}
    for key, val in d.items():
        val_copy = val.copy()
        new_dict[key] = val_copy
    return new_dict

#test code
# recipes_copy = my_deepcopy(recipes)
# recipes_copy["Butter chicken"]["ginger"] = 300
# print(recipes_copy["Butter chicken"]["ginger"]) #300
# print(recipes["Butter chicken"]["ginger"]) #3
