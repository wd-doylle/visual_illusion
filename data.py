import os
import sys
import shutil
import random

illusion = sys.argv[1]
non_illusion = sys.argv[2]

files = {}
files['illusion'] = []
i = 0
for p in os.walk(illusion):
	if p[2]:
		for f in p[2]:
			files['illusion'].append([p[0],f,i])
		i += 1
i = 0
files['non_illusion'] = []
for p in os.walk(non_illusion):
	if p[2]:
		for f in p[2]:
			files['non_illusion'].append([p[0],f,i])
		i += 1			

os.makedirs("data", exist_ok=True)
train_path = os.path.join("data","train")
val_path = os.path.join("data","val")
gen_path = os.path.join("data","gen")
os.makedirs(train_path, exist_ok=True)
os.makedirs(val_path, exist_ok=True)
os.makedirs(gen_path, exist_ok=True)

for typ in ['illusion','non_illusion']:
	random.shuffle(files[typ])
	# print(os.path.join(files[typ][0][0],files[typ][0][1]))
	os.makedirs(os.path.join(train_path,typ), exist_ok=True)
	os.makedirs(os.path.join(val_path,typ), exist_ok=True)
	os.makedirs(os.path.join(gen_path,typ), exist_ok=True)
	for f in files[typ][:450]:
		shutil.copyfile(os.path.join(f[0],f[1]),os.path.join(train_path,typ,str(f[2])+f[1]))
		shutil.copyfile(os.path.join(f[0],f[1]),os.path.join(gen_path,typ,str(f[2])+f[1]))
	for f in files[typ][450:569]:
		shutil.copyfile(os.path.join(f[0],f[1]),os.path.join(val_path,typ,str(f[2])+f[1]))
		shutil.copyfile(os.path.join(f[0],f[1]),os.path.join(gen_path,typ,str(f[2])+f[1]))