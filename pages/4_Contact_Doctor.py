import streamlit as st

st.title("📞 Contact a Doctor Near You")

# --- Doctor Data ---
doctors = {
    "Visakhapatnam": [
        {
            "name": "Dr. Kiran Kumar",
            "title": "Diabetologist",
            "hospital": "Apollo Hospitals",
            "phone": "+91-98480-12345",
            "timing": "Mon–Sat: 10 AM – 5 PM"
        },
        {
            "name": "Dr. Neha Reddy",
            "title": "Endocrinologist",
            "hospital": "Seven Hills Hospital",
            "phone": "+91-99555-88990",
            "timing": "Mon–Fri: 11 AM – 4 PM"
        }
    ],
    "Vizianagaram": [
        {
            "name": "Dr. Lakshmi Narayana",
            "title": "General Physician",
            "hospital": "Sri Sai Clinic",
            "phone": "+91-90101-23456",
            "timing": "Mon–Fri: 9 AM – 1 PM, 5 PM – 8 PM"
        },
        {
            "name": "Dr. Ramesh Gupta",
            "title": "Diabetes Consultant",
            "hospital": "Metro Care Hospital",
            "phone": "+91-90321-44567",
            "timing": "Mon–Sat: 10 AM – 6 PM"
        }
    ],
    "Srikakulam": [
        {
            "name": "Dr. Aruna Devi",
            "title": "Diabetologist",
            "hospital": "Sunrise Hospital",
            "phone": "+91-99887-76543",
            "timing": "Mon–Sat: 10 AM – 6 PM"
        },
        {
            "name": "Dr. Mahesh",
            "title": "Endocrinologist",
            "hospital": "Lifeline Clinic",
            "phone": "+91-88888-77777",
            "timing": "Mon–Fri: 10 AM – 2 PM"
        }
    ],
    "Vijayawada": [
        {
            "name": "Dr. Prasad Reddy",
            "title": "Endocrinologist",
            "hospital": "Ramesh Hospitals",
            "phone": "+91-99444-11223",
            "timing": "Mon–Sat: 9 AM – 4 PM"
        },
        {
            "name": "Dr. Sneha Rao",
            "title": "Diabetes Specialist",
            "hospital": "Vijaya Clinic",
            "phone": "+91-90909-10101",
            "timing": "Mon–Sat: 10 AM – 5 PM"
        }
    ],
    "Guntur": [
        {
            "name": "Dr. Sujatha",
            "title": "Diabetes Specialist",
            "hospital": "Guntur City Clinic",
            "phone": "+91-88990-12300",
            "timing": "Mon–Sat: 10 AM – 6 PM"
        },
        {
            "name": "Dr. Ravi Teja",
            "title": "Endocrinologist",
            "hospital": "Star Hospitals",
            "phone": "+91-88800-22222",
            "timing": "Mon–Fri: 11 AM – 5 PM"
        }
    ],
    "Hyderabad": [
        {
            "name": "Dr. Rajeev Sharma",
            "title": "Senior Endocrinologist",
            "hospital": "Yashoda Hospitals",
            "phone": "+91-77000-44111",
            "timing": "Mon–Fri: 11 AM – 5 PM"
        },
        {
            "name": "Dr. Anitha Das",
            "title": "Diabetes Consultant",
            "hospital": "Apollo Jubilee Hills",
            "phone": "+91-98765-54321",
            "timing": "Mon–Sat: 10 AM – 6 PM"
        }
    ]
}

# --- Dropdown ---
selected_city = st.selectbox("Select your city:", ["Select..."] + list(doctors.keys()))

# --- Display Doctors ---
if selected_city != "Select..." and st.button("Search Doctors"):
    st.success(f"Showing doctors in {selected_city}:")

    for idx, doc in enumerate(doctors[selected_city]):
        with st.container():
            st.markdown(
                f"""
                <div style='font-size:14px; line-height:1.6; padding: 10px; border:1px solid #ddd; border-radius:10px; background-color:#f9f9f9; margin-bottom:10px;'>
                <b>{doc['name']}</b> – {doc['title']}<br>
                🏥 <i>{doc['hospital']}</i><br>
                📞 <b>{doc['phone']}</b><br>
                🕒 <i>{doc['timing']}</i><br><br>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(f"📅 Book Appointment with {doc['name']}", key=f"book_{idx}"):
                st.info(f"📞 Please call {doc['phone']} to confirm your appointment.")
else:
    st.info("Select a city and click 'Search Doctors' to view contact info.")
