# System Design

확장성, 캐시, 메시지 큐, 장애 격리, 관측 가능성과 관련된 면접 질문을 정리합니다.

우선 작성할 질문:

- scale-up과 scale-out의 차이는 무엇인가요?
- 메시지 큐를 왜 사용하나요?
- 동기 처리와 비동기 처리의 장단점은 무엇인가요?
- 멱등성이란 무엇인가요?
- 외부 API 장애를 어떻게 격리할 수 있나요?
- p95, p99 latency를 왜 보나요?
- 로그, 메트릭, 트레이스의 차이는 무엇인가요?

## 레퍼런스 기반 질문 후보

- [단일 장애 지점(SPOF)이란 무엇인가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-85.md) (maeil-mail)
- [동기 방식으로 외부 서비스를 호출할 때 외부 서비스 장애가 나면 어떻게 조치할 수 있나요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-30.md) (maeil-mail)
- [로드 밸런싱에 대해서 설명해주세요](https://dev-letter.kr/posts/load-balancing) (dev-letter)
- [로드 밸런싱에 대해서 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-53.md) (maeil-mail)
- [분산 트랜잭션 — 2PC, Saga, Transactional Outbox](https://dev-letter.kr/posts/distributed-transaction) (dev-letter)
- [분산 환경에서 Redis를 활용한 잠금은 어떻게 구현할 수 있나요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-95.md) (maeil-mail)
- [스케일 아웃과 스케일 업의 차이점을 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-58.md) (maeil-mail)
- [시스템 간 비동기 연동 방식에는 무엇이 있나요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-63.md) (maeil-mail)
- [이벤트 소싱이란 무엇인가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-144.md) (maeil-mail)
- [최종적 일관성이란 무엇인가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-141.md) (maeil-mail)
- [캐시 스탬피드 현상에 대하여 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-62.md) (maeil-mail)
- [캐싱 전략에 대해서 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-55.md) (maeil-mail)
- [트랜잭셔널 아웃박스 패턴에 대해서 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-83.md) (maeil-mail)
- [CAP 정리에 대해서 알고 계신가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-64.md) (maeil-mail)
- [CQRS 패턴이란 무엇인가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-92.md) (maeil-mail)
- [DB Replication에 대해서 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-50.md) (maeil-mail)
- [Graceful Shutdown의 필요성에 대해서 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-93.md) (maeil-mail)
- [HTTP 헤더 심화 — 캐시, 인증, 콘텐츠 협상, 보안](https://dev-letter.kr/posts/http-headers) (dev-letter)
- [Redis가 싱글 스레드로 만들어진 이유를 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-66.md) (maeil-mail)
