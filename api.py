import pandas as pd

def get_dir():
	directory =  pd.read_json('/home/ankit/project/JSON_files/filedir.json')
	return directory

def get_json_file(path):
	file = pd.read_json(path)
	return file

def post_dir(file_path,data_path):
	directory =  pd.read_json('/home/ankit/project/JSON_files/filedir.json')
	directory.filedir.append(file_path)
	directory.datadir.append(data_path)

