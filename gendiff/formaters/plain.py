def format_string(val):
    if isinstance(val, dict):
        return '[complex value]'
    elif isinstance(val, str):
        return f"'{val}'"
    else:
        return val


def plain(diff, current_key=''):
    result = []
    for k, v in diff.items():
        status = v['status']
        match status:
            case 'added':
                if isinstance(v['value'], dict):
                    result.append(
                        f"Property '{current_key}{k}'\
 was added with value: [complex value]"
                    )
                else:
                    result.append(
                        f"Property '{current_key}{k}'\
 was added with value: '{v['value']}'"
                    )
            case 'deleted':
                result.append(f"Property '{current_key}{k}' was removed")
            case 'changed':
                initial_val = format_string(v['initial_value'])
                current_val = format_string(v['current_value'])
                result.append(
                    f"Property '{current_key}{k}'\
 was updated. From {initial_val} to {current_val}"
                )
            case 'unchanged':
                if isinstance(v['value'], dict):
                    cur_key = f'{current_key}{k}.'
                    val = v['value']
                    result.append(plain(val, cur_key))
    return '\n'.join(result)\
        .replace(" 'False'", " false")\
        .replace(" 'True'", " true")\
        .replace(" 'None'", " null")
