n = int(input())
num = (n%10)*10 + (n//10 + n%10)%10  # (주어진 수의 가장 오른쪽 자리 수) * 10 + (각 자리 수 합의 가장 오른쪽 자리 수)
i = 1
while n!=num:  # 원래 수로 돌아올 때까지 반복
    num = (num%10)*10 + (num//10 + num%10)%10
    i += 1
print(i)  # 사이클 길이 출력