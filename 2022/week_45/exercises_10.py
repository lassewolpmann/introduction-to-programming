def task_1():
    inventory = {
        "potato": 15,
        "apple": 10,
        "kiwi": 13,
        "turnip": 7

    }
    price = {
        "potato": 1,
        "apple": 2,
        "kiwi": 1.5,
        "turnip": 0.5
    }

    # Add 10 new potatoes and 5 new pears priced at 1.5
    current_potato_stock = inventory.get('potato')
    inventory.update({'potato': current_potato_stock + 10})

    inventory.update({'pear': 5})
    price.update({'pear': 1.5})

    # Raise all prices by 10%
    for item in price:
        current_price = price.get(item)
        new_price = round(current_price * 1.1, 2)
        price.update({item: new_price})

    # Calculate total worth of inventory
    if inventory.keys() == price.keys():
        total_worth = 0

        for item in inventory:
            item_count = inventory.get(item)
            item_price = price.get(item)
            total_worth += round(item_count * item_price, 2)

        print(f'Total worth of inventory is {total_worth}')

    else:
        print('Inventory and Price list contain mismatched keys')


def task_2():
    def convert_dict(dict_data):
        return {value: key for key, value in dict_data.items()}

    example1 = {100: "velocity", 101: "humidity", 102: "SNR", 103: "RSSI"}
    example2 = convert_dict(example1)
    print(example2)


def task_3():
    import random

    random.seed(111)

    a = {'sensors': []}
    for ind in range(0, 1000):
        a['sensors'].append({})
        a['sensors'][ind]['sensor-name'] = f'aaa-{ind + 1}'
        a['sensors'][ind]['temperature'] = random.randint(0, 30)
        a['sensors'][ind]['humidity'] = random.randint(0, 100)

    b = {}
    for ind in range(0, 1000):
        sensor_name = f'bbb-{ind + 1}'
        b[sensor_name] = {}
        b[sensor_name]['temperature'] = random.randint(0, 30)
        b[sensor_name]['humidity'] = random.randint(0, 100)

    def print_a(sensor):
        # Since we're using a list, we can not access the desired values by its key value, but instead have to loop
        # through the entire list, to find a matching list item.
        for sensor_values in a['sensors']:
            if sensor_values['sensor-name'] == sensor:
                print(f'Values for sensor: {sensor}')
                print(f'Temperature: {sensor_values["temperature"]}')
                print(f'Humidity: {sensor_values["humidity"]}')

    def print_b(sensor):
        # Here we're using a dictionary, meaning we can access the desired values directly by the key value.
        sensor_values = b[sensor]
        print(f'Values for sensor: {sensor}')
        print(f'Temperature: {sensor_values["temperature"]}')
        print(f'Humidity: {sensor_values["humidity"]}')

    print_a('aaa-100')
    print_b('bbb-100')


def task_4():
    letter_list = ['aaaa', 'bbbb', 'aaaa', 'cccc', 'cccc', 'bbbb', 'cccc']
    count_dict = {}

    # Using nested loops
    for item in letter_list:
        count = 0
        for value in letter_list:
            if item == value:
                count += 1

        count_dict.update({item: count})

    # Using count method
    for item in letter_list:
        count_dict.update({item: letter_list.count(item)})

    print(f'The string "cccc" appeared {count_dict["cccc"]} times.')


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
