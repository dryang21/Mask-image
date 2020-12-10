import os
from PIL import Image
import numpy as np

img_dir=r'C:\Users\dongr\Desktop\lung_mask_data\covid_mask\COVID19_DATA'
mask_dir=r'C:\Users\dongr\Desktop\lung_mask_data\covid_mask\manually_processed_mask'
save_dir=r'C:\Users\dongr\Desktop\lung_mask_data\covid_masked'


masks=os.listdir(mask_dir)
imgs=os.listdir(img_dir)
for maskname in masks:

	mask_path=os.path.join(mask_dir,maskname)
	mask=Image.open(mask_path).convert('L')
	mask=np.asarray(mask)
	print('mask',mask.shape)
	#print(type(mask))
	number=maskname.split('_mask')[0]

	for imgname in imgs:
		if number in imgname:
			img_path=os.path.join(img_dir,imgname)
			img=Image.open(img_path).convert('RGB')
			print('img mode',img.mode)
			img= np.asarray(img)
			
			img= img.transpose(2,0,1)
			print('img',img.shape)
			masked=np.multiply(mask,img)
			masked=masked.transpose(1,2,0)

			print('masked',masked.shape)
			masked= Image.fromarray(masked.astype(np.uint8))
			print('masked mode',masked.mode)
			maskedname= save_dir+r'\masked_'+number+'.png'
			

			masked.save(maskedname,'PNG')

