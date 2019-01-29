import os

from src.entities.certificate_info import CertificateInfo
from src.infrastructure.name_helper import NameHelper


class DirectoryHelper(object):

    @classmethod
    def create_folder_if_doesnt_exist(cls, certificate_info: CertificateInfo):
        folder_name = NameHelper.get_folder_name(certificate_info)

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
