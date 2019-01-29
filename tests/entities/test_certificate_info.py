from src.entities.certificate_info import CertificateInfo


def test_random():
    # act
    certificate_info = CertificateInfo.random()

    # assert
    assert certificate_info is not None
    assert certificate_info.event_name is not None
    assert certificate_info.event_type is not None
    assert certificate_info.action is not None
    assert certificate_info.description is not None
    assert certificate_info.date is not None
    assert certificate_info.organizer is not None
    assert certificate_info.signature is not None
    assert certificate_info.background is not None


def test_init():
    # arrange
    random = CertificateInfo.random()

    # act
    certificate_info = CertificateInfo(random.event_name, random.event_type, random.action, random.description, random.date, random.organizer, random.signature, random.background)

    # assert
    assert certificate_info is not None
    assert certificate_info.event_name == random.event_name
    assert certificate_info.event_type == random.event_type
    assert certificate_info.action == random.action
    assert certificate_info.description == random.description
    assert certificate_info.date == random.date
    assert certificate_info.organizer == random.organizer
    assert certificate_info.background == random.background
