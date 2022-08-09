import pandas as pd
source_HAM = 'C:/Users/bruno/OneDrive/Desktop/cancer piel - Copy/MetadataMelanom.csv'
source_ISIC ='C:/Users/bruno/OneDrive/Desktop/ISIC-Archive-Downloader-master/MetadataMelanomISIC.csv' 

df_HAM = pd.read_csv(source_HAM)
df_ISIC = pd.read_csv(source_ISIC)



Id_images = list()
Age = list()
sex = list()
localization = list()

for i in range(len(df_HAM['sex'])):
	Id_images.append(df_HAM['image_id'][i])
	Age.append(df_HAM['age'][i])
	sex .append(df_HAM['sex'][i])
	localization.append(df_HAM['localization'][i])
for j in range(len(df_ISIC['sex'])):
	Id_images.append(df_ISIC['id'][j])
	Age.append(df_ISIC['age'][j])
	sex .append(df_ISIC['sex'][j])
	localization.append(df_ISIC['anatom_site'][j])

newdata = {'image_id': Id_images,'age': Age, 'sex': sex, 'localization': localization}
df = pd.DataFrame(newdata)
df.to_csv('MetadataMelanomBoth.csv')
