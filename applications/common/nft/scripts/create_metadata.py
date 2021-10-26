from pathlib import Path
import requests
import json
import os
import pandas as pd


attributes = [[{"trait_type": "strength","value": 100}],[{"trait_type": "strength","value": 1000}],[{"trait_type": "strength","value": 10000}]]
metadata_template = {
    "name": "",
    "description": "Gamefi club NFT !",
    "image": "",
    "attributes": ""
}

def mysql_api():
    data = {"token_id":2,"name":"mat","discriblem":"Gamefi club NFT !","Rare":0}  # mysql_api()  #  返回dataframe格式，编号作为索引[token_id,name,discriblem,Rare]

    return data


# def load_ipfs(token_id):
#     hx = ""   #  token_id作为索引
#     return hx


# def img_num():
#     im = list()
#     for filename in os.listdir(r"./m"):              #listdir的参数是文件夹的路径
#         im.append(filename)
#     return im 
    

# _b_doge_1888
def NFT_main():
    data = mysql_api()
    token_id = data["token_id"]
    Rare = data["Rare"]
    name = data["name"].upper()
    attributes0 = attributes[data["Rare"]]
    metadata_template["name"] = data["name"].upper()
    metadata_template["attributes"] = attributes0


    # data\img\_0_GCB_1.png
    image_path = "applications/common/nft/data/img/" +"_"+str(Rare) + "_" + str(name.upper()) + "_" + str(token_id) + ".png"
    image_uri = None

    if image_path != "":
        image_uri = upload_to_ipfs(image_path)
    metadata_template["image"] = image_uri


    img_uri_path = "applications/common/nft/data/img_uri/" + str(Rare) + "-" + str(name.upper()) + "-" + str(token_id) + ".json"

    with open(img_uri_path, "w", encoding ='utf8') as file:
        json.dump(metadata_template, file)
    json_uri = upload_to_ipfs(img_uri_path)

    print(json_uri)

    return json_uri

# curl -X POST -F file=@metadata/rinkeby/0-SHIBA_INU.json http://localhost:5001/api/v0/add


def pinata(filepath,filename):
    headers = {
    "pinata_api_key": "cef75f80fefae89ef3b5",
    "pinata_secret_api_key": "ecbc0ebc815dba020faaf640448b5bd0b6815d2762e04bac0b5dd302d8ef57b0",
    }
    PINATA_BASE_URL = "https://api.pinata.cloud/"
    endpoint = "pinning/pinFileToIPFS"

    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (filename, image_binary)},
            headers=headers,
        )
        IpfsHash = response.json()["IpfsHash"]
        image_uri = f"https://ipfs.io/ipfs/{IpfsHash}?filename={filename}"
    return image_uri


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        # "./img/0-PUG.png" -> "0-PUG.png"
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri


