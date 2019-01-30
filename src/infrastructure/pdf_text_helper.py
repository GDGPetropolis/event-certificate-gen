from textwrap import wrap


class PdfTextHelper(object):

    @classmethod
    def write_block(cls, canvas, text, x, y, font_size, vertical_space, horizontal_limit_width):
        lines = wrap(text, horizontal_limit_width)

        jump_line = 0
        for line in lines:
            t = canvas.beginText()
            t.setFont('Helvetica', font_size)
            t.setCharSpace(3)
            t.setTextOrigin(x, y-(jump_line*vertical_space))
            t.textLine(cls.__get_line_centralized(line, horizontal_limit_width))
            canvas.drawText(t)
            jump_line = jump_line + 1

    @classmethod
    def __get_line_centralized(cls, line, size):
        space_to_add = int((size - len(line)) / 2*1.33)
        return (" " * space_to_add) + line
