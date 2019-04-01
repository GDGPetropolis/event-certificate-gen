from certificategen.entities.certificate_info import CertificateInfo
from certificategen.services.certificate_generator import CertificateGenerator

if __name__ == "__main__":
    event_name = "IWD Petrópolis 2019"
    event_type = "evento"
    action = "participou do"
    description = "O <organizer> certifica que <participant> <action> <event_type> <event_name> no dia <date>."
    date = "2019-03-30"
    organizer = "GDG-Petrópolis"
    signature = "assets/signature.png"
    background = "assets/background.pdf"

    certificate_info = CertificateInfo(event_name=event_name, event_type=event_type, action=action, description=description, date=date, organizer=organizer, signature=signature, background=background)

    certificate_generator = CertificateGenerator(certificate_info)

    certificate_generator.generate("Fulano")