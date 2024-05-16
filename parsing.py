import os
import yaml

def flatten_dict(d, parent_key='', sep='_'):
    items = {}
    for key, value in d.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.update(flatten_dict(value, new_key, sep=sep))
        else:
            items[new_key] = str(value)
    return items

with open('input.yaml', 'r') as file:
    data = yaml.safe_load(file)

flattened_data = flatten_dict(data)

with open(os.environ['GITHUB_ENV'], 'a') as github_env_file:
    for key, value in flattened_data.items():
        os.environ[key] = value
        github_env_file.write(f"{key}={value}\n")
