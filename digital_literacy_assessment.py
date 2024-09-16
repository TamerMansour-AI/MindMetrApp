import streamlit as st

def digital_literacy_assessment():
    st.title("Digital Literacy (المهارات الرقمية) Assessment")
    
    # Introduction for the child (bilingual)
    st.markdown("""
    ### **Welcome to the Digital Literacy Assessment | مرحبًا بكم في تقييم المهارات الرقمية**
    
    In this adventure, you'll face challenges where you can use your digital skills to solve problems in fun, imaginative ways. You’re in control, and there are no right or wrong answers—just use your digital wisdom!

    في هذه المغامرة، ستواجه تحديات يمكنك من خلالها استخدام مهاراتك الرقمية لحل المشكلات بطرق ممتعة وخيالية. أنت القائد، ولا توجد إجابات صحيحة أو خاطئة - فقط استخدم حكمتك الرقمية!
    """)

    # Scenario 1
    st.markdown("""
    #### **Scenario 1 | السيناريو الأول:**
    You are the captain of a futuristic spaceship, and your ship’s computer gets hacked by a mysterious signal. To protect your crew, you need to stop the signal. What do you do?

    أنت قائد سفينة فضائية مستقبلية، وقد تعرض الكمبيوتر الخاص بسفينتك للاختراق بواسطة إشارة غامضة. لحماية طاقمك، تحتاج إلى إيقاف الإشارة. ماذا ستفعل؟
    """)

    answer_q1 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would block the signal using my ship's firewall | سأحجب الإشارة باستخدام جدار الحماية الخاص بسفينتي.",
            "I would trace the signal to find where it’s coming from | سأتعقب الإشارة لمعرفة مصدرها.",
            "I would send a counter-signal to confuse the hacker | سأرسل إشارة مضادة لإرباك المخترق."
        )
    )

    # Scenario 2
    st.markdown("""
    #### **Scenario 2 | السيناريو الثاني:**
    You've been transported into a virtual reality city, but the city is being overrun by a virus that turns buildings into giant glitching cubes. You need to find the antivirus to save the city. How do you find it?

    تم نقلك إلى مدينة واقع افتراضي، لكن المدينة تغزوها فيروسات تحول المباني إلى مكعبات متقطعة عملاقة. تحتاج إلى العثور على مضاد الفيروسات لإنقاذ المدينة. كيف ستجده؟
    """)

    answer_q2 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would search the city’s data archives for clues | سأبحث في أرشيف بيانات المدينة عن أدلة.",
            "I would hack into the virus to learn how it works | سأخترق الفيروس لأفهم كيف يعمل.",
            "I would create a virtual tool to track the source of the virus | سأبتكر أداة افتراضية لتتبع مصدر الفيروس."
        )
    )

    # Scenario 3
    st.markdown("""
    #### **Scenario 3 | السيناريو الثالث:**
    You’ve entered a competition where robots have to complete tasks in the digital world. To make your robot the fastest, you can upgrade it with one special digital ability. What ability do you give it?

    لقد دخلت في مسابقة حيث يجب على الروبوتات إكمال المهام في العالم الرقمي. لجعل روبوتك الأسرع، يمكنك ترقيته بقدرة رقمية خاصة واحدة. ما هي القدرة التي ستمنحها له؟
    """)

    answer_q3 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would give it super speed coding to solve problems instantly | سأمنحه قدرة البرمجة الفائقة لحل المشكلات فورًا.",
            "I would give it the ability to predict the next challenge before it happens | سأمنحه القدرة على توقع التحدي القادم قبل حدوثه.",
            "I would give it the ability to transform into any tool it needs | سأمنحه القدرة على التحول إلى أي أداة يحتاجها."
        )
    )

    # Scenario 4
    st.markdown("""
    #### **Scenario 4 | السيناريو الرابع:**
    You’ve been tasked with designing an app for an underwater city where the citizens are sea creatures! The app needs to help them connect and share important information. What’s the most important feature of your app?

    تم تكليفك بتصميم تطبيق لمدينة تحت الماء حيث يكون المواطنون من المخلوقات البحرية! يجب أن يساعد التطبيق في التواصل وتبادل المعلومات الهامة. ما هو أهم ميزة في تطبيقك؟
    """)

    answer_q4 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would add a translation feature so different species can communicate | سأضيف ميزة الترجمة حتى يتمكن الأنواع المختلفة من التواصل.",
            "I would design a visual map to help them find food sources and safe zones | سأصمم خريطة مرئية لمساعدتهم على العثور على مصادر الطعام والمناطق الآمنة.",
            "I would create a feature where they can share real-time water conditions | سأبتكر ميزة تمكنهم من مشاركة حالة المياه في الوقت الحقيقي."
        )
    )

    # Scenario 5
    st.markdown("""
    #### **Scenario 5 | السيناريو الخامس:**
    You’re competing in a digital race where the track changes every few seconds! You need to think fast and adapt to new challenges. How do you make sure you always stay ahead?

    أنت تتنافس في سباق رقمي حيث يتغير المسار كل بضع ثوان! تحتاج إلى التفكير بسرعة والتكيف مع التحديات الجديدة. كيف ستتأكد من أنك تظل متقدمًا دائمًا؟
    """)

    answer_q5 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would design a smart AI that can predict the next part of the track | سأصمم ذكاءً اصطناعيًا ذكيًا يمكنه توقع الجزء التالي من المسار.",
            "I would build a digital vehicle that adapts to any type of track instantly | سأبني مركبة رقمية تتكيف مع أي نوع من المسارات على الفور.",
            "I would connect my brain to the track to react faster than anyone else | سأربط عقلي بالمسار للتفاعل أسرع من أي شخص آخر."
        )
    )

    # Submit Button
    if st.button("Submit | إرسال"):
        st.markdown("### **Thank you for completing the Digital Literacy Assessment! | شكرًا لك على إكمال تقييم المهارات الرقمية!**")
        st.markdown("""
        Based on your answers, you will receive feedback on your digital literacy skills:
        
        - If you thought creatively and adapted to new challenges, it shows you're quick-thinking and skilled at problem-solving in the digital world.
        - Making smart decisions about how to use digital tools shows you're responsible and capable in the digital space.

        بناءً على إجاباتك، ستحصل على ملاحظات حول مهاراتك الرقمية:

        - إذا كنت تفكر بشكل إبداعي وتتكيف مع التحديات الجديدة، فهذا يظهر أنك سريع التفكير وماهر في حل المشكلات في العالم الرقمي.
        - اتخاذ قرارات ذكية حول كيفية استخدام الأدوات الرقمية يظهر أنك مسؤول وقادر في الفضاء الرقمي.
        """)

        # Additional personalized messages could be added depending on the rubric system.
