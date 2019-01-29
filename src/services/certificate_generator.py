import os
from textwrap import wrap
from reportlab.pdfgen import canvas
from src.entities.certificate_info import CertificateInfo
from src.infrastructure.pdf_helper import PdfHelper


class CertificateGenerator(object):
    cerfiticate_info = None
    participant = None

    def __init__(self, cerfiticate_info = CertificateInfo):
        self.cerfiticate_info = cerfiticate_info

    def generate(self, participant: str):
        if participant:
            self.participant = participant
            self.__generate_pdf()

    def __get_event_folder_name(self):
        return "output/" + self.cerfiticate_info.event_name

    def __get_participant_file_name(self, folder: str):
        return folder + "/" + self.participant + ".pdf"

    def __create_event_folder_if_doesnt_exist(self, folder_name: str):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

    def __build_description(self):
        description = self.cerfiticate_info.description

        description = description.replace("<organizer>", self.cerfiticate_info.organizer)
        description = description.replace("<event_type>", self.cerfiticate_info.event_type)
        description = description.replace("<event_name>", self.cerfiticate_info.event_name)
        description = description.replace("<action>", self.cerfiticate_info.action)
        description = description.replace("<participant>", self.participant)
        description = description.replace("<date>", self.cerfiticate_info.date)

        return description

    def __generate_pdf(self):
        font_size = 35
        vertical_space = 50
        horizontal_limit_width = 80
        x = 215
        y = 700

        folder_name = self.__get_event_folder_name()
        self.__create_event_folder_if_doesnt_exist(folder_name)

        file_name = self.__get_participant_file_name(folder_name)

        c = canvas.Canvas(file_name, pagesize=(1920, 1080))
        c.setStrokeColorRGB(0, 0, 0)
        c.setFillColorRGB(0, 0, 0)

        PdfHelper.write_text_block(c, self.__build_description(), x, y, font_size, vertical_space, horizontal_limit_width)

        c.showPage()

        c.save()
