import random
import time


def show_status(name: str, weight: int, hp: int, hunger: float) -> None:
    print(f"캐릭터 이름: {name}")
    print(f"캐릭터 몸무게: {weight}kg")
    print(f"체력: {hp}")
    print(f"배고픔: {hunger}")


def create_character():
    name: str = input("이름을 입력하세요: ")
    weight: int = int(random.randint(45, 100))

    print(f"환영합니다, {name} 생존자님!")
    print(f"당신의 몸무게는 {weight}kg으로 설정되었습니다.")

    hp: int = 80
    hunger: float = 95.2
    print(f"초기 상태 -> 체력: {hp}, 배고픔: {hunger}%")

    print(show_status(name, weight, hp, hunger))


create_character()

print("주위를 살펴보는 중...")
time.sleep(2)
print("아무것도 발견하지 못했다.")
