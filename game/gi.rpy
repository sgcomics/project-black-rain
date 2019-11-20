init 20:
    image ecg ki 1 = "ecg/ki1.png"
    image ecg ki 2 = "ecg/ki2.png"
    image ecg ki 3 = "ecg/ki3.png"

label scene101:
    #1
    #배경글
    scene background black
    nvle "별로 머지 않은 미래."
    nvle "탐욕에 물든 인간들은 지속적으로 자연을 파괴해갔다."
    nvle "결국, 우리가 더 이상 살아갈 수 없을 정도로 오존층이 \n파괴되었고, 인류의 목숨은 경각에 달했다."
    nvle "하지만 소수의 선각자들이 미리 대비해놓은 결과, 인류는 \n안전구역 안에서 목숨을 부지할 수 있었다."
    nvle "이는 안전패널이라는 획기적인 기술 덕분이었다."
    #배경글 끝
    nvl clear
    scene background classday
    show principal happy
    principal "... 이렇게 돔을 자세히 살펴보면, 수많은 투명한 안전패널들로 구성되어 있음을 확인할 수 있어요."
    principal "이 패널들이야말로 인류 기술의 정수라고 할 수 있는데..."
    "수업 종이 울렸다."
    principal "오늘은 여기까지 하도록 합시다."
    principal "반장, 인사하세요."
    hide principal
    with dissolve
    show yeongwon idle at left
    with dissolve
    yeongwon "차렷, 선생님께 경례!"
    
    show mstudent idle at right
    with dissolve
    mstudent "수고하셨습니다~~"
    
    show yeongwon happy at left
    with dissolve
    yeongwon "한별아, 점심 먹으러 갈래?"
    yeongwon "오늘은 맛있는 게 나왔으면 좋겠다!"
    
    show mstudent idle
    with dissolve
    mstudent "오늘은 급식표에 소세지라고 적혀 있네."
    mstudent "그나저나 반장, 매번 한별이랑만 먹지 말고 우리랑도 좀 먹자~"
    hide mstudent
    show yeongwon idle2
    with dissolve
    yeongwon "너, 같이 먹으면 내 거까지 뺏어먹는 거 아냐? 그런 건 질색인데."
    "내가 비싸게 군다는 말이 들리지만, 무시하자."
    hide yeongwon
    hide mstudent
    with dissolve

    #2
    scene background dininghall
    with fade
    show hanseol happy at left
    with dissolve
    hanseol "별아~ 영원아~ 빨리 줄 서자~"
    
    with dissolve
    "언제나 차분한 한별이와 다르게 언제나 해맑은 한설이."
    "한별이의 쌍둥이 동생이지만 둘의 성격은 정반대다."
    "내 대답이 조금 느려지자 한설이의 입이 비쭉 튀어나왔다."
    show hanseol happy2 at left
    with dissolve
    hanseol "영원이 너어, 고등부 올라가서 한별이랑만 같은 반 되더니 둘이서만 친해진 거 아냐?"
    hanseol "나랑도 친하게 지내주지 않으면 삐진다!"
    
    show yeongwon happy at right
    with dissolve
    yeongwon "한설이 너, 보다 보면 한별이 몫의 수다까지 네가 하는 것 같단 말야."
    show yeongwon idle
    with dissolve
    yeongwon "그리고 아무리 쌍둥이라도 언니는 언니인데, 밖에서는 언니라고 불러주는 게 나을 것 같아."
    
    show hanseol happy at left
    with dissolve
    hanseol "쌍둥이인데 뭐 어때?"
    
    show hanbyeol idle
    with dissolve
    hanbyeol "...한설아, 머리 아프네. 조용히 좀 해줄래?"
    
    with dissolve
    "역시나."
    "예상대로의 반응이네."
    show hanseol happy
    with dissolve
    hanseol "그나저나 영원이 네가 반장이 될 줄은 몰랐어."
    hanseol "그전까지는 한별이가 계속 반장이었는데 말이야."
    hanseol "대체 무슨 바람이 불었길래 반장이 된 거야?"
    
    with dissolve
    show yeongwon shock at right
    with dissolve
    yeongwon "어... 그게..."
    
    with dissolve
    "뭐라고 말해야 하지?"
    show hanbyeol idle
    with dissolve
    hanbyeol "중등부까지는 다들 어려서 일하는 반장이 필요했을 뿐이야."
    hanbyeol "하지만 이제는 다들 자기 앞가림을 하니 나보단 활발한 영원이가 더 잘 어울릴 뿐이지."
    
    show hanseol idle
    with dissolve
    hanseol "어쨌거나 어릴 때는 어두침침하던 영원이가 이렇게 밝아질 줄은 몰랐어."
    hanseol "나 감동이야... 영원이 이제 다 컸구나~"
    
    show yeongwon idle2 at right
    with dissolve
    yeongwon "너 정말 그만해! 그리고 내가 너보다 크거든?"
    
    show hanseol shock at left
    with dissolve
    hanseol "윽..."
    
    with dissolve
    "이야기를 나누다보니 벌써 점심시간이 끝났다."
    show yeongwon idle at right
    with dissolve
    yeongwon "어쨌든 오늘 일과시간 끝나고 내 방으로 오는 거 잊지마."
    yeongwon "남 눈에 띄지 않도록 조심하고."
    
    show hanbyeol idle
    with dissolve
    hanbyeol "알았어. 기억할게."
    
    show hanseol idle at left
    with dissolve
    hanseol "응!"
    hide hanseol
    hide yeongwon
    hide hanbyeol
    with dissolve
    #3
    scene background dormyeongwon
    with fade
    show hanseol idle at left
    with dissolve
    hanseol "그래서 할 이야기가 뭔데."
    
    show yeongwon idle at right
    with dissolve
    yeongwon "쉿. 목소리 낮춰."
    
    with dissolve
    "언제나 그렇지만 한설이에겐 위기감이 없다."
    "머리 속이 꽃밭이라 죽어도 꽃밭에서 죽을 것 같다."
    "그래도 이럴 때는 좀 조심해주었으면 하는 바람이다."
    show yeongwon idle
    with dissolve
    yeongwon "직접 읽어봐."
    hide yeongwon
    hide hanseol
    scene background dormyeongwonb
    with dissolve
    #배경글
    nvle "쪽지 쓰는 것도 오랜만이네."
    nvle "한동안 높으신 분이 다녀가신다고 해서 쪽지를 남기지 못했어."
    nvle "보안강화기간이라나. 이해해줘."
    nvle "그래도 희망적인 소식이야."
    nvle "특별동에서 아지트까지 갈 수 있는 샛길과 감시가 허술한 때를 알아냈어."
    nvle "곧 다시 볼 수 있을 것 같아."
    nvl clear
    nvle "이번 보름날 밤에 보자."
    #배경글 끝
    nvl clear
    with fade
    scene background dormyeongwon
    show yeongwon idle dark at right
    show hanseol sad at left
    with dissolve
    hanseol "우리, 하늘이랑 연우 다시 볼 수 있는 거야?"
    "한설이의 눈에 눈물이 그렁그렁 맺혔다."
    
    show yeongwon happy
    with dissolve
    yeongwon "앞으로는 자주 보게 될 텐데 뭘."
    
    show hanbyeol idle
    with dissolve
    hanbyeol "우리들의 관계가 비밀인 건 잊지 않았지?"
    hanbyeol "반에서 표정관리나 조심해."
    
    show hanseol idle
    with dissolve
    hanseol "넌 기쁘지도 않은 거야?"
    
    show hanbyeol happy
    with dissolve
    hanbyeol "나도 당연히 기쁘지."
    hanbyeol "그래도 곧 만날 텐데 미리 감동할 필요는 없지 않을까."
    
    with dissolve
    "한별이의 볼이 붉어졌다."
    "평소에는 좀처럼 볼 수 없는 반응이다."
    "장난을 좀 쳐볼까?"
    "이런. 소등시간이다."
    show yeongwon idle
    with dissolve
    yeongwon "벌써 돌아갈 시간이네."
    yeongwon "나머지는 다음에 또 이야기 하자."
    
    with dissolve
    "이제 자야지."
    "그래도 궁금하다."
    "하늘이랑 연우는 어떤 모습으로 나타나려나..."
    hide yeongwon
    hide hanbyeol
    hide hanseol
    with dissolve
    #4
    scene ecg ki 1
    with fade
    hanbyeol "역시나. 너희 둘은 S반이네. 그럴 것 같았어."
    hanseol "응? 하늘이 표정이 좀 안 좋은데, 혹시 영원이랑 떨어져서 그런 거야?"
    haneullong "아니... 이제 우리가 같이 생활할 수 없다고 생각하니까..."
    yeonwoo "그래도 하늘이라면, 우리 모두가 만날 방법을 찾을 거라고 생각해."
    yeonwoo "하늘이는 특별하니까."
    yeongwon "아냐아냐. 너도 대단한걸."
    yeonwoo "......"
    yeonwoo "우리 하늘 공주님은 내가 지켜줄 테니 걱정마."
    hanseol "그럼 영원이는 내가 지켜주면 되겠네!"
    hanbyeol "모두 몸조심하고, 졸업해서 다시 만나자."
    haneullong "잠시만... 나 공주님 아니라구..."
    #모두 무슨색으로 할까
    "모두" "하하하."
    #5
    scene background black
    with fade
    "......"
    scene background dormyeongwon
    with fade
    "누구지? 문을 열어보자."
    show hanbyeol idle at left
    with dissolve
    hanbyeol "네가 늦잠이라니, 별일이야. 해가 서쪽에서 뜨겠어."
    
    show hanseol shock at right
    with dissolve
    hanseol "영원아, 눈이 빨개! 악몽이라도 꾼 거야?"
    show yeongwon idle
    with dissolve
    yeongwon "아무 일도 아니야, 정말 괜찮아!"
    
    hide hanbyeol
    hide hanseol
    with dissolve
    "꿈을 꿨다."
    "초등부를 졸업하는 꿈."
    "그 탓인지 잠에서 깨어났어도 기분이 싱숭생숭하다."
    "티내지는 않아야 할 텐데..."
    scene background classday
    with pushright
    show yeongwon idle
    with dissolve
    yeongwon "......"
    hide yeongwon
    with dissolve
    show teacher idle at left
    with dissolve
    "A반 담임" "반장?"
    "A반 담임" "반장!"
    
    show yeongwon shock at right
    with dissolve
    yeongwon "아... 아! 차렷! 선생님께 경례!"
    
    with dissolve
    "반 친구들이 웃었다."
    "부끄러워..."
    show yeongwon shock dark at right
    show teacher idle at left
    with dissolve
    "A반 담임" "반장이 실수하는 모습, 처음 본 것 같네."
    show yeongwon shock
    
    with dissolve
    yeongwon "죄송합니다!"
    
    show teacher idle
    with dissolve
    "A반 담임" "아니야, 사람이 그럴 수도 있지."
    "A반 담임" "이제 수업 시작하자."
    scene background dininghall
    with pushright
    show yeongwon idle at left
    with dissolve
    yeongwon "......"
    
    show hanseol idle at right
    with dissolve
    hanseol "영원아, 너 숟가락 거꾸로 들었어."
    show yeongwon shock
    
    with dissolve
    yeongwon "아, 미안. 잠시 다른 생각 하다가."
    
    show hanseol idle2
    with dissolve
    hanseol "너 요즘 이상해."
    scene background schoolhallway
    with pushright
    show hanbyeol idle at left
    with dissolve
    hanbyeol "영원아, 옷 뒤집어 입고 나온 것 같은데?"
    
    show yeongwon idle at right
    with dissolve
    yeongwon "아, 진짜네. 고마워!"
    
    show hanbyeol idle
    with dissolve
    hanbyeol "......"
    hide hanbyeol
    hide yeongwon
    with dissolve
    scene background black
    with fade
    "약속했던 보름날 밤이 다가올수록, 자잘한 실수들이 잦아졌다."
    "주변 사람들이 내 이상을 알아차리고 내게 물어왔다."
    "누구 좋아하는 사람이라도 있냐고. 사랑에 빠진 사람 같다고."
    "사랑... 은 아닌 것 같지만, 설레는 건 맞다."
    "그치만 대답할 수 있을 리가 없잖아."
    "그야 상대는..."
    scene background classday
    with fade
    show hanbyeol idle at left
    show yeongwon idle dark at right
    with dissolve
    hanbyeol "너, 요즘 이상해."
    
    show yeongwon idle
    with dissolve
    yeongwon "...미안."
    
    show hanbyeol idle
    with dissolve
    hanbyeol "물론 네가 좋아하는 마음은 알지만, 주변에 티내고 다녀서 좋을 것 없어."
    
    show yeongwon shock
    with dissolve
    yeongwon "누, 누가 좋아한다고!"
    
    show hanbyeol idle
    with dissolve
    hanbyeol "누구긴 누구야, 연우랑 하늘이지."
    show hanbyeol idle
    
    hanbyeol "우린 친구잖아?"
    
    show yeongwon shock
    with dissolve
    yeongwon "그렇지, 맞지. 그치, 우린 친구지. 아하하."
    show hanbyeol idle
    
    with dissolve
    hanbyeol "하여튼, 너 요즘 좀 이상해. 정신 좀 차려."
    show hanbyeol idle
    
    hanbyeol "비밀이라고 우리 입단속시킨 것도 너잖아."
    show yeongwon shock
    
    with dissolve
    yeongwon "응... 미안, 한별아."
    
    show hanbyeol idle
    with dissolve
    hanbyeol "예전에 우리가 연우, 하늘이와 친구 사이였다는 건 중요하지 않아."
    show hanbyeol idle
    
    hanbyeol "몰래 만나기로 한 걸 들키면 단순한 경고로는 끊나지 않을 거야."
    
    show yeongwon shock
    with dissolve
    yeongwon "알았어. 조심할게."
    
    show hanbyeol idle
    with dissolve
    hanbyeol "......"
    
    show yeongwon idle
    with dissolve
    yeongwon "왜?"
    
    show hanbyeol idle
    with dissolve
    hanbyeol "아니야, 슬슬 가자."
    
    show yeongwon idle
    with dissolve
    yeongwon "싱겁기는."
    hide yeongwon
    hide hanbyeol
    with dissolve
    #6
    scene background dormyeongwon
    with fade
    "몇 주가 몇 년같았던 기다림 끝에, 우리들이 만나기로 한 보름날 밤이 되었다."
    "취침시간 이후 나와 한별, 한설이는 각자의 방에서 빠져 나왔고, 우리의 아지트가 있던 구교사로 발걸음을 옮겼다."
    "아지트에 도착하니 손을 흔드는 하늘이가 보였다."
    scene background nighthideout
    with fade
    show haneullong happy2
    with dissolve
    haneullong "여기야! 여기!"
    hide haneullong
    with dissolve
    "몇 년 만에 만나서일까. 막상 이야기를 하려니 어색한 기운이 감돌았다."
    "하지만 어색함은 곧 눈 녹듯 사라졌다."
    show yeongwon happy at left
    with dissolve
    yeongwon "그나저나 연우는 키 많이 컸네?"
    show yeongwon idle
    with dissolve
    yeongwon "한설이보다 머리 하나는 커 보인다!"
    
    show yeonwoo happy at right
    with dissolve
    yeonwoo "그래? 나 그동안 운동 열심히 했거든."
    
    show yeongwon idle
    with dissolve
    yeongwon "그런데 하늘이는 그대로네?"
    
    show yeonwoo idle
    with dissolve
    yeonwoo "우리 하늘이는 말이야, 공주님이라서 키 같은 거 안 커!"
    hide yeonwoo
    hide yeongwon
    with dissolve
    show haneullong happy dark at right
    show hanseol happy at left
    with dissolve
    hanseol "맞아맞아! 하늘이는 나보다 귀엽기까지 한걸?"
    show haneullong happy
    
    with dissolve
    haneullong "한설이는 여전히 기운차구나."
    
    show hanseol idle
    with dissolve
    hanseol "그래?"
    
    with dissolve
    "일동" "하하하."
    hide hanseol
    hide haneullong
    with dissolve
    "하늘이는 자기 외모에 관한 이야기를 그다지 좋아하지 않았었는데..."
    "하늘이도 어른이 되어가는 걸까. 꽤나 차분해진 것 같다. 옛날이었으면 한 소리 할 타이밍인데."
    "그래도 성격에 비해 외모는 하나도 변하지 않았다. 혼자만 시간이 멈춰버린 듯이."
    "연우가 하늘이의 시간을 모두 가져가버린 걸까?"
    show hanseol happy at left
    show hanbyeol happy dark at right
    
    with dissolve
    hanseol "하늘이는 머릿결도 여전하네."
    
    show hanbyeol happy
    with dissolve
    hanbyeol "하늘이가 머릿결이 좋긴 하지."
    
    show hanseol idle
    with dissolve
    hanseol "하늘아, 지금이라도 그 팔찌, 머리띠로 바꾸는 건 어때?"
    show haneullong happy
    
    with dissolve
    haneullong "그래도 난 팔찌가 좋은걸?"
    hide haneullong
    hide hanseol
    hide hanbyeol
    with dissolve
    show background nighthideoutb
    with dissolve
    "한동안 이야기가 계속됐다."
    show background nighthideout
    with dissolve
    show yeonwoo idle
    with dissolve
    yeonwoo "슬슬 돌아갈 시간이네. 더 있다간 경비에게 걸릴 거야."
    hide yeonwoo
    with dissolve
    show yeongwon idle
    with dissolve
    yeongwon "그래. 슬슬 헤어지자."
    show yeongwon happy
    with dissolve
    yeongwon "그동안 건강하게 지냈다니 다행이야."
    yeongwon "다음에 또 보자!"
    hide yeongwon
    with dissolve
    show haneullong idle
    with dissolve
    haneullong "... 응, 쪽지 남길게. 곧 다시 보자."
    hide haneullong
    with dissolve
    scene background dormyeongwon
    with fade
    "방에 돌아왔다. 선생님들이 새벽순찰을 도는 소리가 들린다."
    "조금만 늦었어도 큰일날 뻔했다."
    "괜히 리본 머리끈이 신경쓰여 만지작거리니, 머리끈을 처음 했을 때의 기억이 떠올랐다."
    "우리 염소 고아원에는 포인트 제도가 있다."
    "우수한 성적을 받거나, 교내봉사를 하면 점수를 받는데, 이 점수로 원하는 물건을 골라 받을 수 있다."
    "꽤 많이 모아야 하지만, 모으지 못할 정도는 아니다."
    "우리들은 초등부를 졸업할 때, 서로 헤어져도 우정은 잊지 말자는 뜻으로 빨간색의 물건을 하나씩 나누어 가졌다."
    "내 기억으로는 하늘이와 연우가 나와 한별, 한설이에게 포인트를 꽤 보태주었었다."
    "하늘이는 팔찌, 연우는 귀걸이, 나는 리본 머리끈, 한별이는 머리핀, 한설이는 방울 머리끈."
    "다들 언제나 약속의 물건을 몸에 지니고 다녔다."
    "오늘 만났을 때도 다들 약속했다는 듯이 각자의 물건을 가지고 있었다."
    "사실, 서로 쪽지를 남기며 연락할 때에는 하늘이, 연우와 서로 소원해지는 느낌이 없지 않았다."
    "그러나 막상 서로 만나고 약속의 물건을 지니고 있는 것을 보니, 울컥하고 북받쳐 오르는 게 있었다."
    "내심 많이 그리워 했었나보다."
    "오늘 하늘이랑 연우 얼굴 봤으니까, 오늘밤에는 푹 잘 수 있을 것 같다."
    "아... 벌써 다시 보고 싶다..."
    #7
    scene background dininghall
    with fade
    show yeongwon idle at left
    show hanseol idle dark at right
    with dissolve
    yeongwon "......"
    
    show hanseol idle
    with dissolve
    hanseol "영원아? 또 밥 먹다 말고 멍때려?"
    
    show yeongwon idle
    with dissolve
    yeongwon "......"
    
    show hanbyeol idle
    with dissolve
    hanbyeol "영원아, 정신 좀 차려."
    show yeongwon idle
    
    with dissolve
    yeongwon "아, 한별아. 그러니까 하늘..."
    show hanseol idle at Position(xalign = 0.25 , yalign = 1.0)
    with move
    show yeongwon idle
    show hanseol idle
    with hpunch
    "한설이가 내 입을 틀어막았다."
    show hanbyeol shock
    
    
    with dissolve
    hanbyeol "식당에서 이름을 말해? 미쳤어?"
    hanbyeol "우리 몰래 만나는 거 들키면 모두 끝장이야. 정신 차려."
    
    show yeongwon shock
    with dissolve
    yeongwon "미안... 조심할게..."
    hide hanbyeol
    hide hanseol
    hide yeongwon
    with dissolve
    scene background schoolhallway
    with fade
    show teacher idle at left
    show yeongwon idle dark at right
    with dissolve
    "A반 담임" "저기 영원아? 미안하지만 여기 종이 옮기는 것 좀 도와줄래?"
    
    show yeongwon idle at right
    with dissolve
    yeongwon "네, 선생님! 자료실 문 앞에 옮겨 놓으면 되나요?"
    
    show teacher idle
    with dissolve
    "A반 담임" "그래. 나는 이제 교무회의에 가봐햐 하거든."
    "A반 담임" "반장이 믿음직하니 안심이네."
    "A반 담임" "그나저나, 방금 반장 '하늘'이라고 하지 않았었니?"
    
    show yeongwon shock
    with dissolve
    yeongwon "아하하..."
    show yeongwon idle
    with dissolve
    yeongwon "사실 제가 하늘 보는 걸 좋아하는데, 오늘 하늘 색이 마음에 들어서요."
    
    with dissolve
    "아... 하늘이 보고 싶어..."
    show teacher idle
    with dissolve
    "A반 담임" "그러게, 오늘 하늘이 맑고 예쁘네!"
    "A반 담임" "선생님은 먼저 가볼게."
    hide yeongwon
    hide teacher
    with dissolve
    #8
    scene background dormhallway
    with fade
    "방 앞에 한별이가 서 있다."
    show hanbyeol serious at left
    show yeongwon idle dark at right
    with dissolve
    hanbyeol "잠깐 나랑 들어가서 이야기 좀 하자."
    show yeongwon idle
    
    with dissolve
    yeongwon "무슨 일이야?"
    scene background dormyeongwon
    with fade
    show yeongwon idle dark at right
    show hanbyeol fury at left
    with dissolve
    hanbyeol "너 요즘 나사 풀렸더라. 정신 차려!"
    
    show yeongwon sad
    with dissolve
    yeongwon "응... 조심할게..."
    
    show hanbyeol idle2
    with dissolve
    hanbyeol "그리고, 너 노력하고 있는 거 다들 알아. 무리하지 않아도 돼."
    
    show yeongwon idle
    with dissolve
    yeongwon "무리는 무슨... 요즘 힘든 일 하나도 없어!"
    
    show hanbyeol idle2
    with dissolve
    hanbyeol "너, 거짓말할 때 버릇 있는 거 알아?"
    hanbyeol "지금처럼, 목소리도 조금 커지고 억지로 웃고."
    hanbyeol "내가 널 몇 년을 봤는데 그걸 모르겠어?"
    
    show yeongwon idle
    with dissolve
    yeongwon "...아냐. 오늘 하늘이 예뻐서 기분 좋아져서 그래."
    
    show hanbyeol idle
    with dissolve
    hanbyeol "그래? 네가 그렇다면 그런 거겠지."
    
    show yeongwon idle
    with dissolve
    yeongwon "푹 쉬어."
    hide hanbyeol
    hide yeongwon
    with dissolve
    "요즘 하늘이 생각에 좀 해이해졌나보다."
    "아무리 한별이가 눈썰미가 있다지만 들켜 버리다니."
    "나한테 그런 습관이 있었는지는 몰랐다."
    "잎으로는 더 조심해야지."
    #9
    scene background classday
    with fade
    show principal happy
    with dissolve
    principal "저번 시간에 배운 패널기술을 적용한 것이 이 '우산'입니다."
    show principal idle
    with dissolve
    principal "이전에는 기술력의 부족으로인해 전신 보호복 형태였지만, 개선된 거죠."
    show principal happy
    with dissolve
    principal "물론 더 나은 형태로 발전시키기 위해 지금도 연구는 계속되고 있습니다."
    principal "이에 대한 예상방안을 이야기해보자면..."
    hide principal
    with dissolve
    "또 저 눈빛."
    "원장 선생님 수업시간은 이래서 싫다."
    "원장 선생님이 예쁘다고 수업시간까지 좋아하는 녀석들이 많은데..."
    "다들 눈치채지 못한 것 같지만... 무언가 기분 나쁘게 오싹하다."
    "...아, 비가 오나보다."
    "비가 오는 날은 싫지 않아. 널 만난 날이 떠오르니까."
    #10
    scene ecg ki 2
    with fade
    "10년 전 쯤, 비가 오는 밤이었지."
    "나는 선생님들 몰래 고아원을 돌아다니고 있었어."
    "그러다 구교사에서 길을 잃어 울고 있었지."
    haneullong "왜 울어?"
    "하얀 머리카락?"
    " ...잠시만, 하얀?!"
    yeongwon "귀...귀신!"
    haneullong "사람을 보고 귀신이라니, 너무한 거 아니야 영원아?"
    yeongwon "너... 너 누구야! 누군데 내 이름을 알아?"
    yeongwon "역시 소문이 맞았어... 안전구역 밖에서 죽은 귀신이 너지?"
    haneullong "내 이름은 하늘이야. 너랑 같은 반 친구."
    yeongwon "하...늘? 친구?"
    haneullong "그래. 귀신이 아니라 친구."
    haneullong "네 이름은 수업시간에 들었어."
    haneullong "자랑은 아니지만, 난 한 번 들은 건 거의 잊지 않거든."
    haneullong "넌 언제나 반 구석에서 햄스터처럼 움츠러들어 있잖아?"
    haneullong "언제나 그러고 있으니, 오히려 눈에 잘 띄어서 기억하고 있었어."
    yeongwon "미안..."
    haneullong "미안할 게 어딨어?"
    yeongwon "널 귀신 취급해서..."
    haneullong "아니야. 놀라면 그럴 수 있지."
    haneullong "그런데 왜 날 귀신이라 생각한 거야?"
    yeongwon "머리카락이 하얗고 빛나서..."
    haneullong "아, 오늘은 날씨가 흐려서 어두우니까 하얀색으로 보이는구나."
    haneullong "내 머리, 원래는 하늘색이야. 그래서 내 이름도 하늘."
    haneullong "머리색이 좀 특이하긴 하지?"
    yeongwon "아니야... 예뻐."
    yeongwon "마치 사람이 아닌 것처럼 말야."
    yeongwon "귀신이 아니면 천사님이야?"
    haneullong "예뻐? 칭찬 고마워."
    yeongwon "헤헤.."
    haneullong "그런데 여기서 왜 울고 있던 거야?"
    yeongwon "몰래 나와서 돌아다니다가... 길을 잃어버렸어."
    yeongwon "근데, 여기 어디야?"
    haneullong "여기? 구교사."
    yeongwon "구교사? 여기 선생님들이 오면 안 된다고 한 곳이잖아?"
    haneullong "응. 맞아."
    yeongwon "선생님들이 여기 오면 안 된다고 했었는데..."
    haneullong "응."
    yeongwon "걸려서 혼나는 거, 무섭지 않아?"
    haneullong "걸리지만 않으면 혼나지도 않는 거 아니야?"
    yeongwon "그래? 그렇게 생각할 수도 있구나."
    haneullong "나 여기 길 잘 아는데, 나랑 같이 돌아갈래?"
    "내가 대답하기도 전에, 너는 내 손을 잡아주었지."
    "네 따듯함에 난 울음을 그칠 수 있었어."
    haneullong "이제 선생님한테 안 혼나겠네?"
    yeongwon "응. 고마워."
    haneullong "고마우면 기억해줘! 내 이름은 하늘이야!"
    yeongwon "응! 기억할게!"
    scene ecg ki 3
    with fade
    "그리고 다음날 교실에서, 너는 평소처럼 조용히 있던 내게 다가와 주었어."
    "그리고 어젯밤처럼 앞장서서 날 친구들에게 데려다 주었지."
    haneullong "얘 이름은 영원이! 우리 친하게 지내!"
    yeonwoo "귀여운 친구네. 안녕? 난 연우야!"
    hanseol "신기해! 하늘이가 누구 데려온 건 처음이야!"
    yeongwon "아... 안녕."
    fstudent "뭐야, 쟨 누구야? 저런 애가 우리 반에 있었나?"
    mstudent "맨날 교실 구석에서 음침하게 앉아 있는 애 있잖아."
    fstudent "아, 그 벽이랑 대화한다는 애? 하늘이네는 왜 저런 애랑 친해지려고 하는 거야? 기분 나빠."
    haneullong "영원이는 내 친구야. 내가 마음에 들어서 친하게 지내자고 했어."
    haneullong "뭐, 문제 있어?"
    mstudent "아...아니..."
    fstudent "야. 너 어떻게 하늘이네랑 친해졌어? 너 뭐라도 했지?"
    yeongwon "아니... 그게..."
    haneullong "너희들 영원이 괴롭히지 말라고 했지?"
    haneullong "또 누가 괴롭히면, 우리들한테 말해! 우리가 다 혼내줄 테니까."
    yeongwon "응. 고마워."
    scene background sky
    with dissolve
    "만약 내가 그날 밤에 나가지 않았다면, 길을 잃지 않았다면, 그래서 널 만나지 못했다면."
    "난 지금과는 완전히 다른 모습의 사람이 되어 있었겠지."
    "하늘아, 널 만난 다음부터 내 인생이 달라졌어."
    "초등부가 끝나고 너와 연우가 특별반으로 갈 때에는 많이 당황스러웠었지."
    "어릴 때처럼 주눅도 들고 움츠러드는 내 마음을 애써 숨기려고 했었어."
    "그래도 네가 내 손을 잡아주었던 때를 생각하면서 용기를 낼 수 있었지."
    "물론 난 네가 될 수는 없지만, 널 조금이라도 더 닮으려고 노력하고 있어."
    "한별이랑 한설이는 내가 잘 지키고 있어. 걱정하지 마."
    "특별반 생활은 어때? 너니까 잘해나갈 거라고 믿어."
    "어서 졸업해서 만날 수 있으면 좋겠네."
    "졸업 후에는 안전구역 곳곳에 흩어질 테지만, 내가 널 찾아갈게."
    "어릴 때의 네가 날 찾아줬으니, 이번에는 내가 널 찾는 게 맞는 거잖아."
    "그러니까 조금만 더 힘내자."
    "언제나 나만의 천사님, 하늘아."
    #11
    scene background dayhideout
    with fade
    "하늘이와 연우를 만난 이후, 꿈을 꾸듯 현실감 없던 내 일상은, 다시 색을 찾기 시작했다."
    "긴 꿈을 꾸다가 우리 다섯 명이 모두 모인 현실로 돌아온 느낌?"
    "그동안 긴 공백 탓에 생긴 비현실적인 느낌이 날 실수투성이로 만들었지만, 이제 괜찮아."
    "이제 하늘이, 연우와 만났으니까."
    "한별이는 내가 꿈꾸는 듯이 멍해져 있었다고 하지만, 그게 정상적인 행동이 아닐까?"
    "그동안은 꿈이었으니까 말이지."
    "우리 다섯 명이 모이지 못했던 때가 비정상이고 이제서야 정상으로 돌아온 것이다."
    "맞아. 지금이 정상이고 현실이다."
    show yeongwon idle
    with dissolve
    yeongwon "... 그래서 말야, 걔들이 나랑 한별이보고서는 매번 한설이랑만 점심 먹지 말고 자기들이랑도 같이 좀 먹자고 하더라니깐."
    hide yeongwon
    with dissolve
    show hanbyeol idle at left
    with dissolve
    hanbyeol "맞아. 내가 내 친구랑 동생이랑 밥 같이 먹겠다는데 무슨 문제인지 모르겠어."
    
    show hanseol happy at right
    with dissolve
    hanseol "어, 뭐야. 걔네들 한별... 아니 언니 좋아하는 거 아냐?"
    hide hanseol
    hide hanbyeol
    with dissolve
    "저번에 한별이에게 했던 잔소리를 기억했는지, 호칭을 고치려고 노력하는 모습이 보인다."
    show yeonwoo happy2 at left
    with dissolve
    yeonwoo "아니면 영원이를 좋아하는 걸 수도 있지."
    show yeonwoo idle at left
    with dissolve
    yeonwoo "영원이는 알게 모르게 인기가 많으니까."
    
    show yeongwon shock2 at right
    with dissolve
    yeongwon "너희들, 무슨 소리 하는 거야?"
    hide yeongwon
    hide yeonwoo
    with dissolve
    "일동" "하하하..."
    "연우의 웃는 모습이 오늘따라 좀 어색하게 느껴진다."
    "기분 탓인가."
    "제발, 앞으로도 이런 나날이 계속되었으면."
    #12
    scene background oldschoolb
    with fade
    "아지트에서의 짧았던 만남이 끝난 후, 다들 자기 방으로 돌아갔다."
    "하지만, 하늘이와의 만남을 떠올렸던 탓일까."
    "헤어짐이 아쉬워 손끝부터 아려오는 주체 못할 공허함."
    "그 공허함에 몸을 맡긴 채, 바람 느끼며 구교사 주변을 헤맨다."
    "그날의 밤하늘은 우울한 색. "
    "되새기는 한 걸음, 한 걸음에 추억이 피어나고,"
    "가슴속이 꽉 메어와 쓸쓸함을 다시 끌어올라,"
    "외로움을 주체하지 못할 때 쯤, 발끝에 무언가가 걸렸다."
    show yeongwon idle
    with dissolve
    yeongwon "이게 뭐지?"
    hide yeongwon
    with dissolve
    "슬픔을 털어내듯 혼잣말 한 번."
    "발 앞은 아무도 돌아보지 않는 낡은 벽이었다."
    "하지만 땅거미가 기는 늦저녁, 앞이 잘 보이지 않아 벽을 더듬어보았다."
    "갈라진 벽 틈새에서 낡은 노트가 나왔다."
    "집어들고 읽으려는데, 발소리가 멀리서 들려온다."
    "경비 아저씨인가?"
    "다행이 걸리지 않고 구교사를 벗어났으나, 기숙사 앞에서 담임선생님과 마주쳤다."
    "나는 반사적으로 노트를 등 뒤로 숨겼다."
    show teacher idle at left
    show yeongwon shock dark at right
    with dissolve
    "A반 담임" "...영원아?"
    show teacher idle dark
    show yeongwon shock at right
    with dissolve
    yeongwon "하하... 안녕하세요?"
    show yeongwon shock dark
    show teacher idle
    with dissolve
    "A반 담임" "소등시간은 한잠 지났는데, 여기서 뭐하니?"
    show teacher idle dark
    show yeongwon idle
    with dissolve
    yeongwon "잠이 오지 않아서 잠시 산책하고 있었어요."
    yeongwon "죄송합니다."
    
    show teacher idle
    with dissolve
    "A반 담임" "널 본 게 다른 선생님이 아니고 나라서 다행이야."
    "A반 담임" "선생님은 못 본 걸로 할 테니 어서 들어가 자렴."
    
    show yeongwon idle
    with dissolve
    yeongwon "네..."
    
    show teacher idle
    with dissolve
    "A반 담임" "요즘 무슨 고민 있는 거니?"
    "A반 담임" "계속 얼굴도 어둡고, 전에는 안 하던 실수도 하고 말이야."
    "A반 담임" "뭔 일 있으면 꼭 선생님한테 말하렴!"
    
    show yeongwon idle
    with dissolve
    yeongwon "아무 일도 없어요!"
    
    show teacher idle
    with dissolve
    "A반 담임" "그래. 좋은 밤 되고."
    
    show yeongwon idle
    with dissolve
    yeongwon "네. 선생님도 안녕히 주무세요."
    hide yeongwon
    hide teacher
    with dissolve
    scene background dormyeongwon
    with fade
    "휴. 들키지 않아서 다행이다."
    "그런데 이 노트는 대체 뭐지?"
    "구교사 벽 안에 있던 노트라... 수상하다."
    #배경글 시작
    nvle "나그네는 바람에 옷깃을 여미었다가 따사로운 햇빛에 \n외투를 벗는다."
    nvle "그렇지만 폭풍 뒤의 햇빛이 비바람보다도 따갑다면 나그네는 \n어떻게 할까."
    nvle "햇빛이 폭풍보다도 따갑다면, 우산을 펼칠 뿐이다."
    nvle "...저항... ...탈출..."
    #배경글 끝
    nvl clear
    with fade
    show yeongwon shock
    with dissolve
    yeongwon "대체... 뭐야..."
    hide yeongwon
    with dissolve
    "심장이 두근거린다."
    "한번도 해보지 못한 생각."
    "내 마음속 깊은 곳에서 자라나는 새싹."
    "떠오르는 생각들이 무서워져 책을 덮었다."
    "내가 2인실을 혼자 쓰는 것이 지금만큼 고마웠던 적이 없다."
    "다른 사람들에게 들키지 않게 빈 침대 틈 사이에 숨겨 놓아야지."
    #13
    scene background black
    with fade
    "우리가 마지막으로 하늘이와 연우를 만난 이후, 더 이상은 둘을 만날 수 없었다."
    "하늘이가 남겨 놓은 쪽지에서 겨우 소식을 들을 수 있었다."
    "하늘이는 감시가 강해졌고, 연우가 시름시름 앓고 있다고 말했다."
    "그렇게 쪽지만을 주고 받는 나날의 연속이었다."
    "결국, 계절이 바뀌고 나서야 하늘이를 만날 수 있었다."
    scene background dayhideout
    with fade
    show yeongwon happy at left
    show haneul idle dark at right
    with dissolve
    yeongwon "하늘아, 그동안 잘 있었어?"
    show haneul idle
    
    with dissolve
    haneul "응. 걱정하지 않아도 돼."
    haneul "그동안 감시가 좀 심해졌을 뿐이야."
    
    with dissolve
    "그러고 보니, 늘 길었던 하늘이의 머리카락이 다른 남자애들처럼 짧아졌다."
    "무슨 심경의 변화라도 있었던 걸까."
    show yeongwon idle
    with dissolve
    yeongwon "머리카락 잘랐네?"
    
    show haneul idle
    with dissolve
    haneul "...응, 그냥 기분 전환 삼아서."
    
    show yeongwon idle
    with dissolve
    yeongwon "짧은 머리도 잘 어울리네!"
    
    show haneul happy
    with dissolve
    haneul "고마워."
    
    show hanseol sad
    with dissolve
    hanseol "그런데... 연우는...?"
    
    with dissolve
    "일동" "......"
    show haneul sad
    with dissolve
    haneul "연우는, 몸이 많이 약해졌어."
    haneul "앞으로 연우는 아지트에 올 수 없을 지도 몰라."
    
    with dissolve
    "순간적으로 하늘이가 울 것 같았다."
    show haneul sad
    with dissolve
    haneul "...나도 몸이 좋지 않아서."
    haneul "오늘은 이만 가볼게."
    haneul "다음에 쪽지 남겨 놓을게."
    
    show yeongwon sad
    with dissolve
    yeongwon "그래, 잘 가."
    hide hanseol
    hide haneul
    hide yeongwon
    with dissolve

    jump scene201
