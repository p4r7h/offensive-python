import urllib, sys

def progress(nblocks, block_size, file_size) :
	print (nblocks*block_size*100)/float(file_size)
# we are passing 3 arguments in wich number of blocks , block_size and file size

url = "download file url"
# download file url

local_file = "name of file"
# this contain name of the file u want to save at localy

urllib.urlretrieve(url, local_file, progress)
# call urlretrieve contain 3 argumets url , local file name and progress function that indicattes the progress of downloading
