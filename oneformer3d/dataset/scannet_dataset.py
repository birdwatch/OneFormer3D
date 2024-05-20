import random
from os import path as osp

import numpy as np
from mmdet3d.datasets.scannet_dataset import ScanNetSegDataset
from mmdet3d.registry import DATASETS

from .constants import SCANNETPP_CALSSES, SCANNETPP_VALID_CLASSES


@DATASETS.register_module()
class ScanNetSegDataset_(ScanNetSegDataset):
    """We just add super_pts_path."""

    def get_scene_idxs(self, *args, **kwargs):
        """Compute scene_idxs for data sampling."""
        return np.arange(len(self)).astype(np.int32)

    def parse_data_info(self, info: dict) -> dict:
        """Process the raw data info.

        Args:
            info (dict): Raw info dict.

        Returns:
            dict: Has `ann_info` in training stage. And
            all path has been converted to absolute path.
        """
        info["super_pts_path"] = osp.join(
            self.data_prefix.get("sp_pts_mask", ""), info["super_pts_path"],
        )

        info = super().parse_data_info(info)

        return info


@DATASETS.register_module()
class ScanNet200SegDataset_(ScanNetSegDataset_):
    # IMPORTANT: the floor and chair categories are swapped.
    METAINFO = {
        "classes": tuple(SCANNETPP_CALSSES),
        # the valid ids of segmentation annotations
        "seg_valid_class_ids": tuple(SCANNETPP_VALID_CLASSES),
        "seg_all_class_ids": tuple(range(1, 1660)),
        # "palette": [random.sample(range(0, 255), 3) for i in range(542)],
        "palette": [random.sample(range(255), 3) for i in range(1660)],
    }
