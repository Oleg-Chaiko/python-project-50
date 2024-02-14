def generate_diff(dict_1, dict_2):
    keys = sorted(dict_1.keys() | dict_2.keys())
    diff_dict = {}
    for key in keys:
        dictionary = {}
        if key not in dict_2:
            dictionary[key] = {
                'status': 'deleted',
                'value': generate_diff(dict_1[key], dict_1[key])
                if isinstance(dict_1[key], dict)
                else dict_1[key]
            }
        elif key not in dict_1:
            dictionary[key] = {
                'status': 'added',
                'value': generate_diff(dict_2[key], dict_2[key])
                if isinstance(dict_2[key], dict)
                else dict_2[key]
            }
        elif dict_1[key] == dict_2[key]:
            dictionary[key] = {
                'status': 'unchanged',
                'value': generate_diff(dict_1[key], dict_2[key])
                if isinstance(dict_1[key], dict)
                else dict_1[key]
            }
        elif dict_1[key] != dict_2[key]:
            dictionary = changed_val(dict_1, dict_2, key)
        diff_dict.update(dictionary)
    return diff_dict


def changed_val(dict_1, dict_2, key):
    stat_value_1 = isinstance(dict_1[key], dict)
    stat_value_2 = isinstance(dict_2[key], dict)
    dict_ = {}
    if stat_value_1 and stat_value_2:
        dict_[key] = {
            'status': 'unchanged',
            'value': generate_diff(dict_1[key], dict_2[key])
        }
    elif stat_value_1 and not stat_value_2:
        dict_[key] = {
            'status': 'changed',
            'initial_value': generate_diff(dict_1[key], dict_1[key]),
            'current_value': dict_2[key]
        }
    elif stat_value_2 and not stat_value_1:
        dict_[key] = {
            'status': 'changed',
            'initial_value': dict_1[key],
            'current_value': generate_diff(dict_2[key], dict_2[key])
        }
    else:
        dict_[key] = {
            'status': 'changed',
            'initial_value': dict_1[key],
            'current_value': dict_2[key]
        }
    return dict_
