import json
from os import environ
from pathlib import Path


if path := environ.get('APPDATA'):
	APP_DATA = Path(path)
else:
	raise Exception('Could not locate AppData folder.')

EXPORTS = Path('./exports/')
EXPORTS.mkdir(exist_ok=True, parents=True)

FACTORIO_MODS_PATH = APP_DATA.joinpath(Path('Factorio/mods'))
MOD_LIST_FILE = Path('mod-list.json')


modpack_name = input('Name: ')
modpack_title = input('Title: ')
modpack_version = input('Version: ')
factorio_version = input('Factorio Version: ')
modpack_author = input('Author: ')
modpack_homepage = input('Homepage: ')
modpack_description = input('Description: ')


MODPACK_JSON = {
	'name': modpack_name,
	'version': modpack_version,
	'factorio_version': factorio_version,
	'title': modpack_title,
	'author': modpack_author,
	'homepage': modpack_homepage,
	'description': modpack_description,
	'dependencies': []
}


with open(FACTORIO_MODS_PATH.joinpath(MOD_LIST_FILE).as_posix(),'r') as file:
	data = json.loads(file.read())

for mod in data['mods']:
	if mod['enabled']:
		print('Adding', mod['name'])
		MODPACK_JSON['dependencies'].append(mod['name'])


MODPACK_EXPORT = Path(f"{MODPACK_JSON['name']}_{MODPACK_JSON['version']}")

export_path = EXPORTS.joinpath(MODPACK_EXPORT)
export_path.mkdir(exist_ok=True, parents=True)

with open(export_path.joinpath('info.json').as_posix(), 'w') as file:
	file.write(json.dumps(MODPACK_JSON, indent=4))
