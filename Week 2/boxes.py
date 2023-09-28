import math
no_of_manufactured_items = float(input('Enter the number of items: '))
no_of_items_user_packs_per_box = float(input('Enter the number of items per box: '))

needed_boxes = math.ceil(no_of_manufactured_items/no_of_items_user_packs_per_box)

print(f'for {no_of_manufactured_items}, packing {no_of_items_user_packs_per_box} in each \
box, you will need {needed_boxes} boxes')
