# 0404 정보보안기사



## 네트워크 기본정리/ tcp, udp, icmp, ip는 기존 정리한 것으로 대체



1. 프로토콜 : 시스템 간에 통신을 하기 위한 규약/ 구문, 의미, 타이밍
2. OSI 7계층 :분산된 이기종 시스템 간의 네트워크 상호호환을 위해 표준 아키텍처
   - 물리계층 - 물리적 장치의 전기적 연결/ 비트/ 허브, 리피터/ Promiscuous(무차별 모드)
   - 데이터링크계층 - 인접한 노드 간의 신뢰성 있는 프레임 전달하는 계층/ 스위치/ 프레임/ 정지-대기 방식, 슬라이딩 윈도우 방식(흐름제어)/ 후진 오류 수정방식, 전진 오류 수정 방식(오류제어)/ Mac address tabke
     - 데이트링크계층의 보안 위협은 ARP 스푸핑, ARP 리다이렉트, 스위치의 SPAN기능, 스위치 재밍
     - 스위치 재밍은 Mac address table을 오버플로우-> 마치 허브처럼 작동
     - ARP 스푸핑 - 특정 호스트의 MAC주소를 자신의 MAC주소로 위장한 ARP REPLY 패킷을 보냄, MAC table에 조작된 정보가 올라감 -> ip forward
     - ARP 리다이렉트 : 공격자가 자신이 라우터인 것처럼 MAC 주소를 위장, 모든 호스트의 ARP 캐시 테이블에 라우터의 MAC 정보가 공격자의 MAC으로 변경
     - ICMP 리다이렉트 : ICMP 리다이렉트 메시지를 이용하여 특정 대역으로 나가는 패킷의 라우팅 경로를 희생자에게 전송
     - 기본적으로 2계층에 관한 공격은 스니핑!, 패킷을 엿보는 기밀성 침해 공격이 대부분
   - 네트워크 계층 - 종단 간의 라우팅/ 패킷/ IP주소/라우터
   - 전송 계층 - 종단 간의 신뢰성있는 연결 / 새그먼트의 분할과 재조립/연결제어 - 연결지향, 비연결지향 / 흐름제어/ 오류제어 / 혼잡제어
   - 세션 계층 - 논리적 연결인 세션에 관한 관리
   - 표현 계층 - 인코딩/디코딩, 암호화/복호화에 관련된 계층
   - 응용 계층 - 직접 접근할 수 있는 인터페이스와 관련된 계층
3. 기본적으로 낮은 계층으로 가면 갈수록 각각의 계층의 해더가 합쳐짐, 올라 갈수록 합쳐졌던 헤더가 하나씩 없어짐





## 포트 스캐닝



1. 공격자가 칩입 전 대상 호스트에 어떤 포트가 열려 있는지 확인 하는 기법

2. NMAP 포트 스캐너

   ```ba
   -sS half open
   -aT connect
   -sU udp 스캔
   -sF fin 스캔
   -sX xmas 스캔
   -sN null 스캔
   -sA ack 스캔
   -SP 핑 
   -D	디코이
   -b FTP 바운스 스캔
   -oN 일반 파일 출력
   -Ox XML파일 출력
   -oG 그래프 형식으로 출력
   -OA 디렉토리로 세 개 전부 출력
   ```

   - TCP connect 스캔 - connect의 시스템 콜을 이용하는 방식/ 특징은 시스템을 사용하고 있는 일반 사용자/ 패킷 자체의 변조를 하지는 않음

     포트가 열리면 syn - syn+ack - ack를 거쳐 연결한 후 rst+ack를 서버 측에 보낸다. 닫혔을 경우 서버 쪽에서 rst+ack가 온다.

     만약 필터가 있는 상태라면 정책에 따라(DROP/REJECT) 달라지며, 전자는 응답이 없지만, 후자는 ICMP unreachable패킷이 서버로부터 온다.

   - TCP half open 스캔 - 패킷 해더를 조작, 제어비트를 조작한다. 그 결과 tcp 세션이 완전히 성립 안된 상태에서 불완전한 제어 비트를 보낸다. 즉 스텔스 스캔의 성격을 가지고 있음, 포트가 열려 있을 시에 서버로 부터 syn+ack를 받으면 바로 RST 패킷을 보내 세션을 성립되지 않게 한다. 필터 있을 때에는 connect와 완전히 동일하다. 

   - TCP FIN/NULL/XMAS 스캔 - 관리자 권한을 획득하여 패킷 헤더가 아닌 패킷 그 자체를 직접 조작합/ 스텔스 스캔이며 각각 제어비트를 저대로 조작해서 진행하는 스캔을 의미한다. OPEN일 시에는 FIN을 서버로 보냈을 때 아무 반응이 없으나, CLOSE일 때는 RST+ACK가 서버로 부터 온다. 즉 닫혀 있는 포트인지 열려 있는 포트인지 확인할 때 주로 사용한다는 특징이 있다. 필터시에는 CONNECT스캔과 다를 바가 없다. 

   - UDP 스캔 -닫힌 UDP 포트로 패킷 수신하면 ICMP 에러 메시지(unreachable)을 이용하는 스캔, 다시 말해 필터 시에 connect 스캔과 거의 비슷한 양상으로 진행된다.

   - NMAP은 이후 와이어샤크 사용예시를 첨부하겠음





## DOS

1. 가용성 침해 공격으로 정상적인 서비스를 할 수 없도록 만드는 공격
2. dos는 단일 컴퓨터를 이용하는 경우이나, DDos는 다수의 컴퓨터를 이용하는 공격을 의미
3. ping of death - icmp 패킷을 정상적인 크기(1500 bytes)보다 크게 만들어 전송/ 그 결과 다량의 ip 단편화 패킷을 전달하여 희생자의 시스템 자원을 할당하게 만듬
4. Land attack - 출발지의 ip주소와 목적지 ip주소 동일, 자문자답하게 해서 시스템 자원을 할당받게 만듬
5. smurf attack - 출발지 주소를 희생자 주소로 위조 증폭 네트워크로 icmp request를 브로드 캐스트 함. 그 결과 응답 메시지가 희생자의 주소를 전달됨/no-ip directed-broadcast
6. teardrop 재조합 과정에서 잘못된 fragment offset 정보, 즉 offset 값을 중첩시킴. 





## 




