from constants import *
import enum
import os
from tika import *
from pascal import *
from yolo import *
from coco import *


curdir=os.getcwd()


def convert(frm_type, to_type, output_mode, data_input_path, anno_output_path=curdir):
    result = ""
    if(output_mode==AnnotationOutputMode.OBJECT):

        if(frm_type == AnnotationOutputFormat.TIKA_XML):
 
            if(to_type == AnnotationOutputFormat.TIKA_JSON):
                result= txml_tjson_obj(data_input_path)
            elif(to_type == AnnotationOutputFormat.PASCALVOC_XML):
                result= txml_pascal_obj(data_input_path)
            elif(to_type == AnnotationOutputFormat.YOLO_TXT):
               result= tjson_yolo_obj(txml_tjson_obj(data_input_path))

        elif(frm_type == AnnotationOutputFormat.TIKA_JSON):
 
            if(to_type == AnnotationOutputFormat.TIKA_XML):
                result= tjson_txml_obj(data_input_path)
            elif(to_type == AnnotationOutputFormat.PASCALVOC_XML):
                result= tjson_pascal_obj(data_input_path)
            elif(to_type == AnnotationOutputFormat.YOLO_TXT):
                result= tjson_yolo_obj(data_input_path)

        elif(frm_type == AnnotationOutputFormat.PASCALVOC_XML):
 
            if(to_type == AnnotationOutputFormat.TIKA_XML):
                result= pascal_txml_obj(data_input_path)
            elif(to_type == AnnotationOutputFormat.TIKA_JSON):
                result= pascal_tjson_obj(data_input_path)
            elif(to_type == AnnotationOutputFormat.YOLO_TXT):
                result= tjson_yolo_obj(pascal_tjson_obj(data_input_path))

        elif(frm_type == AnnotationOutputFormat.YOLO_TXT):

            if(to_type == AnnotationOutputFormat.TIKA_JSON):
                result= yolo_tjson_obj(data_input_path)
            elif(to_type == AnnotationOutputFormat.TIKA_XML):
                result= tjson_txml_obj(yolo_tjson_obj(data_input_path))
            elif(to_type == AnnotationOutputFormat.PASCALVOC_XML):
                result= tjson_pascal_obj(yolo_tjson_obj(data_input_path))
        return result

    elif(output_mode == AnnotationOutputMode.FILE):     

        if(frm_type == AnnotationOutputFormat.TIKA_XML):


            if(to_type==AnnotationOutputFormat.TIKA_JSON):
                txml_tjson_file(data_input_path,anno_output_path)
                
            elif(to_type == AnnotationOutputFormat.PASCALVOC_XML):
                txml_pascal_file(data_input_path,anno_output_path)
        
            elif(to_type==AnnotationOutputFormat.YOLO_TXT):
                obj=read_tika_xml_file(data_input_path)
                write_yolo_file(obj,anno_output_path)
            


        if(frm_type==AnnotationOutputFormat.TIKA_JSON):

            if(to_type==AnnotationOutputFormat.TIKA_XML):
                tjson_txml_file(data_input_path,anno_output_path) 
            
            elif(to_type==AnnotationOutputFormat.YOLO_TXT):
                 tjson_yolo_file(data_input_path,anno_output_path)
            
            elif(to_type==AnnotationOutputFormat.PASCALVOC_XML):
            
                tjson_pascal_file(data_input_path,anno_output_path)  
            

        if(frm_type==AnnotationOutputFormat.PASCALVOC_XML):
            
            
            if(to_type==AnnotationOutputFormat.TIKA_XML):
                 pascal_txml_file(data_input_path,anno_output_path) 
            
            elif(to_type==AnnotationOutputFormat.TIKA_JSON):
            
                pascal_tjson_file(data_input_path,anno_output_path)
            
            elif(to_type==AnnotationOutputFormat.YOLO_TXT):
                pascal_tjson_file(data_input_path,anno_output_path)
                tjson_yolo_file(anno_output_path+"/pascal_tikajson_outputfile.json",anno_output_path)
            
            



        if(frm_type==AnnotationOutputFormat.YOLO_TXT):
            
            if(to_type==AnnotationOutputFormat.TIKA_JSON):
                yolo_tjson_file(data_input_path,anno_output_path)
            
            elif(to_type==AnnotationOutputFormat.TIKA_XML):
                yolo_tjson_file(data_input_path,anno_output_path) 
                tjson_txml_file(anno_output_path+"/yolo_tikajson_outputfile.json",anno_output_path)
            

            elif(to_type==AnnotationOutputFormat.PASCALVOC_XML):
                yolo_tjson_file(data_input_path,anno_output_path) 
                tjson_pascal_file(anno_output_path+"/yolo_tjson_outputfile.json",anno_output_path)
            


        



    elif(output_mode==AnnotationOutputMode.DIR): 

            if(frm_type==AnnotationOutputFormat.TIKA_XML):
                
                if(to_type==AnnotationOutputFormat.TIKA_JSON):
                    txml_tjson_dir(data_input_path,anno_output_path)
       
     
                elif(to_type==AnnotationOutputFormat.PASCALVOC_XML):
                    txml_pascal_dir(data_input_path,anno_output_path)
            
                elif(to_type==AnnotationOutputFormat.YOLO_TXT):
                    txml_tjson_dir(data_input_path,anno_output_path)
                    tjson_yolo_dir(data_input_path+'/meta',anno_output_path)

                elif(to_type==AnnotationOutputFormat.COCO_JSON):
                    txml_tjson_dir(data_input_path,anno_output_path)
                    tjson_cocojson_dir(anno_output_path+'/meta',anno_output_path)

                


            if(frm_type==AnnotationOutputFormat.TIKA_JSON):

                if(to_type==AnnotationOutputFormat.TIKA_XML):
                    tjson_txml_dir(data_input_path,anno_output_path) 
                
                elif(to_type==AnnotationOutputFormat.YOLO_TXT):
                    tjson_yolo_dir(data_input_path,anno_output_path)
                
                elif(to_type==AnnotationOutputFormat.PASCALVOC_XML):
                    tjson_pascal_dir(data_input_path,anno_output_path)   


                elif(to_type==AnnotationOutputFormat.COCO_JSON):
                    tjson_cocojson_dir(data_input_path,anno_output_path)

        
            if(frm_type==AnnotationOutputFormat.PASCALVOC_XML):

                if(to_type==AnnotationOutputFormat.TIKA_XML):
                    pascal_txml_dir(data_input_path,anno_output_path)

                elif(to_type==AnnotationOutputFormat.TIKA_JSON):
                     pascal_tjson_dir(data_input_path,anno_output_path)

                elif(to_type==AnnotationOutputFormat.YOLO_TXT):
                    pascal_tjson_dir(data_input_path,anno_output_path)        
                    tjson_yolo_dir(anno_output_path+"/meta",anno_output_path) 
                

                elif(to_type==AnnotationOutputFormat.COCO_JSON):
                    pascal_tjson_dir(data_input_path)        
                    tjson_cocojson_dir(data_input_path+"/meta",anno_output_path) 
               

            if(frm_type==AnnotationOutputFormat.YOLO_TXT):
                if(to_type==AnnotationOutputFormat.TIKA_JSON):
                    yolo_tjson_dir(data_input_path,anno_output_path)
                
                elif(to_type==AnnotationOutputFormat.TIKA_XML):
                    yolo_tjson_dir(data_input_path,anno_output_path)
                    tjson_txml_dir
                

                elif(to_type==AnnotationOutputFormat.PASCALVOC_XML):
                    yolo_tjson_dir(data_input_path,anno_output_path) 
                    tjson_pascal_dir(data_input_path,anno_output_path)
                


                elif(to_type==AnnotationOutputFormat.COCO_JSON):
                    yolo_tjson_dir(data_input_path,anno_output_path)
                    tjson_cocojson_dir(anno_output_path+'/'+"meta",anno_output_path)
                
