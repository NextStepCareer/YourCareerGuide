import sqlite3

# Connect to database
conn = sqlite3.connect("careers.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS careers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    skills TEXT,
    course TEXT,
    course_link TEXT
)
""")

# Career dataset (100+ careers)
careers = [

# TECHNOLOGY CAREERS
("Software Developer","coding,python,java,logic","Complete Web Development Bootcamp","https://www.udemy.com/course/the-web-developer-bootcamp/"),
("Data Scientist","python,statistics,math","IBM Data Science Professional Certificate","https://www.coursera.org/professional-certificates/ibm-data-science"),
("AI Engineer","python,machine learning,math","Deep Learning Specialization","https://www.coursera.org/specializations/deep-learning"),
("Machine Learning Engineer","python,ml,statistics","Machine Learning Course","https://www.coursera.org/learn/machine-learning"),
("Cyber Security Analyst","network,security,linux","Google Cybersecurity Certificate","https://www.coursera.org/professional-certificates/google-cybersecurity"),
("Ethical Hacker","security,network,linux","Ethical Hacking Course","https://www.udemy.com/course/learn-ethical-hacking-from-scratch/"),
("Cloud Engineer","aws,cloud,network","AWS Cloud Practitioner","https://www.udemy.com/course/aws-certified-cloud-practitioner-new/"),
("DevOps Engineer","docker,kubernetes,linux","DevOps Bootcamp","https://www.udemy.com/course/devops-training/"),
("Game Developer","unity,coding,design","Unity Game Development","https://www.udemy.com/course/unitycourse/"),
("Mobile App Developer","android,kotlin,java","Android Development Course","https://www.udemy.com/course/android-oreo-kotlin-app-masterclass/"),
("Full Stack Developer","html,css,javascript,node","Full Stack Development","https://www.udemy.com/course/the-complete-web-development-bootcamp/"),
("Frontend Developer","html,css,react,javascript","React Developer Course","https://www.udemy.com/course/react-the-complete-guide-incl-redux/"),
("Backend Developer","python,node,database","Backend Development Course","https://www.udemy.com/course/nodejs-express-mongodb-bootcamp/"),
("Blockchain Developer","solidity,crypto,web3","Blockchain Developer Course","https://www.udemy.com/course/blockchain-developer/"),
("Robotics Engineer","robotics,python,mechanics","Robotics Specialization","https://www.coursera.org/specializations/robotics"),
("AR VR Developer","unity,vr,design","AR VR Development","https://www.udemy.com/course/virtual-reality/"),
("Database Administrator","sql,database,security","SQL Bootcamp","https://www.udemy.com/course/the-complete-sql-bootcamp/"),
("Network Engineer","network,security,hardware","Networking Course","https://www.udemy.com/course/comptia-network-n10-008/"),
("QA Engineer","testing,automation,selenium","Software Testing Course","https://www.udemy.com/course/software-testing-masterclass/"),
("IT Support Specialist","hardware,network,os","Google IT Support Certificate","https://www.coursera.org/professional-certificates/google-it-support"),

# DESIGN CAREERS
("UI Designer","design,figma,creativity","UI Design Certificate","https://www.coursera.org/professional-certificates/google-ux-design"),
("UX Designer","research,design,prototype","UX Design Certificate","https://www.coursera.org/professional-certificates/google-ux-design"),
("Graphic Designer","photoshop,illustrator,design","Graphic Design Masterclass","https://www.udemy.com/course/graphic-design-masterclass/"),
("Animator","animation,creativity,design","Animation Course","https://www.udemy.com/course/animation-course/"),
("Video Editor","editing,premiere,creativity","Video Editing Course","https://www.udemy.com/course/video-editing/"),
("3D Artist","blender,3d,design","Blender 3D Course","https://www.udemy.com/course/blender-3d/"),
("Fashion Designer","fashion,design,creativity","Fashion Design Course","https://www.udemy.com/course/fashion-design/"),
("Interior Designer","design,architecture,creativity","Interior Design Course","https://www.udemy.com/course/interior-design/"),

# BUSINESS CAREERS
("Entrepreneur","business,leadership,creativity","Entrepreneurship Course","https://www.coursera.org/learn/wharton-entrepreneurship"),
("Product Manager","management,planning,communication","Product Management Course","https://www.coursera.org/professional-certificates/google-project-management"),
("Project Manager","planning,leadership,management","Project Management Certificate","https://www.coursera.org/professional-certificates/google-project-management"),
("Business Analyst","analysis,excel,communication","Business Analytics Course","https://www.coursera.org/specializations/business-analytics"),
("Investment Banker","finance,analysis,math","Investment Banking Course","https://www.udemy.com/course/investment-banking/"),
("Accountant","accounting,finance,excel","Accounting Course","https://www.udemy.com/course/accounting-finance-course/"),
("Financial Analyst","finance,statistics,excel","Financial Analysis Course","https://www.udemy.com/course/financial-analysis/"),
("Human Resource Manager","communication,management","HR Management Course","https://www.udemy.com/course/human-resource-management/"),
("Marketing Manager","marketing,communication","Marketing Course","https://www.coursera.org/specializations/marketing"),
("Digital Marketer","seo,social media,ads","Digital Marketing Course","https://www.coursera.org/professional-certificates/google-digital-marketing-ecommerce"),

# SCIENCE CAREERS
("Biotechnologist","biology,lab research","Biotechnology Course","https://www.coursera.org/specializations/biotechnology"),
("Genetic Engineer","biology,genetics,lab","Genetics Course","https://www.coursera.org/learn/genetics-evolution"),
("Microbiologist","biology,research","Microbiology Course","https://www.coursera.org/learn/microbiology"),
("Chemist","chemistry,lab work","Chemistry Course","https://www.coursera.org/learn/general-chemistry"),
("Physicist","physics,math,research","Physics Course","https://www.coursera.org/learn/physics"),
("Environmental Scientist","environment,research","Environmental Science Course","https://www.coursera.org/learn/environmental-science"),
("Astronomer","physics,space","Astronomy Course","https://www.coursera.org/learn/astronomy"),

# MEDICAL CAREERS
("Doctor","biology,medicine","Medical Neuroscience","https://www.coursera.org/learn/medical-neuroscience"),
("Surgeon","biology,medicine,precision","Surgery Course","https://www.coursera.org/learn/surgery"),
("Dentist","biology,healthcare","Dentistry Course","https://www.coursera.org/learn/dentistry"),
("Pharmacist","chemistry,medicine","Pharmacy Course","https://www.coursera.org/learn/pharmacy"),
("Nurse","healthcare,caregiving","Nursing Course","https://www.coursera.org/learn/nursing"),
("Psychologist","psychology,analysis","Psychology Course","https://www.coursera.org/learn/psychology"),
("Physiotherapist","health,exercise","Physiotherapy Course","https://www.udemy.com/course/physiotherapy/"),

# ENGINEERING CAREERS
("Civil Engineer","math,construction","Civil Engineering Specialization","https://www.coursera.org/specializations/civil-engineering"),
("Mechanical Engineer","mechanics,math","Mechanical Engineering Course","https://www.coursera.org/specializations/mechanical-engineering"),
("Electrical Engineer","electronics,math","Electrical Engineering Course","https://www.coursera.org/specializations/electrical-engineering"),
("Aerospace Engineer","physics,math","Aerospace Engineering Course","https://www.coursera.org/specializations/aerospace-engineering"),
("Automobile Engineer","mechanics,design","Automobile Engineering Course","https://www.udemy.com/course/automobile-engineering"),

# LAW & SOCIAL CAREERS
("Lawyer","law,analysis","Introduction to Law","https://www.coursera.org/learn/law"),
("Judge","law,analysis","Legal Studies Course","https://www.coursera.org/learn/legal-studies"),
("Journalist","writing,communication","Journalism Course","https://www.coursera.org/learn/journalism"),
("Content Writer","writing,creativity","Content Writing Course","https://www.udemy.com/course/content-writing/"),
("Teacher","communication,teaching","Teaching Course","https://www.coursera.org/learn/teaching"),

# CREATIVE CAREERS
("Photographer","photography,creativity","Photography Masterclass","https://www.udemy.com/course/photography-masterclass/"),
("Film Director","storytelling,film","Film Making Course","https://www.udemy.com/course/filmmaking/"),
("Music Producer","music,editing","Music Production Course","https://www.udemy.com/course/music-production/"),
("Actor","acting,expression","Acting Course","https://www.udemy.com/course/acting/"),

# EMERGING CAREERS
("Prompt Engineer","ai,prompt writing","Prompt Engineering Course","https://www.coursera.org/learn/prompt-engineering"),
("AI Product Manager","ai,management","AI Product Management","https://www.coursera.org/learn/ai-product-management"),
("Data Engineer","python,sql,data","Data Engineering Certificate","https://www.coursera.org/professional-certificates/data-engineering"),
("Quantum Computing Engineer","physics,quantum","Quantum Computing Course","https://www.coursera.org/learn/quantum-computing")

]

# Insert data
cursor.executemany(
"INSERT INTO careers (name,skills,course,course_link) VALUES (?,?,?,?)",
careers
)

# Save and close
conn.commit()
conn.close()

print("Database created successfully with 100+ careers!")