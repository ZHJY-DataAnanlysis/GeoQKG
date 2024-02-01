# GeoQKG
GeoQKG is the pre-training-free representation method that comprehensively extracts the relational information among key elements of a question and stores it in a knowledge structure. This repository provides the code for reproducing GeoQKG method, which is proposed in our paper "**knowledge-structure chimera: towards pre-training-free representation for multimodal geometry question**" 

For the code of the method, please refer to [GeoQKG](https://github.com/ZHJY-DataAnanlysis/GeoQKG).

The Geometry3K  dataset is now available on [Geometry3K](https://lupantech.github.io/inter-gps/).

The GeoQA dataset is now available on [GeoQA](https://drive.google.com/drive/folders/1fiLTJUq7EPiZHs6AxundNfNEDLw4gtP5).

## How to use
To generate a new Medical-Diff-VQA dataset(due to the randomness, the generated dataset will not be 100% the same as our provided one), please follow the steps below:
1. Enter the 'code' directory
    ```bash
    cd code
    ```
2. Prepare for the mimic_all.csv (MIMIC-CXR-JPG needs to be ready)
    ```bash
    python get_mimic_all.py -p <path_to_mimic_cxr_jpg>
    ```
3. Extract the intermediate KeyInfo json dataset. The <path_to_reports_folder> refers to the "files" folder that is unzipped from the mimic-cxr-reports.zip file in the MIMIC-CXR database.
    ```bash
    python question_gen.py -j -r <path_to_reports_folder>
    ```
4. Generate the full version of question answer pairs
    ```bash
    python question_gen.py -q
    ```

    Alternatively, you can execute step 3 and step 4 simultaneously by running:
    ```bash
    python question_gen.py -j -q
    ```
