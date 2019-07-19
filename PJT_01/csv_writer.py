avengers = [
    {
        "name": "tony stark",
        "gender": "male",
        "appearances": 3068,
        "years since joining": 52
    },
    {
        "name": "robert bruce banner",
        "gender": "male",
        "appearances": 2089,
        "years since joining": 52
    }
]

import csv

with open('avengers.csv', 'w', newline='', encoding='utf-8') as f:
    # 저장할 필드의 이름을 미리 지정
    fieldnames = ('name', 'gender', 'appearances', 'years since joining')
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    # 필드 이름을 csv 최상단에 작성
    writer.writeheader()

    # Dictionary를 순회하며 key 값에 맞는 value를 한 줄씩 작성
    for avenger in avengers:
        writer.writerow(avenger)
