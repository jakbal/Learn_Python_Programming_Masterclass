computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]

another_list = computer_parts

print(id(computer_parts))
print(id(another_list))

computer_parts += ["battery"]
print(id(computer_parts))

computer_parts.append("ulock")
print(computer_parts)
