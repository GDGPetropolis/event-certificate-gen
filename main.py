from datetime import datetime

from src.entities.certificate_info import CertificateInfo
from src.services.certificate_generator import CertificateGenerator

if __name__ == "__main__":
    event_name = "Carreira de TI: Por Onde Começar"
    event_type = "evento"
    action = "participou do"
    description = "O <organizer> certifica que <participant> <action> <event_type> <event_name> no dia <date>."
    date = "26 de Janeiro de 2019"
    organizer = "GDG-Petrópolis"
    signature = "Laion"
    background = "assets/background.pdf"

    certificate_info = CertificateInfo(event_name=event_name, event_type=event_type, action=action, description=description, date=date, organizer=organizer, signature=signature, background=background)

    certificate_generator = CertificateGenerator(certificate_info)

    certificate_generator.generate("Johnathan Fercher da Rosa")


