
# coding=utf-8
import tinify
import os
import os.path




AppKey = "App_Key" # AppKey
fromFilePath = "./res/images" # 需要压缩图片文件夹
toFilePath = "./pressedImag" # 压缩后存放位置


def mkOutPutDir():
	if os.path.isdir(toFilePath):
		pass
	else:
		os.mkdir(toFilePath)

def compressFolderImages():
	for file in os.listdir(fromFilePath):
		filePath = os.path.join(fromFilePath, file)
		if os.path.isfile(filePath):
			fileName, fileSuffix = os.path.splitext(file)
			if fileSuffix == '.png' or fileSuffix == '.jpg':
				toFullName = toFilePath + '/' + file
				print 'compressing ', filePath , "into " , toFullName
				source = tinify.from_file(filePath)
				source.to_file(toFullName)

if __name__ == '__main__':
	mkOutPutDir()
	try:
		tinify.key = AppKey
		tinify.validate
		compressFolderImages()
	except tinify.Error, e:
		print tinify.Error , e
	
	print "compres complete !"