import json
import sys
#from read_write_file import *
import os
from tika import *

# json_dir=sys.argv[1]
curdir = os.getcwd()
anno_output_path = curdir

width = int(27)
height = int(18)

print(width, height)


def read_yolo_file(data_input_path):
    width = int(27)
    height = int(18)
    fl = {}
    sl = {}
    tl = {}
    print(width, height)
    li = []
    filename = data_input_path.split('/')[-1]
    
    with open(data_input_path, 'r') as f:
        fg = f.readlines()
    print(fg)
    print("===")
    no_of_lines=len(fg)
    
    for i in fg:
        print(i)
        print(len(i.split(" ")))
        if((len(i.split(" ")))>1):

                l = i.rsplit("\n")
                print(l)
                label = l[0].split(" ")[0]

                xc = (float(l[0].split(" ")[1]))*width

                yc = (float(l[0].split(" ")[2]))*height

                wi = (float(l[0].split(" ")[3]))*width

                he = (float(l[0].split(" ")[4]))*height

                xa = xc+(wi/2)
                ya = yc-(he/2)
                xi = xc-(wi/2)
                yi = yc+(he/2)

                li.append({"classification_label": label, "point_2D": [
                            str(str(xa)+","+str(ya)), str(str(xi)+","+str(yi))]})
                tl["bounding_box"] = li            

        else:
            l = i.rsplit("\n")
            print(l)
            label = l[0].split(" ")[0]
            li.append({"classification_label": label })
           

            tl["image_classification"] = li

            
    sl["data_filename"] =filename
    sl["data_type"] = "image"
    sl["data_annotation"] = tl
    fl["annotation"] = sl



    
    return fl



def write_yolo_file(obj, anno_file_output_path):
    
    f = obj
    output_filename=f['annotation']['data_filename']
    out = open(anno_file_output_path+'/'+output_filename.split('.')[0]+'.txt', 'a+')
    print(list(f["annotation"]["data_annotation"].keys()))
    print("=============")
    if("bounding_box" in list(f["annotation"]["data_annotation"].keys())):
        for i in range(len(f["annotation"]["data_annotation"]["bounding_box"])):
            fn = f["annotation"]["data_annotation"]["bounding_box"][i]["classification_label"]
            li = f["annotation"]["data_annotation"]["bounding_box"][i]["point_2D"]
            print(li)
            [x_min, y_min] = li[0].split(",")
            print([x_min, y_min])
            [x_max, y_max] = li[1].split(",")
            hei = int(y_max)-int(y_min)
            wid = int(x_max)-int(x_min)
            x_centre = int(x_max)-(wid/2)
            y_centre = int(y_max)-(hei/2)
            out.write(str(fn)+" ")
            out.write(str(x_centre)+" ")
            out.write(str(y_centre)+" ")
            out.write(str(wid)+" ")
            out.write(str(hei)+" "+"\n")
    else:
            for i in range(len(f["annotation"]["data_annotation"]["image_classification"])):
                fn = f["annotation"]["data_annotation"]["image_classification"][i]["classification_label"]
                
                out.write(str(fn)+" ")
                print("\n")




def yolo_tjson_file(yolo_file, anno_output_path=curdir):
    obj=read_yolo_file(yolo_file)
    write_tika_json_file(obj,anno_output_path)


def yolo_tjson_dir(yolo_dir, anno_output_path=curdir):
    for filename in  os.listdir(yolo_dir):
        obj=read_yolo_file(yolo_dir+'/'+filename)
        write_tika_json_file(obj,anno_output_path)


def yolo_tjson_obj(yolo_obj):
    for i in range(len(yolo_obj)):
        l = yolo_obj[i]
        lx = []
        fn = l[0].split(" ")[0]

        xc = (float(l[0].split(" ")[1]))*width

        yc = (float(l[0].split(" ")[2]))*height

        wi = (float(l[0].split(" ")[3]))*width

        he = (float(l[0].split(" ")[4]))*height

        xa = xc+(wi/2)
        ya = yc-(he/2)
        xi = xc-(wi/2)
        yi = yc+(he/2)

        lx.append({"classification_label": fn, "point_2D": [xa, ya, xi, yi]})

    tl = {}

    tl["bounding_box"] = lx

    fl = {}
    sl = {}
    sl["data_filename"] = "ina.jfif"
    sl["data_type"] = "image"
    sl["data_annotation"] = tl
    fl["annotation"] = sl

    return fl


def tjson_yolo_file(tjson_file, anno_output_path=curdir):
    obj=read_tika_json_file(tjson_file)
    write_yolo_file(obj,anno_output_path)


def tjson_yolo_dir(json_dir, anno_output_path=curdir):
    os.makedirs(json_dir+'meta')
    for filename in os.listdir(json_dir):
        if filename.endswith(".json"):
           obj=read_tika_json_file(json_dir+'/'+filename)
           write_yolo_file(obj,anno_output_path)


def tjson_yolo_obj(f):
    out1 = []
    for i in range(len(f["annotation"]["data_annotation"]["bounding_box"])):
        fn = f["annotation"]["data_annotation"]["bounding_box"][i]["classification_label"]
        li = f["annotation"]["data_annotation"]["bounding_box"][i]["point_2D"]
        print(li)
        [x_min, y_min] = li[0].split(",")
        print([x_min, y_min])
        [x_max, y_max] = li[1].split(",")
        hei = int(y_max)-int(y_min)
        wid = int(x_max)-int(x_min)
        x_centre = int(x_max)-(wid/2)
        y_centre = int(y_max)-(hei/2)
        out = []
        out.append(str(fn)+" ")
        out.append(str(x_centre)+" ")
        out.append(str(y_centre)+" ")
        out.append(str(wid)+" ")
        out.append(str(hei)+" "+"\n")
        out1.append(out)
    return out1           
