from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.pdfgen import canvas
from certificategen.entities.certificate_info import CertificateInfo
from certificategen.infrastructure.description_helper import DescriptionHelper
from certificategen.infrastructure.directory_helper import DirectoryHelper
from certificategen.infrastructure.name_helper import NameHelper
from certificategen.infrastructure.pdf_text_helper import PdfTextHelper


class CertificateGenerator(object):

    def __init__(self, cerfiticate_info: CertificateInfo):
        self.cerfiticate_info = cerfiticate_info

    def generate(self, participant: str):
        if participant:
            self.participant = participant
            self.__generate_watermark()
            self.__generate_pdf()

    def __generate_watermark(self):
        font_size = 32
        vertical_space = 50
        horizontal_limit_width = 60
        text_block_x = 430
        text_block_y = 650
        sign_x = 630
        sign_y = -30
        description = DescriptionHelper.interpolate(self.cerfiticate_info, self.participant)

        DirectoryHelper.create_folder_if_doesnt_exist(self.cerfiticate_info)

        c = canvas.Canvas(filename="output/watermark.pdf", pagesize=(1920, 1080))

        c.setStrokeColorRGB(0, 0, 0)
        c.setFillColorRGB(0, 0, 0)

        PdfTextHelper.write_block(c, description, text_block_x, text_block_y, font_size, vertical_space,
                                  horizontal_limit_width)

        c.drawImage(self.cerfiticate_info.signature, sign_x, sign_y, mask='auto', width=650, height=650)

        c.showPage()

        c.save()

    def __generate_pdf(self):
        file_name = NameHelper.get_participant_file_name(self.cerfiticate_info, self.participant)
        watermark = PdfFileReader(open("output/watermark.pdf", "rb"))

        output_file = PdfFileWriter()

        input_file = PdfFileReader(open(self.cerfiticate_info.background, "rb"))
        input_page = input_file.getPage(0)
        input_page.scaleTo(1920, 1080)

        watermark_page = watermark.getPage(0)
        watermark_page.scaleTo(1920, 1080)

        input_page.mergePage(watermark_page)

        output_file.addPage(input_page)

        with open(file_name, "wb") as outputStream:
            output_file.write(outputStream)
