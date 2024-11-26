import streamlit as st
import datetime 

st.set_page_config(page_title="Keisha's Biography", page_icon="🤡", layout="wide")

if 'toggle_state' not in st.session_state:
    st.session_state.toggle_state = False

# Define a function to toggle the state
def Drawing_button():
    st.session_state.toggle_state = not st.session_state.toggle_state
    
import streamlit as st



# Display the name dynamically
st.markdown(
    f"""
    <div style="text-align: center; font-size: 40px;">
        <strong> Keisha's Biography </strong>  
    </div>
    """,
    unsafe_allow_html=True,
)

    
with st.container(): 
     st.write("---") 
     left_column, right_column = st.columns(2) 
     
     with left_column: #left column
        
          
        st.image("PROFILE.jpg")
        
        
        
        st.text_input("My Name", "Keisha Terece Dequit Gibertas")
        
        st.write("---") 
        
        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>What I do: </strong>
            </div>
        """, unsafe_allow_html=True)
         
        
        
        st.text_area("","""> Watching movies
> Dancing routine
> Sleep
> Study
> Household chores""", height=125 )
        st.write("---")
        
        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>My Achievements: </strong>
                </di
            
        """, unsafe_allow_html=True)
        st.text_area("Description: ", """I've been in a lot of competitions and activities that molded me to what I am now. I've always known what I am passionate about and that's mostly dancing. Dancing has given me opportunities that I never knew that could give me different type of happiness. It makes me feel alive in stage and can understand the flow of music in my ears. Beside dancing, I also compete in academic activities such as writing, patimpalak, quizzes, and many more school competitions. I once stopped everything, being the competent woman I am. But everything has it ways to go back and move forward.
           """, height = 330)
        

        
        st.write("   ")
        st.write("   ")
        if st.button("Click here to see my Dancing Career "):
            Drawing_button()
        
        if st.session_state.toggle_state == True:
            st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>My Dancing Career: </strong>
            </div>
            """, unsafe_allow_html=True)
            st.write("---")
            inner_col1, inner_col2 = st.columns(2)
            with inner_col1:
                st.image('1.jpg', width=300)
                st.image('3.jpg', width=300)
            with inner_col2:
                st.image('2.jpg', width=300)
                st.image('4.jpg', width=300)
                
                
            st.write("---")   
            
            
            
        st.write("---")  
        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>Social Media Accounts: </strong>
            </div>
        """, unsafe_allow_html=True)
        st.write("[Facebook](https://www.facebook.com/share/1EJw3EheES/)")
        st.write("[Instagram](https://www.instagram.com/kkeishangg.qt/profilecard/?igsh=MTlqY29ubThyNHI5bQ==)")
            
            
     with right_column: #right column
        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>ABOUT ME: </strong>
            </div>
        """, unsafe_allow_html=True)
        
        st.text_area("", """Hi, I'm Keisha Terece D. Gibertas, and I'm passionate about dancing and in my academic. I believe that I can survive every obstacle that comes my way, that everything has a hard path while going on a journey. Everything happens for a reason, and I am glad I have everyone that I can be with through this beautiful but harsh life.

Professionally, I am a first year student in Surigao Del Norte State University, and I’m always looking for ways to achieve what I always wanted in life. My skills include hardwork and dedication to fullfil what I've been longing for.

In my free time, I enjoy listening to music, dancing, watching movies and many more that I can think that will help me cope with stress. I also believe in being positive even if everything goes hard, that I really can do it no matter what.

I’m always open to connect with others, explore new opportunities, learning, etc. Feel free to reach out if you'd like to chat about life interests.""", height = 330)
        
        
        
        mbday = st.date_input("My Birthday", datetime.date(2006, 2, 3))
        st.text_input("Birthplace", "Pasig City")
        
        st.radio("Gender", ["Female", "Male"])
        st.subheader("Family Background: ")  
        mother = st.text_input("Mother's name", "Nadia Dequit Gibertas")
        mbday = st.date_input("Mother's Birthday", datetime.date(1985, 6, 25))
        father = st.text_input("Father's Name", "Alvie Aclo Gibertas")
        mother = st.text_input("Brother's name", "Bhester Ahl Dequit Gibertas")
        mbday = st.date_input("Brother's Birthday", datetime.date(2007, 2, 22))
        father = st.text_input("Second Brother's Name", "Jairu Dequit Gibertas")
        mbday = st.date_input("Second Brother's Birthday", datetime.date(2009, 2, 9))
        st.text_input("Sister's Name", "Vahn Aimyreine Dequit Gibertas")
        mbday = st.date_input("Sister's Birthday", datetime.date(2012, 2, 19))  
        st.subheader("Educational Attainment: ")
        elem = st.text_input("Elementary: ", "Roxas Elementary School")
        hs = st.text_input("High School: ", "Surigao Del Norte National Highschool")
        shs = st.text_input("Senior High School: ", "Surigao Del Norte National Highschool")
        college = st.text_input("College: ", "Surigao Del Norte State University")
        st.write("---")
                
        
      
        

st.write('\n')
st.write ("---")
tab1, tab2, tab3, tab4 = st.tabs(["Achievements", "Consistent Honor Student", "Club and Organizations", "Classroom Officers"])
with tab1:
    st.write("### Achievements:")
    tab1.markdown(
        """
        <ul style="margin-left: 20px; font-size: 16px;">
            <ul style="margin-left: 20px;">
                <li>RSPC Journalism 2017</li>
                <li>2nd Feature Writing 2016</li>
                <li>4th Science and Health Writing Contest 2016</li>
                <li>7th DSPC Journalism 2017</li>
                <li>2nd Patimpalak Buwan ng Wika 2016</li>
                <li>3rd CollaboraVideo Statistics School Level 2023</li>
                <li>1st Popdance Competition 2022</li>
                <li>1st Sport Festival Dance Competition 2023</li> 
            </ul>
        </ul>
        """,
        unsafe_allow_html=True,
    )
# Initialize session state for accomplishments if not present
if 'accomplishments' not in st.session_state:
    st.session_state.accomplishments = {
        'elementary': [
            "🏅Batch 2017 - 2018 Valedictorian"
        ],
        'secondary': [
            "🏅Grade 7: With Honor",
            "🏅Grade 8: With High Honor",
            "🏅Grade 10: With Honor",
            "🏅Grade 11: With Honor",
            "🏅Grade 12: With High Honor"
        ],
        
    }
# Function to display accomplishments
def display_accomplishments(data):
    for key, values in data.items():
        st.markdown(f"**{key.upper()}**:")
        st.markdown("<ul style='margin-left: 20px;'>", unsafe_allow_html=True)
        for value in values:
            st.markdown(f"<li>{value}</li>", unsafe_allow_html=True)
        st.markdown("</ul>", unsafe_allow_html=True)

# --- Tab 2: Accomplishments ---
with tab2:
    st.write("### Current Accomplishments:")
    display_accomplishments(st.session_state.accomplishments)

    # --- Add/Update Accomplishment ---
    st.write("### Add/Update Accomplishment")
    level = st.selectbox("Choose accomplishment level:", ["Elementary", "Secondary"])
    accomplishment = st.text_input(f"Enter accomplishment for {level}:")

    # Button to add or update
    if st.button(f"Add/Update {level}"):
        level_key = level.lower()
        if accomplishment:
            st.session_state.accomplishments[level_key].append(accomplishment)
            st.success(f"Accomplishment added/updated for {level}!")
        else:
            st.warning("Please enter an accomplishment.")

    # --- Remove Accomplishment ---
    st.write("### Remove Accomplishment")
    remove_level = st.selectbox("Select level to remove an accomplishment from:", ["Elementary", "Secondary", "College"])
    accomplishments_to_remove = st.session_state.accomplishments[remove_level.lower()]
    accomplishment_to_remove = st.selectbox("Select accomplishment to remove:", accomplishments_to_remove)

    # Button to remove an accomplishment
    if st.button(f"Remove Accomplishment from {remove_level}"):
        if accomplishment_to_remove in accomplishments_to_remove:
            st.session_state.accomplishments[remove_level.lower()].remove(accomplishment_to_remove)
            st.success(f"Accomplishment removed from {remove_level}!")
        else:
            st.warning("Accomplishment not found.")

# --- Tab 3: Club and Organizations ---
with tab3:
    st.write("### Club and Organizations:")
    tab3.markdown(
    """
    <ul style="margin-left: 20px; font-size: 16px;">
        <ul style="margin-left: 20px;">
            <li>Reading Program Seminar - Workshop on Peer Tutoring S.Y. 2018-2019</li>
            <li>DRRM Member S.Y. 2022-2023</li>
            <li>Research Member S.Y. 2023-2024</li>
            <li>Red Cross Youth Volunteer 2024</li>
        </ul>
    </ul>
    """,
    unsafe_allow_html=True,
)

with tab4:
    st.write("### Classroom Officers:")
    tab4.markdown(
    """
    <ul style="margin-left: 20px; font-size: 16px;">
        <ul style="margin-left: 20px;">
            <li>Grade 6 - Vice President</li>
            <li>Grade 5 - President</li>
            <li>Grade 8 - President</li>
        </ul>
    </ul>
    """,
    unsafe_allow_html=True,
    )
    st.write("### Supreme School Pupil:")
    tab4.markdown(
    """
    <ul style="margin-left: 20px; font-size: 16px;">
        <ul style="margin-left: 20px;">
            <li>President S.Y. 2016-2017</li>
        </ul>
    </ul>
    """,
    unsafe_allow_html=True,
)