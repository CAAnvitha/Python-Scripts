import os
import json
import sys


curdir=os.getcwd()
def cocojson_tjson_dir(json_dir,anno_output_path=curdir):

    with open(json_dir) as json_file:
      f= json.load(json_file)
    
    for i in range(len(f["images"])):
        out={}
        sl={}
        tl={}
        tl["b_box"]=[]
        image_id=f["images"][i]["id"]
        filename=f["images"][i]["file_name"]
        string_1=str(f["images"][i]["file_name"])
        name_of_the_file=string_1.split('.')[0]

        
        for item in range(len(f['annotations'])):
            if(image_id==f["annotations"][j]["image_id"]):
                li=f["annotations"][item]["bbox"]
                category_id=f["annotations"][j]["category_id"]


                for element in range(len(f['categories'])):
                    if(category_id==f["categories"][element]["id"]):
                        pname=f["categories"][element]["name"]
                        tl["b_box"].append({"classification_label":pname,"point_2D":li})
        sl[str("data_filename")]=filename
        sl["data_type"]="image"
        sl["data_annotation"]=tl
        out["annotation"]=sl

        fp=open(anno_output_path+'//' + name_of_the_file +'.json','w')
        fp.write(json.dumps(out))
        fp.close()
            


#tika json to cocojson

def tjson_cocojson_dir(json_dir,anno_output_path=curdir):
    
    j=0
    coco_json={}
    coco_json["incoco_jsono"]={}
    coco_json["images"]=[]
    coco_json["annotation"]=[]
    l=[
        {"supercategory": "person","id": 1,"name": "person"},
        {"supercategory": "vehicle","id": 2,"name": "bicycle"},
        {"supercategory": "vehicle","id": 3,"name": "car"},
        {"supercategory": "vehicle","id": 4,"name": "motorcycle"},
        {"supercategory": "vehicle","id": 5,"name": "airplane"},
        {"supercategory": "vehicle","id": 6,"name": "bus"},
        {"supercategory": "vehicle","id": 7,"name": "train"},
        {"supercategory": "vehicle","id": 8,"name": "truck"},
        {"supercategory": "vehicle","id": 9,"name": "boat"},
        {"supercategory": "outdoor","id": 10,"name": "traffic light"},
        {"supercategory": "outdoor","id": 11,"name": "fire hydrant"},
        {"supercategory": "outdoor","id": 13,"name": "stop sign"},
        {"supercategory": "outdoor","id": 14,"name": "parking meter"},{"supercategory": "outdoor","id": 15,"name": "bench"},{"supercategory": "animal","id": 16,"name": "bird"},{"supercategory": "animal","id": 17,"name": "cat"},{"supercategory": "animal","id": 18,"name": "dog"},{"supercategory": "animal","id": 19,"name": "horse"},{"supercategory": "animal","id": 20,"name": "sheep"},{"supercategory": "animal","id": 21,"name": "cow"},{"supercategory": "animal","id": 22,"name": "elephant"},{"supercategory": "animal","id": 23,"name": "bear"},{"supercategory": "animal","id": 24,"name": "zebra"},{"supercategory": "animal","id": 25,"name": "giraffe"},{"supercategory": "accessory","id": 27,"name": "backpack"},{"supercategory": "accessory","id": 28,"name": "umbrella"},{"supercategory": "accessory","id": 31,"name": "handbag"},{"supercategory": "accessory","id": 32,"name": "tie"},{"supercategory": "accessory","id": 33,"name": "suitcase"},{"supercategory": "sports","id": 34,"name": "frisbee"},{"supercategory": "sports","id": 35,"name": "skis"},{"supercategory": "sports","id": 36,"name": "snowboard"},{"supercategory": "sports","id": 37,"name": "sports ball"},{"supercategory": "sports","id": 38,"name": "kite"},{"supercategory": "sports","id": 39,"name": "baseball bat"},{"supercategory": "sports","id": 40,"name": "baseball glove"},{"supercategory": "sports","id": 41,"name": "skateboard"},{"supercategory": "sports","id": 42,"name": "surfboard"},{"supercategory": "sports","id": 43,"name": "tennis racket"},{"supercategory": "kitchen","id": 44,"name": "bottle"},{"supercategory": "kitchen","id": 46,"name": "wine glass"},{"supercategory": "kitchen","id": 47,"name": "cup"},{"supercategory": "kitchen","id": 48,"name": "fork"},{"supercategory": "kitchen","id": 49,"name": "knife"},{"supercategory": "kitchen","id": 50,"name": "spoon"},{"supercategory": "kitchen","id": 51,"name": "bowl"},{"supercategory": "food","id": 52,"name": "banana"},{"supercategory": "food","id": 53,"name": "apple"},{"supercategory": "food","id": 54,"name": "sandwich"},{"supercategory": "food","id": 55,"name": "orange"},{"supercategory": "food","id": 56,"name": "broccoli"},{"supercategory": "food","id": 57,"name": "carrot"},{"supercategory": "food","id": 58,"name": "hot dog"},{"supercategory": "food","id": 59,"name": "pizza"},{"supercategory": "food","id": 60,"name": "donut"},{"supercategory": "food","id": 61,"name": "cake"},{"supercategory": "furniture","id": 62,"name": "chair"},{"supercategory": "furniture","id": 63,"name": "couch"},{"supercategory": "furniture","id": 64,"name": "potted plant"},{"supercategory": "furniture","id": 65,"name": "bed"},{"supercategory": "furniture","id": 67,"name": "dining table"},{"supercategory": "furniture","id": 70,"name": "toilet"},{"supercategory": "electronic","id": 72,"name": "tv"},{"supercategory": "electronic","id": 73,"name": "laptop"},{"supercategory": "electronic","id": 74,"name": "mouse"},{"supercategory": "electronic","id": 75,"name": "remote"},{"supercategory": "electronic","id": 76,"name": "keyboard"},{"supercategory": "electronic","id": 77,"name": "cell phone"},{"supercategory": "appliance","id": 78,"name": "microwave"},{"supercategory": "appliance","id": 79,"name": "oven"},{"supercategory": "appliance","id": 80,"name": "toaster"},{"supercategory": "appliance","id": 81,"name": "sink"},{"supercategory": "appliance","id": 82,"name": "refrigerator"},{"supercategory": "indoor","id": 84,"name": "book"},{"supercategory": "indoor","id": 85,"name": "clock"},{"supercategory": "indoor","id": 86,"name": "vase"},{"supercategory": "indoor","id": 87,"name": "scissors"},{"supercategory": "indoor","id": 88,"name": "teddy bear"},{"supercategory": "indoor","id": 89,"name": "hair drier"},
        {"supercategory": "indoor","id": 90,"name": "toothbrush"}]            

   

    for filename in os.listdir(json_dir):
     if filename.endswith(".json") :
      with open(json_dir + '/' + filename) as ff:
        fg=json.load(ff)
        j=j+1
        coco_json["images"].append({"license":0,"file_name":filename,"coco_url":0,
            "height": 0,"width": 0,
            "date_captured": 0,
            "flickr_url": 0,"id": j})
        uc= list(map(lambda d:d["id"],l))  
        print(uc)  
        s=len(fg["annotation"]["data_annotation"]["b_box"])
        if(s==1):
            uk=list(map(lambda d:d["name"]==fg["annotation"]["data_annotation"]["b_box"][0]["classification_label"],l))
            print(uk)
            xy=uk.index(True)     
            coco_json["annotation"].append({"segimenation":0,"area":0,"iscrowd":0,"image_id":j,
                    "b_box":fg["annotation"]["data_annotation"]["b_box"][0]["point_2D"],
                    "category_id":uc[xy]})
        else:
            for k in range(s):
                uk=list(map(lambda d:d["name"]==fg["annotation"]["data_annotation"]["b_box"][k]["classification_label"],l))
                
                xy=uk.index(True)  
                
                coco_json["annotation"].append({"segimenation":0,"area":0,"iscrowd":1,"image_id":j,
                "b_box":fg["annotation"]["data_annotation"]["b_box"][k]["point_2D"],
                "category_id":uc[xy]})
                    
    coco_json["categories"]=l         
    g=open(anno_output_path+'/'+"j2co.json",'w')

    g.write(json.dumps(coco_json))
    g.close()