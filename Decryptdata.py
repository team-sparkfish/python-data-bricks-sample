# This file contains functions related to gpg.

import os
import gnupg


def initialize_gpg(key_paths):
    gpg = gnupg.GPG()
    for path in key_paths:
        key_data = open(path).read()
        gpg.import_keys(key_data)
    # return
    return gpg


def remove_gpg_from_path(path):
    """
    We expect the given path as argument to have the form: file-name.ext.gpg
    So we want to return: file-name.ext
    For example:
        input: bottles.csv.gpg
        output: bottles.csv
    """
    return os.path.splitext(path)[0]


def decrypt_file(gpg, encrypted_path):
    with open(encrypted_path, 'rb') as a_file:
        decrypted_path = remove_gpg_from_path(encrypted_path)
        status = gpg.decrypt_file(a_file, output=decrypted_path)

    print 'ok: ', status.ok
    print 'status: ', status.status
    print 'stderr: ', status.stderr





if __name__ == '__main__':
    key_paths = ["/root/PycharmProjects/sparkfish/python-data-bricks-sample/slim.shady.sec.asc",
                 "/root/PycharmProjects/sparkfish/python-data-bricks-sample/slim.shady.pub.asc"]
    mygpg = initialize_gpg(key_paths)
    decrypt_file(mygpg,'titanic.csv.gpg')
