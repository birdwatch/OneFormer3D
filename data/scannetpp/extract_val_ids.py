import json
import os

class_list_path = 'metadata/semantic_classes.txt'

class_list = []
with open(class_list_path, 'r') as file:
    for line in file:
        class_list.append(line.strip())

print(len(class_list))

# List of scan IDs
scan_ids = [
    "7b6477cb95", "c50d2d1d42", "cc5237fd77", "acd95847c5", "fb5a96b1a2", 
    "a24f64f7fb", "1ada7a0617", "5eb31827b7", "3e8bba0176", "3f15a9266d", 
    "21d970d8de", "5748ce6f01", "c4c04e6d6c", "7831862f02", "bde1e479ad", 
    "38d58a7a31", "5ee7c22ba0", "f9f95681fd", "3864514494", "40aec5fffa", 
    "13c3e046d7", "e398684d27", "a8bf42d646", "45b0dac5e3", "31a2c91c43", 
    "e7af285f7d", "286b55a2bf", "7bc286c1b6", "f3685d06a9", "b0a08200c9", 
    "825d228aec", "a980334473", "f2dc06b1d2", "5942004064", "25f3b7a318", 
    "bcd2436daf", "f3d64c30f8", "0d2ee665be", "3db0a1c8f3", "ac48a9b736", 
    "c5439f4607", "578511c8a9", "d755b3d9d8", "99fa5c25e1", "09c1414f1b", 
    "5f99900f09", "9071e139d9", "6115eddb86", "27dd4da69e", "c49a8c6cff"
]

# Function to extract objectId from a given JSON file path
def extract_label(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return [group['label'] for group in data.get('segGroups', [])]

# Path to the directory containing the folders with scan IDs
base_path = 'data'


# scan_ids = os.listdir(base_path)

# Dictionary to hold object IDs for each scan ID
labels_dict = {}

# Iterate over each scan ID
for scan_id in scan_ids:
    json_file_path = os.path.join(base_path, scan_id, 'scans', 'segments_anno.json')
    if os.path.exists(json_file_path):
        labels_dict[scan_id] = extract_label(json_file_path)
    else:
        labels_dict[scan_id] = None

# # list of object IDs for each scan ID
# object_ids_list = [object_ids_dict[scan_id] for scan_id in scan_ids]

# # fix duplicate object IDs
# object_ids_list = list(set([item for sublist in object_ids_list if sublist for item in sublist]))

# print(object_ids_list)

class_ids = []
for scan_id in scan_ids:
    for label in labels_dict[scan_id]:
        if label in class_list:
            class_ids.append(class_list.index(label))
        else:
            print(label + " not found in class_list")
            
class_ids = list(set(class_ids))
class_ids.sort()
class_ids = [class_id+1 for class_id in class_ids]
print(class_ids)
print(len(class_ids))
