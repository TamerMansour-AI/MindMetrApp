import streamlit as st

def emotional_intelligence_assessment():
    st.title("Emotional Intelligence (الذكاء العاطفي) Assessment")
    
    # Introduction for the child (bilingual)
    st.markdown("""
    ### **Welcome to the Emotional Intelligence Assessment | مرحبًا بكم في تقييم الذكاء العاطفي**
    
    In this assessment, you'll explore how you understand and manage emotions, both yours and others'. You'll face interesting challenges where you can express how you feel and how you respond to different situations.

    في هذا التقييم، ستستكشف كيفية فهمك وإدارتك للعواطف، سواء كانت مشاعرك أو مشاعر الآخرين. ستواجه تحديات مثيرة حيث يمكنك التعبير عن شعورك وكيف تتفاعل مع المواقف المختلفة.
    """)

    # Scenario 1
    st.markdown("""
    #### **Scenario 1 | السيناريو الأول:**
    You’re walking through a magical forest when you see a creature that looks scared and alone. It’s hiding behind a tree, unsure whether to trust you. How do you make it feel safe?

    أنت تمشي في غابة سحرية عندما ترى مخلوقًا يبدو خائفًا ووحيدًا. يختبئ خلف شجرة، وغير متأكد من إمكانية الوثوق بك. كيف ستجعله يشعر بالأمان؟
    """)

    answer_q1 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would approach slowly and speak gently to show I mean no harm | سأقترب ببطء وأتحدث بلطف لإظهار أنني لا أريد الأذى.",
            "I would stay still and wait for the creature to feel comfortable | سأبقى في مكاني وأنتظر حتى يشعر المخلوق بالراحة.",
            "I would offer some food or a gift to show my kindness | سأقدم بعض الطعام أو هدية لإظهار لطفني."
        )
    )

    # Scenario 2
    st.markdown("""
    #### **Scenario 2 | السيناريو الثاني:**
    During a team game, one of your friends gets upset because they made a mistake. They feel embarrassed in front of the group. How do you help them feel better?

    خلال لعبة جماعية، يشعر أحد أصدقائك بالإحباط لأنه ارتكب خطأ. يشعر بالإحراج أمام المجموعة. كيف ستساعده على الشعور بتحسن؟
    """)

    answer_q2 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would remind them that everyone makes mistakes, and it’s okay | سأذكره أن الجميع يرتكب الأخطاء، وهذا طبيعي.",
            "I would try to make them laugh and forget about the mistake | سأحاول أن أجعله يضحك وينسى الخطأ.",
            "I would encourage the group to support them and move on | سأشجع المجموعة على دعمه والمضي قدمًا."
        )
    )

    # Scenario 3
    st.markdown("""
    #### **Scenario 3 | السيناريو الثالث:**
    You’ve been given a special hat that lets you see other people's emotions as colors around them. You notice that one of your classmates has a very dark color, which means they are sad. What do you do?

    تم إعطاؤك قبعة خاصة تتيح لك رؤية مشاعر الآخرين كألوان تحيط بهم. تلاحظ أن أحد زملائك في الصف لديه لون داكن جدًا، مما يعني أنه حزين. ماذا ستفعل؟
    """)

    answer_q3 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would ask them if they want to talk about what’s bothering them | سأطلب منه التحدث عن ما يزعجه.",
            "I would try to cheer them up by telling them a funny story | سأحاول أن أرفع معنوياته بإخباره قصة مضحكة.",
            "I would give them space and check on them later | سأعطيه مساحة خاصة وأتحقق منه لاحقًا."
        )
    )

    # Scenario 4
    st.markdown("""
    #### **Scenario 4 | السيناريو الرابع:**
    You’ve been given a task that feels overwhelming, and you're starting to feel stressed. What do you do to help yourself manage your emotions?

    تم إعطاؤك مهمة تشعر بأنها مرهقة، وبدأت تشعر بالتوتر. ماذا ستفعل لمساعدة نفسك على إدارة مشاعرك؟
    """)

    answer_q4 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would take a break and focus on breathing deeply | سأخذ استراحة وأركز على التنفس بعمق.",
            "I would break the task into smaller steps to make it easier | سأقسم المهمة إلى خطوات أصغر لتسهيلها.",
            "I would talk to someone I trust to share how I feel | سأتحدث إلى شخص أثق به لمشاركة مشاعري."
        )
    )

    # Scenario 5
    st.markdown("""
    #### **Scenario 5 | السيناريو الخامس:**
    One of your friends is very excited about a project, but they’re starting to get frustrated because things aren’t going the way they expected. How do you help them stay calm and focused?

    أحد أصدقائك متحمس جدًا لمشروع، لكنه بدأ يشعر بالإحباط لأن الأمور لا تسير كما كان يتوقع. كيف ستساعده على البقاء هادئًا ومركزًا؟
    """)

    answer_q5 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would encourage them to take a break and return with a fresh mind | سأشجعه على أخذ استراحة والعودة بعقل منتعش.",
            "I would remind them that it’s okay if things don’t go perfectly at first | سأذكره أنه لا بأس إذا لم تسر الأمور بشكل مثالي في البداية.",
            "I would help them find a new approach to tackle the problem | سأساعده في إيجاد نهج جديد للتعامل مع المشكلة."
        )
    )

    # Submit Button
    if st.button("Submit | إرسال"):
        st.markdown("### **Thank you for completing the Emotional Intelligence Assessment! | شكرًا لك على إكمال تقييم الذكاء العاطفي!**")
        st.markdown("""
        Based on your answers, you will receive feedback on your emotional intelligence skills:
        
        - If you offered support to others, it shows you're empathetic and caring about others' emotions.
        - Managing stress and helping friends stay calm demonstrates your emotional awareness and leadership.

        بناءً على إجاباتك، ستحصل على ملاحظات حول مهاراتك في الذكاء العاطفي:

        - إذا قدمت الدعم للآخرين، فهذا يظهر أنك متعاطف وتهتم بمشاعر الآخرين.
        - إدارة التوتر ومساعدة الأصدقاء على البقاء هادئين يظهر وعيك العاطفي وقدرتك على القيادة.
        """)

        # Additional personalized messages could be added depending on the rubric system.
