import pandas as pd
import shutil 
import os

def melanom (dataset):
	data1 = list()
	data2 = list()
	data3 = list()
	data4 = list()
	for i in range(len(dataset['lesion_id'])):
		if (dataset['dx'][i] == 'mel'):
			data1.append(dataset['image_id'][i])
			data2.append(dataset['age'][i])
			data3.append(dataset['sex'][i])
			data4.append(dataset['localization'][i])
	return data1,data2,data3,data4
def moveImg(destination, data):
	source = r'C:/Users/bruno/OneDrive/Desktop/cancer piel - Copy/HAM10000_images_part_2'
	images = os.listdir(source)
	aux = False
	for i in data:
		for j in images:
			if (i == j[:len(j)-4]):
				shutil.move(f"{source}/{j}", destination)
				aux = True
	return aux

data = pd.read_csv('HAM10000_metadata.csv')
data1, data2, data3, data4 = melanom(data)

# newdata = {'image_id': data1,'age': data2, 'sex': data3, 'localization': data4}
# df = pd.DataFrame(newdata)
# df.to_csv('MetadataMelanom.csv')

destination = 'C:/Users/bruno/OneDrive/Desktop/cancer piel - Copy/ImgMel'
images = moveImg(destination, data1)

print (images)
