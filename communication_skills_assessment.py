import streamlit as st

def communication_skills_assessment():
    st.title("Communication Skills (مهارات التواصل) Assessment")
    
    # Introduction for the child (bilingual)
    st.markdown("""
    ### **Welcome to the Communication Skills Assessment | مرحبًا بكم في تقييم مهارات التواصل**
    
    In this assessment, you'll face fun and interesting situations where you can practice how you communicate with others. The goal is to see how you express your ideas and understand others.

    في هذا التقييم، ستواجه مواقف ممتعة ومثيرة حيث يمكنك ممارسة كيفية تواصلك مع الآخرين. الهدف هو معرفة كيف تعبر عن أفكارك وتفهم الآخرين.
    """)

    # Scenario 1
    st.markdown("""
    #### **Scenario 1 | السيناريو الأول:**
    You’re in charge of explaining a complicated game to a group of younger children. The rules are a bit tricky, and you don’t want them to feel confused. How do you explain the game?

    أنت مسؤول عن شرح لعبة معقدة لمجموعة من الأطفال الصغار. القواعد صعبة بعض الشيء، ولا تريد أن يشعروا بالارتباك. كيف ستشرح اللعبة؟
    """)

    answer_q1 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would explain the rules step by step and make sure they understand each part | سأشرح القواعد خطوة بخطوة وأتأكد من فهمهم لكل جزء.",
            "I would use simple words and examples to make it easy to understand | سأستخدم كلمات بسيطة وأمثلة لجعلها سهلة الفهم.",
            "I would show them how to play by demonstrating the game | سأريهم كيفية اللعب عن طريق عرض اللعبة."
        )
    )

    # Scenario 2
    st.markdown("""
    #### **Scenario 2 | السيناريو الثاني:**
    You’re writing a letter to a friend who lives far away. You want to tell them about something exciting that happened at school, but you also want to make sure they feel connected to your experience. How do you write the letter?

    أنت تكتب رسالة إلى صديق يعيش بعيدًا. تريد أن تخبره عن شيء مثير حدث في المدرسة، لكنك أيضًا تريد التأكد من أنه يشعر بالتواصل مع تجربتك. كيف ستكتب الرسالة؟
    """)

    answer_q2 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would describe what happened in detail so they can imagine it clearly | سأصف ما حدث بالتفصيل حتى يتمكن من تخيله بوضوح.",
            "I would tell them how I felt during the event to make it more personal | سأخبره كيف شعرت خلال الحدث لجعله أكثر شخصية.",
            "I would include some questions about their life to make the conversation go both ways | سأطرح بعض الأسئلة حول حياتهم لجعل المحادثة تسير في كلا الاتجاهين."
        )
    )

    # Scenario 3
    st.markdown("""
    #### **Scenario 3 | السيناريو الثالث:**
    You’re part of a team project, and everyone has different ideas on how to complete it. The group is getting stuck because no one can agree. How do you help the team communicate better?

    أنت جزء من مشروع جماعي، وكل شخص لديه أفكار مختلفة حول كيفية إنجازه. الفريق يواجه صعوبة لأن لا أحد يستطيع الاتفاق. كيف ستساعد الفريق على التواصل بشكل أفضل؟
    """)

    answer_q3 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would ask everyone to share their ideas one by one and listen carefully | سأطلب من الجميع مشاركة أفكارهم واحدًا تلو الآخر وأستمع بعناية.",
            "I would suggest combining ideas to find a middle ground that works for everyone | سأقترح دمج الأفكار للعثور على حل وسط يناسب الجميع.",
            "I would help the group focus on the main goal and remind them to stay calm | سأساعد المجموعة على التركيز على الهدف الرئيسي وأذكرهم بالحفاظ على الهدوء."
        )
    )

    # Scenario 4
    st.markdown("""
    #### **Scenario 4 | السيناريو الرابع:**
    You’re telling a story to your classmates, but you notice that some of them are losing interest. How do you make sure everyone stays engaged and interested in your story?

    أنت تروي قصة لزملائك في الصف، لكنك تلاحظ أن بعضهم يفقد الاهتمام. كيف ستتأكد من أن الجميع يظل مندمجًا ومهتمًا بقصتك؟
    """)

    answer_q4 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would add exciting details to make the story more interesting | سأضيف تفاصيل مثيرة لجعل القصة أكثر تشويقًا.",
            "I would ask questions to involve the listeners and make them part of the story | سأطرح أسئلة لجعل المستمعين جزءًا من القصة.",
            "I would change my tone and use more expression to keep them engaged | سأغير نبرتي وأستخدم المزيد من التعبير لإبقاءهم مندمجين."
        )
    )

    # Scenario 5
    st.markdown
