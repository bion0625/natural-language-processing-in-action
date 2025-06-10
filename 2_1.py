# 띄어쓰기 단위로 분리
input_text = "나는 최근 파리 여행을 다녀왔다"
input_text_list = input_text.split()
print("input_text_list: ", input_text_list)

# 토큰 -> 아이디 딕셔너리와 아이디 -> 토큰 딕셔너리 만들기
str2idx = {word:idx for idx, word in enumerate(input_text_list)}
idx2str = {idx:word for idx, word in enumerate(input_text_list)}
print("str2idx: ", str2idx)
print("idx2str: ", idx2str)

# 토큰을 토큰 아이디로 변환
input_ids = [str2idx[word] for word in input_text_list]
print("input_ids: ", input_ids)

# 출력 결과
# input_text_list:  ['나는', '최근', '파리', '여행을', '다녀왔다']
# str2idx:  {'나는': 0, '최근': 1, '파리': 2, '여행을': 3, '다녀왔다': 4}
# idx2str:  {0: '나는', 1: '최근', 2: '파리', 3: '여행을', 4: '다녀왔다'}
# input_ids:  [0, 1, 2, 3, 4]