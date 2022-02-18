# 목 표 : 손글씨 숫자 판별 프로그램
# 데이터 : mnist 60000만개
# 학습 방법 : 데이터 + 라벨 => 지도 학습 => SVC
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
from sklearn import model_selection, svm, metrics

def load_csv(fname):
    labels =[]
    images = []

    with open (fname, "r") as f:
        for line in f:
            cols = line.split(',')
            if len(cols) < 2 : continue
            labels.append(int(cols.pop(0)))
            vals = list (map(lambda  n : int(n) / 256 , cols))
            images.append(vals)
    return {"labels" : labels, "images" : images}

data = load_csv("../mnist/train.csv")
test = load_csv("../mnist/t10k.csv")

clf = svm.SVC()
clf.fit(data["images"], data["labels"])

pre = clf.predict(test["images"])

score = metrics.accuracy_score(test["labels"],pre)
report = metrics.classification_report(test["labels"],pre)
print("정답률 : ", score)
print("리포트 =")
print(report)
