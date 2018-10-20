import io
import pytesseract

from PIL import Image
from wand.image import Image as wi


class OCR:
    TYPE_IMAGE = 'TYPE_IMAGE'
    TYPE_PDF = 'TYPE_PDF'

    def predict(self, file, file_type):
        result = []
        if file_type == self.TYPE_IMAGE:
            result = self.__predict_image(file)
        elif file_type == self.TYPE_PDF:
            result = self.__predict_pdf(file)
        return result

    def __predict_image(self, file):
        prediction = []

        file_bytes = io.BytesIO()
        file.save(file_bytes)
        image = Image.open(file_bytes)

        prediction.append(pytesseract.image_to_string(image, lang='eng'))
        return prediction

    def __predict_pdf(self, file):
        prediction = []
        image_blobs = []

        with wi(blob=file, resolution=300) as pdf:
            pdf_image = pdf.convert('jpeg')

            for image in pdf_image.sequence:
                image_page = wi(image=image)
                image_blobs.append(image_page.make_blob('jpeg'))

        for image_blob in image_blobs:
            image = Image.open(io.BytesIO(image_blob))
            prediction.append(pytesseract.image_to_string(image, lang='eng'))

        return prediction
