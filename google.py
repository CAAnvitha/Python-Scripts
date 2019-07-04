import base64
import json
import requests
import os
import shutil

def _convert_image_to_base64(image_filename):
    with open(image_filename, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    return encoded_string

def call_vision_api(image_filename, api_keys):
    api_key = api_keys
    post_url = "https://vision.googleapis.com/v1/images:annotate?key=" + api_key

    base64_image = _convert_image_to_base64(image_filename)

    post_payload = {
      "requests": [
        {
          "image": {
            "content" : base64_image
          },
          "features": [
            {
              "type": "LABEL_DETECTION",
              "maxResults": 10
            },
            {
              "type": "FACE_DETECTION",
              "maxResults": 10
            },
            {
              "type": "LANDMARK_DETECTION",
              "maxResults": 10
            },
            {
              "type": "LOGO_DETECTION",
              "maxResults": 10
            },
            {
              "type": "SAFE_SEARCH_DETECTION",
              "maxResults": 10
            },
          ]
        }
      ]
    }

    result = requests.post(post_url, json=post_payload)
    result.raise_for_status()

    api_result= json.loads(result.text)
    output = {
        'tags' : [],
    }

    api_result = api_result['responses'][0]

    if 'labelAnnotations' in api_result:
        for tag in api_result['labelAnnotations']:
            output['tags'].append(tag['description'])
    else:
        output['tags'].append(('none found', None))

    if 'logoAnnotations' in api_result:
        output['logo_tags'] = []
        for annotation in api_result['logoAnnotations']:
            output['logo_tags'].append(annotation['description'])

    return output


 

intrests=["tiger","lion","person","people","sand"]
directory="C:/Users/anvitha/Apis/work/meta"
if not os.path.exists(directory):
    os.makedirs(directory)

img_dir="C:/Users/anvitha/Apis/work/photo"
for filename in os.listdir(img_dir):
    image_filename=img_dir+'/'+filename

    file_name=image_filename.split('/')[-1]
    api_keys="AIzaSyBOi2p8BiRGNOspx9ymGoBV-ZoaENanCus"

    output=call_vision_api(image_filename, api_keys)
    lables=[]
    list_of_json=[]
    list_of_labels=[]
    for label in output['tags']:
        list_of_labels.append({'classification_label':label})
        lables.append(label)
    out={}
    annotation={}
    data_annotation={}
    data_annotation['image_classification']=list_of_labels
    annotation['data_filename']=file_name
    annotation['date_type']="image"
    annotation['data_annotation']=data_annotation
    out["annotation"]=annotation
    list_of_json.append(out)


    for item in intrests:
      if item in lables:
        shutil.copy(img_dir+'/'+filename,directory+'/'+file_name)
       
      

    print("\nLables in Image \n",img_dir+'/'+filename)
    print(lables)
    print("\nTika json Output:-\n")
    print(out)


print(list_of_json)





    
