# GIT  

## 1. GIT REPO 설정 (일반 파일 -> REPO)

`git init` 명령어 사용. 디렉터리의 경우는 하위 파일들 모두 git이 관리하는 저장소인 'local repo'에 소속됨. 

이때 home directory를 repo로 만들지 말아야 하며, repo 안에 repo를 만드는 것(submodule)을 절대로 해서는 안된다.

## 2. GIT REPO 해제 (REPO -> 일반 파일)
`rm -rf repo의 파일명`

local repo를 잘못 만들었을 때 사용하며, 이때 작용했던 것이 모두 날아가므로 주의 필요

## 3. 수정자 인증

`git config --global user.name 별명`

`git config --global user.email 깃과 연결된 이메일명`

해당 컴퓨터에서 작업할 때 누가 작업하는지를 선언하는 명령어. 

## 4. add, commit, push

 ### 1) add (분장실 -> 스테이지) 

`git add 파일명 혹은 쉘 명령어의 특수문자(.)`

commit을 하기 위해 변경사항 목록에 올리는 것을 의미. 또한 여러 파일들을 한번에 변경사항 목록에 올리는 것 또한 가능하다. 만약 add를 잘못하여 변경사항을 스테이지에 잘못 올렸다면, `git restore --staged 파일명` 명령어를 사용하면 된다.

### 2)commit(스테이지 -> 메모리카드(사진첩))
`git commit -m '메시지'`

add로 변경사항 목록에 올린 변경사항을 실제로 저장하는 것을 의미. 이때 add한 파일의 변경사항이 없다면 commit되지 않기 때문에 반드시 컴퓨터에 저장을 하고 add한 후 commit해야 한다.


### 3)push(사진 공유)

1. 사진을 공유할 remote repo를 github에서 생성
2. local repo가 remote repo를 가리키기 위해서 만들어서 사용
    
    `git remote add origin remote repo의 url`

     이때 확인은 `git remote -v`로 하면 된다.
3. local repo와 remote repo를 동기화

    `git push origin master`
    
    

## 5. Status, log

1. `git status`
   
   add, commit, commit으로 저장한 파일들의 정보를 출력
2.  `git log`
    
    commit으로 저장한 파일들의 정보를 출력

## 6, README, .gitignore
1. README 
    
    깃헙의 대문으로 repo 디렉터리의 최상단에 위치한다. 설정시 github의 README가 활성화됨
2. .gitignore 
    
    특정 파일의 변경사항을 영구적으로 add할 수 없도록 설정하는 파일.
    단, 대상 파일의 파일명이 .gitignore에 있어야만 작동하며, 소급해서 적용되지 않으니 주의 필요.

## 6, Clone, Pull (Remote -> Local)

1. `git clone remote repo의 url 주소.git (이름명)`
   
   remote repo를 최초 복제할 때 사용, 그 이후는 모두 pull을 통해 진향

   이름명이 없을 시에는 remote repo의 이름이 자동적으로 할당. 

2. `git pull origin master`
    
    remote repo의 저장되어 있는 것을 local repo로 가져옴. 

### 주의사항

1. github애서 가급적이면 하지 말자. pull, push가 잘못 되면 동기화가 안되는 상황인 '**충돌**'이 발생함.
2. push를 함부로 하지 말 것, 
    

    
