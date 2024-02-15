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
                if isinstance(v['initial_value'], dict):
                    in_val = '[complex value]'
                else:
                    in_val = v['initial_value']
                if isinstance(v['current_value'], dict):
                    cur_val = '[complex value]'
                else:
                    cur_val = v['current_value']
                result.append(
                    f"Property '{current_key}{k}'\
 was updated. From '{in_val}' to '{cur_val}'"
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
