from PIL import Image
import qrcode

BASE_URL = "https://YOUR-USERNAME.github.io/subiksha-certificate-verification/"
CERTIFICATE_ID = "SMA-2026-001"

url = BASE_URL.rstrip("/") + "/?id=" + CERTIFICATE_ID
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=2)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image()
img.save("verification_qr.png")
print("QR generated for:", url)
