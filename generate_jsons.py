import datetime
import errno
import json
import os
import time
from collections import defaultdict, deque

import torch
import torch.distributed as dist
import config_file as confs


def create_single_json_file(data_category, data_phase):
    ann_destination = os.path.join(confs.base_path, data_category, data_phase + '_annotations/')
    annFile = os.path.join(confs.base_path, data_category, 'annotations', confs.ann_type + '_' + data_phase + '.json')

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


# main_path = os.path.join(confs.base_path, data_category, 'images', data_phase)

# to create single json files for ms_coco person_keypoints_train2017.json file
create_single_json_file(confs.dataset_type[0], confs.dataset_phase[0])

# to create single json files for ms_coco person_keypoints_train2017.json file
create_single_json_file(confs.dataset_type[0], confs.dataset_phase[1])


test_ann_file = os.path.join(confs.base_path, confs.dataset_type[0],
                             confs.dataset_phase[0] + '_annotations/000000184613.json')
with open(test_ann_file) as json_file:
    single_data = json.load(json_file)
    print((single_data['info']))

