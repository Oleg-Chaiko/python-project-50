import json
import yaml


def parser(path):
    format = path.split('.')[-1]
    try:
        with open(path) as file:
            match format:
                case 'json':
                    data = json.load(file)
                case 'yaml' | 'yml':
                    data = yaml.load(file, Loader=yaml.CLoader)
            return data
    except (FileNotFoundError) as err:
        return err
