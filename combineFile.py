import os

filepath = '/Users/zhangtianqi/desktop/music_box_project/data/play'
filelist = os.listdir(filepath)

finalFile = open('all_play.log', 'w')

for filename in filelist:
	if filename.endswith(".log"):
		with open(filename, 'r') as f:
			for line in f:
				line = line.split('\t')
				if (len(line) >= 5):
					line = line[0] + '\t' + line[1] + '\t' + filename[:8] + '\n'
					finalFile.write(line)
		print ('File %s Complete' % filename)
finalFile.close()
