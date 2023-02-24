# convert_a_json_to_multiple_json_files

This python script is to convert a single ms-coco json file to multiple json files for each image.

I used here ms_coco 2017 person_keypoints json file an example, but it can be modified to other files too


Datasets structure
  datasets
    ms_coco
      annotations
      images
      train2017_annotations
      val2017_annotations

![image](https://user-images.githubusercontent.com/18215999/221136004-a20bc689-45bd-48ee-a2d6-4630fcdd683e.png)

Run the python code

  > python generate_jsons.py
