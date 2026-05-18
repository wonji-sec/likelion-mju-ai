# 4주차 과제: Attention Mechanism 구현하기

이번 주 과제는 교재 Chapter 3 흐름에 맞춰 Attention Mechanism을 직접 구현해보는 실습입니다.

각자 본인 이름 폴더 안에 있는 `attention_mechanism_student.ipynb` 파일을 열고, 노트북에 표시된 `TODO` 부분을 채워주세요.

## 실습 목표

아래 개념을 코드로 구현하면서 Attention이 어떻게 동작하는지 이해하는 것이 목표입니다.

- Dot Product Attention
- Attention Weight와 Context Vector
- Self-Attention
- Query, Key, Value를 사용하는 Self-Attention
- Causal Mask
- Attention Dropout
- Multi-Head Attention

## 진행 방법

1. 본인 이름 폴더로 이동합니다.
2. `attention_mechanism_student.ipynb` 파일을 엽니다.
3. 위에서부터 순서대로 실행하며 `TODO` 주석이 있는 코드를 완성합니다.
4. 각 Part의 출력과 `assert`가 정상적으로 통과하는지 확인합니다.
5. 마지막 최종 과제 셀까지 실행해 `"최종 과제 기본 실행 통과"`가 출력되도록 합니다.

## 제출 위치

완성한 노트북은 본인 이름 폴더 안에 그대로 제출하면 됩니다.

```text
week04/{본인 이름}/attention_mechanism_student.ipynb
```

## 제출 체크리스트

- 모든 `TODO` 코드를 채웠는지 확인
- 노트북을 처음부터 끝까지 다시 실행했을 때 에러가 없는지 확인
- 각 Part의 출력 shape가 의도한 형태인지 확인
- Q/K/V, causal mask, multi-head attention을 자신의 말로 간단히 설명할 수 있는지 확인

## Pull Request 제목

Pull Request 제목은 아래 형식으로 작성해주세요.

```text
[4주차 과제] 홍길동 과제 제출
```
