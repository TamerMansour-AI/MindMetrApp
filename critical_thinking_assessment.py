import streamlit as st

def critical_thinking_assessment():
    st.title("Critical Thinking (التفكير النقدي) Assessment")
    
    # Introduction for the child (bilingual)
    st.markdown("""
    ### **Welcome to the Critical Thinking Assessment | مرحبًا بكم في تقييم التفكير النقدي**
    
    In this assessment, you'll be faced with puzzles and scenarios that will test how you analyze situations, think logically, and make decisions. Remember, there are no right or wrong answers—just choose what you think is the best solution!

    في هذا التقييم، ستواجه ألغازًا وسيناريوهات تختبر كيفية تحليلك للمواقف وتفكيرك المنطقي واتخاذك للقرارات. تذكر، لا توجد إجابات صحيحة أو خاطئة - فقط اختر ما تعتقد أنه الحل الأفضل!
    """)

    # Scenario 1
    st.markdown("""
    #### **Scenario 1 | السيناريو الأول:**
    You discover an ancient puzzle box in a hidden cave. The box has symbols on it, and a message tells you that solving the puzzle will reveal a great treasure. How do you approach solving the puzzle?

    تكتشف صندوق ألغاز قديمًا في كهف مخفي. يحتوي الصندوق على رموز، وتخبرك رسالة أن حل اللغز سيكشف عن كنز عظيم. كيف ستقترب من حل اللغز؟
    """)

    answer_q1 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would look for patterns in the symbols to solve it logically | سأبحث عن أنماط في الرموز لحلها بطريقة منطقية.",
            "I would try turning the symbols one by one and see what happens | سأحاول تدوير الرموز واحدة تلو الأخرى لمعرفة ما سيحدث.",
            "I would search for clues in the cave that might help me understand the symbols | سأبحث عن أدلة في الكهف قد تساعدني في فهم الرموز."
        )
    )

    # Scenario 2
    st.markdown("""
    #### **Scenario 2 | السيناريو الثاني:**
    You’ve been invited to a kingdom where all the roads are mazes. You need to find your way to the castle, but each road has a different challenge. One road leads through a dark forest, another through a river with stepping stones, and the last one through a desert. How do you decide which path to take?

    تمت دعوتك إلى مملكة حيث جميع الطرق متاهات. تحتاج إلى إيجاد طريقك إلى القلعة، لكن كل طريق يحتوي على تحديات مختلفة. أحد الطرق يمر عبر غابة مظلمة، والآخر عبر نهر به حجارة عابرة، والأخير عبر صحراء. كيف ستقرر أي طريق ستسلك؟
    """)

    answer_q2 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would choose the path I think is the shortest to save time | سأختار الطريق الذي أعتقد أنه الأقصر لتوفير الوقت.",
            "I would consider my strengths—I'm good at balance, so I'd take the stepping stones | سأفكر في نقاط قوتي - أنا جيد في التوازن، لذا سأختار الحجارة العابرة.",
            "I would try to find more information before choosing a path | سأحاول العثور على المزيد من المعلومات قبل اختيار الطريق."
        )
    )

    # Scenario 3
    st.markdown("""
    #### **Scenario 3 | السيناريو الثالث:**
    You are part of a detective team trying to solve a mystery. There are three suspects, each with a different story, and one clue that doesn’t seem to fit. How do you figure out who is telling the truth?

    أنت جزء من فريق محققين يحاول حل لغز. هناك ثلاثة مشتبه بهم، ولكل منهم قصة مختلفة، وهنالك دليل واحد لا يبدو منطقيًا. كيف ستكتشف من يقول الحقيقة؟
    """)

    answer_q3 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would compare their stories and look for inconsistencies | سأقارن بين قصصهم وأبحث عن التناقضات.",
            "I would ask more questions to see who seems the most nervous | سأطرح المزيد من الأسئلة لمعرفة من يبدو أكثر توترًا.",
            "I would focus on the clue and see how it fits with each story | سأركز على الدليل وأرى كيف يتناسب مع كل قصة."
        )
    )

    # Scenario 4
    st.markdown("""
    #### **Scenario 4 | السيناريو الرابع:**
    You are tasked with building a bridge over a river, but you only have limited materials: some wood, a few ropes, and a handful of stones. What is your plan to build the bridge?

    طُلب منك بناء جسر فوق نهر، لكن لديك مواد محدودة: بعض الخشب، بضع حبال، وكمية من الحجارة. ما هي خطتك لبناء الجسر؟
    """)

    answer_q4 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would use the stones to create a foundation and build the bridge with wood and ropes | سأستخدم الحجارة لإنشاء الأساس وأبني الجسر بالخشب والحبال.",
            "I would design a rope bridge and save the wood for support | سأصمم جسرًا من الحبال وأحتفظ بالخشب للدعم.",
            "I would experiment with different combinations of materials to see what works best | سأجرب تركيبات مختلفة من المواد لمعرفة ما هو الأفضل."
        )
    )

    # Scenario 5
    st.markdown("""
    #### **Scenario 5 | السيناريو الخامس:**
    You find a mysterious machine that has many buttons, but no labels. Pressing the wrong button might cause a problem, but pressing the right one could open a door to a secret lab. How do you decide which button to press?

    تجد آلة غامضة بها العديد من الأزرار، لكن لا توجد عليها علامات. الضغط على الزر الخطأ قد يتسبب في مشكلة، لكن الضغط على الزر الصحيح قد يفتح بابًا إلى مختبر سري. كيف ستقرر أي زر تضغط؟
    """)

    answer_q5 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would carefully study the buttons for any clues before pressing one | سأدرس الأزرار بعناية للبحث عن أي أدلة قبل الضغط على أحدها.",
            "I would press the one that looks the least risky | سأضغط على الزر الذي يبدو الأقل خطورة.",
            "I would test each button cautiously, one at a time | سأختبر كل زر بحذر، واحدًا تلو الآخر."
        )
    )

    # Submit Button
    if st.button("Submit | إرسال"):
        st.markdown("### **Thank you for completing the Critical Thinking Assessment! | شكرًا لك على إكمال تقييم التفكير النقدي!**")
        st.markdown("""
        Based on your answers, you will receive feedback on your critical thinking skills:
        
        - If you carefully analyzed the clues, it shows you're a logical and thoughtful problem solver.
        - Trying out different options shows you're flexible and willing to explore new ideas.

        بناءً على إجاباتك، ستحصل على ملاحظات حول مهاراتك في التفكير النقدي:

        - إذا قمت بتحليل الأدلة بعناية، فهذا يظهر أنك محلل منطقي ومفكر متأنٍ.
        - تجربة خيارات مختلفة تظهر أنك مرن ومستعد لاستكشاف أفكار جديدة.
        """)

        # Additional personalized messages could be added depending on the rubric system.
