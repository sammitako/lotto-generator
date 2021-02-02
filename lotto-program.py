import random

# 내 로또번호 생성
def generate_numbers(num):
    my_lotto = []
    while len(my_lotto) < num:
        new_number = random.randint(1, 45)
        if new_number not in my_lotto:
            my_lotto.append(new_number)

    return my_lotto

# 당첨 로또번호 생성
def real_winning_number():
    winning_list = generate_numbers(7) # 보너스 포함
    # 1. 내 로또번호 6개와 당첨 번호 6개 중 몇개가 일치?
    # 2. 내 로또번호 6개와 보너스 번호 1개 중 몇개가 일치?
    return sorted(winning_list[:6]) + winning_list[6:] # 마지막 1개 = 보너스 번호

def count_matching_number(my_lotto, winning_list):
    cnt = 0

    for num in my_lotto:
        if num in winning_list:
            cnt += 1
    return cnt

def check_result(my_lotto, winning_list):
    cnt = count_matching_number(my_lotto, winning_list[:6])
    bonus_cnt = count_matching_number(my_lotto, winning_list[6:])

    if cnt == 6:
        return str('1등')
    elif cnt == 5 and bonus_cnt == 1:
        return str('2등')
    elif cnt == 5:
        return str('3등')
    elif cnt == 4:
        return str('4등')
    elif cnt == 3:
        return str('5등')
    else:
        return str('꽝')

# 복권 5장
winning_list = real_winning_number()
result = []
print('당첨 복권: ', winning_list)

for i in range(0, 5):
    tmp = generate_numbers(6)
    print(f'[{i+1}]장', tmp)
    str_result = check_result(tmp, winning_list)
    result.append(str_result)

# 결과 출력
print('--<결과 보기>--')
for i in range(5):
    print(f'[{i+1}]장: ', result[i])

# 갯수 출력
cnt = [0,0,0,0,0,0]
for j in range(5):
    for i in result[j]:
        # print(i) # 꽝을 제외하고 n등이 2줄로 출력됨
        if '꽝' == i:
            cnt[0] += 1
        elif '5' == i:
            cnt[5] += 1
        elif '4' == i:
            cnt[4] += 1
        elif '3' == i:
            cnt[3] += 1
        elif '2' == i:
            cnt[2] += 1
        elif '1' == i:
            cnt[1] += 1
        else:
            pass

print('--<총 당첨 갯수>--')
print('(1등 : {}개), (2등 : {}개), (3등 : {}개), (4등 : {}개), (5등 : {}개), (꽝 : {}개)'.format(cnt[1], cnt[2], cnt[3], cnt[4], cnt[5], cnt[0]))