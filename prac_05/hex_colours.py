COLOURS_CODES = {"black": "#000000", "brown": "#a52a2a",
                 "coral": "#ff7f50", "darkgreen": "#006400",
                 "gray": "#bebebe", "firebrick": "#b22222",
                 "darkviolet": "#9400d3", "aliceblue": "#f0f8ff",
                 "azure": "#838b8b", "beige": "#f5f5dc"}

colour = input("Enter a colour: ").lower()
while colour != "":
    if colour in COLOURS_CODES:
        print(colour, "is", COLOURS_CODES[colour])
    else:
        print("Invalid Colour")
    colour = input("Enter a colour: ").lower()
