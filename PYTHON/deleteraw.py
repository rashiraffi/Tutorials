import os
i=0
folder_raw = '/home/rashi/Pictures/Tharang_2020/Day_02/DCIM/RAW'
folder_jpeg = '/home/rashi/Pictures/Tharang_2020/Day_02/DCIM/100MSDCF'
lst_jpeg = os.listdir(folder_jpeg)
lst_raw = os.listdir(folder_raw)
"""for filename in os.listdir(folder_raw):
	f_name=filename[0:len(filename)-3]+"JPG"
	if(f_name in lst_jpeg):
		pass
	else:
		path = os.path.join(folder_raw, filename)
		os.remove(path)
		i=i+1
print(i)"""
for filename in os.listdir(folder_jpeg):
	f_name=filename[0:len(filename)-3]+"ARW"
	if(f_name in lst_raw):
		pass
	else:
		i=i+1
		print(filename)
print(i)
