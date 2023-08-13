def log(title,content):
	color_dic={
		'ERROR':'\033[37;41m',
		'INFO':'\x1b[30;47m',
		'SUCCESS':'\x1b[37;42m'
	}
	print('[LOG]'+color_dic[title]+title+'\033[0m:',content)