import csv

class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class InventoryManagementSystem:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                self.inventory.remove(item)
                break

    def update_item(self, item_name, quantity=None, price=None):
        for item in self.inventory:
            if item.name == item_name:
                if quantity is not None:
                    item.quantity = quantity
                if price is not None:
                    item.price = price
                break

    def display_inventory(self):
        for item in self.inventory:
            print(f'Name: {item.name}, Quantity: {item.quantity}, Price: {item.price}')

    def load_inventory(self, file_name='inventory.csv'):
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            next(reader) # skip header row
            for row in reader:
                name, quantity, price = row
                item = InventoryItem(name, int(quantity), float(price))
                self.add_item(item)

    def save_inventory(self, file_name='inventory.csv'):
        with open(file_name, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Quantity', 'Price'])
            for item in self.inventory:
                writer.writerow([item.name, item.quantity, item.price])

def main():
    inventory_system = InventoryManagementSystem()
    while True:
        print('1. Add Item')
        print('2. Remove Item')
        print('3. Update Item')
        print('4. Display Inventory')
        print('5. Load Inventory')
        print('6. Save Inventory')
        print('7. Quit')
        choice = input('Enter your choice: ')
        if choice == '1':
            name = input('Enter the name of the item: ')
            quantity = int(input('Enter the quantity of the item: '))
            price = float(input('Enter the price of the item: '))
            item = InventoryItem(name, quantity, price)
            inventory_system.add_item(item)
        elif choice == '2':
            name = input('Enter the name of the item to remove: ')
            inventory_system.remove_item(name)
        elif choice == '3':
            name = input('Enter the name of the item to update: ')
            quantity = input('Enter the new quantity (leave blank to skip): ')
            price = input('Enter the new price (leave blank to skip): ')
            inventory_system.update_item(name,
                                        int(quantity) if quantity else None,
                                        float(price) if price else None)
        elif choice == '4':
            inventory_system.display_inventory()
        elif choice == '5':
            inventory_system.load_inventory('inventory.csv')
        elif choice == '6':
            inventory_system.save_inventory()
        elif choice == '7':
            break
if __name__ == '__main__':
    main()

