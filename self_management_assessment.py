import streamlit as st

def self_management_assessment():
    st.title("Self-Management (إدارة الذات) Assessment")
    
    # Introduction for the child (bilingual)
    st.markdown("""
    ### **Welcome to the Self-Management Assessment | مرحبًا بكم في تقييم إدارة الذات**
    
    In this adventure, you'll face challenges that test how well you manage your time, goals, and emotions. There are no right or wrong answers—just choose what you feel would be the best way to handle each situation!

    في هذه المغامرة، ستواجه تحديات تختبر مدى قدرتك على إدارة وقتك وأهدافك وعواطفك. لا توجد إجابات صحيحة أو خاطئة - فقط اختر ما تشعر أنه أفضل طريقة للتعامل مع كل موقف!
    """)

    # Scenario 1
    st.markdown("""
    #### **Scenario 1 | السيناريو الأول:**
    You are an explorer on a mission to find a hidden treasure. Along the way, you find a map, but it’s torn into three pieces. How do you manage your time to put the pieces together and continue your journey?

    أنت مستكشف في مهمة للعثور على كنز مخفي. على طول الطريق، تجد خريطة، لكنها ممزقة إلى ثلاث قطع. كيف ستدير وقتك لتجميع القطع ومواصلة رحلتك؟
    """)

    answer_q1 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would take my time to carefully match the pieces before moving forward | سأستغرق وقتي بعناية لمطابقة القطع قبل المضي قدمًا.",
            "I would try to fit the pieces together as quickly as possible to save time | سأحاول تجميع القطع بأسرع ما يمكن لتوفير الوقت.",
            "I would ask for help from my teammates to solve the puzzle faster | سأطلب المساعدة من زملائي لحل اللغز بسرعة."
        )
    )

    # Scenario 2
    st.markdown("""
    #### **Scenario 2 | السيناريو الثاني:**
    You’re the leader of a team building a giant robot to help defend your city. But suddenly, you realize that you’re running out of materials and time. How do you stay calm and lead your team to finish the robot?

    أنت قائد فريق يبني روبوتًا عملاقًا للمساعدة في الدفاع عن مدينتك. ولكن فجأة، تدرك أنك نفدت منك المواد والوقت. كيف ستحافظ على هدوئك وتقود فريقك لإنهاء الروبوت؟
    """)

    answer_q2 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would divide the remaining work into smaller steps and keep the team focused | سأقسم العمل المتبقي إلى خطوات أصغر وأبقي الفريق مركزًا.",
            "I would think about creative ways to use fewer materials and still finish on time | سأفكر في طرق إبداعية لاستخدام مواد أقل والانتهاء في الوقت المحدد.",
            "I would encourage my team to stay positive and work faster without stressing | سأشجع فريقي على البقاء إيجابيًا والعمل بسرعة دون ضغط."
        )
    )

    # Scenario 3
    st.markdown("""
    #### **Scenario 3 | السيناريو الثالث:**
    You’ve set a personal goal to read five books by the end of the month, but now you’re feeling distracted with other fun activities. How do you stay on track and reach your goal?

    لقد وضعت هدفًا شخصيًا لقراءة خمسة كتب بحلول نهاية الشهر، لكنك الآن تشعر بالتشتت بسبب أنشطة أخرى ممتعة. كيف ستبقى على المسار الصحيح وتحقق هدفك؟
    """)

    answer_q3 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would make a schedule for when to read and when to do other activities | سأضع جدولًا زمنيًا للقراءة والأنشطة الأخرى.",
            "I would remind myself of why I set the goal in the first place | سأذكر نفسي لماذا وضعت الهدف في المقام الأول.",
            "I would balance my time by reading a little every day while still having fun | سأوازن وقتي من خلال القراءة قليلاً كل يوم مع الاستمتاع بالأنشطة."
        )
    )

    # Scenario 4
    st.markdown("""
    #### **Scenario 4 | السيناريو الرابع:**
    You’re training for a big race in a fantasy world, but you start to feel tired and lose motivation halfway through. What do you do to keep going and finish the race?

    أنت تتدرب لسباق كبير في عالم خيالي، لكنك بدأت تشعر بالتعب وفقدان الحافز في منتصف الطريق. ماذا ستفعل لتستمر وتنهي السباق؟
    """)

    answer_q4 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would take a short break to rest and then keep going | سأخذ استراحة قصيرة للراحة ثم أستمر.",
            "I would focus on reaching small milestones instead of thinking about the whole race | سأركز على تحقيق أهداف صغيرة بدلاً من التفكير في السباق بأكمله.",
            "I would think about how great it will feel when I cross the finish line | سأفكر في مدى روعة الشعور عندما أعبر خط النهاية."
        )
    )

    # Scenario 5
    st.markdown("""
    #### **Scenario 5 | السيناريو الخامس:**
    You’re working on a secret project, but you keep getting interrupted by messages from friends. How do you manage your time and stay focused?

    أنت تعمل على مشروع سري، لكنك تستمر في تلقي رسائل من الأصدقاء تقاطعك. كيف ستدير وقتك وتبقى مركزًا؟
    """)

    answer_q5 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would set my device to 'Do Not Disturb' mode until I finish the project | سأضع جهازي في وضع 'عدم الإزعاج' حتى أنتهي من المشروع.",
            "I would set specific times to check messages and stay focused in between | سأحدد أوقاتًا معينة للتحقق من الرسائل وأبقى مركزًا بين تلك الأوقات.",
            "I would let my friends know I’m busy and will reply later | سأخبر أصدقائي أنني مشغول وسأرد لاحقًا."
        )
    )

    # Submit Button
    if st.button("Submit | إرسال"):
        st.markdown("### **Thank you for completing the Self-Management Assessment! | شكرًا لك على إكمال تقييم إدارة الذات!**")
        st.markdown("""
        Based on your answers, you will receive feedback on your self-management skills:
        
        - If you planned your time wisely, it shows you're good at managing your tasks and staying focused.
        - Keeping calm and motivated in difficult situations shows you have strong emotional control and perseverance.

        بناءً على إجاباتك، ستحصل على ملاحظات حول مهاراتك في إدارة الذات:

        - إذا كنت قد خططت وقتك بحكمة، فهذا يظهر أنك جيد في إدارة مهامك والبقاء مركزًا.
        - الحفاظ على الهدوء والتحفيز في المواقف الصعبة يظهر أن لديك سيطرة قوية على عواطفك وقدرة على المثابرة.
        """)

        # Additional personalized messages could be added depending on the rubric system.
