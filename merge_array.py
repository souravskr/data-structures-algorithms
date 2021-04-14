def merge_lists(original_ist, add_ist, delete_list):
    # Make hash table from original and add list to get unique item
    dict_out = {}
    for i in original_ist+add_ist:
        dict_out[i] = len(i)  # add the length of the each string as value

    # Remove items from the hash table according to delete_list
    for i in delete_list:
        dict_out.pop(i)

    # reverse the hastable and group by based on strings' length
    group_dict = {}
    for key, value in dict_out.items():
        if value not in group_dict:
            group_dict[value] = [key]
        else:
            group_dict[value].append(key)

    # Get the maximum key, reverse its value and add to out_arr
    out_arr = []
    for _ in range(len(group_dict)):
        max_key = max(group_dict, key=int)
        out_arr += (sorted(group_dict[max_key], reverse=True))
        group_dict.pop(max_key)

    return out_arr


original_ist = ['one', 'two', 'three', 'four']
add_ist = ['one', 'two', 'five', 'six']
delete_list = ['two', 'five']

print(merge_lists(original_ist, add_ist, delete_list))
