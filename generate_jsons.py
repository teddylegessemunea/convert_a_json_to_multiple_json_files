import json
import os

import config_file as confs


def create_single_json_file(data_category, data_phase):
    ann_destination = os.path.join(base_path, data_category, data_phase + '_annotations/')
    annFile = os.path.join(base_path, data_category, 'annotations', ann_type + '_' + data_phase + '.json')

    with open(annFile) as json_file:
        data = json.load(json_file)
        data_imgs = data['images']
        data_anns = data['annotations']
        for imgs in data_imgs:
            a_img_dict = {'info': data['info'],
                          'licenses': data['licenses'],
                          'categories': data['categories'],
                          'license': imgs['license'],
                          'file_name': imgs['file_name'],
                          'coco_url': imgs['coco_url'],
                          'height': imgs['height'],
                          'width': imgs['width'],
                          'date_captured': imgs['date_captured'],
                          'flickr_url': imgs['flickr_url'],
                          'image_id': imgs['id']}

            a_img_data_anns = []
            for anns in data_anns:
                if anns['image_id'] == imgs['id']:
                    a_img_ann = {'segmentation': anns['segmentation'],
                                 'num_keypoints': anns['num_keypoints'],
                                 'area': anns['area'],
                                 'iscrowd': anns['iscrowd'],
                                 'keypoints': anns['keypoints'],
                                 'bbox': anns['bbox'],
                                 'category_id': anns['category_id'],
                                 'annotation_id': anns['id']}

                    a_img_data_anns.append(a_img_ann)

            a_img_dict['annotations'] = a_img_data_anns

            file_name_ext_idx = imgs['file_name'].index('.')
            a_img_file_name = imgs['file_name'][:file_name_ext_idx]
            a_json_key = f'{ann_destination}{a_img_file_name}.json'
            with open(a_json_key, 'w') as json_key:
                json.dump(a_img_dict, json_key, indent=4)
                print(f'{json_key} created !')


base_path = datasets  # the directory which contain all your datasets including ms_coco datasets
ann_type = 'person_keypoints'  # ann_type can be person_keypoints, captions, instances, image_info
base_path = os.path.join(confs.base_path, data_category, 'images', data_phase)

# to create single json files for ms_coco person_keypoints_train2017.json file
create_single_json_file('ms_coco', 'train2017')

# to create single json files for ms_coco person_keypoints_train2017.json file
create_single_json_file('ms_coco', 'val2017')

print('finished')

