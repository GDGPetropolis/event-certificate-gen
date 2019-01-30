from reportlab.pdfgen import canvas
from src.entities.certificate_info import CertificateInfo
from src.infrastructure.description_helper import DescriptionHelper
from src.infrastructure.directory_helper import DirectoryHelper
from src.infrastructure.name_helper import NameHelper
from src.infrastructure.pdf_text_helper import PdfTextHelper


class CertificateGenerator(object):
    cerfiticate_info = None
    participant = None

    def __init__(self, cerfiticate_info: CertificateInfo):
        self.cerfiticate_info = cerfiticate_info

    def generate(self, participant: str):
        if participant:
            self.participant = participant
            self.__generate_pdf()

    def __generate_pdf(self):
        font_size = 35
        vertical_space = 50
        horizontal_limit_width = 80
        text_block_x = 215
        text_block_y = 700
        sign_x = 850
        sign_y = 200
        description = DescriptionHelper.interpolate(self.cerfiticate_info, self.participant)

        DirectoryHelper.create_folder_if_doesnt_exist(self.cerfiticate_info)
        file_name = NameHelper.get_participant_file_name(self.cerfiticate_info, self.participant)

        c = canvas.Canvas(file_name, pagesize=(1920, 1080))
        c.setStrokeColorRGB(0, 0, 0)
        c.setFillColorRGB(0, 0, 0)

        PdfTextHelper.write_block(c, description, text_block_x, text_block_y, font_size, vertical_space, horizontal_limit_width)

        c.drawImage(self.cerfiticate_info.signature, sign_x, sign_y, mask='auto', width=200, height=200)

        c.showPage()

        c.save()
