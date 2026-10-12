percept_sequence = ["Dark", "Dim", "Bright", "Dark"]
 
def room_light_agent(percept):
    if percept == "Dark":
        return "Turn Light ON"
    elif percept == "Bright":
        return "Turn Light OFF"
    else:
        return "Leave Light As Is"
 
print("Percept\t\tAction")
for percept in percept_sequence:
    print(percept, "\t\t", room_light_agent(percept))
