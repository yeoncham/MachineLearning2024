import pandas as pd

def load_and_preprocess(csv_path: str, encoding: str = "cp949"):
    """
    Student Performance 데이터 전처리 함수
    - 결측값: 최빈값으로 대체
    - 범주형 변수: 수동 매핑(Label Encoding)
    """

    df = pd.read_csv(csv_path, encoding=encoding)

    # 결측값 처리 (최빈값 대체)
    for col in ["Teacher_Quality", "Parental_Education_Level", "Distance_from_Home"]:
        df[col] = df[col].fillna(df[col].mode()[0])

    # 범주형 컬럼 매핑 정의
    category_mappings = {
        "Parental_Involvement": {"Low": 0, "Medium": 1, "High": 2},
        "Access_to_Resources": {"Low": 0, "Medium": 1, "High": 2},
        "Extracurricular_Activities": {"No": 0, "Yes": 1},
        "Motivation_Level": {"Low": 0, "Medium": 1, "High": 2},
        "Internet_Access": {"No": 0, "Yes": 1},
        "Family_Income": {"Low": 0, "Medium": 1, "High": 2},
        "Teacher_Quality": {"Low": 0, "Medium": 1, "High": 2},
        "School_Type": {"Public": 0, "Private": 1},
        "Peer_Influence": {"Negative": 0, "Neutral": 1, "Positive": 2},
        "Learning_Disabilities": {"No": 0, "Yes": 1},
        "Parental_Education_Level": {"High School": 0, "College": 1, "Postgraduate": 2},
        "Distance_from_Home": {"Far": 0, "Moderate": 1, "Near": 2},
        "Gender": {"Male": 0, "Female": 1}
    }

    # 각 범주형 변수에 매핑 적용
    for col, mapping in category_mappings.items():
        df[col] = df[col].map(mapping)

    return df


if __name__ == "__main__":
    df = load_and_preprocess("data/StudentPerformanceFactors.csv")
    print(df.head())
