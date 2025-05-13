import json

# Sample inventory data
inventory = {
    'item1': {'name': 'Laptop', 'quantity': 10, 'price': 1000},
    'item2': {'name': 'Smartphone', 'quantity': 20, 'price': 500},
    # Add more items
}

# Save inventory to JSON file
with open('inventory.json', 'w') as f:
    json.dump(inventory, f)

# Load inventory from JSON file
with open('inventory.json', 'r') as f:
    loaded_inventory = json.load(f)

print(loaded_inventory)
