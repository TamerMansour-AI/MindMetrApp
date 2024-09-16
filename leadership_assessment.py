import streamlit as st

def leadership_assessment():
    st.title("Leadership (القيادة) Assessment")
    
    # Introduction for the child (bilingual)
    st.markdown("""
    ### **Welcome to the Leadership Assessment | مرحبًا بكم في تقييم القيادة**
    
    In this adventure, you'll face challenges where you'll need to guide others, make important decisions, and think like a leader. There are no right or wrong answers—just choose what you think would make the best leader!

    في هذه المغامرة، ستواجه تحديات تحتاج فيها إلى توجيه الآخرين واتخاذ قرارات مهمة والتفكير كقائد. لا توجد إجابات صحيحة أو خاطئة - فقط اختر ما تعتقد أنه يجعل القائد الأفضل!
    """)

    # Scenario 1
    st.markdown("""
    #### **Scenario 1 | السيناريو الأول:**
    You’re the captain of a ship sailing through a stormy sea. Your crew is looking to you for direction. What do you do to keep everyone calm and on course?

    أنت قبطان سفينة تبحر في بحر عاصف. طاقمك ينظر إليك للحصول على التوجيه. ماذا ستفعل للحفاظ على هدوء الجميع ومتابعة المسار؟
    """)

    answer_q1 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would give clear instructions to keep everyone focused on their tasks | سأعطي تعليمات واضحة لإبقاء الجميع مركزين على مهامهم.",
            "I would encourage the crew by reminding them that we’ve faced storms before | سأشجع الطاقم بتذكيرهم أننا واجهنا عواصف من قبل.",
            "I would lead by example, staying calm and working alongside my team | سأقود بالقدوة من خلال البقاء هادئًا والعمل جنبًا إلى جنب مع فريقي."
        )
    )

    # Scenario 2
    st.markdown("""
    #### **Scenario 2 | السيناريو الثاني:**
    You’ve been chosen to lead an expedition to explore a hidden jungle. Your team is nervous because no one has ever been there before. How do you motivate them and make sure the mission is a success?

    تم اختيارك لقيادة بعثة لاستكشاف غابة مخفية. فريقك يشعر بالتوتر لأن لا أحد ذهب إلى هناك من قبل. كيف ستحفزهم وتتأكد من أن المهمة ستكون ناجحة؟
    """)

    answer_q2 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would create a clear plan and explain everyone's role so they feel prepared | سأضع خطة واضحة وأشرح دور كل شخص ليشعروا بالاستعداد.",
            "I would inspire them by talking about the excitement of discovering something new | سأحفزهم بالحديث عن الإثارة في اكتشاف شيء جديد.",
            "I would ask the team for their ideas and input to make them feel involved | سأطلب من الفريق أفكارهم ومشاركتهم لجعلهم يشعرون بالمشاركة."
        )
    )

    # Scenario 3
    st.markdown("""
    #### **Scenario 3 | السيناريو الثالث:**
    You’re the leader of a group of superheroes, and each team member has a different superpower. A big challenge is ahead, and you need to decide how to use each person's strengths to save the day. How do you organize your team?

    أنت قائد مجموعة من الأبطال الخارقين، ولكل عضو في الفريق قوة خارقة مختلفة. هناك تحد كبير في الأمام، وتحتاج إلى اتخاذ قرار حول كيفية استخدام نقاط قوة كل شخص لإنقاذ الموقف. كيف ستنظم فريقك؟
    """)

    answer_q3 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would match each person’s superpower to the part of the challenge they’re best at | سأطابق قوة كل شخص مع الجزء من التحدي الذي يتقنه.",
            "I would encourage teamwork by pairing people with complementary powers | سأشجع العمل الجماعي عن طريق جمع الأشخاص ذوي القوى المتكاملة.",
            "I would let the team choose which part of the challenge they feel most confident in | سأدع الفريق يختار الجزء الذي يشعرون بالثقة فيه."
        )
    )

    # Scenario 4
    st.markdown("""
    #### **Scenario 4 | السيناريو الرابع:**
    You’ve been asked to lead a team of inventors to create a brand-new gadget for the future. The team is having trouble agreeing on a design. How do you help everyone work together and reach a decision?

    طُلب منك قيادة فريق من المخترعين لإنشاء أداة جديدة للمستقبل. الفريق يواجه صعوبة في الاتفاق على التصميم. كيف ستساعد الجميع على العمل معًا والتوصل إلى قرار؟
    """)

    answer_q4 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would listen to each person's ideas and find a way to combine the best parts | سأستمع إلى أفكار كل شخص وأجد طريقة لدمج الأجزاء الأفضل.",
            "I would suggest a vote to let the majority decide | سأقترح إجراء تصويت ليتخذ الأغلبية القرار.",
            "I would ask the team to brainstorm more ideas and keep an open mind | سأطلب من الفريق العصف الذهني لأفكار جديدة والبقاء منفتحين."
        )
    )

    # Scenario 5
    st.markdown("""
    #### **Scenario 5 | السيناريو الخامس:**
    You’re the leader of a group of explorers who have discovered an ancient city. The team is excited but also nervous about what lies ahead. How do you guide them as they explore and make important discoveries?

    أنت قائد مجموعة من المستكشفين الذين اكتشفوا مدينة قديمة. الفريق متحمس ولكنه أيضًا متوتر بشأن ما ينتظرهم. كيف ستوجههم أثناء استكشافهم وتوجيه الاكتشافات الهامة؟
    """)

    answer_q5 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would lead by encouraging curiosity while making sure everyone stays safe | سأقود الفريق من خلال تشجيع الفضول والتأكد من بقاء الجميع في أمان.",
            "I would divide the team into smaller groups, each with a clear goal | سأقسم الفريق إلى مجموعات أصغر، لكل منها هدف واضح.",
            "I would ask the team for ideas on how to explore the city in the best way | سأطلب من الفريق أفكارًا حول كيفية استكشاف المدينة بأفضل طريقة."
        )
    )

    # Submit Button
    if st.button("Submit | إرسال"):
        st.markdown("### **Thank you for completing the Leadership Assessment! | شكرًا لك على إكمال تقييم القيادة!**")
        st.markdown("""
        Based on your answers, you will receive feedback on your leadership skills:
        
        - If you made clear plans and encouraged teamwork, it shows you're a strong leader who knows how to guide others.
        - Leading by example and staying calm in difficult situations shows you're a responsible and inspiring leader.

        بناءً على إجاباتك، ستحصل على ملاحظات حول مهاراتك القيادية:

        - إذا وضعت خططًا واضحة وشجعت العمل الجماعي، فهذا يظهر أنك قائد قوي يعرف كيف يقود الآخرين.
        - القيادة بالقدوة والبقاء هادئًا في المواقف الصعبة يظهر أنك قائد مسؤول وملهم.
        """)

        # Additional personalized messages could be added depending on the rubric system.
