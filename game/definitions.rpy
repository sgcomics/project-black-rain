init 10:

    ################
    # Character Definition
    ################

    define yeongwon = Character('영원', image="yeongwon", color="#c8ffc8", show_two_window = True)
    define haneul = Character('하늘', image="haneul", color="#c8ffc8", show_two_window = True)
    define hanbyeol = Character('한별', image="hanbyeol", color="#c8ffc8", show_two_window = True)
    define hanseol = Character('한설', image="hanseol", color="#c8ffc8", show_two_window = True)
    define yeonwoo = Character('연우', image="yeonwoo", color="#c8ffc8", show_two_window = True)
    define principal = Character('원장', image="principal", color="#c8ffc8", show_two_window = True)
    define overwatch = Character('감시자', image="overwatch", color="#c8ffc8", show_two_window = True)
    define keibi = Character('경비원', color="#c8ffc8", show_two_window = True)
    define teacher = Character('선생님', image="teacher", color="#c8ffc8", show_two_window = True)
    define mstudent = Character('남학생', color="#c8ffc8", show_two_window = True)
    define fstudent = Character('여학생', color="#c8ffc8", show_two_window = True)
    define haneul2 = Character('??', color="#c8ffc8", show_two_window = True)
    define shonen = Character('소년', color="#c8ffc8", show_two_window = True)
    define shojo = Character('소녀', color="#c8ffc8", show_two_window = True)

    ################
    # Character Standing CG Definition
    ################

    image fstudent idle = "extra/fstudent.png"
    image keibi idle = "extra/keibi.png"
    image mstudent idle = "extra/mstudent.png"
    image teacher idle = "extra/teacher.png"

    image hanbyeol fury = "hanbyeol/fury.png"
    image hanbyeol fury2 = "hanbyeol/fury2.png"
    image hanbyeol happy = "hanbyeol/happy.png"
    image hanbyeol happy2 = "hanbyeol/happy2.png"
    image hanbyeol idle = "hanbyeol/idle.png"
    image hanbyeol idle2 = "hanbyeol/idle2.png"
    image hanbyeol sad = "hanbyeol/sad.png"
    image hanbyeol sad2 = "hanbyeol/sad2.png"
    image hanbyeol serious = "hanbyeol/serious.png"
    image hanbyeol serious2 = "hanbyeol/serious2.png"
    image hanbyeol shock = "hanbyeol/shock.png"
    image hanbyeol shock2 = "hanbyeol/shock2.png"

    image haneul fury = "haneul/fury.png"
    image haneul happy = "haneul/happy.png"
    image haneul happy2 = "haneul/happy2.png"
    image haneul idle = "haneul/idle.png"
    image haneul sad = "haneul/sad.png"
    image haneul serious = "haneul/serious.png"
    image haneul shock = "haneul/shock.png"

    image haneullong fury = "haneullong/fury.png"
    image haneullong happy = "haneullong/happy.png"
    image haneullong happy2 = "haneullong/happy2.png"
    image haneullong idle = "haneullong/idle.png"
    image haneullong sad = "haneullong/sad.png"
    image haneullong serious = "haneullong/serious.png"
    image haneullong shock = "haneullong/shock.png"

    image hanseol happy = "hanseol/happy.png"
    image hanseol happy2 = "hanseol/happy2.png"
    image hanseol idle = "hanseol/idle.png"
    image hanseol idle2 = "hanseol/idle2.png"
    image hanseol sad = "hanseol/sad.png"
    image hanseol sad2 = "hanseol/sad2.png"
    image hanseol shock = "hanseol/shock.png"
    image hanseol shock2 = "hanseol/shock2.png"

    image overwatch devil = "overwatch/devil.png"
    image overwatch fury = "overwatch/fury.png"
    image overwatch idle = "overwatch/idle.png"
    image overwatch idle2 = "overwatch/idle2.png"

    image principal cry = "principal/cry.png"
    image principal cry2 = "principal/cry2.png"
    image principal happy = "principal/happy.png"
    image principal happy2 = "principal/happy2.png"
    image principal idle = "principal/idle.png"
    image principal idle2 = "principal/idle2.png"
    image principal sad = "principal/sad.png"
    image principal sad2 = "principal/sad2.png"
    image principal sentimental = "principal/sentimental.png"
    image principal sentimental2 = "principal/sentimental2.png"
    image principal shock = "principal/shock.png"
    image principal shock2 = "principal/shock2.png"

    image principalglass happy = "principalglass/happy.png"
    image principalglass happy2 = "principalglass/happy2.png"
    image principalglass idle = "principalglass/idle.png"
    image principalglass idle2 =  "principalglass/idle2.png"

    image yeonwoo happy = "yeonwoo/happy.png"
    image yeonwoo happy2 = "yeonwoo/happy2.png"
    image yeonwoo idle = "yeonwoo/idle.png"
    image yeonwoo idle2 = "yeonwoo/idle2.png"

    image yeongwon blush = "yeongwon/blush.png"
    image yeongwon blush2 = "yeongwon/blush2.png"
    image yeongwon fury = "yeongwon/fury.png"
    image yeongwon fury2 = "yeongwon/fury2.png"
    image yeongwon happy = "yeongwon/happy.png"
    image yeongwon happy2 = "yeongwon/happy2.png"
    image yeongwon idle = "yeongwon/idle.png"
    image yeongwon idle2 = "yeongwon/idle2.png"
    image yeongwon sad = "yeongwon/sad.png"
    image yeongwon sad2 = "yeongwon/sad2.png"
    image yeongwon serious = "yeongwon/serious.png"
    image yeongwon serious2 = "yeongwon/serious2.png"
    image yeongwon shock = "yeongwon/shock.png"
    image yeongwon shock2 = "yeongwon/shock2.png"

    # Darker varients
    image fstudent idleb = im.MatrixColor("extra/fstudent.png",im.matrix.brightness(-0.2))
    image keibi idleb = im.MatrixColor("extra/keibi.png",im.matrix.brightness(-0.2))
    image mstudent idleb = im.MatrixColor("extra/mstudent.png",im.matrix.brightness(-0.2))
    image teacher idleb = im.MatrixColor("extra/teacher.png",im.matrix.brightness(-0.2))
    image hanbyeol furyb = im.MatrixColor("hanbyeol/fury.png",im.matrix.brightness(-0.2))
    image hanbyeol fury2b = im.MatrixColor("hanbyeol/fury2.png",im.matrix.brightness(-0.2))
    image hanbyeol happyb = im.MatrixColor("hanbyeol/happy.png",im.matrix.brightness(-0.2))
    image hanbyeol happy2b = im.MatrixColor("hanbyeol/happy2.png",im.matrix.brightness(-0.2))
    image hanbyeol idleb = im.MatrixColor("hanbyeol/idle.png",im.matrix.brightness(-0.2))
    image hanbyeol idle2b = im.MatrixColor("hanbyeol/idle2.png",im.matrix.brightness(-0.2))
    image hanbyeol sadb = im.MatrixColor("hanbyeol/sad.png",im.matrix.brightness(-0.2))
    image hanbyeol sad2b = im.MatrixColor("hanbyeol/sad2.png",im.matrix.brightness(-0.2))
    image hanbyeol seriousb = im.MatrixColor("hanbyeol/serious.png",im.matrix.brightness(-0.2))
    image hanbyeol serious2b = im.MatrixColor("hanbyeol/serious2.png",im.matrix.brightness(-0.2))
    image hanbyeol shockb = im.MatrixColor("hanbyeol/shock.png",im.matrix.brightness(-0.2))
    image hanbyeol shock2b = im.MatrixColor("hanbyeol/shock2.png",im.matrix.brightness(-0.2))
    image haneul furyb = im.MatrixColor("haneul/fury.png",im.matrix.brightness(-0.2))
    image haneul happyb = im.MatrixColor("haneul/happy.png",im.matrix.brightness(-0.2))
    image haneul happy2b = im.MatrixColor("haneul/happy2.png",im.matrix.brightness(-0.2))
    image haneul idleb = im.MatrixColor("haneul/idle.png",im.matrix.brightness(-0.2))
    image haneul sadb = im.MatrixColor("haneul/sad.png",im.matrix.brightness(-0.2))
    image haneul seriousb = im.MatrixColor("haneul/serious.png",im.matrix.brightness(-0.2))
    image haneul shockb = im.MatrixColor("haneul/shock.png",im.matrix.brightness(-0.2))
    image haneullong furyb = im.MatrixColor("haneullong/fury.png",im.matrix.brightness(-0.2))
    image haneullong happyb = im.MatrixColor("haneullong/happy.png",im.matrix.brightness(-0.2))
    image haneullong happy2b = im.MatrixColor("haneullong/happy2.png",im.matrix.brightness(-0.2))
    image haneullong idleb = im.MatrixColor("haneullong/idle.png",im.matrix.brightness(-0.2))
    image haneullong sadb = im.MatrixColor("haneullong/sad.png",im.matrix.brightness(-0.2))
    image haneullong seriousb = im.MatrixColor("haneullong/serious.png",im.matrix.brightness(-0.2))
    image haneullong shockb = im.MatrixColor("haneullong/shock.png",im.matrix.brightness(-0.2))
    image hanseol happyb = im.MatrixColor("hanseol/happy.png",im.matrix.brightness(-0.2))
    image hanseol happy2b = im.MatrixColor("hanseol/happy2.png",im.matrix.brightness(-0.2))
    image hanseol idleb = im.MatrixColor("hanseol/idle.png",im.matrix.brightness(-0.2))
    image hanseol idle2b = im.MatrixColor("hanseol/idle2.png",im.matrix.brightness(-0.2))
    image hanseol sadb = im.MatrixColor("hanseol/sad.png",im.matrix.brightness(-0.2))
    image hanseol sad2b = im.MatrixColor("hanseol/sad2.png",im.matrix.brightness(-0.2))
    image hanseol shockb = im.MatrixColor("hanseol/shock.png",im.matrix.brightness(-0.2))
    image hanseol shock2b = im.MatrixColor("hanseol/shock2.png",im.matrix.brightness(-0.2))
    image overwatch devilb = im.MatrixColor("overwatch/devil.png",im.matrix.brightness(-0.2))
    image overwatch furyb = im.MatrixColor("overwatch/fury.png",im.matrix.brightness(-0.2))
    image overwatch idleb = im.MatrixColor("overwatch/idle.png",im.matrix.brightness(-0.2))
    image overwatch idle2b = im.MatrixColor("overwatch/idle2.png",im.matrix.brightness(-0.2))
    image principal cryb = im.MatrixColor("principal/cry.png",im.matrix.brightness(-0.2))
    image principal cry2b = im.MatrixColor("principal/cry2.png",im.matrix.brightness(-0.2))
    image principal happyb = im.MatrixColor("principal/happy.png",im.matrix.brightness(-0.2))
    image principal happy2b = im.MatrixColor("principal/happy2.png",im.matrix.brightness(-0.2))
    image principal idleb = im.MatrixColor("principal/idle.png",im.matrix.brightness(-0.2))
    image principal idle2b = im.MatrixColor("principal/idle2.png",im.matrix.brightness(-0.2))
    image principal sadb = im.MatrixColor("principal/sad.png",im.matrix.brightness(-0.2))
    image principal sad2b = im.MatrixColor("principal/sad2.png",im.matrix.brightness(-0.2))
    image principal sentimentalb = im.MatrixColor("principal/sentimental.png",im.matrix.brightness(-0.2))
    image principal sentimental2b = im.MatrixColor("principal/sentimental2.png",im.matrix.brightness(-0.2))
    image principal shockb = im.MatrixColor("principal/shock.png",im.matrix.brightness(-0.2))
    image principal shock2b = im.MatrixColor("principal/shock2.png",im.matrix.brightness(-0.2))
    image principalglass happyb = im.MatrixColor("principalglass/happy.png",im.matrix.brightness(-0.2))
    image principalglass happy2b = im.MatrixColor("principalglass/happy2.png",im.matrix.brightness(-0.2))
    image principalglass idleb = im.MatrixColor("principalglass/idle.png",im.matrix.brightness(-0.2))
    image principalglass idle2b = im.MatrixColor("principalglass/idle2.png",im.matrix.brightness(-0.2))
    image yeonwoo happyb = im.MatrixColor("yeonwoo/happy.png",im.matrix.brightness(-0.2))
    image yeonwoo happy2b = im.MatrixColor("yeonwoo/happy2.png",im.matrix.brightness(-0.2))
    image yeonwoo idleb = im.MatrixColor("yeonwoo/idle.png",im.matrix.brightness(-0.2))
    image yeonwoo idle2b = im.MatrixColor("yeonwoo/idle2.png",im.matrix.brightness(-0.2))
    image yeongwon blushb = im.MatrixColor("yeongwon/blush.png",im.matrix.brightness(-0.2))
    image yeongwon blush2b = im.MatrixColor("yeongwon/blush2.png",im.matrix.brightness(-0.2))
    image yeongwon furyb = im.MatrixColor("yeongwon/fury.png",im.matrix.brightness(-0.2))
    image yeongwon fury2b = im.MatrixColor("yeongwon/fury2.png",im.matrix.brightness(-0.2))
    image yeongwon happyb = im.MatrixColor("yeongwon/happy.png",im.matrix.brightness(-0.2))
    image yeongwon happy2b = im.MatrixColor("yeongwon/happy2.png",im.matrix.brightness(-0.2))
    image yeongwon idleb = im.MatrixColor("yeongwon/idle.png",im.matrix.brightness(-0.2))
    image yeongwon idle2b = im.MatrixColor("yeongwon/idle2.png",im.matrix.brightness(-0.2))
    image yeongwon sadb = im.MatrixColor("yeongwon/sad.png",im.matrix.brightness(-0.2))
    image yeongwon sad2b = im.MatrixColor("yeongwon/sad2.png",im.matrix.brightness(-0.2))
    image yeongwon seriousb = im.MatrixColor("yeongwon/serious.png",im.matrix.brightness(-0.2))
    image yeongwon serious2b = im.MatrixColor("yeongwon/serious2.png",im.matrix.brightness(-0.2))
    image yeongwon shockb = im.MatrixColor("yeongwon/shock.png",im.matrix.brightness(-0.2))
    image yeongwon shock2b = im.MatrixColor("yeongwon/shock2.png",im.matrix.brightness(-0.2))

    ################
    # Background Sprite Definition
    ################

    image bg classroom = "background/classroom.jpg"
    image bg hallway = "background/hallway.jpg"
    image bg hideout = "background/hideout.jpg"
    image bg lab = "background/lab.jpg"
    image bg oldschool = "background/oldschool.jpg"
    image bg school = "background/school.jpg"
    image bg sky = "background/sky.jpg"
    image bg stairs = "background/stairs.jpg"
    image bg what = "background/what.jpg"
    image bg what2 = "background/what2.jpg"

    image bg classroomb = im.MatrixColor("background/classroom.jpg",im.matrix.brightness(-0.2))
    image bg hallwayb = im.MatrixColor("background/hallway.jpg",im.matrix.brightness(-0.2))
    image bg hideoutb = im.MatrixColor("background/hideout.jpg",im.matrix.brightness(-0.2))
    image bg labb = im.MatrixColor("background/lab.jpg",im.matrix.brightness(-0.2))
    image bg schoolb = im.MatrixColor("background/school.jpg",im.matrix.brightness(-0.2))
    image bg oldschoolb = im.MatrixColor("background/oldschool.jpg",im.matrix.brightness(-0.2))
    image bg skyb = im.MatrixColor("background/sky.jpg",im.matrix.brightness(-0.2))
    image bg stairsb = im.MatrixColor("background/stairs.jpg",im.matrix.brightness(-0.2))
    image bg whatb = im.MatrixColor("background/what.jpg",im.matrix.brightness(-0.2))