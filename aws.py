import boto3

def call_vision_api(image_filename, api_keys):
    client = boto3.client('rekognition')

    with open(image_filename, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
        api_result=response

        
    output = {
        'tags' : [],
    }
    if 'Labels' not in api_result:
        return output

    labels = api_result['Labels']
    for tag in labels:
        output['tags'].append(tag['Name'])

    return output

image_filename="C:/Users/anvitha/Apis/work/photo/im_3.jpeg"
file_name=image_filename.split('/')[-1]
api_keys=""
output=call_vision_api(image_filename, api_keys)
print(call_vision_api(image_filename, api_keys))

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


print(out)
