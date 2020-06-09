import os
import aese
import json
import shutil


def concat_files(src_files, dest, pub_key):
    offset = 0
    with open(dest, 'wb') as dest:
        for filename in src_files:
            with open(filename, 'rb') as file:
                shutil.copyfileobj(file, dest)
            new_offset = dest.tell()
            yield filename, offset, new_offset - offset
            offset = new_offset
    #не нужно так делать.Переписать срочно!
    with open("file.bin", "rb") as ref:
        data = ref.read()
        data = aese.encode_run(data, pub_key)
    with open("file.bin", "wb") as wef:
        wef.write(data)


def extract(file_name, dest_name, offset, size, block_size=1024):
    with open(file_name, 'rb') as file:
         file.seek(offset)
         with open(dest_name, 'wb') as dest:
             while size > 0:
                 block = file.read(block_size if size > block_size else size)
                 dest.write(block)
                 size -= block_size


def list_files(dir):
    list_ = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            list_.append(os.path.join(root, name))
    return list_


def decode_bin(priv):
    # стереть с лица земли
    with open("file.bin", "rb") as red:
        cdata = red.read()
        data = aese.decode_run(cdata, priv)
    with open("file.bin", "wb") as wr:
        wr.write(data)


def meta_outer(meta):
    with open('meta.json', "w") as writer:
        json.dump(meta, writer)


def meta_decode():
    with open("meta.json", "r") as reader:
        return_data = json.load(reader)
    return return_data

