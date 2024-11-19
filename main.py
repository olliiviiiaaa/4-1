"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
charge = 0.00
# Number of characters.
numChars = 18
# Color of characters.
color = "black"
# Type of wood.
woodType = "oak"

# Write assignment and if statements here as appropriate.

# Minimum charge
charge = 35.00

# Check for additional characters
if numChars > 5:
    charge += (numChars - 5) * 4

# Check for wood type
if woodType == "oak":
    charge += 20.00

# Check for character color
if color == "gold":
    charge += 15.00

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
