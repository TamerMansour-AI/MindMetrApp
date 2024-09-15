import streamlit as st

def cognitive_assessment():
    st.title("Cognitive Development (التطور المعرفي) Assessment")
    
    # Introduction for the child (bilingual)
    st.markdown("""
    ### **Welcome to the Cognitive Development Assessment | مرحبًا بكم في تقييم التطور المعرفي**
    
    In this assessment, you'll face creative and fun challenges that will test your thinking, imagination, and problem-solving skills. There are no right or wrong answers, so choose what feels best for you!

    في هذا التقييم، ستواجه تحديات إبداعية وممتعة لاختبار تفكيرك وخيالك وقدراتك على حل المشكلات. لا توجد إجابات صحيحة أو خاطئة، لذا اختر ما تشعر أنه الأفضل لك!
    """)

    # Scenario 1
    st.markdown("""
    #### **Scenario 1 | السيناريو الأول:**
    You discover a hidden door in your school’s library. Behind it, you find a magical forest where books can talk. One of the books tells you that to find your way back home, you need to solve a riddle. What do you do?

    تكتشف بابًا مخفيًا في مكتبة المدرسة. خلفه، تجد غابة سحرية حيث يمكن للكتب أن تتحدث. يخبرك أحد الكتب أنك بحاجة إلى حل لغز للعودة إلى المنزل. ماذا ستفعل؟
    """)

    answer_q1 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would ask the talking books for hints | سأطلب تلميحات من الكتب المتحدثة.",
            "I would try to solve the riddle myself using clues around me | سأحاول حل اللغز بنفسي باستخدام الأدلة حولي.",
            "I would look for a hidden map or guide | سأبحث عن خريطة أو دليل مخفي."
        )
    )

    # Scenario 2
    st.markdown("""
    #### **Scenario 2 | السيناريو الثاني:**
    While exploring an abandoned spaceship, you find a control panel that has 5 glowing buttons, each a different color. Pressing the right button will unlock the ship’s secret, but pressing the wrong one will make the spaceship fly away! What is your strategy?

    أثناء استكشاف سفينة فضائية مهجورة، تجد لوحة تحكم بها 5 أزرار متوهجة، كل زر بلون مختلف. الضغط على الزر الصحيح سيفتح سر السفينة، لكن الضغط على الزر الخاطئ سيجعل السفينة تطير! ما هي استراتيجيتك؟
    """)

    answer_q2 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would look for clues around the spaceship before pressing any button | سأبحث عن أدلة حول السفينة قبل الضغط على أي زر.",
            "I would test each button carefully, starting with the least risky one | سأختبر كل زر بحذر، بدءًا من الأقل خطورة.",
            "I would trust my instinct and press the button that feels right | سأثق بغرائزي وأضغط على الزر الذي يبدو صحيحًا."
        )
    )

    # Scenario 3
    st.markdown("""
    #### **Scenario 3 | السيناريو الثالث:**
    You have been transported to a world where everything is upside down. Trees grow from the sky, and fish fly in the air. To return to your world, you need to understand how this strange world works. What is your first step?

    تم نقلك إلى عالم يكون فيه كل شيء مقلوبًا. تنمو الأشجار من السماء وتطير الأسماك في الهواء. للعودة إلى عالمك، تحتاج إلى فهم كيفية عمل هذا العالم الغريب. ما هي خطوتك الأولى؟
    """)

    answer_q3 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would observe how things move and behave in this world | سأراقب كيف تتحرك الأشياء وتتصرف في هذا العالم.",
            "I would try to talk to the creatures here and ask for their help | سأحاول التحدث إلى المخلوقات هنا وطلب مساعدتهم.",
            "I would experiment with walking, jumping, or flying to learn more about the environment | سأجرب المشي أو القفز أو الطيران للتعرف على المزيد عن البيئة."
        )
    )

    # Scenario 4
    st.markdown("""
    #### **Scenario 4 | السيناريو الرابع:**
    You find a magical paintbrush that can bring anything you draw to life. You can use it to create one tool that will help you overcome a challenge you are facing. What do you draw?

    تجد فرشاة سحرية يمكنها أن تحيي أي شيء ترسمه. يمكنك استخدامها لإنشاء أداة واحدة لمساعدتك على التغلب على تحدٍ تواجهه. ماذا سترسم؟
    """)

    answer_q4 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would draw a flying vehicle to help me travel quickly | سأرسم مركبة طائرة لمساعدتي على السفر بسرعة.",
            "I would draw a magical shield to protect myself from danger | سأرسم درعًا سحريًا لحمايتي من الخطر.",
            "I would draw a smart robot to solve the challenge for me | سأرسم روبوتًا ذكيًا ليحل التحدي نيابة عني."
        )
    )

    # Scenario 5
    st.markdown("""
    #### **Scenario 5 | السيناريو الخامس:**
    You are in a land where the seasons change every hour. You need to plant a special tree that only grows when the conditions are just right. How do you make sure the tree grows?

    أنت في أرض تتغير فيها الفصول كل ساعة. تحتاج إلى زراعة شجرة خاصة تنمو فقط عندما تكون الظروف مناسبة تمامًا. كيف ستتأكد من أن الشجرة تنمو؟
    """)

    answer_q5 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would plant the tree and wait for the perfect moment | سأزرع الشجرة وأنتظر اللحظة المثالية.",
            "I would create a shelter to protect the tree from sudden weather changes | سأقوم بإنشاء ملجأ لحماية الشجرة من التغيرات المفاجئة في الطقس.",
            "I would experiment by planting multiple seeds at different times | سأجرب زراعة عدة بذور في أوقات مختلفة."
        )
    )

    # Submit Button
    if st.button("Submit | إرسال"):
        st.markdown("### **Thank you for completing the Cognitive Development Assessment! | شكرًا لك على إكمال تقييم التطور المعرفي!**")
        st.markdown("""
        Based on your answers, you will receive feedback on your cognitive skills:
        
        - If you like to experiment or explore first, it shows curiosity and a willingness to learn through trial and error.
        - Trusting your instincts or seeking help shows that you know when to act and when to collaborate.

        بناءً على إجاباتك، ستحصل على ملاحظات حول مهاراتك المعرفية:

        - إذا كنت تحب التجريب أو الاستكشاف أولاً، فهذا يظهر فضولك واستعدادك للتعلم من خلال المحاولة والخطأ.
        - الثقة بحدسك أو طلب المساعدة يظهر أنك تعرف متى تتصرف ومتى تتعاون.
        """)

        # Additional personalized messages could be added depending on the rubric system.
