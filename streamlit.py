import streamlit as st
#import matplotlib.pyplot as plt
import requests
import pandas as pd
import altair as alt
import datetime
from io import StringIO

st.set_page_config(layout="wide")

local_host = 'http://localhost:8000/'

session_state = st.session_state

def get_jwt_token(username, password):
    
    url = local_host + 'api/token/'
    data = {
        'username': username,
        'password': password
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        token = response.json()
        access_token = token['access']
        return access_token
    else:
        return None
    

def get_data(token):
    url = local_host + 'data/'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return token
    else:
        return None
base_url=local_host+ 'analytics/'
def get_history():
    response=requests.get(base_url)
    if response.status_code==200:
        return response.json()
    else:
        return []
def create_task(data):
    response=requests.post(base_url,data=data)
    if response.status_code==200:
        return response.json()
    else:
       return None


def update_student(id, data):
    url = f"{base_url}{id}/"
    response = requests.patch(url, data=data)
    if response.status_code == 200:
        return response.json()
    else:
       return "data not updated"


def delete_student(id):
    url = f"{base_url}{id}/"
    response = requests.delete(url)
    if response.status_code == 200:
        return True
    return False

if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    
    st.markdown("<h1 style='text-align: center; '>LOGIN</h1> <br>", unsafe_allow_html=True)
    col1,col2,col3 = st.columns(3)
    with col1:
        st.write("")
    with col2:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        col1, col2 ,col3= st.columns(3)
        with col2:
            login_button = st.button("Login")

    if login_button:
        token = get_jwt_token(username, password)
        
        if token:
            data = get_data(token)
            
            if data:
                st.session_state['logged_in'] = True
                st.session_state['token'] = token
                st.experimental_rerun()
            else:
                 st.write("You do not have permission to access the next page")

        else:
            st.error("Invalid username or password.")
if 'logged_in' in st.session_state and st.session_state['logged_in']:

    token=st.session_state['token']    
    st.markdown("<h1 style='text-align: center; '>TODO application</h1> <br>", unsafe_allow_html=True)

    def Main():
        st.title("TODO APP LIST WITH STREAMLIT")

        menu = ["Create","Read","Update","Delete","About"]
        choice = st.sidebar.selectbox("MENU",menu)

        if choice == "Create":
            st.subheader("Add Items")

            col1,col2 = st.columns(2)

            with col1:
                task_title= st.text_area("Task to do")

            with col2:
                task_status = st.selectbox("Status",["Todo","doing","done"])
               # due_date = st.date_input("Due Date")
            if task_status=="done":
                
                

                file=st.file_uploader("please choose a file")


            data={"task_title":task_title,"task_status":task_status}
            if st.button("Add Task"):
                result=create_task(data)
                if result:
                    st.success("successfully posted")
                


                st.success(f"Successfully added data :{task_title}")

        elif choice =="Read":
            st.header("view tasks")
            hist=get_history()
            data_to_view=pd.DataFrame(hist)
            
            st.write(data_to_view)
            

        elif choice == "Update":
            st.header("EDIT/UPDATE ITEMS")
            update_id=st.text_input("id")
            update_task_title=st.text_input("task_title")
            update_status=st.selectbox("status",["Todo","doing","done"])
            datas={"task_title":update_task_title,"task_status":update_status}
            if st.button("update task"):
                Id=int(update_id)
                hist=update_student(Id,datas)
                st.write(hist)


        elif choice == "Delete":
            st.header("delete")
            del_id=st.text_input("id")
            
            if st.button("delete"):
                Id=int(del_id)
                hist=delete_student(Id)
                st.write(hist)

        else:
            st.subheader("About")




    if __name__=="__main__":
        Main()


