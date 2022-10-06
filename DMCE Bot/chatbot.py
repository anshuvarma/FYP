from email.policy import default
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy
spacy.load('en_core_web_sm')
# from spacy.lang.en import English
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr
import pyttsx3 as pp

# Creating ChatBot Instance
chatbot = ChatBot('<b>DMCE BOT</b>')

engine = pp.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

chatbot = ChatBot(
    'ChatBot for College Enquiry',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "Hi there, 👋 If you need any assistance, I'm always here.Go ahead and write the number of any query. 😃✨<br><br><br>  Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry</br> 2.&emsp;Parent's Section Enquiry.</br>3.&emsp;Visitor's Section Enquiry.</br><br>",
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///chatbot.sqlite3'  
) 
trainer = ListTrainer(chatbot)


faqs = [
"Hi",
"Helloo!",
"Hey",

"What is the address of dmce?",
"Plot No. 98, Sector-3, Airoli, Opp Khandoba Temple Sri Sadguru Vanamrao Pai Marg, Navi Mumbai, Maharashtra 400708",

"How are you?",
"I'm good.",

"Who is the HOD?",
"Dr. Amol Pande",

"Great",

"Good",

"I am Fine",
"Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br> 2.&emsp;Parent's Section Enquiry.</br> 3.&emsp;Visitor's Section Enquiry.</br>",

"Thank You",
"Your Welcome 😄",

"Thanks",
"Your Welcome 😄",

"Bye",
"Thank You for visiting!..",

"What do you do?",
"I am made to give Information about DMCE college.",

"What else can you do?",
"I can help you know more about DMCE",
    
    # STUDENT ENQUIRY SECTION
    "1",
    "<b>STUDENT <br>The following are frequently searched terms related to student . Please select one from the options below : <br> <br> 1.1 Admission <br>1.2  Departments<br>1.3 ERP Login<br>1.4 Examination <br>1.5 Placements <br>1.6 Student Clubs <br>1.7 Time Table </b>",


    # ADMISSION SECTION
    "1.1",
    "<b>  ADMISSIONS <br>  These are the top results: <br> <br> 1.1.1 B.E <br> 1.1.2 M.E <br> 1.1.3 PHD </b>",
    "1.1.1",
    "<b> 1.1.1 Admission for B.E <br>The link for B.E Admissions 👉 <a href=" 'https://dmce.ac.in/admission/under_graduation_BE' ">Click Here</a> </b>",
    
    "1.1.2",
    "<b > 1.1.2 Admission for B.E <br>The link for M.E Admissions👉<a href=" 'https://dmce.ac.in/admission/post_graduation_ME' ">Click Here</a> </b>",
    
    "1.1.3",
    "<b> 1.1.3 Admission for P.H.D <br>The link for M.E Admissions 👉 <a href=" 'https://dmce.ac.in/admission/doctorate_PHD' ">Click Here</a> </b>",


    # DEPARTMENTS SECTION
    "1.2",
    "<b> DEPARTMENTS <br>These are the top results: <br> <br> 1.2.1 Artificial Intelligence and Data Science Engineering<br> 1.2.2 Chemical Engineering <br> 1.2.3 Civil Engineering <br> 1.2.4 Civil Engineering(Second Shift) <br> 1.2.5 Computer Engineering <br> 1.2.6 Electronics Engineering <br> 1.2.7 Humanities and Sciences(First Year) <br> 1.2.8 Information Technology <br> 1.2.9 Mechanical Engineering </b>",
    
    "1.2.1",
    "<b > 1.2.1 Artificial Intelligence and Data Science Engineering<br>The link for AI and Data Science Department👉 <a href=" 'https://dmce.ac.in/department/aids' ">Click Here</a></b>",
    
    "1.2.2",
    "<b > 1.2.2 Chemical Engineering <br>The link for Chemical Engineering Department 👉<a href=" 'https://dmce.ac.in/department/chem' ">Click Here</a> </b>",
    
    "1.2.3",
    "<b > 1.2.3 Civil Engineering <br>The link for Civil Engineering Department👉 <a href=" 'https://dmce.ac.in/department/civil' ">Click Here</a> </b>",

    "1.2.4",
    "<b > 1.2.4 Civil Engineering(Second Shift) <br>The link for Civil Engineering(Second Shift) Department👉 <a href=" 'https://dmce.ac.in/department/civil-ss' ">Click Here</a> </b>",

    "1.2.5",
    "<b > 1.2.5 Computer Engineering <br>The link for Computer Engineering Department👉 <a href=" 'https://dmce.ac.in/department/comp' ">Click Here</a> </b>",

    "1.2.6",
    "<b > 1.2.6 Electronics Engineering <br>The link for Electronics Engineering Department👉 <a href=" 'https://dmce.ac.in/department/elec' ">Click Here</a> </b>",
    
    "1.2.7",
    "<b > 1.2.7 Humanities and Sciences(First Year) <br>The link for Humanities and Sciences Department👉 <a href=" 'https://dmce.ac.in/department/humanities' ">Click Here</a> </b>",

    "1.2.8",
    "<b > 1.2.8 Information Technology <br>The link for Information Technology Department👉 <a href=" 'https://dmce.ac.in/department/it' ">Click Here</a> </b>",

    "1.2.9",
    "<b > 1.2.9 Mechanical Engineering <br>The link for Mechanical Engineering Department👉 <a href=" 'https://dmce.ac.in/department/mech' ">Click Here</a> </b>",

    
    # ERP SECTION
    "1.3",
    "<b>1.3 ERP LOGIN <br>These are the top results: <br> <br> 1.3.1 ERP Login </b>",
    "1.3.1",
    "<b> 1.3.1 Students Portal<br>The link for ERP Portal👉 <a href=" 'https://dmce.ac.in/' ">Click Here</a> </b>",
    
    
    # EXAMINATION SECTION
    "1.4",
    "<b > EXAMINATION <br>These are the top results:<br> 1.4.1 Updates<br> 1.4.2 Procedures </b>",
    
    "1.4.1",
    "<b > 1.4.1 Updates<br>The link to Exam Updates <a href=" 'https://dmce.ac.in/examination/updates' ">Click Here</a> </b>",
    
    "1.4.2",
    "<b > 1.4.2 Procedure<br>The link to for Exam Procedures👉<a href=" 'https://dmce.ac.in/examination/procedure' ">Click Here</a> </b>",
    

    # PLACEMENT SECTION
    "1.5",
    "<b > PLACEMENTS These are the top results:<br> 1.5.1 About<br> 1.5.2 Faculty <br> 1.5.3 Internships <br> 1.5.4 Our Recruiters <br> 1.5.5 Placements Statistics <br> 1.5.6 Training and Placement Message </b>",
    
    "1.5.1",
    "<b> 1.5.1 About <br>The link to Placements 👉 <a href=" 'https://dmce.ac.in/placement/placement-about' ">Click Here</a> </b>",
    
    "1.5.2",
    "<b> 1.5.2 Faculty <br>The link for the list of Placement Faculty 👉<a href=" 'https://dmce.ac.in/placement/placement-faculty' ">Click Here</a> </b>",
    
    "1.5.3",
    "<b > 1.5.3 Internships Statistics <br>The link for Internship Statistics👉 <a href=" 'https://dmce.ac.in/placement/internship-statistic.php' ">Click Here</a> </b>",

    "1.5.4",
    "<b > 1.5.4 Our Recruiters <br>The link for Our major Recruiters👉 <a href=" 'https://dmce.ac.in/placement/recruiters.php' ">Click Here</a> </b>",
    
    "1.5.5",
    "<b > 1.5.5 Placements Statistics <br>The link for Placements Statistics👉 <a href=" 'https://dmce.ac.in/placement/placement-statistic' ">Click Here</a> </b>",

    "1.5.6",
    "<b >1.5.6 T&P Message <br>The link to the T&P Message👉 <a href=" 'https://dmce.ac.in/placement/placement-tandp' ">Click Here</a> </b>",

    
    # STUDENT CLUBS SECTION
    "1.6",
    "<b > STUDENT CLUBS These are the top results:<br> 1.6.1 CSI <br> 1.6.2 GITS <br> 1.6.3 CATT <br> 1.6.4 FOMES <br> 1.6.5 EESA <br> 1.6.6 SOCHE <br> 1.6.7 IEEE <br> 1.6.8 ISTE <br> 1.6.9 IETE <br> 1.6.10 CODECHEF <br> 1.6.11 IIIE <br> 1.6.12 NSS <br> 1.6.13 SCIENCE CLUB(FE) <br> 1.6.14 ACES <br> 1.6.15 HOBBY CLUB </b>",
    
    "1.6.1",
    "<b> 1.6.1 CSI <br>The link for CSI committee 👉<a href=" 'https://dmce.ac.in/student-clubs/csi' ">Click Here</a> </b>",
    
    "1.6.2",
    "<b> 1.6.2 GITS <br>The link for GITS committee 👉<a href=" 'https://dmce.ac.in/student-clubs/gits' ">Click Here</a> </b>",
    
    "1.6.3",
    "<b > 1.6.3 CATT <br>The link for CATT committee 👉<a href=" 'https://dmce.ac.in/student-clubs/catt' ">Click Here</a> </b>",

    "1.6.4",
    "<b > 1.6.4 FOMES <br>The link for FOMES committee 👉<a href=" 'https://dmce.ac.in/student-clubs/fomes' ">Click Here</a> </b>",
    
    "1.6.5",
    "<b > 1.6.5 EESA <br>The link for EESA committee 👉<a href=" 'https://dmce.ac.in/student-clubs/eesa' ">Click Here</a> </b>",

    "1.6.6",
    "<b > 1.6.6 SOCHE <br>The link For SOCHE committee 👉<a href=" 'https://dmce.ac.in/student-clubs/soche' ">Click Here</a> </b>",

    "1.6.7",
    "<b > 1.6.7 IEEE <br>The link For IEEE committee 👉<a href=" 'https://dmce.ac.in/student-clubs/ieee' ">Click Here</a> </b>",
    
    "1.6.8",
    "<b > 1.6.8 ISTE <br>The link For ISTE committee 👉<a href=" 'https://dmce.ac.in/student-clubs/iste' ">Click Here</a> </b>",
    
    "1.6.9",
    "<b > 1.6.9 IETE <br>The link For IETE committee 👉<a href=" 'https://dmce.ac.in/student-clubs/iete' ">Click Here</a> </b>",
    
    "1.6.10",
    "<b > 1.6.10 CODECHEF <br>The link For CODECHEF committee 👉<a href=" 'https://dmce.ac.in/student-clubs/codechef' ">Click Here</a> </b>",
    
    "1.6.11",
    "<b > 1.6.11 IIIE <br>The link For IIIE committee 👉<a href=" 'https://dmce.ac.in/student-clubs/iiie' ">Click Here</a> </b>",
    
    "1.6.12",
    "<b > 1.6.12 NSS <br>The link For NSS committee 👉<a href=" 'https://dmce.ac.in/student-clubs/nss' ">Click Here</a> </b>",
    
    "1.6.13",
    "<b > 1.6.13 SCIENCE CLUB(FE) <br>The link For SCIENCE CLUB(FE) 👉<a href=" 'https://dmce.ac.in/student-clubs/science-club' ">Click Here</a> </b>",

    "1.6.14",
    "<b > 1.6.14 ACES <br>The link For ACES committee 👉<a href=" 'https://dmce.ac.in/student-clubs/aces' ">Click Here</a> </b>",
    
    "1.6.15",
    "<b > 1.6.15 HOBBY CLUB <br>The link For HOBBY CLUB 👉<a href=" 'https://dmce.ac.in/student-clubs/hobby-club' ">Click Here</a> </b>",

#   TIME-TABLE SECTION
    "1.7",
    "<b> TIME - TABLE <br>These are the top results: <br> <br> 1.7.1 Chemical Engineering <br> 1.7.2 Civil Engineering <br> 1.7.3 Civil Engineering(Second Shift) <br> 1.7.4 Computer Engineering <br> 1.7.5 Electronics Engineering <br> 1.7.6 Humanities and Sciences(First Year) <br> 1.7.7 Information Technology <br> 1.7.8 Mechanical Engineering </b>",
    
    "1.7.1",
    "<b > 1.7.1 Chemical Engineering <br>The link for Chemical Engineering Time-Table 👉<a href=" 'https://www.dmce.ac.in/department/chem-timetable' ">Click Here</a> </b>",
    
    "1.7.2",
    "<b > 1.7.2 Civil Engineering <br>The link for Civil Engineering Time-Table 👉 <a href=" 'https://www.dmce.ac.in/department/civil-timetable' ">Click Here</a> </b>",

    "1.7.3",
    "<b > 1.7.3 Civil Engineering(Second Shift) <br>The link for Civil Engineering(Second Shift) Time-table 👉 <a href=" 'https://www.dmce.ac.in/department/civil-ss-timetable' ">Click Here</a> </b>",

    "1.7.4",
    "<b > 1.7.4 Computer Engineering <br>The link for Computer Engineering Time Table 👉 <a href=" 'https://www.dmce.ac.in/department/comp-timetable' ">Click Here</a> </b>",

    "1.7.5",
    "<b > 1.7.5 Electronics Engineering <br>The link for Electronics Engineering Time-Table 👉 <a href=" 'https://www.dmce.ac.in/department/elec-timetable' ">Click Here</a> </b>",
    
    "1.7.6",
    "<b > 1.7.6 Humanities and Sciences(First Year) <br>The link for Humanities and Sciences Time-Table 👉 <a href=" 'https://www.dmce.ac.in/department/humanities-timetable' ">Click Here</a> </b>",

    "1.7.7",
    "<b > 1.7.7 Information Technology <br>The link for Information Technology Time-Table 👉 <a href=" 'https://www.dmce.ac.in/department/it-timetable' ">Click Here</a> </b>",

    "1.7.8",
    "<b > 1.7.8 Mechanical Engineering <br>The link for Mechanical Engineering Time-Table 👉 <a href=" 'https://www.dmce.ac.in/department/mech-timetable' ">Click Here</a> </b>",


#   PARENTS ENQUIRY SECTION
    "2",
    "<b>PARENTS <br>The following are frequently searched terms related to parents . Please select one from the options below : <br> <br> 2.1 About Us <br>2.2  Admissions <br>2.3 Accreditation <br>2.4 Examination <br>2.5 Placements </b>",
    
    # About us section
    "2.1",
    "<b > ABOUT US <br>These are the top results:<br> 2.1.1 About DMCE <br> 2.1.2 Vision and Mission <br> 2.1.3 Campus Amenities <br> 2.1.4 Principal's Desk <b>",
    
    "2.1.1",
    "<b > 2.1.1 About DMCE <br>The link to know about DMCE 👉 <a href=" 'https://www.dmce.ac.in/about/about_dmce' ">Click Here</a> </b>",
    
    "2.1.2",
    "<b > 2.1.2 Vision and Mission <br>The link to know about the vision and mission of DMCE 👉 <a href=" 'https://www.dmce.ac.in/about/dmce-vision-mission' ">Click Here</a> </b>",

    "2.1.3",
    "<b > 2.1.3 Campus Amenities <br>The link to know about the campus 👉 <a href=" 'https://www.dmce.ac.in/about/amenities' ">Click Here</a> </b>",

    "2.1.4",
    "<b > 2.1.4 Principal's Desk <br>The link to Principal's Desk 👉 <a href=" 'https://www.dmce.ac.in/about/principal-desk' ">Click Here</a> </b>",

    # Admission Section 
    "2.2",
    "<b>ADMISSIONS <br> These are the top results: <br> <br> 2.2.1 B.E <br> 2.2.2 M.E <br> 2.2.3 PHD </b>",
    
    "2.2.1",
    "<b> 2.2.1 Admission for B.E <br>The link for B.E Admissions 👉 <a href=" 'https://dmce.ac.in/admission/under_graduation_BE' ">Click Here</a> </b>",
    
    "2.2.2",
    "<b > 2.2.2 Admission for B.E <br>The link for M.E Admissions👉<a href=" 'https://dmce.ac.in/admission/post_graduation_ME' ">Click Here</a> </b>",
    
    "2.2.3",
    "<b> 2.2.3 Admission for P.H.D <br>The link for M.E Admissions 👉 <a href=" 'https://dmce.ac.in/admission/doctorate_PHD' ">Click Here</a> </b>",
    
    # Accreditation Section 
    "2.3",
    "<b>ACCREDITATION <br>  These are the top results: <br> <br> 2.3.1 NAAC and AQAR <br> 2.3.2 Affilations and Approvals </b>",
    
    "2.3.1",
    "<b> 2.3.1 NAAC and AQAR <br>The link for NAAC and AQAR Accreditation 👉 <a href=" 'https://www.dmce.ac.in/accredition/naacaqar' ">Click Here</a> </b>",
    
    "2.3.2",
    "<b > 2.3.2 Affilation and Approvals <br>The link for Affilation and Approvals 👉<a href=" 'https://www.dmce.ac.in/accredition/affiliations-and-approvals' ">Click Here</a> </b>",

    # Examination Section 
    "2.4",
    "<b > EXAMINATION <br>These are the top results:<br> 2.4.1 Updates<br> 2.4.2 Procedures </b>",
    
    "2.4.1",
    "<b > 2.4.1 Updates<br>The link to Exam Updates 👉 <a href=" 'https://dmce.ac.in/examination/updates' ">Click Here</a> </b>",
    
    "2.4.2",
    "<b > 2.4.2 Procedure<br>The link to for Exam Procedures 👉 <a href=" 'https://dmce.ac.in/examination/procedure' ">Click Here</a> </b>",

    # PLACEMENT SECTION
    "2.5",
    "<b > PLACEMENTS These are the top results:<br> 2.5.1 About<br> 2.5.2 Faculty <br> 2.5.3 Internships <br> 2.5.4 Our Recruiters <br> 2.5.5 Placements Statistics <br> 2.5.6 Training and Placement Message </b>",
    
    "2.5.1",
    "<b> 2.5.1 About <br>The link to Placements 👉 <a href=" 'https://dmce.ac.in/placement/placement-about' ">Click Here</a> </b>",
    
    "2.5.2",
    "<b> 2.5.2 Faculty <br>The link for the list of Placement Faculty 👉<a href=" 'https://dmce.ac.in/placement/placement-faculty' ">Click Here</a> </b>",
    
    "2.5.3",
    "<b > 2.5.3 Internships Statistics <br>The link for Internship Statistics👉 <a href=" 'https://dmce.ac.in/placement/internship-statistic.php' ">Click Here</a> </b>",

    "2.5.4",
    "<b > 2.5.4 Our Recruiters <br>The link for Our major Recruiters👉 <a href=" 'https://dmce.ac.in/placement/recruiters.php' ">Click Here</a> </b>",
    
    "2.5.5",
    "<b > 2.5.5 Placements Statistics <br>The link for Placements Statistics👉 <a href=" 'https://dmce.ac.in/placement/placement-statistic' ">Click Here</a> </b>",

    "2.5.6",
    "<b >2.5.6 T&P Message <br>The link to the T&P Message👉 <a href=" 'https://dmce.ac.in/placement/placement-tandp' ">Click Here</a> </b>",

    #  VISITORS ENQUIRY SECTION
    "3",
    "<b>VISITORS <br>The following are frequently searched terms related to visitors . Please select one from the options below : <br> <br> 3.1 About Us <br>3.2  Departments <br>3.3 Admissions <br>3.4 Placements <br>3.5 Research </b>",

    # About us section
    "3.1",
    "<b > ABOUT US <br>These are the top results:<br> 3.1.1 About DMCE <br> 3.1.2 Vision and Mission <br> 3.1.3 Campus Amenities <br> 3.1.4 Principal's Desk <b>",
    
    "3.1.1",
    "<b > 3.1.1 About DMCE <br>The link to know about DMCE 👉 <a href=" 'https://www.dmce.ac.in/about/about_dmce' ">Click Here</a> </b>",
    
    "3.1.2",
    "<b > 3.1.2 Vision and Mission <br>The link to know about the vision and mission of DMCE 👉 <a href=" 'https://www.dmce.ac.in/about/dmce-vision-mission' ">Click Here</a> </b>",

    "3.1.3",
    "<b > 3.1.3 Campus Amenities <br>The link to know about the campus 👉 <a href=" 'https://www.dmce.ac.in/about/amenities' ">Click Here</a> </b>",

    "3.1.4",
    "<b > 3.1.4 Principal's Desk <br>The link to Principal's Desk 👉 <a href=" 'https://www.dmce.ac.in/about/principal-desk' ">Click Here</a> </b>",

    # Departments Section
    "3.2",
    "<b> DEPARTMENTS <br>These are the top results: <br> <br> 3.2.1 Artificial Intelligence and Data Science Engineering<br> 3.2.2 Chemical Engineering <br> 3.2.3 Civil Engineering <br> 3.2.4 Civil Engineering(Second Shift) <br> 3.2.5 Computer Engineering <br> 3.2.6 Electronics Engineering <br> 3.2.7 Humanities and Sciences(First Year) <br> 3.2.8 Information Technology <br> 3.2.9 Mechanical Engineering </b>",
    
    "3.2.1",
    "<b > 3.2.1 Artificial Intelligence and Data Science Engineering<br>The link for AI and Data Science Department👉 <a href=" 'https://dmce.ac.in/department/aids' ">Click Here</a></b>",
    
    "3.2.2",
    "<b > 3.2.2 Chemical Engineering <br>The link for Chemical Engineering Department 👉<a href=" 'https://dmce.ac.in/department/chem' ">Click Here</a> </b>",
    
    "3.2.3",
    "<b > 3.2.3 Civil Engineering <br>The link for Civil Engineering Department👉 <a href=" 'https://dmce.ac.in/department/civil' ">Click Here</a> </b>",

    "3.2.4",
    "<b > 3.2.4 Civil Engineering(Second Shift) <br>The link for Civil Engineering(Second Shift) Department👉 <a href=" 'https://dmce.ac.in/department/civil-ss' ">Click Here</a> </b>",

    "3.2.5",
    "<b > 3.2.5 Computer Engineering <br>The link for Computer Engineering Department👉 <a href=" 'https://dmce.ac.in/department/comp' ">Click Here</a> </b>",

    "3.2.6",
    "<b > 3.2.6 Electronics Engineering <br>The link for Electronics Engineering Department👉 <a href=" 'https://dmce.ac.in/department/elec' ">Click Here</a> </b>",
    
    "3.2.7",
    "<b > 3.2.7 Humanities and Sciences(First Year) <br>The link for Humanities and Sciences Department👉 <a href=" 'https://dmce.ac.in/department/humanities' ">Click Here</a> </b>",

    "3.2.8",
    "<b > 3.2.8 Information Technology <br>The link for Information Technology Department👉 <a href=" 'https://dmce.ac.in/department/it' ">Click Here</a> </b>",

    "3.2.9",
    "<b > 3.2.9 Mechanical Engineering <br>The link for Mechanical Engineering Department👉 <a href=" 'https://dmce.ac.in/department/mech' ">Click Here</a> </b>",

    # Admission Section
    "3.3",
    "<b>ADMISSIONS <br>  These are the top results: <br> <br> 3.3.1 B.E <br> 3.3.2 M.E <br> 3.3.3 PHD </b>",
    
    "3.3.1",
    "<b> 3.3.1 Admission for B.E <br>The link for B.E Admissions 👉 <a href=" 'https://dmce.ac.in/admission/under_graduation_BE' ">Click Here</a> </b>",
    
    "3.2.2",
    "<b > 3.2.2 Admission for B.E <br>The link for M.E Admissions👉<a href=" 'https://dmce.ac.in/admission/post_graduation_ME' ">Click Here</a> </b>",
    
    "3.3.3",
    "<b> 3.3.3 Admission for P.H.D <br>The link for M.E Admissions 👉 <a href=" 'https://dmce.ac.in/admission/doctorate_PHD' ">Click Here</a> </b>",

    # Placements Section
    "3.4",
    "<b > PLACEMENTS <br> These are the top results:<br> 3.4.1 About<br> 3.4.2 Faculty <br> 3.4.3 Internships <br> 3.4.4 Our Recruiters <br> 3.4.5 Placements Statistics <br> 3.4.6 Training and Placement Message </br>",
    
    "3.4.1",
    "<b> 3.4.1 About <br>The link to Placements 👉 <a href=" 'https://dmce.ac.in/placement/placement-about' ">Click Here</a> </b>",
    
    "3.4.2",
    "<b> 3.4.2 Faculty <br>The link for the list of Placement Faculty 👉<a href=" 'https://dmce.ac.in/placement/placement-faculty' ">Click Here</a> </b>",
    
    "3.4.3",
    "<b > 3.4.3 Internships Statistics <br>The link for Internship Statistics👉 <a href=" 'https://dmce.ac.in/placement/internship-statistic.php' ">Click Here</a> </b>",

    "3.4.4",
    "<b > 3.4.4 Our Recruiters <br>The link for Our major Recruiters👉 <a href=" 'https://dmce.ac.in/placement/recruiters.php' ">Click Here</a> </b>",
    
    "3.4.5",
    "<b > 3.4.5 Placements Statistics <br>The link for Placements Statistics👉 <a href=" 'https://dmce.ac.in/placement/placement-statistic' ">Click Here</a> </b>",

    "3.4.6",
    "<b > 3.4.6 T&P Message <br>The link to the T&P Message👉 <a href=" 'https://dmce.ac.in/placement/placement-tandp' ">Click Here</a> </b>",

    # Research Section
    "3.5",
    "<b > RESEARCH <br>These are the top results: <br> 3.5.1 Books Publised <br> 3.5.2 Patents <br> 3.5.3 Consultancies <br> 3.5.4 Sponsorships <br> 3.5.5 IPR Cells </br>",
    
    "3.5.1",
    "<b> 3.5.1 Books Published <br>The link to Published Books 👉 <a href=" 'https://www.dmce.ac.in/research/publications' ">Click Here</a> </b>",
    
    "3.5.2",
    "<b> 3.5.2 Patents <br>The link for the Patents 👉 <a href=" 'https://www.dmce.ac.in/research/patents' ">Click Here</a> </b>",
    
    "3.5.3",
    "<b > 3.5.3 Consultancies <br>The link for Consultancies 👉 <a href=" 'https://www.dmce.ac.in/research/consultancies' ">Click Here</a> </b>",

    "3.5.4",
    "<b > 3.5.4 Sponsorships <br>The link for the Sponsorships 👉 <a href=" 'https://www.dmce.ac.in/research/sponsership' ">Click Here</a> </b>",
    
    "3.5.5",
    "<b > 3.5.5 IPR Cells <br>The link for IPR Cells 👉 <a href=" 'https://www.dmce.ac.in/research/ipr' ">Click Here</a> </b>",

]

trainer.train(faqs)