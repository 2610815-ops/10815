import streamlit as str
popcorn = str.selectbox("팝콘 선택", ["기본", "카라멜", "어니언"])
drink = str.selectbox("음료 선택", ["생수", "탄산음료"])
str.write(f"🍿 선택하신 메뉴: 세트메뉴 {popcorn} 팝콘 + {drink}")