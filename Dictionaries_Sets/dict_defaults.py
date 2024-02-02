from contents import pantry

chicken_qunatity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_qunatity}")

beans_qunatity = pantry.setdefault("beans", 0)
print(f"beans: {beans_qunatity}")

ketchup_qunatity = pantry.get("ketchup", 0)
print(f"ketchup: {ketchup_qunatity}")

z_quantity = pantry.setdefault("zuchinni", "eight")
print(f"zuchinni: ", {z_quantity})

print()
print("`pantry` now contains...")
for key, value in sorted(pantry.items()):
    print(key, value)
