import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def organizer(origin_paths = 'C:/Users/willy/Desktop/git/rascunho/imgs', save_paths = 'C:/Users/willy/Desktop/git/rascunho/img_labels')
    counts = {}
    for index, row in img_labels.iterrows():
        #print(row['class'],row['xmin'],row['xmax'],row['ymin'], row['ymax'])
        img_path = glob.glob(os.path.join(origin_paths, f"{row['filename']}"))
        image = cv2.imread(img_path[0])
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        letter_image = gray[row['ymin']:row['ymax'], row['xmin']:row['xmax']]
        save_path = os.path.join(save_paths, str(row['class']))
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        count = counts.get(str(row['class']), 1)
        p = os.path.join(save_path, "{}.png".format(str(count)))
        cv2.imwrite(p, letter_image)

        counts[str(row['class'])] = count+1

    return counts