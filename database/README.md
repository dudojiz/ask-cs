# Database

백엔드 면접에서 자주 다루는 데이터베이스 질문을 정리합니다.

우선 작성할 질문:

- 트랜잭션이란 무엇인가요?
- ACID란 무엇인가요?
- 트랜잭션 격리 수준에는 무엇이 있나요?
- 인덱스는 어떻게 동작하나요?
- 낙관 락과 비관 락의 차이는 무엇인가요?
- N+1 문제는 왜 발생하나요?
- Redis를 왜 사용하나요?

## 레퍼런스 기반 질문 후보

- [공유 락과 배타 락에 대해서 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-33.md) (maeil-mail)
- [관계형 데이터베이스와 비 관계형 데이터베이스의 차이점은 무엇인가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-61.md) (maeil-mail)
- [낙관적 락과 비관적 락에 대해 설명해 주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-120.md) (maeil-mail)
- [논리 삭제와 물리 삭제의 차이점은 무엇인가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-136.md) (maeil-mail)
- [데드락(Deadlock) — 교착 상태의 모든 것](https://dev-letter.kr/posts/deadlock) (dev-letter)
- [데이터베이스 시스템에서 동시성을 제어하는 방법에 대해 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-39.md) (maeil-mail)
- [데이터베이스 인덱스 — B-Tree부터 실행 계획까지](https://dev-letter.kr/posts/database-index) (dev-letter)
- [데이터베이스 인덱스에 대해서 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-22.md) (maeil-mail)
- [데이터베이스 정규화 — 1NF부터 BCNF, 역정규화까지](https://dev-letter.kr/posts/database-normalization) (dev-letter)
- [데이터베이스 정규화에 대해서 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-94.md) (maeil-mail)
- [데이터베이스 커넥션 풀(Connection Pool)을 사용하지 않으면 어떤 문제가 발생할 수 있나요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-36.md) (maeil-mail)
- [비관적 락 vs 낙관적 락 — 동시성 문제를 해결하는 두 가지 전략](https://dev-letter.kr/posts/pessimistic-vs-optimistic-lock) (dev-letter)
- [스프링 트랜잭션 전파 속성에 대해서 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-102.md) (maeil-mail)
- [어떤 예외가 발생하면 트랜잭션을 롤백하나요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-135.md) (maeil-mail)
- [열 기반 DB와 행 기반 DB의 차이점은 무엇인가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-126.md) (maeil-mail)
- [트랜잭션 격리 수준과 동시성 문제를 설명해주세요](https://dev-letter.kr/posts/transaction-isolation-levels) (dev-letter)
- [트랜잭션 격리수준은 무엇인가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-23.md) (maeil-mail)
- [트랜잭션과 ACID — 데이터베이스가 신뢰를 지키는 방법](https://dev-letter.kr/posts/transaction-acid) (dev-letter)
- [ACID에 대해서 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-57.md) (maeil-mail)
- [MySQL InnoDB에서 갭락과 넥스트키 락이란 무엇이며, 어떻게  팬텀 리드를 방지하나요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-40.md) (maeil-mail)
- [NoSQL 데이터베이스의 유형에는 어떤 것들이 있나요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-138.md) (maeil-mail)
- [NOT IN 쿼리를 사용할 때 발생할 수 있는 문제와 최적화 방법에 대해 설명해 주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-142.md) (maeil-mail)
- [RDB에서 페이징 쿼리의 필요성을 설명해 주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-121.md) (maeil-mail)
- [Spring 트랜잭션 전파 — REQUIRED부터 NESTED까지](https://dev-letter.kr/posts/spring-transaction-propagation) (dev-letter)
- [Statement와 PreparedStatement의 차이점은 무엇인가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-143.md) (maeil-mail)
