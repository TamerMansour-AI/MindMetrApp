import streamlit as st

def global_citizenship_assessment():
    st.title("Global Citizenship (المواطنة العالمية) Assessment")
    
    # Introduction for the child (bilingual)
    st.markdown("""
    ### **Welcome to the Global Citizenship Assessment | مرحبًا بكم في تقييم المواطنة العالمية**
    
    In this adventure, you'll explore challenges that test how you think about the world, other cultures, and the environment. There are no right or wrong answers—just choose the path that feels right to you!

    في هذه المغامرة، ستستكشف تحديات تختبر كيفية تفكيرك في العالم والثقافات الأخرى والبيئة. لا توجد إجابات صحيحة أو خاطئة - فقط اختر الطريق الذي تشعر أنه صحيح!
    """)

    # Scenario 1
    st.markdown("""
    #### **Scenario 1 | السيناريو الأول:**
    You’ve been invited to a special event where children from all over the world share their traditions. One child asks you about a unique tradition from your country. How do you explain it in a way they will understand?

    تمت دعوتك إلى حدث خاص حيث يشارك الأطفال من جميع أنحاء العالم تقاليدهم. يسألك أحد الأطفال عن تقليد فريد من بلدك. كيف ستشرحه بطريقة يمكنه فهمها؟
    """)

    answer_q1 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would explain the tradition by telling a story about how it started | سأشرح التقليد عن طريق رواية قصة حول كيفية بدايته.",
            "I would show them pictures or videos to help them visualize it | سأريهم صورًا أو مقاطع فيديو لمساعدتهم على تصوره.",
            "I would invite them to try the tradition with me so they can experience it | سأدعوهم لتجربة التقليد معي حتى يتمكنوا من تجربته بأنفسهم."
        )
    )

    # Scenario 2
    st.markdown("""
    #### **Scenario 2 | السيناريو الثاني:**
    You’re part of a team working to solve a global issue like pollution or hunger. Each team member is from a different country and has a different idea of what should be done. How do you help the team agree on the best solution?

    أنت جزء من فريق يعمل على حل مشكلة عالمية مثل التلوث أو الجوع. كل عضو في الفريق من بلد مختلف ولديه فكرة مختلفة حول ما يجب فعله. كيف ستساعد الفريق على الاتفاق على الحل الأفضل؟
    """)

    answer_q2 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would suggest combining ideas to create a solution that works for everyone | سأقترح دمج الأفكار لإنشاء حل يناسب الجميع.",
            "I would encourage everyone to explain their ideas and listen to each other | سأشجع الجميع على شرح أفكارهم والاستماع إلى بعضهم البعض.",
            "I would suggest voting on the idea that seems the most effective | سأقترح التصويت على الفكرة التي تبدو الأكثر فعالية."
        )
    )

    # Scenario 3
    st.markdown("""
    #### **Scenario 3 | السيناريو الثالث:**
    You’ve discovered a new island, and people from different cultures are moving there to start a new community. You’ve been asked to help decide what rules should be in place to make sure everyone feels respected. What rules would you suggest?

    لقد اكتشفت جزيرة جديدة، والناس من ثقافات مختلفة ينتقلون إليها لبدء مجتمع جديد. طُلب منك المساعدة في تحديد القواعد التي يجب أن تكون موجودة لضمان شعور الجميع بالاحترام. ما هي القواعد التي ستقترحها؟
    """)

    answer_q3 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would suggest that everyone shares their traditions and learns from each other | سأقترح أن يشارك الجميع تقاليدهم ويتعلمون من بعضهم البعض.",
            "I would make sure that everyone has a say in the decisions that affect the community | سأضمن أن يكون للجميع رأي في القرارات التي تؤثر على المجتمع.",
            "I would create a rule that everyone helps to take care of the island and the environment | سأضع قاعدة بأن على الجميع المساعدة في رعاية الجزيرة والبيئة."
        )
    )

    # Scenario 4
    st.markdown("""
    #### **Scenario 4 | السيناريو الرابع:**
    You’ve been given the chance to talk to world leaders about protecting the environment. You want to inspire them to take action. What message would you share with them?

    تم منحك الفرصة للتحدث إلى قادة العالم حول حماية البيئة. تريد إلهامهم لاتخاذ الإجراءات. ما هي الرسالة التي ستشاركها معهم؟
    """)

    answer_q4 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would remind them that protecting the environment means protecting our future | سأذكرهم بأن حماية البيئة تعني حماية مستقبلنا.",
            "I would share stories of how the environment is important to people around the world | سأشارك قصصًا حول أهمية البيئة للناس في جميع أنحاء العالم.",
            "I would encourage them to think about the impact their decisions have on future generations | سأشجعهم على التفكير في تأثير قراراتهم على الأجيال القادمة."
        )
    )

    # Scenario 5
    st.markdown("""
    #### **Scenario 5 | السيناريو الخامس:**
    You’re organizing a festival to celebrate different cultures from around the world. Each part of the festival will feature something special from a different culture—food, music, games, or art. How do you make sure everyone feels included?

    أنت تنظم مهرجانًا للاحتفال بالثقافات المختلفة من جميع أنحاء العالم. سيشمل كل جزء من المهرجان شيئًا خاصًا من ثقافة مختلفة—طعامًا أو موسيقى أو ألعابًا أو فنًا. كيف ستتأكد من أن الجميع يشعرون بأنهم مشمولون؟
    """)

    answer_q5 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would ask people from each culture to help plan their part of the festival | سأطلب من الناس من كل ثقافة المساعدة في تخطيط الجزء الخاص بهم من المهرجان.",
            "I would make sure that each culture’s traditions are represented equally | سأحرص على تمثيل تقاليد كل ثقافة بشكل متساوٍ.",
            "I would create activities where people can learn about and participate in other cultures | سأبتكر أنشطة يمكن للناس من خلالها تعلم والمشاركة في ثقافات أخرى."
        )
    )

    # Submit Button
    if st.button("Submit | إرسال"):
        st.markdown("### **Thank you for completing the Global Citizenship Assessment! | شكرًا لك على إكمال تقييم المواطنة العالمية!**")
        st.markdown("""
        Based on your answers, you will receive feedback on your global citizenship skills:
        
        - If you focused on understanding and respecting other cultures, it shows you're a thoughtful and open-minded global citizen.
        - Helping others work together and make decisions shows you’re a responsible and inclusive leader in a global community.

        بناءً على إجاباتك، ستحصل على ملاحظات حول مهاراتك في المواطنة العالمية:

        - إذا ركزت على فهم واحترام الثقافات الأخرى، فهذا يظهر أنك مواطن عالمي مدروس ومنفتح الذهن.
        - مساعدة الآخرين على العمل معًا واتخاذ القرارات يظهر أنك قائد مسؤول وشامل في المجتمع العالمي.
        """)

        # Additional personalized messages could be added depending on the rubric system.
