# Network

HTTP, TCP/IP, DNS, TLS, API 통신과 관련된 면접 질문을 정리합니다.

우선 작성할 질문:

- HTTP와 HTTPS의 차이는 무엇인가요?
- GET과 POST의 차이는 무엇인가요?
- TCP와 UDP의 차이는 무엇인가요?
- TCP 3-way handshake란 무엇인가요?
- 브라우저에 URL을 입력하면 어떤 일이 일어나나요?
- timeout과 retry는 왜 필요한가요?
- CORS란 무엇인가요?

## 레퍼런스 기반 질문 후보

- [네트워크란 무엇인가 — 완벽 가이드 Ch.1](https://dev-letter.kr/posts/network-basics) (dev-letter)
- [네트워크에서 회선 교환 방식과 패킷 교환 방식은 어떤 차이점 있나요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-107.md) (maeil-mail)
- [리버스 프록시와 포워드 프록시의 차이점에 대해 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-42.md) (maeil-mail)
- [사용자가 웹사이트에 처음 접근했을 때 발생하는 일련의 과정에 대해 설명해 주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-37.md) (maeil-mail)
- [소켓이 무엇인지 설명하고, 하나의 서버 포트에 여러 클라이언트가 동시에 접속할 수 있는 이유를 설명해주세요](https://dev-letter.kr/posts/port-and-socket) (dev-letter)
- [정적 IP 주소 할당 방식과 동적 IP 주소 할당 방식의 차이점을 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-86.md) (maeil-mail)
- [쿠키와 세션의 차이에 대해서 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-148.md) (maeil-mail)
- [클래스풀 IP 주소 체계에 대해서 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-78.md) (maeil-mail)
- [CDN이란 무엇인가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-103.md) (maeil-mail)
- [Connection Timeout, Socket Timeout, Read Timeout의 차이점은 무엇인가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-44.md) (maeil-mail)
- [CORS란 무엇인가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-41.md) (maeil-mail)
- [DNS 동작 원리에 대해서 설명해주세요](https://dev-letter.kr/posts/dns-resolution) (dev-letter)
- [DNS 심화 (DNSSEC, Round Robin, CDN 연계)](https://dev-letter.kr/posts/dns-advanced) (dev-letter)
- [DNS란 무엇인가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-100.md) (maeil-mail)
- [HTTP 기본 — Stateless, 비연결성, 메시지 구조](https://dev-letter.kr/posts/http-basics) (dev-letter)
- [HTTP 메서드에서 멱등성이란 무엇인가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-38.md) (maeil-mail)
- [HTTP 상태 코드 — 1xx부터 5xx까지 완벽 정리](https://dev-letter.kr/posts/http-status-code) (dev-letter)
- [HTTP Method — GET, POST, PUT, PATCH, DELETE를 제대로 이해하기](https://dev-letter.kr/posts/http-method) (dev-letter)
- [HTTP/1.1 vs HTTP/2 vs HTTP/3 — 버전별 핵심 차이](https://dev-letter.kr/posts/http-versions) (dev-letter)
- [HTTP/1.1과  HTTP/2.0에 대해서 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-60.md) (maeil-mail)
- [HTTPS에 대해서 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-48.md) (maeil-mail)
- [IP 주소 체계 — IPv4, 사설 IP, NAT, ARP 완전 정복](https://dev-letter.kr/posts/ip-address) (dev-letter)
- [Keep Alive에 대해 설명해 주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-114.md) (maeil-mail)
- [NAT 기능을 사용하는 이유를 알고 계신가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-81.md) (maeil-mail)
- [OSI 7계층과 TCP/IP 4계층의 차이를 설명해주세요](https://dev-letter.kr/posts/osi-7-layer) (dev-letter)
- [REST란 무엇인가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-56.md) (maeil-mail)
- [TCP 3-way / 4-way Handshake — 완벽 가이드 Ch.2 Section 2](https://dev-letter.kr/posts/tcp-handshake) (dev-letter)
- [TCP 3-way handshake에 대해서 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-31.md) (maeil-mail)
- [TCP 흐름 제어와 혼잡 제어 — 완벽 가이드 Ch.2 Section 3](https://dev-letter.kr/posts/tcp-flow-congestion-control) (dev-letter)
- [TCP vs UDP — 신뢰성과 속도, 무엇을 선택할까](https://dev-letter.kr/posts/tcp-vs-udp) (dev-letter)
- [UDP와 QUIC — 완벽 가이드 Ch.2 Section 4](https://dev-letter.kr/posts/udp-and-quic) (dev-letter)
- [URI, URL, URN의 차이점은 무엇인가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-72.md) (maeil-mail)
- [WAS와 웹 서버의 차이점은 무엇인가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-47.md) (maeil-mail)
- [WS vs WAS — 웹 서버와 웹 애플리케이션 서버의 차이](https://dev-letter.kr/posts/ws-vs-was) (dev-letter)
