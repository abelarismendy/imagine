import json
import yaml

def yaml_to_json(yaml_file, json_file):
    with open(yaml_file, 'r', encoding='utf-8') as f:
        yaml_data = yaml.safe_load(f)

    integrantes = {}
    for key, value in yaml_data.items():
        integrante = value
        if 'image' in integrante and integrante['image'].startswith('/img/people/'):
            integrante['image'] = integrante['image'][len('/img/people/'):]
            integrante['image'] = integrante['image'].split('.')[0] + '.jpg'
        integrantes[key.split('-')[-1]] = integrante

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(integrantes, f, ensure_ascii=False, indent=4)

yaml_to_json('./_data/people.yml', './_data/people.json')
