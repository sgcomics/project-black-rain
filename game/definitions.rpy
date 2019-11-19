init 10:

    ################
    # Character Definition
    ################

    define yeongwon = Character('영원', image="yeongwon", color="#c8ffc8")
    define haneul = Character('하늘', image="haneul", color="#c8ffc8")
    define hanbyeol = Character('한별', image="hanbyeol", color="#c8ffc8")
    define hanseol = Character('한설', image="hanseol", color="#c8ffc8")
    define yeonwoo = Character('연우', image="yeonwoo", color="#c8ffc8")
    define principal = Character('원장', image="principal", color="#c8ffc8")
    define overwatch = Character('감시자', image="overwatch", color="#c8ffc8")
    define keibi = Character('경비원', color="#c8ffc8")
    define teacher = Character('선생님', image="teacher", color="#c8ffc8")
    define mstudent = Character('남학생', color="#c8ffc8")
    define fstudent = Character('여학생', color="#c8ffc8")
    define haneul2 = Character('??', color="#c8ffc8")
    define shonen = Character('소년', color="#c8ffc8")
    define shojo = Character('소녀', color="#c8ffc8")

    define nvle = Character("", kind=nvl, what_text_align=0.5, what_xalign=0.5, what_yalign=0.5)

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
    image fstudent idle dark = im.MatrixColor("extra/fstudent.png", im.matrix.brightness(-0.2))
    image keibi idle dark = im.MatrixColor("extra/keibi.png", im.matrix.brightness(-0.2))
    image mstudent idle dark = im.MatrixColor("extra/mstudent.png", im.matrix.brightness(-0.2))
    image teacher idle dark = im.MatrixColor("extra/teacher.png", im.matrix.brightness(-0.2))
    
    image hanbyeol fury dark = im.MatrixColor("hanbyeol/fury.png", im.matrix.brightness(-0.2))
    image hanbyeol fury2 dark = im.MatrixColor("hanbyeol/fury2.png", im.matrix.brightness(-0.2))
    image hanbyeol happy dark = im.MatrixColor("hanbyeol/happy.png", im.matrix.brightness(-0.2))
    image hanbyeol happy2 dark = im.MatrixColor("hanbyeol/happy2.png", im.matrix.brightness(-0.2))
    image hanbyeol idle dark = im.MatrixColor("hanbyeol/idle.png", im.matrix.brightness(-0.2))
    image hanbyeol idle2 dark = im.MatrixColor("hanbyeol/idle2.png", im.matrix.brightness(-0.2))
    image hanbyeol sad dark = im.MatrixColor("hanbyeol/sad.png", im.matrix.brightness(-0.2))
    image hanbyeol sad2 dark = im.MatrixColor("hanbyeol/sad2.png", im.matrix.brightness(-0.2))
    image hanbyeol serious dark = im.MatrixColor("hanbyeol/serious.png", im.matrix.brightness(-0.2))
    image hanbyeol serious2 dark = im.MatrixColor("hanbyeol/serious2.png", im.matrix.brightness(-0.2))
    image hanbyeol shock dark = im.MatrixColor("hanbyeol/shock.png", im.matrix.brightness(-0.2))
    image hanbyeol shock2 dark = im.MatrixColor("hanbyeol/shock2.png", im.matrix.brightness(-0.2))
    
    image haneul fury dark = im.MatrixColor("haneul/fury.png", im.matrix.brightness(-0.2))
    image haneul happy dark = im.MatrixColor("haneul/happy.png", im.matrix.brightness(-0.2))
    image haneul happy2 dark = im.MatrixColor("haneul/happy2.png", im.matrix.brightness(-0.2))
    image haneul idle dark = im.MatrixColor("haneul/idle.png", im.matrix.brightness(-0.2))
    image haneul sad dark = im.MatrixColor("haneul/sad.png", im.matrix.brightness(-0.2))
    image haneul serious dark = im.MatrixColor("haneul/serious.png", im.matrix.brightness(-0.2))
    image haneul shock dark = im.MatrixColor("haneul/shock.png", im.matrix.brightness(-0.2))
    
    image haneullong fury dark = im.MatrixColor("haneullong/fury.png", im.matrix.brightness(-0.2))
    image haneullong happy dark = im.MatrixColor("haneullong/happy.png", im.matrix.brightness(-0.2))
    image haneullong happy2 dark = im.MatrixColor("haneullong/happy2.png", im.matrix.brightness(-0.2))
    image haneullong idle dark = im.MatrixColor("haneullong/idle.png", im.matrix.brightness(-0.2))
    image haneullong sad dark = im.MatrixColor("haneullong/sad.png", im.matrix.brightness(-0.2))
    image haneullong serious dark = im.MatrixColor("haneullong/serious.png", im.matrix.brightness(-0.2))
    image haneullong shock dark = im.MatrixColor("haneullong/shock.png", im.matrix.brightness(-0.2))
    
    image hanseol happy dark = im.MatrixColor("hanseol/happy.png", im.matrix.brightness(-0.2))
    image hanseol happy2 dark = im.MatrixColor("hanseol/happy2.png", im.matrix.brightness(-0.2))
    image hanseol idle dark = im.MatrixColor("hanseol/idle.png", im.matrix.brightness(-0.2))
    image hanseol idle2 dark = im.MatrixColor("hanseol/idle2.png", im.matrix.brightness(-0.2))
    image hanseol sad dark = im.MatrixColor("hanseol/sad.png", im.matrix.brightness(-0.2))
    image hanseol sad2 dark = im.MatrixColor("hanseol/sad2.png", im.matrix.brightness(-0.2))
    image hanseol shock dark = im.MatrixColor("hanseol/shock.png", im.matrix.brightness(-0.2))
    image hanseol shock2 dark = im.MatrixColor("hanseol/shock2.png", im.matrix.brightness(-0.2))
    
    image overwatch devil dark = im.MatrixColor("overwatch/devil.png", im.matrix.brightness(-0.2))
    image overwatch fury dark = im.MatrixColor("overwatch/fury.png", im.matrix.brightness(-0.2))
    image overwatch idle dark = im.MatrixColor("overwatch/idle.png", im.matrix.brightness(-0.2))
    image overwatch idle2 dark = im.MatrixColor("overwatch/idle2.png", im.matrix.brightness(-0.2))
    
    image principal cry dark = im.MatrixColor("principal/cry.png", im.matrix.brightness(-0.2))
    image principal cry2 dark = im.MatrixColor("principal/cry2.png", im.matrix.brightness(-0.2))
    image principal happy dark = im.MatrixColor("principal/happy.png", im.matrix.brightness(-0.2))
    image principal happy2 dark = im.MatrixColor("principal/happy2.png", im.matrix.brightness(-0.2))
    image principal idle dark = im.MatrixColor("principal/idle.png", im.matrix.brightness(-0.2))
    image principal idle2 dark = im.MatrixColor("principal/idle2.png", im.matrix.brightness(-0.2))
    image principal sad dark = im.MatrixColor("principal/sad.png", im.matrix.brightness(-0.2))
    image principal sad2 dark = im.MatrixColor("principal/sad2.png", im.matrix.brightness(-0.2))
    image principal sentimental dark = im.MatrixColor("principal/sentimental.png", im.matrix.brightness(-0.2))
    image principal sentimental2 dark = im.MatrixColor("principal/sentimental2.png", im.matrix.brightness(-0.2))
    image principal shock dark = im.MatrixColor("principal/shock.png", im.matrix.brightness(-0.2))
    image principal shock2 dark = im.MatrixColor("principal/shock2.png", im.matrix.brightness(-0.2))
    
    image principalglass happy dark = im.MatrixColor("principalglass/happy.png", im.matrix.brightness(-0.2))
    image principalglass happy2 dark = im.MatrixColor("principalglass/happy2.png", im.matrix.brightness(-0.2))
    image principalglass idle dark = im.MatrixColor("principalglass/idle.png", im.matrix.brightness(-0.2))
    image principalglass idle2 dark = im.MatrixColor("principalglass/idle2.png", im.matrix.brightness(-0.2))
    
    image yeonwoo happy dark = im.MatrixColor("yeonwoo/happy.png", im.matrix.brightness(-0.2))
    image yeonwoo happy2 dark = im.MatrixColor("yeonwoo/happy2.png", im.matrix.brightness(-0.2))
    image yeonwoo idle dark = im.MatrixColor("yeonwoo/idle.png", im.matrix.brightness(-0.2))
    image yeonwoo idle2 dark = im.MatrixColor("yeonwoo/idle2.png", im.matrix.brightness(-0.2))
    
    image yeongwon blush dark = im.MatrixColor("yeongwon/blush.png", im.matrix.brightness(-0.2))
    image yeongwon blush2 dark = im.MatrixColor("yeongwon/blush2.png", im.matrix.brightness(-0.2))
    image yeongwon fury dark = im.MatrixColor("yeongwon/fury.png", im.matrix.brightness(-0.2))
    image yeongwon fury2 dark = im.MatrixColor("yeongwon/fury2.png", im.matrix.brightness(-0.2))
    image yeongwon happy dark = im.MatrixColor("yeongwon/happy.png", im.matrix.brightness(-0.2))
    image yeongwon happy2 dark = im.MatrixColor("yeongwon/happy2.png", im.matrix.brightness(-0.2))
    image yeongwon idle dark = im.MatrixColor("yeongwon/idle.png", im.matrix.brightness(-0.2))
    image yeongwon idle2 dark = im.MatrixColor("yeongwon/idle2.png", im.matrix.brightness(-0.2))
    image yeongwon sad dark = im.MatrixColor("yeongwon/sad.png", im.matrix.brightness(-0.2))
    image yeongwon sad2 dark = im.MatrixColor("yeongwon/sad2.png", im.matrix.brightness(-0.2))
    image yeongwon serious dark = im.MatrixColor("yeongwon/serious.png", im.matrix.brightness(-0.2))
    image yeongwon serious2 dark = im.MatrixColor("yeongwon/serious2.png", im.matrix.brightness(-0.2))
    image yeongwon shock dark = im.MatrixColor("yeongwon/shock.png", im.matrix.brightness(-0.2))
    image yeongwon shock2 dark = im.MatrixColor("yeongwon/shock2.png", im.matrix.brightness(-0.2))

    ################
    # Background Sprite Definition
    ################

    image background bed = "background/bed.png"
    image background classday = "background/classday.png"
    image background classnight = "background/classnight.png"
    image background dayhideout = "background/dayhideout.png"
    image background dininghall = "background/dininghall.png"
    image background dormhallway = "background/dormhallway.png"
    image background dormhanbyeol = "background/dormhanbyeol.png"
    image background dormlowchroma = "background/dormlowchroma.png"
    image background dormyeongwon = "background/dormyeongwon.png"
    image background hiddenlab = "background/hiddenlab.png"
    image background hospital = "background/hospital.png"
    image background house = "background/house.png"
    image background lab = "background/lab.png"
    image background labhallway = "background/labhallway.png"
    image background nighthideout = "background/nighthideout.png"
    image background oldclass = "background/oldclass.png"
    image background oldhallway = "background/oldhallway.png"
    image background oldschool = "background/oldschool.png"
    image background oldstairs = "background/oldstairs.png"
    image background principaloffice = "background/principaloffice.png"
    image background school = "background/school.png"
    image background schoolhallway = "background/schoolhallway.png"
    image background schoolhallwaynight = "background/schoolhallwaynight.png"
    image background shelter = "background/shelter.png"
    image background sky = "background/sky.png"
    image background stairs = "background/stairs.png"
    image background wasteland = "background/wasteland.png"

    image background black = Solid("#000000")

    image background bed dark = im.MatrixColor("background/bed.png", im.matrix.brightness(-0.2))
    image background classday dark = im.MatrixColor("background/classday.png", im.matrix.brightness(-0.2))
    image background classnight dark = im.MatrixColor("background/classnight.png", im.matrix.brightness(-0.2))
    image background dayhideout dark = im.MatrixColor("background/dayhideout.png", im.matrix.brightness(-0.2))
    image background dininghall dark = im.MatrixColor("background/dininghall.png", im.matrix.brightness(-0.2))
    image background dormhallway dark = im.MatrixColor("background/dormhallway.png", im.matrix.brightness(-0.2))
    image background dormhanbyeol dark = im.MatrixColor("background/dormhanbyeol.png", im.matrix.brightness(-0.2))
    image background dormlowchroma dark = im.MatrixColor("background/dormlowchroma.png", im.matrix.brightness(-0.2))
    image background dormyeongwon dark = im.MatrixColor("background/dormyeongwon.png", im.matrix.brightness(-0.2))
    image background hiddenlab dark = im.MatrixColor("background/hiddenlab.png", im.matrix.brightness(-0.2))
    image background hospital dark = im.MatrixColor("background/hospital.png", im.matrix.brightness(-0.2))
    image background house dark = im.MatrixColor("background/house.png", im.matrix.brightness(-0.2))
    image background lab dark = im.MatrixColor("background/lab.png", im.matrix.brightness(-0.2))
    image background labhallway dark = im.MatrixColor("background/labhallway.png", im.matrix.brightness(-0.2))
    image background nighthideout dark = im.MatrixColor("background/nighthideout.png", im.matrix.brightness(-0.2))
    image background oldclass dark = im.MatrixColor("background/oldclass.png", im.matrix.brightness(-0.2))
    image background oldhallway dark = im.MatrixColor("background/oldhallway.png", im.matrix.brightness(-0.2))
    image background oldschool dark = im.MatrixColor("background/oldschool.png", im.matrix.brightness(-0.2))
    image background oldstairs dark = im.MatrixColor("background/oldstairs.png", im.matrix.brightness(-0.2))
    image background principaloffice dark = im.MatrixColor("background/principaloffice.png", im.matrix.brightness(-0.2))
    image background school dark = im.MatrixColor("background/school.png", im.matrix.brightness(-0.2))
    image background schoolhallway dark = im.MatrixColor("background/schoolhallway.png", im.matrix.brightness(-0.2))
    image background schoolhallwaynight dark = im.MatrixColor("background/schoolhallwaynight.png", im.matrix.brightness(-0.2))
    image background shelter dark = im.MatrixColor("background/shelter.png", im.matrix.brightness(-0.2))
    image background sky dark = im.MatrixColor("background/sky.png", im.matrix.brightness(-0.2))
    image background stairs dark = im.MatrixColor("background/stairs.png", im.matrix.brightness(-0.2))
    image background wasteland dark = im.MatrixColor("background/wasteland.png", im.matrix.brightness(-0.2))

    ################
    # Predefined positions
    ################

    transform slightleft:
        xalign 0.30
        yalign 1.0

    transform slightright:
        xalign 0.75
        yalign 1.0

    transform moveright:
        linear 0.5 xalign 0.95

    transform movecenter:
        linear 0.5 xalign 0.5

    transform moveslightright:
        linear 0.5 xalign 0.75

    transform moveleft:
        linear 0.5 xalign 0.05

    transform moveslightleft:
        linear 0.5 xalign 0.3
