
import pandas as pd
from sklearn import metrics
import os
from sklearn.svm import SVC
import joblib

datafile = '../data/lang/freq.json'

if not os.path.exists(datafile):
    print(f"{datafile}이 존재하지 않습니다.")
else:
    # (1) 데이터 파일 로딩
    df= pd.read_json(datafile)
    # 데이터 확인
    df.info()
    print(f"data ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n{df.head()}")
    print(f"df.index =>{df.index}\ndf.columns => {df.columns}")

    # 데이터 분리 / 학습용 테스트용
    train_data = df.iloc[0, 0]
    train_label = df.iloc[0, 1]
    test_data = df.iloc[1, 0]
    test_label = df.iloc[1, 1]
    print(f"train data ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n{train_data}")
    print(f"train label ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n{train_label}")

    svcModel = SVC() # SVC로 학습한 결과를 svcModel안에 저장

    svcModel.fit(train_data, train_label) # train 으로 데이터 학습

    pre = svcModel.predict(test_data) # pre 변수 안에 test 결과
    score = metrics.accuracy_score(test_label,pre) # 정답율 계산
    report =metrics.classification_report(test_label, pre)

# score의 정확도가 0.98이 넘으면 저장
if score >= 0.98:
    modelName="../data/lang/lang.pkl" # data 안에 lang 안에 lang.pk1이라는 이름
    joblib.dump(svcModel, modelName) # svcModel을 불러와서 modelName으로 저장
    if os.path.exists(modelName): print("save model!")







