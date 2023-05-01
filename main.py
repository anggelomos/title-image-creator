import textwrap

from PIL import Image, ImageDraw, ImageFont

ticket_title = "[Ticket-204] A very long sample ticket title that needs to be wrapped to multiple lines and centered"
image_size = (2000, 250)
font_size = 50
line_width = 75
line_padding = 5

font = ImageFont.truetype("font/Poppins-Regular.ttf", size=font_size)
image_width, image_height = image_size
image = Image.new("L", image_size, color=255)
draw = ImageDraw.Draw(image)

wrapped_ticket_title = textwrap.wrap(ticket_title, width=line_width)
current_height = 0
for line in wrapped_ticket_title:
    _, _, text_width, text_height = draw.textbbox((0, 0), line, font=font)

    if not current_height:
        current_height = (image_height - text_height) / 2 - (len(wrapped_ticket_title) * line_padding * 4)

    draw.text(((image_width - text_width) / 2, current_height), line, font=font, fill="black")
    current_height += text_height + line_padding

image.save("sample_ticket_image.png", "PNG")
