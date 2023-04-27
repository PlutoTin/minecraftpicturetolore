from PIL import Image

# Define the Minecraft color codes
color_codes = ["§0", "§1", "§2", "§3", "§4", "§5", "§6", "§7", "§8", "§9", "§a", "§b", "§c", "§d", "§e", "§f"]

# Prompt the user for the X and Y dimensions of the picture to resize
x = int(input("X of the picture to resize: "))
y = int(input("Y of the picture to resize: "))

# Load the input image and resize it to the user-specified dimensions
img = Image.open("input_image.png").resize((x, y))

# Convert the image to a Minecraft color palette
palette = []
for pixel in img.getdata():
    r, g, b, *_ = pixel
    # Convert RGB values to a single value between 0 and 15
    index = int(round((r + g + b) / 3 / 16))
    # Check if the index is within the range of valid indices for the color_codes list
    if index >= 0 and index < len(color_codes):
        # Add the corresponding Minecraft color code to the palette if it hasn't been added yet
        if color_codes[index] not in palette:
            palette.append(color_codes[index])

# Construct the /give command with custom lore
command = f"/give @p diamond_sword{{display:{{Name:\"Custom Sword\",}},Lore:["
for i in range(len(palette)):
    command += f"\"{{\\\"text\\\":\\\"{palette[i]}■\\\"}}\","
    if (i + 1) % y == 0:
        command += "\"\\n\","
command += "]}} 1"

# Print the /give command
print(command)
