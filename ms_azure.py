import json
import requests

def call_vision_api(image_filename, api_keys):
    api_key = api_keys
    post_url = "https://eastus.api.cognitive.microsoft.com/vision/v1.0/analyze?visualFeatures=Categories,Tags,Description,Faces,ImageType,Color,Adult&subscription-key=" + api_key

    image_data = open(image_filename, 'rb').read()
    result = requests.post(post_url, data=image_data, headers={'Content-Type': 'application/octet-stream'})
    result.raise_for_status()

    api_result=json.loads(result.text)

# Return a dictionary of features to their scored values (represented as lists of tuples).
# Scored values must be sorted in descending order.
#
# {
#    'feature_1' : [(element, score), ...],
#    'feature_2' : ...
# }
#
# E.g.,
#
# {
#    'tags' : [('throne', 0.95), ('swords', 0.84)],
#    'description' : [('A throne made of pointy objects', 0.73)]
# }
#

    output = {
        'tags' : [],
        'captions' : [],
#        'categories' : [],
#        'adult' : [],
#        'image_types' : []
#        'tags_without_score' : {}
    }

    for tag_data in api_result['tags']:
        output['tags'].append(tag_data['name'])

    for caption in api_result['description']['captions']:
        output['captions'].append(caption['text'])

#    for category in api_result['categories']:
#        output['categories'].append(([category['name'], category['score']))

#    output['adult'] = api_result['adult']

#    for tag in api_result['description']['tags']:
#        output['tags_without_score'][tag] = 'n/a'

#    output['image_types'] = api_result['imageType']
    list_of_labels=[]
    for label in output['tags']:
        list_of_labels.append({'classification_label':label})
    out={}
    annotation={}
    data_annotation={}
    data_annotation['image_classification']=list_of_labels
    annotation['data_filename']=file_name
    annotation['date_type']="image"
    annotation['data_annotation']=data_annotation
    out["annotation"]=annotation
    return out




   
image_filename="C:/Users/anvitha/Apis/work/photo/im_3.jpeg"
file_name=image_filename.split('/')[-1]
api_keys="a8c7d3bc66514a19b2a823dbf769b4d6"

print(call_vision_api(image_filename,api_keys))
