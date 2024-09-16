import streamlit as st
from cognitive_assessment import cognitive_assessment
from social_interaction_assessment import social_interaction_assessment
from critical_thinking_assessment import critical_thinking_assessment
from creative_thinking_assessment import creative_thinking_assessment
from emotional_intelligence_assessment import emotional_intelligence_assessment
from communication_skills_assessment import communication_skills_assessment

# Page configuration (called only once and at the top)
st.set_page_config(
    page_title="MindMetr Child Assessment | تقييم الطفل المرتكز على العقل",
    page_icon="🧠",
    layout="wide"
)

# Main title (English and Arabic)
st.title("Welcome to MindMetr Child Assessment | مرحبًا بكم في تقييم الطفل المرتكز على العقل")

# Custom CSS for child-friendly design
st.markdown("""
    <style>
    /* Body styling: light cyan background and dark gray text for readability */
    body {
        background-color: #e6f7ff; /* Light cyan background */
        color: #333; /* Dark gray text color */
        font-family: 'Comic Sans MS', cursive, sans-serif; /* Fun, child-friendly font */
    }

    /* Main title styling */
    h1 {
        color: #ff6600; /* Bright orange for headings */
        font-size: 36px; /* Large font size */
        text-align: center; /* Center-align the title */
    }

    /* Subtitle styling */
    h2 {
        color: #33cc33; /* Bright green for subheadings */
        font-size: 28px; /* Slightly smaller than main heading */
    }

    /* Button styling */
    .stButton>button {
        background-color: #4CAF50; /* Green background for buttons */
        color: white; /* White text on buttons */
        padding: 10px 20px; /* Padding inside buttons */
        border-radius: 12px; /* Rounded button corners */
        border: none; /* Remove borders */
        font-size: 18px; /* Increase button text size */
    }

    /* Input box styling */
    .stTextInput>div>div>input {
        border: 2px solid #ff6600; /* Orange border for input boxes */
        border-radius: 8px; /* Rounded input corners */
        padding: 10px; /* Add padding inside input boxes */
        font-size: 16px; /* Increase input text size */
    }

    /* Checkbox styling */
    .stCheckbox>div>div>input {
        accent-color: #33cc33; /* Green checkboxes */
    }
    </style>
""", unsafe_allow_html=True)

# Adjust image path to relative path for cloud deployment
image_base_path = "images/"

# Display the MindMetr logo with the relative path
st.image(f"{image_base_path}logo.png", width=120)

# Main title and description (English and Arabic)
st.title("Mind-Centric Child Assessment Framework (MCAF) | إطار تقييم الطفل المرتكز على العقل (MCAF)")

# Main content for the app (Bilingual)
st.markdown("""
### **Mind-Centric Child Assessment Framework (MCAF) | إطار تقييم الطفل المرتكز على العقل**

The Mind-Centric Child Assessment Framework (MCAF) is a comprehensive tool designed to assess children's abilities across 10 developmental domains. This app allows children between the ages of 8-12 to engage with interactive scenarios and receive personalized feedback.

إطار تقييم الطفل المرتكز على العقل (MCAF) هو أداة شاملة تهدف إلى تقييم قدرات الأطفال في 10 مجالات تطويرية. يتيح هذا التطبيق للأطفال الذين تتراوح أعمارهم بين 8-12 عامًا التعامل مع سيناريوهات تفاعلية وتلقي ملاحظات مخصصة.

#### **Purpose of the MCAF | الغرض من (MCAF):**
1. **Assess multiple domains | تقييم مجالات متعددة**: The MCAF assesses children across a variety of domains including Cognitive Development, Social Interaction, Critical Thinking, Creative Thinking, Emotional Intelligence, Communication Skills, Digital Literacy, Self-Management, Leadership, and Global Citizenship.
   (يقيم MCAF الأطفال عبر مجموعة متنوعة من المجالات بما في ذلك التطور المعرفي، التفاعل الاجتماعي، التفكير النقدي، التفكير الإبداعي، الذكاء العاطفي، مهارات التواصل، الإلمام الرقمي، إدارة الذات، القيادة، والمواطنة العالمية.)

2. **Personalized Feedback | ملاحظات مخصصة**: The feedback provided encourages children to strengthen their abilities in areas they excel and improve in areas needing development.
   (تشجع الملاحظات المقدمة الأطفال على تقوية قدراتهم في المجالات التي يتفوقون فيها وتحسين المجالات التي يحتاجون فيها إلى تطوير.)

3. **Rubrics-based assessment | التقييم القائم على النماذج**: There are no true or false answers, as the assessment relies on rubrics to evaluate the child’s thinking patterns and approach.
   (لا توجد إجابات صحيحة أو خاطئة حيث يعتمد التقييم على نماذج لتقييم أنماط تفكير الطفل ونهجه.)

4. **Track progress | متابعة التقدم**: Over time, the assessment helps track a child's development and aids educators, parents, and caregivers in planning interventions.
   (يساعد التقييم مع مرور الوقت في متابعة تطور الطفل ويساعد المعلمين والآباء ومقدمي الرعاية في التخطيط للتدخلات.)

#### **How it works | كيف يعمل التقييم:**
- The child selects one of the 10 domains.
  (يختار الطفل أحد المجالات العشرة.)
- Each domain presents 5 to 10 interactive scenarios or questions.
  (يقدم كل مجال من 5 إلى 10 سيناريوهات أو أسئلة تفاعلية.)
- The child answers the scenarios, and based on rubrics, the app generates a report of their strengths and areas for improvement in that domain.
  (يجيب الطفل على السيناريوهات، وبناءً على النماذج، يقوم التطبيق بإنشاء تقرير حول نقاط قوتهم والمجالات التي تحتاج إلى تحسين في هذا المجال.)
- The report can motivate children to challenge themselves, develop their skills, and build on their strengths.
  (يمكن للتقرير أن يحفز الأطفال على تحدي أنفسهم وتطوير مهاراتهم والبناء على نقاط قوتهم.)

#### **The 10 Domains | المجالات العشرة:**
1. **Cognitive Development (التطور المعرفي)**: Focuses on logical reasoning, memory, and the ability to process information.
2. **Social Interaction (التفاعل الاجتماعي)**: Assesses the child’s ability to interact positively with others and develop social skills.
3. **Critical Thinking (التفكير النقدي)**: Evaluates problem-solving, logical reasoning, and the ability to evaluate information.
4. **Creative Thinking (التفكير الإبداعي)**: Encourages originality, imagination, and the ability to think outside the box.
5. **Emotional Intelligence (الذكاء العاطفي)**: Measures how well the child understands and manages emotions, both their own and others'.
6. **Communication Skills (مهارات التواصل)**: Tests verbal and written communication, including the ability to express thoughts clearly.
7. **Digital Literacy (الإلمام الرقمي)**: Assesses the ability to use technology responsibly and effectively.
8. **Self-Management (إدارة الذات)**: Looks at time management, goal setting, and self-discipline.
9. **Leadership (القيادة)**: Evaluates the child’s ability to take initiative, motivate others, and make responsible decisions.
10. **Global Citizenship (المواطنة العالمية)**: Focuses on awareness of different cultures and the understanding of global issues.

#### **What the Report Includes | ما يتضمنه التقرير:**
- Each child receives a report for the selected domain, with detailed feedback on their strengths and areas of improvement.
   (يتلقى كل طفل تقريرًا عن المجال الذي تم اختياره مع ملاحظات تفصيلية حول نقاط قوتهم والمجالات التي تحتاج إلى تحسين.)
- The report encourages the child to continue developing their skills, particularly in areas they excel at or need to improve.
   (يشجع التقرير الطفل على الاستمرار في تطوير مهاراته، وخاصة في المجالات التي يتفوق فيها أو يحتاج إلى تحسين.)
""")

# Instructions for the child (Bilingual)
st.markdown("""
#### **How to start | كيفية البدء:**
1. Select a domain from the list of 10. (اختر مجالًا من القائمة المكونة من 10 مجالات.)
2. Answer the questions or scenarios presented to you. (أجب عن الأسئلة أو السيناريوهات المقدمة إليك.)
3. Submit your answers and receive your personalized report. (قم بإرسال إجاباتك واحصل على تقرير مخصص لك.)

Explore and have fun while learning about yourself and how to grow stronger in each area! (استمتع أثناء اكتشاف نفسك وكيفية تقوية نفسك في كل مجال!)
""")

# List of Domains (Bilingual)
fields = [
    "Cognitive Development (التطور المعرفي)",
    "Social Interaction (التفاعل الاجتماعي)",
    "Critical Thinking (التفكير النقدي)",
    "Creative Thinking (التفكير الإبداعي)",
    "Emotional Intelligence (الذكاء العاطفي)",
    "Communication Skills (مهارات التواصل)",
    "Digital Literacy (الإلمام الرقمي)",
    "Self-Management (إدارة الذات)",
    "Leadership (القيادة)",
    "Global Citizenship (المواطنة العالمية)"
]

# Domain selection using selectbox (Bilingual)
selected_field = st.selectbox("Select a domain to assess | اختر مجالًا للتقييم:", fields)

# Display the appropriate assessment or a message based on selection
if selected_field == "Cognitive Development (التطور المعرفي)":
    st.image(f"{image_base_path}cognitive.png", width=200)
    cognitive_assessment()  # This will call the cognitive assessment function
if selected_field == "Social Interaction (التفاعل الاجتماعي)":
    st.image(f"{image_base_path}social.png", width=200)
    social_interaction_assessment()  # This will call the social interaction assessment function
if selected_field == "Critical Thinking (التفكير النقدي)":
    st.image(f"{image_base_path}critical.png", width=200)
    critical_thinking_assessment()  # Call the critical thinking assessment function
if selected_field == "Creative Thinking (التفكير الإبداعي)":
    st.image(f"{image_base_path}creative.png", width=200)
    creative_thinking_assessment()  # Call the creative thinking assessment function
if selected_field == "Emotional Intelligence (الذكاء العاطفي)":
    st.image(f"{image_base_path}emotional.png", width=200)
    emotional_intelligence_assessment()  # Call the emotional intelligence assessment function
if selected_field == "Communication Skills (مهارات التواصل)":
    st.image(f"{image_base_path}communication.png", width=200)
    communication_skills_assessment()  # Call the communication skills assessment function
elif selected_field == "Digital Literacy (الإلمام الرقمي)":
    st.image(f"{image_base_path}digital.png", width=200)
    st.write("Placeholder: Digital Literacy assessment will be shown here. | التقييم الخاص بالإلمام الرقمي سيتم عرضه هنا.")
elif selected_field == "Self-Management (إدارة الذات)":
    st.image(f"{image_base_path}self.png", width=200)
    st.write("Placeholder: Self-Management assessment will be shown here. | التقييم الخاص بإدارة الذات سيتم عرضه هنا.")
elif selected_field == "Leadership (القيادة)":
    st.image(f"{image_base_path}leadership.png", width=200)
    st.write("Placeholder: Leadership assessment will be shown here. | التقييم الخاص بالقيادة سيتم عرضه هنا.")
elif selected_field == "Global Citizenship (المواطنة العالمية)":
    st.image(f"{image_base_path}global.png", width=200)
    st.write("Placeholder: Global Citizenship assessment will be shown here. | التقييم الخاص بالمواطنة العالمية سيتم عرضه هنا.")
else:
    st.write(f"Assessment for {selected_field} is coming soon. | التقييم الخاص بـ {selected_field} قادم قريباً.")
