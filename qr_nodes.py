
import numpy as np
import qrcode
from PIL import Image
import torch
import torch.nn.functional as F


class QRBase:
    def __init__(self):
        self.text = ""
        self.fill = None
        self.back = None
        self.margin = 4  # Default margin set to 4, which is typical for QR codes

    FUNCTION = "generate_qr"
    CATEGORY = "ComfyQR"

    def _get_error_correction_constant(self, error_correction_string):
        if error_correction_string == "Low":
            return qrcode.constants.ERROR_CORRECT_L
        if error_correction_string == "Medium":
            return qrcode.constants.ERROR_CORRECT_M
        # ... (Rest of the error correction methods)
        
    def generate_qr(self):
        # Assuming there's a method like this to generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=self._get_error_correction_constant(self.error_correction),
            box_size=10,
            border=self.margin,  # Set the margin size here
        )
        qr.add_data(self.text)
        qr.make(fit=True)

        img = qr.make_image(fill_color=self.fill, back_color=self.back)
        return img
