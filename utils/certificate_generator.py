from PIL import Image, ImageDraw, ImageFont

def generate_certificate(name,template_path,save_path,course_name='Blockchain Basics'):
    # Load the certificate template
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Load a font
    font = ImageFont.truetype('fonts/Parisienne-Regular.ttf', 175)
    text_width = draw.textlength(name, font=font)
    x_center = (img.width - text_width) // 2
    draw.text((x_center, 610), name, font=font, fill='#111110')

    font2 = ImageFont.truetype('fonts/Poppins-Regular.ttf', 40)
    x_center = (img.width - draw.textlength('Who has completed the course in', font=font2)) // 2
    draw.text((x_center, 800), 'Who has completed the course in', font=font2, fill='#111110')

    x_center = (img.width - draw.textlength(course_name, font=font2)) // 2
    draw.text((x_center, 850), course_name, font=font2, fill='#111110')



    # Save the certificate to gen_certs folder
    img.save(save_path)

