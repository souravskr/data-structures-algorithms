# def sortBoxes(boxList):
#     # boxList.sort(key=str)
#     # return boxList
#     my_dict = {}
#     for box in boxList:
#         for char in box:
#             print(char)
#             if char.isalnum() or char.isdigit():
#                 print(char)
#
#
# my_list = [['ykc 82 01'],
#            ['eo first qpx'],
#            ['09z cat hamster'],
#            ['06f 12 25 6'],
#            ['az0 first qpx'],
#            ['236 cat dog rabbit snake']]
# print(sortBoxes(my_list))

def getItems(entries):
    # Write your code here
    product_dict = {}
    for item in entries:
        if 'INSERT' in item:
            price = int(item[2])
            if price in product_dict:
                product_dict[price].append(item[1])
            product_dict[price] = [item[1]]
    sort_price = []
    for price in product_dict:
        sort_price.append(price)
    sort_price.sort()
    for price in sort_price:
        print(product_dict[price].sort())


entries = [['INSERT', 'milk', '4'], ['INSERT', 'coffee', '3'], ['VIEW', '-', '-'], ['INSERT', 'pizza', '5'],
           ['INSERT', 'gum', '1'], ['VIEW', '-', '-']]

print(getItems(entries))
