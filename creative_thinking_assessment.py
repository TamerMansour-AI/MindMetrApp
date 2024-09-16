import streamlit as st

def creative_thinking_assessment():
    st.title("Creative Thinking (التفكير الإبداعي) Assessment")
    
    # Introduction for the child (bilingual)
    st.markdown("""
    ### **Welcome to the Creative Thinking Assessment | مرحبًا بكم في تقييم التفكير الإبداعي**
    
    In this assessment, you'll use your imagination and creativity to solve fun and unique challenges. There are no limits to what you can come up with—let your creativity flow!

    في هذا التقييم، ستستخدم خيالك وإبداعك لحل تحديات ممتعة وفريدة. لا حدود لما يمكنك ابتكاره - دع إبداعك يتدفق!
    """)

    # Scenario 1
    st.markdown("""
    #### **Scenario 1 | السيناريو الأول:**
    You find a magical paintbrush that can bring anything you draw to life. You have to paint something that will help you explore a mysterious island. What do you paint?

    تجد فرشاة سحرية يمكنها إحياء أي شيء ترسمه. عليك أن ترسم شيئًا لمساعدتك في استكشاف جزيرة غامضة. ماذا سترسم؟
    """)

    answer_q1 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would paint a flying ship to explore the island from the sky | سأرسم سفينة طائرة لاستكشاف الجزيرة من السماء.",
            "I would paint a map that shows all the hidden secrets of the island | سأرسم خريطة تظهر جميع الأسرار المخفية للجزيرة.",
            "I would paint an animal companion to help me on my adventure | سأرسم رفيقًا حيوانيًا لمساعدتي في مغامرتي."
        )
    )

    # Scenario 2
    st.markdown("""
    #### **Scenario 2 | السيناريو الثاني:**
    You're in charge of designing a playground for a group of robots. The robots can do anything: jump, fly, or even swim through the air! What kind of playground do you create for them?

    أنت مسؤول عن تصميم ملعب لمجموعة من الروبوتات. الروبوتات يمكنها فعل أي شيء: القفز، الطيران، أو حتى السباحة في الهواء! ما نوع الملعب الذي ستصممه لهم؟
    """)

    answer_q2 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would create a playground with floating platforms and flying obstacle courses | سأصمم ملعبًا به منصات عائمة ودورات عقبات طائرة.",
            "I would design a space with pools of air where they can swim and glide | سأصمم مساحة بها برك هوائية يمكنهم السباحة والانزلاق فيها.",
            "I would create a playground where they can shape-shift into different forms | سأصمم ملعبًا يمكنهم فيه تغيير أشكالهم."
        )
    )

    # Scenario 3
    st.markdown("""
    #### **Scenario 3 | السيناريو الثالث:**
    You've been given a special pen that can draw anything into existence. The challenge is to create a new toy that’s never been seen before. What toy do you design?

    تم إعطاؤك قلمًا خاصًا يمكنه رسم أي شيء ليصبح حقيقيًا. التحدي هو ابتكار لعبة جديدة لم تُرَ من قبل. ما هي اللعبة التي ستصممها؟
    """)

    answer_q3 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would design a toy that can change colors and shapes depending on how you play with it | سأصمم لعبة يمكنها تغيير الألوان والأشكال بناءً على كيفية اللعب بها.",
            "I would create a toy that can float and move around on its own | سأبتكر لعبة يمكنها الطفو والتحرك من تلقاء نفسها.",
            "I would design a toy that tells stories when you press its buttons | سأصمم لعبة تروي قصصًا عندما تضغط على أزرارها."
        )
    )

    # Scenario 4
    st.markdown("""
    #### **Scenario 4 | السيناريو الرابع:**
    You discover a room where the walls change into any scene you can imagine. You can choose one scene to bring to life and explore. What do you create?

    تكتشف غرفة حيث يمكن للجدران أن تتحول إلى أي مشهد يمكنك تخيله. يمكنك اختيار مشهد واحد لإحيائه واستكشافه. ماذا ستخلق؟
    """)

    answer_q4 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would create a jungle with talking animals and glowing plants | سأخلق غابة بها حيوانات تتحدث ونباتات متوهجة.",
            "I would design an underwater world with magical sea creatures | سأصمم عالمًا تحت الماء به مخلوقات بحرية سحرية.",
            "I would turn the room into a futuristic city with robots and flying cars | سأحول الغرفة إلى مدينة مستقبلية بها روبوتات وسيارات طائرة."
        )
    )

    # Scenario 5
    st.markdown("""
    #### **Scenario 5 | السيناريو الخامس:**
    You've been asked to invent a new holiday that everyone will celebrate. What is the holiday about, and how do people celebrate it?

    طُلب منك ابتكار عطلة جديدة يحتفل بها الجميع. ما موضوع العطلة وكيف سيحتفل الناس بها؟
    """)

    answer_q5 = st.radio(
        "Choose an option | اختر خيارًا:",
        (
            "I would create a day where people build giant sculptures out of recycled materials | سأبتكر يومًا يقوم فيه الناس ببناء منحوتات عملاقة من المواد المعاد تدويرها.",
            "I would invent a holiday where people dress up as their favorite animals and have parades | سأبتكر عطلة يرتدي فيها الناس ملابس حيواناتهم المفضلة ويقيمون مواكب.",
            "I would create a day where people exchange stories and celebrate creativity through art | سأبتكر يومًا يتبادل فيه الناس القصص ويحتفلون بالإبداع من خلال الفن."
        )
    )

    # Submit Button
    if st.button("Submit | إرسال"):
        st.markdown("### **Thank you for completing the Creative Thinking Assessment! | شكرًا لك على إكمال تقييم التفكير الإبداعي!**")
        st.markdown("""
        Based on your answers, you will receive feedback on your creative thinking skills:
        
        - If you like to come up with unique ideas, it shows you're imaginative and love exploring new possibilities.
        - Designing fun and engaging worlds shows you’re a visionary with a lot of creativity to share.

        بناءً على إجاباتك، ستحصل على ملاحظات حول مهاراتك في التفكير الإبداعي:

        - إذا كنت تحب ابتكار أفكار فريدة، فهذا يظهر أنك شخص ذو خيال واسع وتحب استكشاف إمكانيات جديدة.
        - تصميم عوالم ممتعة وجذابة يظهر أنك صاحب رؤية ولديك الكثير من الإبداع لتشاركه.
        """)

        # Additional personalized messages could be added depending on the rubric system.
