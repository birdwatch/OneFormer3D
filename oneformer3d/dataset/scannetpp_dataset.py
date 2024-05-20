import json
import os
import random

import numpy as np
from mmdet3d.registry import DATASETS

from .constants import SCANNETPP_CALSSES, SCANNETPP_VALID_CLASSES
from .scannet_dataset import ScanNetSegDataset_


@DATASETS.register_module()
class ScanNetPPSegDataset(ScanNetSegDataset_):
    # IMPORTANT: the floor and chair categories are swapped.
    METAINFO = {
        "classes": tuple(SCANNETPP_CALSSES),
        # the valid ids of segmentation annotations
        "seg_valid_class_ids": tuple(SCANNETPP_VALID_CLASSES),
        "seg_all_class_ids": tuple(range(1, 1663)),
        "palette": [random.sample(range(255), 3) for i in range(1663)],
    }

    # override function
    def _load_annotations(self, split):
        assert split in ["train", "val", "test"]
        if split == "test":
            return []
        json_file = os.path.join(self._data_dir, "annotations", f"{split}.json")
        with open(json_file) as f:
            data = json.load(f)
        return data

    # override functions to check problem in data loading
    def __getitem__(self, idx: int) -> dict:
        print("ScanNetPPSegDataset.__getitem__")
        return super().__getitem__(idx)
    
    def __
