import re
import streamlit as st


st.set_page_config(page_title="Password Strength Meter By Muhammad Ashhad Khan", page_icon="🔑" , layout="centered")
#custom css
st.markdown("""
<style>
            .main {text-align: center;}
            st.TextInput {width: 60% !important; margin: auto;}
            .st.button {width: 50%, background-color $4CAF50; color: white; font-size:18px;}
            .st.button button:hover {background-color: #45a049;}
</style>
""", unsafe_allow_html=True)

st.title("🔐Password Strength Generator(Application Form)")



#function
st.write("Enter Your Password Below to check it's security level.")
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters**")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]",password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase(A-Z) and lowercase(a-z**")

    if re.search(r"\d",password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one digit(0-9).**")
    
    if re.search(r"[!@#$%^&*()_-+=?/><.,';:]",password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one special character(!@#$%^&*()_-+=?/><.,';:)**.")

        #display  password strength result
        if score == 4 :
            st.success("✅ **Strong Password** Your password is safe.")
        elif score == 3 :
            st.info("⚠️**Moderate Password** -Consider improving security by adding more feature.")
        else:
            st.error("❌ **Weak Password** - Follow the suggestion below to strength it.")

        #feedback
        if feedback:
            with st.expander("🔍 **Improve your password**"):
                for item in feedback:
                    st.write(item)



user = st.text_input("Enter your Username")
if len(user) >= 6:
    print("Username Saved Successfully!")
else:
    print("Username must be at least 6 characters")
)
            
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong 🔐")

if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
