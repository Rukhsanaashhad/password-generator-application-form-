import re  
import streamlit as st  

st.set_page_config(page_title="Password Strength Meter By Muhammad Ashhad Khan", page_icon="🔑", layout="centered")  

# Custom CSS  
st.markdown("""  
<style>  
    .main {text-align: center;}  
    st.text_input {width: 60% !important; margin: auto;}  
    .st.button {width: 50%; background-color: #4CAF50; color: white; font-size: 18px;}  
    .st.button:hover {background-color: #45a049;}  
</style>  
""", unsafe_allow_html=True)  

st.title("🔐 Password Strength Generator (Application Form)")  
st.write("Create a secure username and password to protect your account.")  

# Password strength checking function  
def check_password_strength(password):  
    score = 0  
    feedback = []  

    if len(password) >= 8:  
        score += 1  
    else:  
        feedback.append("❌ Password should be **at least 8 characters**")  

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):  
        score += 1  
    else:  
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z)**")  

    if re.search(r"\d", password):  
        score += 1  
    else:  
        feedback.append("❌ Password should include **at least one digit (0-9).**")  
    
    if re.search(r"[!@#$%^&*()_\-+=?/><.,';:]", password):  
        score += 1  
    else:  
        feedback.append("❌ Password should include **at least one special character (!@#$%^&*()_-+=?/><.,';:)**.")  

    return score, feedback  

# Username input  
user = st.text_input("Enter your Username")  
username_valid = False  

if user:  
    if len(user) >= 6:  
        st.success("✅ Username Saved Successfully!")  
        username_valid = True  
    else:  
        st.error("❌ Username must be at least 6 characters!")  

# Password input  
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong 🔐")  

if st.button("Check Strength and Submit"):  
    if username_valid and password:  
        score, feedback = check_password_strength(password)  
        
        # Only show success message if the password is strong  
        if score == 4:  
            st.success("✅ Strong Password: Your Application Form has been submitted.")  
        elif score >= 3:  
            st.info("⚠️ Moderate Password - Consider improving security by adding more features.")  
        else:  
            st.error("❌ Weak Password - Follow the suggestions below to strengthen it.")  
        
        # Feedback  
        if feedback:  
            with st.expander("🔍 Improve your password"):  
                for item in feedback:  
                    st.write(item)  
    else:  
        if not username_valid:  
            st.error("❌ Please ensure your username is valid.")  
        if not password:  
            st.warning("⚠️ Please enter a password first!")  

# Footer  
st.write("-----------")  
st.write("©️ Created by [Muhammad Ashhad Khan](https://github.com/Rukhsanaashhad)")  
