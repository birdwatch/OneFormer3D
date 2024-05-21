cd data/scannetpp/
../../.venv/bin/python3 batch_load_scannetpp_data.py --output_folder scannetpp_tmp --train_scannet_dir data --test_scannet_dir data --label_map_file nazo --train_scan_names_file splits/nvs_sem_train.txt --test_scan_names_file splits/nvs_sem_val.txt
cd ../../
.venv/bin/python3 tools/preprocessing/scannetpp/create_data.py scannetpp --root-path data/scannetpp_converted2 --out-dir data/scannetpp_mmdet --extra-tag scannetpp --workers 4 
