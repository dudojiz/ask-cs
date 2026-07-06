# Backend

Spring MVC, Servlet, JPA, 트랜잭션 경계, 웹 애플리케이션 계층처럼 백엔드 애플리케이션 구현에 직접 연결되는 질문을 정리합니다.

우선 작성할 질문:

- Spring MVC 요청 흐름을 설명해주세요.
- Filter와 Interceptor의 차이는 무엇인가요?
- @Transactional은 어떻게 동작하나요?
- JPA를 사용하는 이유는 무엇인가요?
- OSIV란 무엇인가요?

## 레퍼런스 기반 질문 후보

- [@Component, @Controller, @Service, @Repository의 차이점에 대해서 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-29.md) (maeil-mail)
- [@ComponentScan 동작 원리에 대해서 설명해주세요](https://dev-letter.kr/posts/component-scan) (dev-letter)
- [@Controller 와 @RestController 의 차이점을 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-8.md) (maeil-mail)
- [@ExceptionHandler 어노테이션은 무엇인가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-4.md) (maeil-mail)
- [@OneToOne 연관관계에서 Lazy Loading을 설정할 때 주의할 점은 무엇일까요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-110.md) (maeil-mail)
- [@ResponseBody(or ResponseEntity<T>)가 있을 때와 없을 때의 동작 방식의 차이점을 말해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-5.md) (maeil-mail)
- [@Transactional은 어떻게 동작하나요? — 프록시 원리부터 self-invocation까지](https://dev-letter.kr/posts/transactional-proxy) (dev-letter)
- [@Value 어노테이션 사용 시 주의할 점을 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-3.md) (maeil-mail)
- [스프링 트랜잭션 AOP 동작 흐름에 대해서 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-88.md) (maeil-mail)
- [엔티티 매니저에 대해 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-18.md) (maeil-mail)
- [의존성 주입 3가지 방식에 대해서 설명해주세요](https://dev-letter.kr/posts/spring-di-methods) (dev-letter)
- [의존성 주입이란 무엇인가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-89.md) (maeil-mail)
- [톰캣에 대해서 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-11.md) (maeil-mail)
- [AutoConfiguration 동작 원리를 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-12.md) (maeil-mail)
- [BeanFactory와 ApplicationContext의 차이를 설명해주세요](https://dev-letter.kr/posts/beanfactory-vs-applicationcontext) (dev-letter)
- [ControllerAdvice에 대해 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-9.md) (maeil-mail)
- [DispatcherServlet 요청 흐름에 대해서 설명해주세요](https://dev-letter.kr/posts/dispatcher-servlet) (dev-letter)
- [Filter vs Interceptor vs AOP — Spring에서 요청을 가로채는 3가지 방법](https://dev-letter.kr/posts/filter-interceptor-aop) (dev-letter)
- [Filter와 Interceptor의 차이점을 말해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-6.md) (maeil-mail)
- [IoC 컨테이너에 대해서 설명해주세요](https://dev-letter.kr/posts/ioc-container) (dev-letter)
- [JDK Dynamic Proxy vs CGLIB — Spring AOP가 프록시를 만드는 두 가지 방식](https://dev-letter.kr/posts/jdk-dynamic-proxy-vs-cglib) (dev-letter)
- [JPA Fetch Join과 페이징을 함께 사용할 때 주의점을 설명해 주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-131.md) (maeil-mail)
- [JPA, Hibernate, Spring Data JPA 의 차이가 무엇인가요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-15.md) (maeil-mail)
- [JPA를 사용하는 이유를 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-14.md) (maeil-mail)
- [JPA에서 ID 생성 전략에 대해 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-26.md) (maeil-mail)
- [JPA의 ddl-auto 옵션은 각각 어떤 동작을 하고 어떤 상황에서 사용해야 할까요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-17.md) (maeil-mail)
- [JPA의 N + 1 문제에 대해서 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-19.md) (maeil-mail)
- [OSIV(Open Session In View) 옵션에 대해서 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-1.md) (maeil-mail)
- [private 메서드에 @Transactional 선언하면 트랜잭션이 동작할까요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-43.md) (maeil-mail)
- [RequestBody VS ModelAttribute의 차이점을 말해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-10.md) (maeil-mail)
- [Servlet은 무엇이고, Spring은 어떻게 그 위에 올라타나요?](https://dev-letter.kr/posts/spring-servlet) (dev-letter)
- [Spring @Controller vs @RestController](https://dev-letter.kr/posts/spring-controller-vs-rest-controller) (dev-letter)
- [Spring @ControllerAdvice — 전역 예외 처리의 모든 것](https://dev-letter.kr/posts/controller-advice) (dev-letter)
- [Spring AOP — 횡단 관심사를 분리하는 프록시 마법](https://dev-letter.kr/posts/spring-aop) (dev-letter)
- [Spring Bean 등록 방법 4가지에 대해서 설명해주세요](https://dev-letter.kr/posts/spring-bean-registration) (dev-letter)
- [Spring Bean 라이프사이클 — 생성부터 소멸까지](https://dev-letter.kr/posts/spring-bean-lifecycle) (dev-letter)
- [Spring Bean Scope에 대해서 설명해주세요](https://dev-letter.kr/posts/spring-bean-scope) (dev-letter)
- [Spring Data JPA에서 새로운 Entity인지 판단하는 방법은 무엇일까요?](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-16.md) (maeil-mail)
- [Spring MVC의 실행 흐름에 대해 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-7.md) (maeil-mail)
- [Spring과 Spring Boot의 차이를 말해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-13.md) (maeil-mail)
- [Spring에서 객체를 Bean으로 관리하는 이유를 설명해주세요.](https://github.com/maeil-mail/maeil-mail-contents/blob/main/backend/contents/be-146.md) (maeil-mail)
