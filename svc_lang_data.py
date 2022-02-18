# 알파벳 언어별 데이터를 학습에 사용할 수 있도록 데이터 변환
# Json 형태로 변환
# Python dictionary 형태와 유사하다.
# Json => {키 : 값 , 키 : 값} = > [1, 2, 3]
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
import os
import json, glob, re
from sklearn import svm, metrics
# 파일 관련 변수 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
dir = "../data/lang"
dataFile = f"{dir}freq.json"
# 폴더 생성
if not os.path.exists(dir): os.mkdir(dir)
# 사용자 정의 함수
# 파일에서 a ~ z 알파벳 반도 수 체크, 라벨 함수
def check_freq (fname):
    name = os.path.basename(fname)
    lang = re.match(r'^[a-z]{2,}', name).group()
    with open(fname, "r",encoding="utf-8") as f:
        text = f.read()
    text = text.lower() # 소문자 변환
    cnt = [0 for n in range(0,26)]
    code_a = ord("a")
    code_z = ord("z")
    # 알파벳 출현 횟수 구하기
    for ch in text:
        n = ord(ch)
        if code_a <= n <= code_z:
            cnt[n - code_a] += 1
    total = sum(cnt)
    freq = list(map(lambda  n : n / total, cnt))
    return (freq, lang)

# 전체 파일 a ~ z 알파벳 빈도수 따른 데이터 추출 함수
def load_files(path):
    freqs =[]
    labels = []
    file_list = glob.glob(path)
    for fname in file_list:
        r = check_freq(fname)
        freqs.append(r[0])
        labels.append(r[1])
    return{"freqs": freqs, "labels" : labels}
data = load_files('../data/lang/train/*.txt')
test = load_files('../data/lang/test/*.txt')

with open("../data/lang/freq.json","w",encoding="utf-8") as fp:
    json.dump([data, test], fp)


clf = svm.SVC()
clf.fit(data["freqs"], data["labels"])

pre = clf.predict(test["freqs"])

score = metrics.accuracy_score(test["labels"],pre)
report = metrics.classification_report(test["labels"],pre)
print("정답률 : ", score)
print("리포트 =")
print(report)

