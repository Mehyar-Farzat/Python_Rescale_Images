from PIL import Image
import os

fit_size =  int(input('Enter size : '))
output_folder = input('Enter Output folder name :')

os.chdir("D:\Automation_1\images")

if not os.path.isdir(output_folder):
    os.mkdir(output_folder)

for filename in os.listdir('.'):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        image=Image.open(filename)
        width, height =image.size

        if width > fit_size and height > fit_size:
            if width > height:
                height = int((fit_size/width)*height)
                width = fit_size
            
            else:
                width= int((fit_size/height)*width)
                height = fit_size
            print('Hi')

            image2 = image.resize((width,height))
            image2.save(os.path.join(output_folder,filename.lower()))
print('DONE ..... ')

