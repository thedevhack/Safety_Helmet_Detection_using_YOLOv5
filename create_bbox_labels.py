import xml.etree.ElementTree as ET
import os

def read_content(xml_file: str):

    tree = ET.parse(xml_file)
    root = tree.getroot()

    list_with_all_boxes = []

    for boxes in root.iter('object'):

        filename = root.find('filename').text
        file = filename.split(".",1)
        file_name = file[0]

        ymin, xmin, ymax, xmax = None, None, None, None
        
        nameo = boxes.find("name").text
        if nameo == "head":
            name = 0
        else:
            name = 1
             
        ymin = int(float(boxes.find("bndbox/ymin").text))
        xmin = int(float(boxes.find("bndbox/xmin").text))
        ymax = int(float(boxes.find("bndbox/ymax").text))
        xmax = int(float(boxes.find("bndbox/xmax").text))
        x_center = (xmin + xmax)/2
        y_center = (ymin + ymax)/2
        width = xmax - xmin
        height = ymax - ymin
        x_center /= 416
        y_center /= 416
        width /= 416
        height /= 416

        list_with_single_boxes = [name, x_center, y_center, width, height]
        list_with_all_boxes.append(list_with_single_boxes)
        with open('E:/Python_Projects/HardHat/hats_data/labels/train/'+file_name+'.txt', 'w') as f:
            for item in list_with_all_boxes:
                item_s = str(item)[1: -1]
                item_o = item_s.replace(",","")
                f.write("%s\n" % item_o)
    return filename


if __name__ == "__main__":
    files = os.listdir('E:/Python_Projects/HardHat/hats_data/labels/train/annotations')
    

    for file in files:
        name = read_content('E:/Python_Projects/HardHat/hats_data/labels/train/annotations/' + file)