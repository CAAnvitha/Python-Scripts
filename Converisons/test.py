from convert import *
import json
import sys
import os 
from xml.etree import ElementTree as x
from lxml import etree
from xml.etree.ElementTree import Element, SubElement
import codecs
b={"annotation": 
    {"data_filename": "horse_man.jpg", 
        "data_type": "image",
         "data_annotation": 
         {"bounding_box":
             [{"classification_label": "meatballs", "point_2D": ["10,34", "92,126"]}, 
             {"classification_label": "cat", "point_2D": ["188,13", "280,142"]}]}}}

data = x.Element('annotation')  
data_filename = x.SubElement(data, 'data_filename')  
data_type=x.SubElement(data,'data_type')
data_filename.text="fiel.jpg"
data_type.text="image"
data_annotation=x.SubElement(data,'data_annotation')
bndbx=x.SubElement(data_annotation,'bounding_box')
class_fi=x.SubElement(bndbx,'classification_label')
class_fi.text="meatballs"
point1=x.SubElement(bndbx,'point_2D')
point1.text="10,23"
point2=x.SubElement(bndbx,'point_2D')
point2.text="10,23"

# create a new XML file with the results
mydata = x.tostring(data)  
myfile = open("items2.xml", "wb+")  
myfile.write(mydata) 


# print(convert(AnnotationOutputFormat.TIKA_JSON,AnnotationOutputFormat.TIKA_XML,AnnotationOutputMode.OBJECT,a,"C:/Users/anvitha/Desktop/new"))
# print(convert(AnnotationOutputFormat.TIKA_XML,AnnotationOutputFormat.TIKA_JSON,AnnotationOutputMode.OBJECT,data,))






#convert(AnnotationOutputFormat.TIKA_JSON,AnnotationOutputFormat.PASCALVOC_XML,AnnotationOutputMode.FILE,"C:/Users/anvitha/Downloads/Tika json/1b.json","C:/Users/anvitha/Downloads/Tika json")
#convert(AnnotationOutputFormat.TIKA_JSON,AnnotationOutputFormat.TIKA_XML,AnnotationOutputMode.FILE,"C:/Users/anvitha/Downloads/Tika json/1b.json","C:/Users/anvitha/Downloads/Tika json")
#convert(AnnotationOutputFormat.TIKA_JSON,AnnotationOutputFormat.YOLO_TXT,AnnotationOutputMode.FILE,"C:/Users/anvitha/Downloads/Tika json/1b.json","C:/Users/anvitha/Downloads/Tika json")


#convert(AnnotationOutputFormat.TIKA_XML,AnnotationOutputFormat.TIKA_JSON,AnnotationOutputMode.FILE,"C:/Users/anvitha/Downloads/Tika xml/classify_sample.xml","C:/Users/anvitha/Downloads/Tika json")
convert(AnnotationOutputFormat.TIKA_XML,AnnotationOutputFormat.TIKA_JSON,AnnotationOutputMode.FILE,"C:/Users/anvitha/Downloads/Tika json/horse_man.xml","C:/Users/anvitha/Desktop")


#convert(AnnotationOutputFormat.TIKA_XML,AnnotationOutputFormat.YOLO_TXT,AnnotationOutputMode.FILE,"C:/Users/anvitha/Downloads/Tika xml/classify_sample.xml","C:/Users/anvitha/Desktop")




#  Checking the object
a={"annotation": 
    {"data_filename": "horse_man.jpg", 
        "data_type": "image",
         "data_annotation": 
         {"bounding_box": [
             {"classification_label": "french onion soup", "point_2D": ["103,25", "158,156"]}, 
             {"classification_label": "tv", "point_2D": ["165,11", "203,81"]}]}}}




data = x.Element('annotation')  
data_filename = x.SubElement(data, 'data_filename')  
data_type=x.SubElement(data,'data_type')
data_filename.text="fiel.jpg"
data_type.text="image"
data_annotation=x.SubElement(data,'data_annotation')
bndbx=x.SubElement(data_annotation,'bounding_box')
class_fi=x.SubElement(bndbx,'classification_label')
class_fi.text="meatballs"
point1=x.SubElement(bndbx,'point_2D')
point1.text="10,23"
point2=x.SubElement(bndbx,'point_2D')
point2.text="10,23"

# create a new XML file with the results
mydata = x.tostring(data)  
myfile = open("items2.xml", "wb+")  
myfile.write(mydata)       



#unit testing











# res=convert(AnnotationOutputFormat.TIKA_JSON,AnnotationOutputFormat.TIKA_XML,AnnotationOutputMode.OBJECT,a)
# print(res)


# res=convert(AnnotationOutputFormat.TIKA_JSON,AnnotationOutputFormat.YOLO_TXT,AnnotationOutputMode.OBJECT,a)
# print(res)

# res=convert(AnnotationOutputFormat.TIKA_JSON,AnnotationOutputFormat.PASCALVOC_XML,AnnotationOutputMode.OBJECT,a)
# print(res)




#convert(AnnotationOutputFormat.TIKA_XML,AnnotationOutputFormat.PASCALVOC_XML,AnnotationOutputMode.FILE,"C:/Users/anvitha/Downloads/Tika json/tjson_to_txml.xml","C:/Users/anvitha/Downloads/Tika json")



# res=convert(AnnotationOutputFormat.TIKA_XML,AnnotationOutputFormat.PASCALVOC_XML,AnnotationOutputMode.OBJECT,data)
# print(res)


# res=convert(AnnotationOutputFormat.TIKA_XML,AnnotationOutputFormat.TIKA_JSON,AnnotationOutputMode.OBJECT,data)
# print(res)

# res=convert(AnnotationOutputFormat.TIKA_XML,AnnotationOutputFormat.YOLO_TXT,AnnotationOutputMode.OBJECT,data)
# print(res)
