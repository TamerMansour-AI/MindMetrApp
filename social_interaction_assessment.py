import streamlit as st

def social_interaction_assessment():
    st.title("Social Interaction (التفاعل الاجتماعي) Assessment")
    
    # Introduction for the child (bilingual)
    st.markdown("""
    ### **Welcome to the Social Interaction Assessment | مرحبًا بكم في تقييم التفاعل الاجتماعي**
    
    In this adventure, you will face some exciting challenges that will test how you interact with others in magical and real-world situations. Remember, there are no right or wrong answers—just choose what feels right to you!

    في هذه المغامرة، ستواجه بعض التحديات المثيرة التي ستختبر كيفية تفاعلك مع الآخرين في مواقف سحرية وحقيقية. تذكر، لا توجد إجابات صحيحة أو خاطئة - فقط اختر ما تشعر أنه صحيح لك!
    """)

    # Scenario 1
    st.markdown("""
    #### **Scenario 1 | السيناريو الأول:**
    You are the captain of a spaceship exploring a distant planet. One of your crew members is nervous about an upcoming mission because they’ve never done it before. How do you help them feel confident?

    أنت قائد سفينة فضائية تستكشف كوكبًا بعيدًا. أحد أعضاء فريقك يشعر بالتوتر بشأن مهمة قادمة لأنه لم يقم بها من قبل. كيف ستساعدهم على الشعور بالثقة؟
    """)

    answer_q1 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would remind them of their past successes and offer to guide them | سأذكرهم بنجاحاتهم السابقة وأعرض مساعدتي.",
            "I would organize a quick training session with the team | سأقوم بتنظيم جلسة تدريب سريعة مع الفريق.",
            "I would encourage them to trust themselves and go for it | سأشجعهم على الثقة بأنفسهم والقيام بالمهمة."
        )
    )

    # Scenario 2
    st.markdown("""
    #### **Scenario 2 | السيناريو الثاني:**
    You’ve been invited to a secret party hosted by talking animals in a magical forest. A friendly fox invites you to join their dance circle, but one of the rabbits seems too shy to dance. What do you do?

    لقد تمت دعوتك إلى حفلة سرية تستضيفها حيوانات ناطقة في غابة سحرية. يدعوك ثعلب ودود للانضمام إلى دائرة الرقص، لكن أحد الأرانب يبدو خجولاً جدًا للرقص. ماذا ستفعل؟
    """)

    answer_q2 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would ask the rabbit if they’d like to dance with me | سأطلب من الأرنب أن يرقص معي.",
            "I would encourage the rabbit by dancing extra silly to make them laugh | سأشجع الأرنب بالرقص بطريقة مضحكة ليضحك.",
            "I would let the rabbit watch until they feel ready to join | سأترك الأرنب يشاهد حتى يشعر بأنه مستعد للانضمام."
        )
    )

    # Scenario 3
    st.markdown("""
    #### **Scenario 3 | السيناريو الثالث:**
    While traveling through an enchanted city, you meet a group of characters from different worlds. Some of them have trouble understanding each other because they speak different languages. How do you help them communicate?

    أثناء سفرك في مدينة مسحورة، تقابل مجموعة من الشخصيات من عوالم مختلفة. بعضهم يجد صعوبة في فهم بعضهم البعض لأنهم يتحدثون لغات مختلفة. كيف ستساعدهم على التواصل؟
    """)

    answer_q3 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would use gestures and drawings to help everyone understand each other | سأستخدم الإيماءات والرسومات لمساعدة الجميع على فهم بعضهم البعض.",
            "I would teach them some simple words from each language | سأعلمهم بعض الكلمات البسيطة من كل لغة.",
            "I would create a magical translation spell to help them communicate | سأصنع تعويذة ترجمة سحرية لمساعدتهم على التواصل."
        )
    )

    # Scenario 4
    st.markdown("""
    #### **Scenario 4 | السيناريو الرابع:**
    You are part of a team of explorers searching for a legendary treasure. Everyone has different ideas about where to go next, and the group is getting frustrated. How do you help them decide?

    أنت جزء من فريق من المستكشفين يبحثون عن كنز أسطوري. كل شخص لديه أفكار مختلفة حول المكان الذي يجب الذهاب إليه بعد ذلك، والفريق يشعر بالإحباط. كيف ستساعدهم على اتخاذ القرار؟
    """)

    answer_q4 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would suggest listening to everyone’s ideas and voting on the best one | سأقترح الاستماع إلى أفكار الجميع والتصويت على الفكرة الأفضل.",
            "I would suggest splitting into smaller teams to explore different paths | سأقترح تقسيم الفريق إلى مجموعات صغيرة لاستكشاف مسارات مختلفة.",
            "I would try combining ideas to come up with a new plan that makes everyone happy | سأحاول دمج الأفكار للتوصل إلى خطة جديدة تجعل الجميع سعداء."
        )
    )

    # Scenario 5
    st.markdown("""
    #### **Scenario 5 | السيناريو الخامس:**
    You’re in a land where everyone has a unique superpower. A new friend of yours has a power they feel embarrassed about because it’s different from others. How do you help them feel proud of their unique ability?

    أنت في أرض حيث لكل شخص قوة خارقة فريدة. صديقك الجديد لديه قوة يشعر بالإحراج منها لأنها مختلفة عن الآخرين. كيف ستساعدهم على الشعور بالفخر بقدرتهم الفريدة؟
    """)

    answer_q5 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would show them how their power can be useful in unexpected ways | سأريهم كيف يمكن أن تكون قوتهم مفيدة بطرق غير متوقعة.",
            "I would tell them that everyone’s power is special in its own way | سأخبرهم أن قوة كل شخص مميزة بطريقتها الخاصة.",
            "I would ask them to use their power in a fun challenge with me | سأطلب منهم استخدام قوتهم في تحدٍ ممتع معي."
        )
    )

    # Submit Button
    if st.button("Submit | إرسال"):
        st.markdown("### **Thank you for completing the Social Interaction Assessment! | شكرًا لك على إكمال تقييم التفاعل الاجتماعي!**")
        st.markdown("""
        Based on your answers, you will receive feedback on your social interaction skills:
        
        - If you helped others feel confident or included, it shows you are caring and supportive.
        - Solving conflicts and finding creative solutions means you are a great communicator and leader.

        بناءً على إجاباتك، ستحصل على ملاحظات حول مهاراتك في التفاعل الاجتماعي:

        - إذا ساعدت الآخرين على الشعور بالثقة أو المشاركة، فهذا يظهر أنك شخص داعم وتهتم بالآخرين.
        - حل النزاعات وابتكار حلول إبداعية يعني أنك متواصل جيد وقائد عظيم.
        """)

        # Additional personalized messages could be added depending on the rubric system.
