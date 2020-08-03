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

dir_for_encryption = parameters.dir_for_encryption


def hide():
    offsets = list(tools.concat_files(tools.list_files(dir_for_encryption), 'file.bin', pub_key))
    tools.meta_outer(offsets)
    shutil.rmtree(dir_for_encryption, ignore_errors=True)


def repay():
    os.mkdir(dir_for_encryption)
    tools.decode_bin(priv_key)
    meta = tools.meta_decode()
    tools.smart_extract("file_decode.bin", meta)
    os.remove("file_decode.bin")


if os.path.exists(hidden_directory):
    start_ = datetime.datetime.now() # time test
    hide()
else:
    window = form.PasswordWindow(password, error_count)
    if window.run():
        start_ = datetime.datetime.now() # time test
        repay()
    else:
        start_ = datetime.datetime.now() # time test

print(datetime.datetime.now() - start_)
