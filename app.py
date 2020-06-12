import os
import shutil
from hide import parameters
from hide.tools import aese, tools
from hide.interface import form

# time test
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
    shutil.rmtree(parameters.dir_for_encryption, ignore_errors=True)


def repay():
    os.mkdir(parameters.dir_for_encryption)
    tools.decode_bin(priv_key)
    meta = tools.meta_decode()
    tools.smart_extract("file_decode.bin", meta)
    os.remove("file_decode.bin")


aese.accept_key(pub_key, priv_key)

if os.path.exists(hidden_directory) == True:
    start_ = datetime.datetime.now() # time test
    hide()
else:
    password_status = form.main(password, error_count)
    start_ = datetime.datetime.now() # time test
    if password_status == True:
        repay()
    else:
        pass


print(datetime.datetime.now() - start_)
