import os
import shutil
from hide import parameters
from hide.tools import aese, tools
from hide.interface import form

#test
import datetime

# import parameters
pub_key = parameters.pub_key
priv_key = parameters.private_key

password = parameters.password
error_count = parameters.error_count

hidden_directory = parameters.dir_for_encryption




def hide():
    offsets = list(tools.concat_files(tools.list_files(hidden_directory), 'file.bin', pub_key))
    tools.meta_outer(offsets)
    shutil.rmtree(parameters.dir_for_encryption)


def repay():
    os.mkdir(parameters.dir_for_encryption)
    tools.decode_bin(priv_key)
    meta = tools.meta_decode()
    for i in meta:
        tools.extract("file.bin", (i[0]), i[1], i[2])

#test


if os.path.exists(hidden_directory) == True:
    start_ = datetime.datetime.now() # test
    hide()
else:
    password_status = form.main(password, error_count)
    start_ = datetime.datetime.now() # test
    if password_status == True:
        repay()
    else:
        pass


print(datetime.datetime.now() - start_)