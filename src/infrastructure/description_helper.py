from src.entities.certificate_info import CertificateInfo


class DescriptionHelper(object):

    @classmethod
    def interpolate(cls, certificate_info: CertificateInfo, participant: str):
        description = certificate_info.description

        description = description.replace("<organizer>", certificate_info.organizer)
        description = description.replace("<event_type>", certificate_info.event_type)
        description = description.replace("<event_name>", certificate_info.event_name)
        description = description.replace("<action>", certificate_info.action)
        description = description.replace("<participant>", participant)
        description = description.replace("<date>", certificate_info.date)

        return description
