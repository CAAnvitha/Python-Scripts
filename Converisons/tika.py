import json
import sys
import os
from xml.etree import ElementTree  as ET
from lxml import etree
#from read_write_file import *
from xml.etree.ElementTree import Element, SubElement
import codecs
curdir=os.getcwd()






def write_tika_json_file(obj, anno_file_output_path):
    output_filename=obj['annotation']['data_filename']
    with open(anno_file_output_path+'/'+output_filename.split('.')[0]+'.json','w+') as f:
        json.dump(obj,f) 

def write_tika_xml_file(obj, anno_file_output_path):
        print(anno_file_output_path)
        print("====spa")
        flag = obj
        output_filename=flag['annotation']['data_filename']
        print(flag['annotation']['data_filename'])
        
        top = Element('annotation')
        data_filename = SubElement(top, 'data_filename')
        data_filename.text = flag['annotation']['data_filename']

        data_type = SubElement(top, 'data_type')
        data_type.text = 'image'

        data_annotation = SubElement(top, 'data_annotation')
        typ = list(flag['annotation']['data_annotation'].keys())[0]
        
        if("bounding_box" in list(flag['annotation']['data_annotation'].keys())):
             
            for i in range(len(flag['annotation']['data_annotation']['bounding_box'])) :
                object_item = SubElement(data_annotation, 'bounding_box') 
                classification_label = SubElement(object_item, 'classification_label')
                classification_label.text = flag['annotation']['data_annotation']['bounding_box'][i]['classification_label']
                point1 = SubElement(object_item, 'point_2D')
                point1.text = flag['annotation']['data_annotation']['bounding_box'][i]['point_2D'][0]
                point2 = SubElement(object_item, 'point_2D')
                point2.text = flag['annotation']['data_annotation']['bounding_box'][i]['point_2D'][0]

                   
        else:
            object_item = SubElement(data_annotation, 'image_classification')
            for i in range(len(flag['annotation']['data_annotation']['image_classification'])):  
                classification_label = SubElement(object_item, 'classification_label')
                classification_label.text = flag['annotation']['data_annotation']['image_classification'][i]['classification_label']
                    
        rough_string = ET.tostring(top, 'utf8')
        root = etree.fromstring(rough_string)
        out = etree.tostring(root, pretty_print=True, encoding='utf-8').replace("  ".encode(), "\t".encode())
        out_file = codecs.open(anno_file_output_path+'/'+output_filename.split('.')[0]+".xml", 'w',encoding='utf8')
        out_file.write(out.decode('utf8'))
        out_file.close()


def read_tika_xml_file(data_input_path):
    
    parser = etree.XMLParser(encoding='utf8')
    xmltree = ET.parse(data_input_path, parser=parser).getroot()
    print(xmltree)
    print([elem.tag for elem in xmltree.iter()])
   
    

    data_annotation = xmltree.find('data_annotation')
    if("bounding_box" in [elem.tag for elem in xmltree.iter()]):
        print('in bound')
        ann_data={}
        ann={}
        out={}


        for object_iter in data_annotation.findall('bounding_box'):
            label_data={}
            label_data['classification_label']=object_iter.find('classification_label').text
            flag=[]
            for point_iter in object_iter.findall('point_2D'):
                
                flag.append(point_iter.text)
            label_data['point_2D'] = flag
            ann_data.setdefault('bounding_box', []).append(label_data)
            print(flag)
        ann['data_filename']= xmltree.find('data_filename').text
        ann['data_type']='image'
        ann['data_annotation']=ann_data
        out['annotation']=ann
        return out 
    else:

        
        li=[]
        ann_data={}
        ann={}
        out={}


        image_classfication=data_annotation.find('image_classification')
        print(image_classfication)
        for object_iter in image_classfication.findall('classification_label'):
            print("====\n")
            print(object_iter)
            li.append({'classification_label':object_iter.text})


        ann['data_filename']= xmltree.find('data_filename').text
        ann['data_type']='image'
        ann_data['image_classification']=li
        ann['data_annotation']=ann_data
        out['annotation']=ann   
        return out


def read_tika_json_dir(data_input_path):
    list_of_objects=[]
    with open(data_input_path) as fg:
        f = json.load(fg)
        list_of_objects.append(f)
    return list_of_objects 


def read_tika_xml_dir(data_input_path):
    list_of_objects=[]
    for filename in os.listdir(data_input_path):
        parser = etree.XMLParser(encoding='utf8')
        xmltree = ET.parse(data_input_path, parser=parser).getroot()
        print(xmltree)
        print([elem.tag for elem in xmltree.iter()])
    
        

        data_annotation = xmltree.find('data_annotation')
        if("bounding_box" in [elem.tag for elem in xmltree.iter()]):
            print('in bound')
            ann_data={}
            ann={}
            out={}


            for object_iter in data_annotation.findall('bounding_box'):
                label_data={}
                label_data['classification_label']=object_iter.find('classification_label').text
                flag=[]
                for point_iter in object_iter.findall('point_2D'):
                    
                    flag.append(point_iter.text)
                label_data['point_2D'] = flag
                ann_data.setdefault('bounding_box', []).append(label_data)
                print(flag)
            ann['data_filename']= xmltree.find('data_filename').text
            ann['data_type']='image'
            ann['data_annotation']=ann_data
            out['annotation']=ann
            list_of_objects.append(out)
        else:

            
            li=[]
            ann_data={}
            ann={}
            out={}


            image_classfication=data_annotation.find('image_classification')
            print(image_classfication)
            for object_iter in image_classfication.findall('classification_label'):
                print("====\n")
                print(object_iter)
                li.append({'classification_label':object_iter.text})


            ann['data_filename']= xmltree.find('data_filename').text
            ann['data_type']='image'
            ann_data['image_classification']=li
            ann['data_annotation']=ann_data
            out['annotation']=ann   
            list_of_objects.append(out)
    return list_of_objects

def read_tika_json_file(data_input_path):
    
    with open(data_input_path) as f:
            flag = json.load(f)


    return flag
        
def tjson_txml_dir(json_dir,anno_output_path=curdir):
    os.makedirs(json_dir+'/meta')
    for filename in os.listdir(json_dir):
        if filename.endswith(".json") :
           obj=read_tika_json_file(json_dir+'/'+filename)
           write_tika_xml_file(obj,anno_output_path)

        


def tjson_txml_file(json_dir,anno_output_path=curdir):
    obj=read_tika_json_file(json_dir)
    write_tika_xml_file(obj,anno_output_path)

def tjson_txml_obj(flag):
 print(flag)   
 top = Element('annotation')
 data_filename = SubElement(top, 'data_filename')
 data_filename.text = flag['annotation']['data_filename']

 data_type = SubElement(top, 'data_type')
 data_type.text = 'image'

 data_annotation = SubElement(top, 'data_annotation')
 typ = list(flag['annotation']['data_annotation'].keys())[0]

 for each_object in flag['annotation']['data_annotation'][typ]:
        if typ == 'bounding_box':
            object_item = SubElement(data_annotation, typ)
            classification_label = SubElement(object_item, 'classification_label')
            classification_label.text = each_object['classification_label']
            point1 = SubElement(object_item, 'point_2D')
            point1.text = each_object['point_2D'][0]
            point2 = SubElement(object_item, 'point_2D')
            point2.text = each_object['point_2D'][1]
        elif typ == 'image_classification':
            object_item = SubElement(data_annotation, typ)
            classification_label = SubElement(object_item, 'label')
            classification_label.text = each_object['label']
            
 rough_string = ET.tostring(top, 'utf8')
 root = etree.fromstring(rough_string)
 out = etree.tostring(root, pretty_print=True, encoding='utf-8').replace("  ".encode(), "\t".encode())
 return out


def txml_tjson_dir(xml_dir,anno_output_path):
    for filename in os.listdir(xml_dir):
        if filename.endswith(".xml") :
            obj=read_tika_xml_file(xml_dir+'/'+filename)
            write_tika_json_file(obj,anno_output_path)
def txml_tjson_file(xml_file,anno_output_path=curdir):
    
        obj=read_tika_xml_file(xml_file)
        write_tika_json_file(obj,anno_output_path)
        
    
def txml_tjson_obj(xml_obj):
    print("inside tika")
    rough_string = ET.tostring(xml_obj, 'utf8')
    root = etree.fromstring(rough_string)
    out = etree.tostring(root, pretty_print=True, encoding='utf-8').replace("  ".encode(), "\t".encode()) 
    out_file = codecs.open('tika_xml.xml', 'wb+',encoding='utf8')
    out_file.write(out.decode('utf8'))
    out_file.close()   


    xml_dir="C:/Users/anvitha/Desktop/annoformats/tika_xml.xml"
    parser = etree.XMLParser(encoding='utf8')
    xmltree = ET.parse(xml_dir, parser=parser).getroot()
    ann_data={}
    ann={}
    out={}
    data_annotation = xmltree.find('data_annotation')
    for object_iter in data_annotation.findall('bounding_box'):
        label_data={}
        label_data['classification_label']=object_iter.find('classification_label').text
        flag=[]
    for point_iter in object_iter.findall('point_2D'):
        flag.append(point_iter.text)
    label_data['point_2D'] = flag
    ann_data.setdefault('bounding_box', []).append(label_data)
    for object_iter in data_annotation.findall('image_classification'):
        label_data={}
        label_data['label']=object_iter.find('label').text
        ann_data.setdefault('image_classification', []).append(label_data)
    ann['data_filename']= xmltree.find('data_filename').text
    ann['data_type']='image'
    ann['data_annotation']=ann_data
    out['annotation']=ann
    return out   
