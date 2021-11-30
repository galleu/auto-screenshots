import glob
import img2pdf
import sys

with open("name.pdf","wb") as f:
    filepath = sys.argv[1]

    indexs = glob.glob(filepath+"/*.png")
    name_list = []
    index_list = []
    for i in indexs:
        i = int(i.replace("\\", "/").split("/")[-1].split(".")[0])
        index_list.append(i)
    index_list.sort()

    for i in index_list:
        name_list.append(filepath+"/"+str(i)+".png")

    print(name_list)
    f.write(img2pdf.convert(name_list))
