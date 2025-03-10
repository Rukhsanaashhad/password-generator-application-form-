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

# Password strength checking function  
st.write("Create a secure username and password to protect your account.")  

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
        feedback.append("❌ Password should include **both uppercase(A-Z) and lowercase(a-z)**")  

    if re.search(r"\d", password):  
        score += 1  
    else:  
        feedback.append("❌ Password should include **at least one digit (0-9).**")  
    
    if re.search(r"[!@#$%^&*()_\-+=?/><.,';:]", password):  
        score += 1  
    else:  
        feedback.append("❌ Password should include **at least one special character (!@#$%^&*()_-+=?/><.,';:)**.")  

    # Display password strength result  
    if score == 4:  
        st.success("✅ **Strong Password** Your password is safe.")  
    elif score == 3:  
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features.")  
    else:  
        st.error("❌ **Weak Password** - Follow the suggestions below to strengthen it.")  

    # Feedback  
    if feedback:  
        with st.expander("🔍 **Improve your password**"):  
            for item in feedback:  
                st.write(item)  

# Username input  
user = st.text_input("Enter your Username")  
if user:  
    if len(user) >= 6:  
        st.success("✅ Username Saved Successfully!")  
    else:  
        st.error("❌ Username must be at least 6 characters!")  
        
# Password input  
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong 🔐")  

if st.button("Check Strength"):  
    if password:  
        check_password_strength(password)  
    else:  
        st.warning("⚠️ Please enter a password first!")  



st.write("----------")
st.write("©️ Created by [Muhammad Ashhad Khan](https://github.com/Rukhsanaashhad)")
