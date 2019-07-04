import json
import sys
import os
from misc import *
from tika import *
#from read_write_file import *
from xml.etree import ElementTree as ET
from lxml import etree
from xml.etree.ElementTree import Element, SubElement
import codecs


curdir = os.getcwd()

def read_pascal_voc_file(data_input_path):
    parser = etree.XMLParser(encoding='utf8')
    xmltree = ET.parse(data_input_path, parser=parser).getroot()
    print(xmltree)
    print([elem.tag for elem in xmltree.iter()])
    
    if("bndbox" in [elem.tag for elem in xmltree.iter()]):
        li=[]
        for object_iter in xmltree.findall('object'):

            cl = object_iter.find('name').text
            bb = object_iter.find('bndbox')
            xmin = bb.find('xmin').text
            ymin = bb.find('ymin').text
            xmax = bb.find('xmax').text
            ymax = bb.find('xmax').text
            li.append({'classification_label': cl, 'point_2D': [
                    str(xmin)+","+str(ymin), str(xmax)+","+str(ymax)]})

                            
        fl = {}
        sl = {}
        tl = {}
        sl['data_filename'] = xmltree.find('filename').text
        sl['data_image'] = "image"
        tl['bounding_box'] = li
        sl['data_annotation'] = tl
        fl['annotation'] = sl    
        return fl
    else:
        li=[]
        for object_iter in xmltree.findall('object'):

            cl = object_iter.find('name').text
            
            li.append({'classification_label': cl})

                            
        fl = {}
        sl = {}
        tl = {}
        sl['data_filename'] = xmltree.find('filename').text
        sl['data_image'] = "image"
        tl['image_classification'] = li
        sl['data_annotation'] = tl
        fl['annotation'] = sl   
        return fl 



            
def write_pascal_voc_file(obj, anno_file_output_path):
    
    
    file_path=os.getcwd()
    print(str(file_path))
    print(str(file_path).split('\\'))
    file_name =file_path.split('\\')[-2]

    length_file_name = int(len(file_name))

    directory = file_path[:-(length_file_name)]

    
    flag = obj
    output_filename=obj['annotation']['data_filename']
    
    dict_key=list(flag['annotation']['data_annotation'].keys())
    if "bounding_box" in dict_key:

            top = ET.Element('annotation')
            folder = ET.SubElement(top, 'folder')
            folder.text =file_path.split('\\')[-2]


            filename = ET.SubElement(top, 'filename')
            filename.text = flag['annotation']['data_filename']

            path = ET.SubElement(top, 'path')
            path.text =file_path

            source = ET.SubElement(top, 'source')
            database = ET.SubElement(source, 'database')
            database.text = 'unknown'

            size = ET.SubElement(top, 'size')
            width = ET.SubElement(size, 'width')
            width.text = '500'
            height = ET.SubElement(size, 'height')
            height.text = '500'
            depth = ET.SubElement(size, 'depth')
            depth.text = '2'

            segmented = ET.SubElement(top, 'segmented')

            segmented.text = '0'

            lp = flag['annotation']['data_annotation']['bounding_box']
            print(lp)
            for i in range(len(lp)):

                object_1 = ET.SubElement(top, 'object')
                name = ET.SubElement(object_1, 'name')

                name.text = flag['annotation']['data_annotation']['bounding_box'][i]['classification_label']
                print(name.text)
                pose = ET.SubElement(object_1, 'pose')
                pose.text = 'unspecified'
                truncated = ET.SubElement(object_1, 'truncated')
                truncated.text = '0'
                difficult = ET.SubElement(object_1, 'difficult')
                difficult.text = '0'
                bndbox = ET.SubElement(object_1, 'bndbox')

                xmin = ET.SubElement(bndbox, 'xmin')
                ymin = ET.SubElement(bndbox, 'ymin')
                x = flag['annotation']['data_annotation']['bounding_box'][i]['point_2D'][0]
                xmin.text = x.split(',')[0]
                ymin.text = x.split(',')[1]

                xmax = ET.SubElement(bndbox, 'xmin')
                ymax = ET.SubElement(bndbox, 'xmin')
                y = flag['annotation']['data_annotation']['bounding_box'][i]['point_2D'][0]
                xmax.text = y.split(',')[0]
                ymax.text = y.split(',')[1]

            rough_string = ET.tostring(top, 'utf8')
            root = etree.fromstring(rough_string)
            out = etree.tostring(root, pretty_print=True,
                                encoding='utf-8').replace("  ".encode(), "\t".encode())
        
            out_file = codecs.open(
                anno_file_output_path+'/'+output_filename.split('.')[0]+'.xml', 'w', encoding='utf8')
            out_file.write(out.decode('utf8'))
            out_file.close()
            

    else:
            top = ET.Element('annotation')
            folder = ET.SubElement(top, 'folder')
            folder.text =file_path.split('\\')[-2]


            filename = ET.SubElement(top, 'filename')
            filename.text = flag['annotation']['data_filename']

            path = ET.SubElement(top, 'path')
            path.text =file_path

            source = ET.SubElement(top, 'source')
            database = ET.SubElement(source, 'database')
            database.text = 'unknown'

            size = ET.SubElement(top, 'size')
            width = ET.SubElement(size, 'width')
            width.text = '500'
            height = ET.SubElement(size, 'height')
            height.text = '500'
            depth = ET.SubElement(size, 'depth')
            depth.text = '2'

            segmented = ET.SubElement(top, 'segmented')

            segmented.text = '0'

            lp = flag['annotation']['data_annotation']['image_classification']
            print(lp)
            for i in range(len(lp)):

                object_1 = ET.SubElement(top, 'object')
                name = ET.SubElement(object_1, 'name')

                name.text = flag['annotation']['data_annotation']['image_classification'][i]['classification_label']
                print(name.text)
                pose = ET.SubElement(object_1, 'pose')
                pose.text = 'unspecified'
                truncated = ET.SubElement(object_1, 'truncated')
                truncated.text = '0'
                difficult = ET.SubElement(object_1, 'difficult')
                difficult.text = '0'
                

            rough_string = ET.tostring(top, 'utf8')
            root = etree.fromstring(rough_string)
            out = etree.tostring(root, pretty_print=True,
                                encoding='utf-8').replace("  ".encode(), "\t".encode())
        
            out_file = codecs.open(
                anno_file_output_path+'/'+output_filename.split('.')[0]+'.xml', 'w', encoding='utf8')
            out_file.write(out.decode('utf8'))
            out_file.close()


def write_pascal_voc_dir(list_of_objects,anno_output_path)
    for obj in list_of_objects:
        write_pascal_voc_file(obj,anno_file_output_path)

            
                
def read_pascal_voc_dir(data_input_path) :
    list_of_objects=[]
    print("----")
    dire=os.listdir(data_input_path)
    for filename in dire:
        print(filename)
        print("==========")
        parser = etree.XMLParser(encoding='utf8')
        xmltree = ET.parse(data_input_path+'/'+filename, parser=parser).getroot()
        print(xmltree)
        print([elem.tag for elem in xmltree.iter()])
        if("bndbox" in [elem.tag for elem in xmltree.iter()]):
            li=[]
            for object_iter in xmltree.findall('object'):

                cl = object_iter.find('name').text
                bb = object_iter.find('bndbox')
                xmin = bb.find('xmin').text
                ymin = bb.find('ymin').text
                xmax = bb.find('xmax').text
                ymax = bb.find('xmax').text
                li.append({'classification_label': cl, 'point_2D': [
                        str(xmin), str(ymin), str(xmax), str(ymax)]})

                                
            fl = {}
            sl = {}
            tl = {}
            sl['data_filename'] = xmltree.find('filename').text
            sl['data_image'] = "image"
            tl['bounding_box'] = li
            sl['data_annotation'] = tl
            fl['annotation'] = sl    
            list_of_objects.append(fl)
            print(list_of_objects)
            
        else:
            li=[]
            for object_iter in xmltree.findall('object'):

                cl = object_iter.find('name').text
                
                li.append({'classification_label': cl})

                                
            fl = {}
            sl = {}
            tl = {}
            sl['data_filename'] = xmltree.find('filename').text
            sl['data_image'] = "image"
            tl['image_classification'] = li
            sl['data_annotation'] = tl
            fl['annotation'] = sl  
            list_of_objects.append(fl) 
    return(list_of_objects)       


     


       
def pascal_tjson_file(pascal_file, anno_output_path=curdir):

    obj=read_pascal_voc_file(pascal_file)
    write_tika_json_file(obj,anno_output_path)

def pascal_tjson_obj(pascal_obj):

    tree = ET.ElementTree(pascal_obj)
    tree.write("pascal_tjson_intermediate_file.xml")
    li = []
    cur = os.getcwd()
    parser = etree.XMLParser(encoding='utf8')
    xmltree = ET.parse(
        curdir+'/pascal_tjson_intermediate_file', parser=parser).getroot()
    for object_iter in xmltree.findall('object'):

        cl = object_iter.find('name').text
        bb = object_iter.find('bndbox')
        xmin = bb.find('xmin').text
        ymin = bb.find('ymin').text
        xmax = bb.find('xmax').text
        ymax = bb.find('xmax').text
        li.append({'classification_label': cl, 'point_2D': [
                  str(xmin), str(ymin), str(xmax), str(ymax)]})
    fl = {}
    sl = {}
    tl = {}
    sl['data_filename'] = xmltree.find('filename').text
    sl['data_image'] = "image"
    tl['bounding_box'] = li
    sl['data_annotation'] = tl
    fl['annotation'] = sl
    print(fl)
    return fl


def pascal_tjson_dir(pascal_dir, anno_output_path=curdir):

    os.makedirs(anno_output_path+'/meta') 
    for filename in os.listdir(pascal_dir):
       obj=read_pascal_voc_file(pascal_dir+'/'+filename)
       write_tika_json_file(obj,anno_output_path+'/meta')

# pascal to xml

def pascal_txml_file(pascal_file, anno_output_path=curdir):
    obj=read_pascal_voc_file(pascal_file)
    write_tika_xml_file(obj,anno_output_path)
             

def pascal_txml_obj(pascal_obj):

    tree = ET.ElementTree(pascal_obj)
    tree.write("pascal_txml_intermediate_file.xml")

    parser = etree.XMLParser(encoding='utf8')
    xmltree = ET.parse(
        curdir+'/pascal_txml_intermediate_file.xml', parser=parser).getroot()
    top = ET.Element('annotation')
    data_filename = ET.SubElement(top, 'data_filename')
    data_filename.text = xmltree.find('filename').text
    data_type = ET.SubElement(top, 'data_type')
    data_type.text = 'image'

    data_annotation = ET.SubElement(top, 'data_annotation')
    for object_iter in xmltree.findall('object'):
        bounding_box = ET.SubElement(data_annotation, 'bounding_box')
        classification_label = ET.SubElement(
            bounding_box, 'classification_label')
        classification_label.text = object_iter.find('name').text
        p1 = object_iter.find('bndbox')
        print(p1.find('xmin').text)
        point1 = ET.SubElement(bounding_box, 'point_2D')
        point1.text = p1.find('xmin').text+" ,"+p1.find('ymin').text
        point2 = ET.SubElement(bounding_box, 'point_2D')
        point2.text = p1.find('xmax').text+","+p1.find('ymax').text
    rough_string = ET.tostring(top, 'utf8')
    root = etree.fromstring(rough_string)
    out = etree.tostring(root, pretty_print=True,
                         encoding='utf-8').replace("  ".encode(), "\t".encode())
    return out


def pascal_txml_dir(pascal_dir, anno_output_path=curdir):
    os.makedirs(anno_output_path+'/meta') 
    for filename in os.listdir(pascal_dir):
        if filename.endswith(".xml"):
           obj=read_pascal_voc_file(pascal_dir)
           write_tika_xml_file(obj,anno_output_path+'/meta')
    





    


# tika json to pascal


def tjson_pascal_file(tjson_file, anno_output_path=curdir):
    print(tjson_file)
    obj=read_tika_json_file(tjson_file)
    print("----------",obj)
    write_pascal_voc_file(obj,anno_output_path)

def tjson_pascal_obj(tikajsonobj):

    flag = tikajsonobj

    cur = os.getcwd()
    print(cur)
    print(cur.split('\\')[-1])
    top = ET.Element('annotation')
    folder = ET.SubElement(top, 'folder')
    folder.text = cur.split('/')[-1]

    filename = ET.SubElement(top, 'filename')
    filename.text = "tikajson.json"

    path = ET.SubElement(top, 'path')
    path.text = cur

    source = ET.SubElement(top, 'source')
    database = ET.SubElement(source, 'database')
    database.text = 'unknown'

    size = ET.SubElement(top, 'size')
    width = ET.SubElement(size, 'width')
    width.text = '500'
    height = ET.SubElement(size, 'height')
    height.text = '500'
    depth = ET.SubElement(size, 'depth')
    depth.text = '2'
    segmented = ET.SubElement(top, 'segmented')
    segmented.text = '0'
    lp = flag['annotation']['data_annotation']['bounding_box']
    print(lp)
    for i in range(len(lp)):

        object_1 = ET.SubElement(top, 'object')
        name = ET.SubElement(object_1, 'name')

        name.text = flag['annotation']['data_annotation']['bounding_box'][i]['classification_label']
        print(name.text)
        pose = ET.SubElement(object_1, 'pose')
        pose.text = 'unspecified'
        truncated = ET.SubElement(object_1, 'truncated')
        truncated.text = '0'
        difficult = ET.SubElement(object_1, 'difficult')
        difficult.text = '0'
        bndbox = ET.SubElement(object_1, 'bndbox')
        xmin = ET.SubElement(bndbox, 'xmin')
        ymin = ET.SubElement(bndbox, 'ymin')
        x = flag['annotation']['data_annotation']['bounding_box'][i]['point_2D'][0]
        xmin.text = x.split(',')[0]
        ymin.text = x.split(',')[1]
        y = flag['annotation']['data_annotation']['bounding_box'][i]['point_2D'][1]
        xmax = ET.SubElement(bndbox, 'xmin')
        ymax = ET.SubElement(bndbox, 'xmin')
        xmax.text = y.split(',')[0]
        ymax.text = y.split(',')[1]
    rough_string = ET.tostring(top, 'utf8')
    root = etree.fromstring(rough_string)
    out = etree.tostring(root, pretty_print=True,
                         encoding='utf-8').replace("  ".encode(), "\t".encode())
    print(out)
    return out


def tjson_pascal_dir(json_dir, anno_output_path=curdir):
    os.makedirs(anno_output_path+'/meta')
    for filename in os.listdir(json_dir):
        obj=read_tika_json_file(json_dir+'/'+filename)
        write_pascal_voc_file(obj,anno_output_path+'/meta')
     


# tikaxml to pascal


def txml_pascal_file(txml_file, anno_output_path=curdir):
    obj=read_tika_json_file(txml_file)
    write_pascal_voc_file(obj,anno_output_path)

    
def txml_pascal_obj(xml_obj):

    rough_string = ET.tostring(xml_obj, 'utf8')
    root = etree.fromstring(rough_string)
    out = etree.tostring(root, pretty_print=True,
                         encoding='utf-8').replace("  ".encode(), "\t".encode())
    out_file = codecs.open(
        'tikaxml_pascal_intermediate_file.xml', 'wb+', encoding='utf8')
    out_file.write(out.decode('utf8'))
    out_file.close()
    cur = os.getcwd()
    print(cur)
    parser = etree.XMLParser(encoding='utf8')
    xml_dir = PASCAL_VOC_INTERMEDIATE_FILE_PATH
    xmltree = ET.parse(xml_dir, parser=parser).getroot()
    s = xml_dir.split('/')
    print(s)
    top = Element('annotation')
    folder = SubElement(top, 'folder')
    folder.text = s[-3]
    filename = SubElement(top, 'filename')
    filename.text = xmltree.find('data_filename').text
    path = SubElement(top, 'path')
    path.text = xml_dir
    source = SubElement(top, 'source')
    database = SubElement(source, 'database')
    database.text = 'unknown'
    size = SubElement(top, 'size')
    width = SubElement(size, 'width')
    width.text = '500'
    height = SubElement(size, 'height')
    height.text = '500'
    depth = SubElement(size, 'depth')
    depth.text = '2'
    segmented = SubElement(top, 'segmented')
    segmented.text = '0'
    f1 = xmltree.findall('point2D')
    print(f1)
    data_annotation = xmltree.find('data_annotation')
    f1 = xmltree.findall('point2D')
    print(f1)
    for object_iter in data_annotation.findall('bounding_box'):
        object_1 = SubElement(top, 'object')
        name = SubElement(object_1, 'name')
        print(type(object_iter.find('classification_label').text))
        name.text = object_iter.find('classification_label').text
        print(name.text)
        pose = SubElement(object_1, 'pose')
        pose.text = 'unspecified'
        truncated = SubElement(object_1, 'truncated')
        truncated.text = '0'
        difficult = SubElement(object_1, 'difficult')
        difficult.text = '0'
        bndbox = SubElement(object_1, 'bndbox')

        type(object_iter.find('point_2D').text)
        flag = []
        for point_iter in object_iter.findall('point_2D'):
            flag.append(point_iter.text)
        xmin = SubElement(bndbox, 'xmin')
        ymin = SubElement(bndbox, 'ymin')
        xmin.text = flag[0].split(',')[0]
        ymin.text = flag[0].split(',')[1]
        xmax = SubElement(bndbox, 'xmin')
        ymax = SubElement(bndbox, 'xmin')
        [xmax.text, ymax.text] = flag[1].split(',')
    rough_string = ET.tostring(top, 'utf8')
    root = etree.fromstring(rough_string)
    out = etree.tostring(root, pretty_print=True,
                         encoding='utf-8').replace("  ".encode(), "\t".encode())
    return out


def txml_pascal_dir(xml_dir, anno_output_path=curdir):
    os.makedirs(xml_dir+'/meta')
    for filename1 in os.listdir(xml_dir):
        if filename1.endswith(".xml"):
            obj=read_tika_xml_file(xml_dir)
            write_pascal_voc_file(obj,anno_output_path)