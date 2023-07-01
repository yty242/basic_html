from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import os

def extract_images_from_pdf(pdf_path, output_path):
    pdf = PdfReader(pdf_path)

    for page_number in range(len(pdf.pages)):
        images = convert_from_path(pdf_path, first_page=page_number+1, last_page=page_number+1)

        for i, image in enumerate(images):
            image.save(f"{output_path}/page_{page_number+1}_image_{i+1}.jpg", "JPEG")

# 사용 예시
pdf_path = r"D:\pdf\4428.pdf"  # 추출할 PDF 파일 경로
output_path = "output_images"  # 이미지를 저장할 디렉토리 경로

# 디렉토리 생성
os.makedirs(output_path, exist_ok=True)

# 이미지 추출
extract_images_from_pdf(pdf_path, output_path)


'''  
	cd /d D:\_s\python_code  #cmd에서 다른 드라이브로 디렉토리 변경
	cd c:\python_code      #cmd에서 같은 드라이브 내 디렉토리 변경
	python pdf_to_image.py

'''