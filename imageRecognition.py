import easyocr

class ImageRecognition:

    def getImageText(self):
        image_path = 'campmail.jpg'
        reader = easyocr.Reader(['en'])
        results = reader.readtext(image_path)
        extracted_text = []
        for (bbox, text, prob) in results:
            extracted_text.append(text)

        return extracted_text[0]