from src.entities.certificate_info import CertificateInfo


class NameHelper(object):

    @classmethod
    def get_folder_name(cls, certificate_info: CertificateInfo):
        return "output/" + certificate_info.event_name

    @classmethod
    def get_participant_file_name(cls, certificate_info: CertificateInfo, participant):
        return cls.get_folder_name(certificate_info) + "/" + participant + ".pdf"
