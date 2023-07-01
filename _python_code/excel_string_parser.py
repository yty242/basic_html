# https://blog.naver.com/djsudaqw/223144165549
import pandas as pd
import re

# 데이터 파일 경로
file_path = r"D:\python\영문 한글 나누기.xlsx"

# Excel 파일 읽기
df = pd.read_excel(file_path, sheet_name="Sheet1")

# 데이터 분리 함수 정의
def split_data(data):
    data = data.strip()  # 공백 제거
    english = re.findall(r"[a-zA-Z\s]+", data)
    korean = re.findall(r"[ㄱ-ㅎ가-힣\s]+", data)
    numbers = "".join(re.findall(r"(?<!\S)\d+|\d+(?!\S)", data))
    hanja = "".join(re.findall(r"(?<!\S)[一-龥]+|[一-龥]+(?!\S)", data))
    return english[0] if english else "", korean[0] if korean else "", numbers, hanja

# 데이터 분리
result = []
for index, row in df.iterrows():
    english, korean, numbers, hanja = split_data(row["no artist"])
    result.append((english, korean, numbers, hanja))

# 결과를 데이터프레임으로 변환
result_df = pd.DataFrame(result, columns=["영어", "한글", "숫자", "한자"])

# 각 열에서 좌우 공백 제거
result_df["영어"] = result_df["영어"].str.strip()
result_df["한글"] = result_df["한글"].str.strip()
result_df["숫자"] = result_df["숫자"].str.strip()
result_df["한자"] = result_df["한자"].str.strip()

# 결과를 Excel 파일로 저장
output_file = r"D:\python\영문 한글 나누기_결과.xlsx"
result_df.to_excel(output_file, index=False)
