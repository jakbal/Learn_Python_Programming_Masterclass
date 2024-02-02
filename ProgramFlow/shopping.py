shopping_list = ["milk", "pasta", "eggs", "bread", "rice"]

#for item in shopping_list:
#    if item != "eggs":
#        print("Buy " + item)

# for item in shopping_list:
#     if item == "eggs":
#         continue
#     print("Buy " + item)

for item in shopping_list:
    if item == "eggs":
        break
    print("Buy " + item)
