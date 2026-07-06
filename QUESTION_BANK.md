# 전체 질문 목록

이 문서는 백엔드 신입/주니어 면접에서 나올 수 있는 보편 질문과, 이력서 기반으로 깊게 이어질 수 있는 질문을 함께 정리한 목록입니다.

개별 문서는 이 목록에서 질문을 하나씩 골라 `TEMPLATE.md` 형식으로 작성합니다.

## Database

- 트랜잭션이란 무엇인가요?
- ACID를 설명해주세요.
- 트랜잭션 격리 수준에는 무엇이 있나요?
- Dirty Read, Non-repeatable Read, Phantom Read의 차이는 무엇인가요?
- 인덱스는 왜 조회를 빠르게 하나요?
- 인덱스를 많이 만들면 왜 안 좋나요?
- clustered index와 non-clustered index의 차이는 무엇인가요?
- 복합 인덱스에서 컬럼 순서가 중요한 이유는 무엇인가요?
- 정규화와 반정규화의 차이는 무엇인가요?
- JOIN의 종류를 설명해주세요.
- DB 락에는 어떤 종류가 있나요?
- 낙관 락과 비관 락의 차이는 무엇인가요?
- Redis를 왜 사용하나요?
- Redis와 RDB의 차이는 무엇인가요?
- 캐시 무효화는 어떻게 처리하나요?
- 재고 1개에 동시에 100명이 주문하면 어떻게 막나요?
- 비관 락을 쓰면 성능이 떨어지는데 왜 선택하나요?
- MySQL에서 인덱스가 왜 조회를 빠르게 하나요?
- Redis 캐시와 DB 데이터가 불일치하면 어떻게 하나요?
- 트랜잭션 격리 수준을 잘못 고르면 어떤 문제가 생기나요?

## Network

- HTTP와 HTTPS의 차이는 무엇인가요?
- HTTP request/response 구조를 설명해주세요.
- GET과 POST의 차이는 무엇인가요?
- PUT과 PATCH의 차이는 무엇인가요?
- HTTP status code 2xx, 3xx, 4xx, 5xx의 차이는 무엇인가요?
- TCP와 UDP의 차이는 무엇인가요?
- TCP 3-way handshake를 설명해주세요.
- DNS가 무엇인가요?
- 브라우저에 URL을 입력하면 어떤 일이 일어나나요?
- 쿠키와 세션의 차이는 무엇인가요?
- CORS란 무엇인가요?
- REST API란 무엇인가요?
- keep-alive란 무엇인가요?
- timeout은 왜 필요한가요?
- retry를 무조건 하면 안 되는 이유는 무엇인가요?
- 결제 승인 요청이 중복으로 들어오면 어떻게 처리하나요?
- timeout과 retry를 어떻게 설정해야 하나요?
- HTTPS는 어떻게 안전한 통신을 보장하나요?
- webhook을 받을 때 위조 요청은 어떻게 막나요?

## Operating System

- 프로세스와 스레드의 차이는 무엇인가요?
- 멀티프로세스와 멀티스레드의 차이는 무엇인가요?
- 컨텍스트 스위칭이란 무엇인가요?
- 동기와 비동기의 차이는 무엇인가요?
- blocking과 non-blocking의 차이는 무엇인가요?
- 동시성과 병렬성의 차이는 무엇인가요?
- race condition이란 무엇인가요?
- critical section이란 무엇인가요?
- mutex와 semaphore의 차이는 무엇인가요?
- deadlock의 4가지 조건은 무엇인가요?
- thread-safe하다는 것은 무슨 뜻인가요?
- thread pool을 사용하는 이유는 무엇인가요?
- CPU-bound와 I/O-bound 작업의 차이는 무엇인가요?
- 메모리의 stack과 heap 차이는 무엇인가요?
- 스레드풀 고갈은 왜 발생하나요?
- 외부 API 호출을 요청 흐름에서 분리한 이유는 무엇인가요?
- Java synchronized와 DB lock은 무엇이 다른가요?
- JVM GC가 오래 걸리면 서버에 어떤 영향이 있나요?

## Java, Kotlin, JVM

- JVM이란 무엇인가요?
- Java 코드가 실행되는 과정을 설명해주세요.
- GC란 무엇인가요?
- heap과 stack의 차이는 무엇인가요?
- equals와 hashCode를 같이 재정의해야 하는 이유는 무엇인가요?
- String, StringBuilder, StringBuffer의 차이는 무엇인가요?
- final 키워드는 어디에 쓰이나요?
- interface와 abstract class의 차이는 무엇인가요?
- checked exception과 unchecked exception의 차이는 무엇인가요?
- Optional을 왜 사용하나요?
- Java Stream의 장단점은 무엇인가요?
- Kotlin의 nullable 타입은 어떤 장점이 있나요?
- Kotlin data class의 특징은 무엇인가요?
- Java와 Kotlin을 같이 쓸 때 주의할 점은 무엇인가요?

## Spring, JPA

- Spring Framework를 왜 사용하나요?
- IoC와 DI란 무엇인가요?
- Bean이란 무엇인가요?
- Spring Bean의 생명주기는 어떻게 되나요?
- Singleton Bean은 thread-safe한가요?
- Spring MVC 요청 흐름을 설명해주세요.
- Filter와 Interceptor의 차이는 무엇인가요?
- AOP란 무엇인가요?
- `@Transactional`은 어떻게 동작하나요?
- self-invocation에서 `@Transactional`이 적용되지 않는 이유는 무엇인가요?
- JPA 영속성 컨텍스트란 무엇인가요?
- dirty checking이란 무엇인가요?
- lazy loading과 eager loading의 차이는 무엇인가요?
- N+1 문제는 왜 발생하나요?
- JPA에서 cascade와 orphanRemoval의 차이는 무엇인가요?
- QueryDSL을 쓰는 이유는 무엇인가요?

## Data Structure, Algorithm

- Array와 LinkedList의 차이는 무엇인가요?
- Stack과 Queue의 차이는 무엇인가요?
- HashMap은 어떻게 동작하나요?
- Hash 충돌은 어떻게 해결하나요?
- Tree와 Graph의 차이는 무엇인가요?
- Binary Search Tree란 무엇인가요?
- Heap은 어디에 쓰이나요?
- BFS와 DFS의 차이는 무엇인가요?
- 정렬 알고리즘의 시간복잡도를 설명해주세요.
- Big-O 표기법이란 무엇인가요?
- 시간복잡도와 공간복잡도의 차이는 무엇인가요?
- List, Set, Map의 차이는 무엇인가요?
- Java HashMap과 ConcurrentHashMap의 차이는 무엇인가요?

## System Design

- 대용량 트래픽을 어떻게 처리하나요?
- 서버 확장 방식 scale-up과 scale-out의 차이는 무엇인가요?
- 로드밸런서는 왜 필요한가요?
- 캐시는 어디에 두는 게 좋나요?
- CDN은 왜 사용하나요?
- 메시지 큐를 왜 사용하나요?
- 동기 처리와 비동기 처리의 장단점은 무엇인가요?
- 배치와 스케줄러의 차이는 무엇인가요?
- 장애가 난 외부 API를 어떻게 격리하나요?
- 모니터링 지표는 무엇을 봐야 하나요?
- 로그, 메트릭, 트레이스의 차이는 무엇인가요?
- p95, p99 latency는 왜 보나요?
- 무중단 배포는 어떻게 하나요?
- 선착순 주문 시스템을 설계해보세요.
- 배송 추적 시스템을 어떻게 설계하겠습니까?
- 외부 API 장애가 주문 시스템에 영향을 주지 않게 하려면 어떻게 해야 하나요?
- 트래픽이 10배 늘면 어디부터 바꾸겠습니까?

## Security

- 인증과 인가의 차이는 무엇인가요?
- 세션 기반 인증과 토큰 기반 인증의 차이는 무엇인가요?
- JWT의 장단점은 무엇인가요?
- OAuth2 흐름을 설명해주세요.
- SQL Injection이란 무엇인가요?
- XSS란 무엇인가요?
- CSRF란 무엇인가요?
- CORS와 CSRF는 어떻게 다른가요?
- 비밀번호는 어떻게 저장해야 하나요?
- 개인정보 마스킹은 왜 필요한가요?
- HTTPS를 써도 보안상 주의할 점은 무엇인가요?
- refresh token은 왜 필요한가요?
- 개인정보가 로그에 찍히지 않게 하려면 어떻게 해야 하나요?
- 관리자 API는 어떻게 보호하나요?

## Test, Quality

- 단위 테스트와 통합 테스트의 차이는 무엇인가요?
- mocking은 언제 사용하나요?
- 테스트하기 좋은 코드는 어떤 코드인가요?
- 테스트 커버리지가 높으면 좋은 코드인가요?
- TDD란 무엇인가요?
- 회귀 테스트란 무엇인가요?
- E2E 테스트의 장단점은 무엇인가요?
- 동시성 테스트는 어떻게 하나요?
- 테스트에서 DB를 어떻게 다루나요?
- 테스트 격리는 왜 중요한가요?

## Infrastructure, Cloud

- EC2와 Lambda의 차이는 무엇인가요?
- RDS를 쓰는 이유는 무엇인가요?
- S3는 어떤 저장소인가요?
- CDN은 어떻게 동작하나요?
- Docker를 쓰는 이유는 무엇인가요?
- 컨테이너와 VM의 차이는 무엇인가요?
- 환경변수로 설정을 분리하는 이유는 무엇인가요?
- 서버 로그는 어디에 남기고 어떻게 확인하나요?
- health check는 왜 필요한가요?
- 배포 중 장애가 나면 어떻게 롤백하나요?

## Priority 30

- 트랜잭션이란 무엇인가요?
- ACID란 무엇인가요?
- 격리 수준이란 무엇인가요?
- 인덱스는 어떻게 동작하나요?
- N+1 문제란 무엇인가요?
- 낙관 락과 비관 락의 차이는 무엇인가요?
- Redis는 왜 쓰나요?
- 캐시 무효화는 어떻게 하나요?
- HTTP와 HTTPS의 차이는 무엇인가요?
- GET, POST, PUT, PATCH의 차이는 무엇인가요?
- TCP 3-way handshake란 무엇인가요?
- URL 입력 시 어떤 일이 일어나나요?
- timeout과 retry는 왜 필요한가요?
- 프로세스와 스레드의 차이는 무엇인가요?
- blocking과 non-blocking의 차이는 무엇인가요?
- race condition이란 무엇인가요?
- deadlock의 4가지 조건은 무엇인가요?
- thread pool을 왜 쓰나요?
- JVM과 GC란 무엇인가요?
- equals와 hashCode를 왜 같이 재정의하나요?
- IoC와 DI란 무엇인가요?
- Bean이란 무엇인가요?
- `@Transactional`의 동작 원리는 무엇인가요?
- 영속성 컨텍스트란 무엇인가요?
- lazy loading이란 무엇인가요?
- 메시지 큐를 왜 쓰나요?
- 멱등성이란 무엇인가요?
- 인증과 인가의 차이는 무엇인가요?
- JWT의 장단점은 무엇인가요?
- 단위 테스트와 통합 테스트의 차이는 무엇인가요?
