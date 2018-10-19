from flask import Blueprint, jsonify, request

from webapp.ocr import OCR


api = Blueprint('api', __name__)

@api.route('/predict/image', methods=['post'])
def predict_image():
    ocr = OCR()
    try:
        file = request.files['image']
    except Exception:
        return jsonify({ 'error': 'Please send the field \'image\'' }), 400
    
    text = ocr.predict(file, OCR.TYPE_IMAGE)
    return jsonify({ 'predicted_text': text }), 200

@api.route('/predict/document', methods=['post'])
def predict_document():
    ocr = OCR()
    try:
        file = request.files['document']
    except Exception:
        return jsonify({ 'error': 'Please send the field \'document\'' }), 400
    
    text = ocr.predict(file, OCR.TYPE_PDF)
    return jsonify({ 'predicted_text': text }), 200
