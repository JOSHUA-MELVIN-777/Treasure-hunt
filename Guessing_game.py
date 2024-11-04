import streamlit as st

for i in ["name","age","mail"]:
    if i not in st.session_state:
        st.session_state[i]=""
# def save():
#     dict1={"Name":name,"Age":age,"Mail":mail}
#     for i in ["name","age","mail"]:
#         st.session_state[i]=dict1[i]

name=st.text_input("Name")
age=st.text_input("Age")
mail=st.text_input("Mail")

#st.button(label="Save",on_click=save)

def ggame(list,target):
    left=0
    right=len(list)-1

    while left<=right:
        mid=(left+right)//2

        if list[mid]==target:
            print("Congratulations!!!")
            break

        elif list[mid]<target:
            left=mid+1

        else:
            right=mid-1

    print("Number not in list")

def create_list():
    max=st.text_input("Enter maximum number from 0")
    list=[]
    for i in range(0,int(max)+1):
        list.append(i)

st.button("Start",on_click=create_list)