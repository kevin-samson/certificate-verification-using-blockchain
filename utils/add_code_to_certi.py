import qrcode
import PIL

# Read csv file and create QR code
def add_qr_code(file,cert_path,saved_path):
    with open(file, 'r') as f:
        for line in f:
            cert , hash, _ = line.strip().split(',')
            qr = qrcode.QRCode(
                version=2,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=6,
                border=4,
            )
            qr.add_data(f'{hash}')
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            # add qr code to certificate
            cert_img = PIL.Image.open(cert_path+cert+'.png')
            cert_img.paste(img, (875, 1000))
            cert_img.save(saved_path+cert+'.png')

