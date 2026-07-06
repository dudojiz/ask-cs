
| 항목 | 내용 | 
|---|---| 
| 작성일자 | 2026.07.06 | 
| 작성자 | kimmandoo | 
| 카테고리 | android | 
| 난이도 | 기본 | 

## 질문

> Activity가 Single 인스턴스로 유지되려면 어떻게 해야될까?

## 핵심 답변

`AndroidManifest.xml` 매니페스트 파일의 `<activity>` 태그에 `android:launchMode="singleInstance"` 속성을 설정하면 됩니다. `singleInstance`로 설정된 Activity는 새로운 Task에서 실행되며, 그 Task에는 그 Activity 인스턴스 하나만 존재하게 됩니다. 이후 해당 Activity로 들어오는 모든 Intent는 이 기존 인스턴스의 `onNewIntent()`를 호출하게 됩니다.

---

## 해설

답변에 대한 해설을 자세히 작성합니다.

---

## 예시

필요하다면 코드, SQL, 그림, 요청/응답 예시 등을 작성합니다.

---

## 꼬리 질문

- 관련해서 이어질 수 있는 질문을 작성합니다.

---

## 실무 연결

해당 개념이 백엔드 개발, 장애 대응, 성능 개선, 시스템 설계에서 어떻게 쓰이는지 작성합니다.

---

## 참고 자료

- [링크](example.com)
