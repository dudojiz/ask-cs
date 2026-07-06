# 참고 저장소

이 문서는 질문 목록과 문서 구조를 보강할 때 참고할 외부 저장소를 기록합니다.

외부 저장소의 내용을 그대로 복사하지 않습니다. 라이선스가 명확하지 않은 경우에는 질문 분류, 누락 주제 점검, 공식 문서 탐색의 출발점으로만 사용합니다.

## 원칙

- 원본 저장소에 명시 라이선스가 없으면 본문, 해설, 예시를 그대로 가져오지 않습니다.
- 질문 목록은 누락 주제 점검과 문서 작성 후보로만 사용합니다.
- 개별 문서는 우리 템플릿에 맞춰 새로 작성하고, 최종 근거는 공식 문서나 표준 문서로 검증합니다.
- 원본 전체를 보존해야 할 때는 복사본을 만들지 않고 원본 목차와 컨텐츠 디렉터리 링크를 남깁니다.
- 원저작자 허락 또는 재사용 가능한 라이선스가 확인되면, 별도 PR에서 출처와 라이선스 고지를 포함해 가져옵니다.

## maeil-mail-contents

- 저장소: [maeil-mail/maeil-mail-contents](https://github.com/maeil-mail/maeil-mail-contents)
- 설명: 매일메일 기술 면접 컨텐츠 아카이브
- 범위: Backend, Frontend
- 확인한 구조:
  - `backend/toc.md`
  - `backend/toc-category.md`
  - `backend/contents/`
  - `frontend/toc.md`
  - `frontend/toc-category.md`
  - `frontend/contents/`
- 원본 전체 링크:
  - [Backend 질문 ID 기준 목차](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/toc.md)
  - [Backend 카테고리 기준 목차](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/toc-category.md)
  - [Backend 컨텐츠 디렉터리](https://github.com/maeil-mail/maeil-mail-contents/tree/main/backend/contents)
  - [Frontend 질문 ID 기준 목차](https://github.com/maeil-mail/maeil-mail-contents/blob/main/frontend/toc.md)
  - [Frontend 카테고리 기준 목차](https://github.com/maeil-mail/maeil-mail-contents/blob/main/frontend/toc-category.md)
  - [Frontend 컨텐츠 디렉터리](https://github.com/maeil-mail/maeil-mail-contents/tree/main/frontend/contents)
- 활용 방식:
  - 백엔드/프론트엔드 질문 후보를 각 카테고리 README에 분류해 반영
  - 질문은행의 누락 주제 점검
  - 개별 문서 작성 시 참고 자료 후보 탐색
- 주의:
  - GitHub 메타데이터 기준 라이선스가 명시되어 있지 않으므로, 컨텐츠 본문이나 해설을 그대로 가져오지 않습니다.
  - 개별 문서 작성 시 최종 근거는 공식 문서, 표준 문서, 서적 등 신뢰 가능한 자료로 검증합니다.

## dev-letter

- 사이트: [dev-letter](https://dev-letter.kr/)
- 아티클 목록: [전체 아티클](https://dev-letter.kr/articles)
- 설명: 인터랙티브 CS 시각화 뉴스레터
- 범위: Spring, OS, Network, Database, Data Structure, DevOps, Programming, System Design
- 확인한 구조:
  - Foundations: 54개 아티클
  - System Design: 4개 아티클
  - 전체: 58개 아티클
- 활용 방식:
  - 시각화가 필요한 CS 주제를 각 카테고리 README에 분류해 반영
  - 면접 질문의 꼬리 질문과 실무 연결 보강
  - 개별 문서 작성 시 참고 자료 후보 탐색
- 주의:
  - 본문, 예시, 시각화 설명을 그대로 가져오지 않습니다.
  - 개별 문서 작성 시 최종 근거는 공식 문서, 표준 문서, 서적 등 신뢰 가능한 자료로 검증합니다.
