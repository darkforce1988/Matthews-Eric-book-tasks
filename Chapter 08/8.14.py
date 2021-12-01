def car_information(manufacturer, car_model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = car_model
    return car_info


car = car_information(
    'Bentley',
    'Turbo-R',
    color='grey',
    pedal_extenders=True,
    )

print("Your car information:\n\t")
for car_info_type, car_info_value in car.items():
    print(f"{car_info_type}: '{car_info_value}'")
