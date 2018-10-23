FROM python
LABEL maintainer="Narate Ketram <koonnarate@gmail.com>"
WORKDIR /app
RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev
ADD requirements.txt .
RUN pip install -r requirements.txt

ADD . .
EXPOSE 5000
CMD ["python", "main.py"]
