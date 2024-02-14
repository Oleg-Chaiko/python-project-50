def stylish(diff, counter=-2):
    if not isinstance(diff, dict):
        res = str(diff) + '\n'
        return res
    counter += 4
    result = '{\n'
    for key, val in diff.items():
        result += generate_string(key, val, counter)
    ind = ' ' * (counter - 2)
    result += ind + '}' + '\n'
    return result.replace(": False", ": false")\
        .replace(": True", ": true")\
        .replace(": None", ": null")


def generate_string(key, val, counter):
    indent = ' ' * counter
    status = val['status']
    if status == 'unchanged':
        value = val['value']
        res = f'{indent}  {key}: {stylish(value, counter)}'
        return res
    elif status == 'added':
        value = val['value']
        res = f'{indent}+ {key}: {stylish(value, counter)}'
        return res
    elif status == 'deleted':
        value = val['value']
        res = f'{indent}- {key}: {stylish(value, counter)}'
        return res
    elif status == 'changed':
        in_value = val['initial_value']
        cur_value = val['current_value']
        res = f'{indent}- {key}: {stylish(in_value, counter)}{indent}\
+ {key}: {stylish(cur_value, counter)}'
        return res
