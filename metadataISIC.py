import os
import json
import pandas as pd
import shutil 
def moveImg(destination, data):
	source = r'C:/Users/bruno/OneDrive/Desktop/ISIC-Archive-Downloader-master/Data/Images'
	images = os.listdir(source)
	print(images)
	aux = False
	for i in data:
		for j in images:
			if (i == j[:len(j)-5]):
				shutil.move(f"{source}/{j}", destination)
				aux = True
			elif (i == j[:len(j)-3]):
				shutil.move(f"{source}/{j}", destination)
				aux = True
	return aux

source = r'C:/Users/bruno/OneDrive/Desktop/ISIC-Archive-Downloader-master/Data/Descriptions'
description = os.listdir(source)
ids = list()
for i in range(len(description)):
	with open(source + '/' +description[i]) as json_file:
		data = json.load(json_file)
		confirm = data['meta']['clinical']
		if ('diagnosis' in data['meta']['clinical']):	
			diagnosis = data['meta']['clinical']['diagnosis']
			if (diagnosis == 'melanoma'):
				ids.append(description[i])
# age = list()
# anatom_site = list()
# bening_malignant = list()
# sex = list()
# melanocytic = list()
# for i in range(len(ids)):
# 	with open(source + '/' + ids[i]) as json_file:
# 		data = json.load(json_file)
# 		if('age_approx' in data['meta']['clinical']):
# 			age.append(data['meta']['clinical']['age_approx'])
# 		else:
# 			age.append('')
# 		if('anatom_site_general' in data['meta']['clinical']):
# 			anatom_site.append(data['meta']['clinical']['anatom_site_general'])
# 		else:
# 			anatom_site.append('')
# 		if('sex' in data['meta']['clinical']):
# 			sex.append(data['meta']['clinical']['sex'])
# 		else:
# 			sex.append('')
# 		# anatom_site.append(data['meta']['clinical']['anatom_site_general'])
# 		# bening_malignant.append(data['meta']['clinical']['benign_malignant'])
# 		# sex.append(data['meta']['clinical']['sex'])
# 		# melanocytic.append(data['meta']['clinical']['melanocytic'])

# metada = {'id': ids,'age':age,'sex':sex, 'anatom_site':anatom_site,}
# df = pd.DataFrame(metada)
# df.to_csv('MetadataMelanomISIC.csv')
# print(ids)
destination = 'C:/Users/bruno/OneDrive/Desktop/ISIC-Archive-Downloader-master/Data/ImagesMelISIC'
images = moveImg(destination, ids)