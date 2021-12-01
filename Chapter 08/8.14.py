def view_car_information(manufacturer, car_model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = car_model
    return car_info


car = view_car_information(
    'Bentley',
    'Turbo-R',
    color='grey',
    pedal_extenders=True,
    )

print("Your car information:")
for car_info_key, car_info_value in car.items():
    print(f"\t{car_info_key}: '{car_info_value}'")
