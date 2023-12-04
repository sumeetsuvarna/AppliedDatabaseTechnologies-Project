def code_main():
    import streamlit as st
    import sqlite3
    import pandas as pd
    conn = sqlite3.connect('Project.db')

    job_titles = ["Marketing Manager", "Search Marketing Manager", "Corporate Marketing Manager", "Corporate Marketing Manager Manager Manager"]*5
    df = pd.read_sql_query("SELECT * from JobPost order by id desc limit 10", conn)
    
    st.markdown("""
    <style>
    .stApp [data-testid="stToolbar"] {
    display: none;
    }
    </style>
    """
                , unsafe_allow_html=True
    )

    # nav_container = st.container()

    # # Set the position of the navigation bar to fixed and bottom
    # nav_container.style.position = "fixed"
    # nav_container.style.bottom = "0"
    # nav_container.style.left = "0"
    # nav_container.style.width = "100%"
    # #nav_container.style.background-color = "rgba(0, 0, 0, 0.8)"
    # nav_container.style.padding = "10px"

    # # Create the navigation bar content
    # with nav_container:
    #     st.markdown("**Navigation Bar**")

    #     # Create a list of navigation links
    #     navigation_links = ["Home", "About", "Contact"]

    #     # Create a button for each navigation link
    #     for link in navigation_links:
    #         if st.button(link):
    #             # Handle the clicked link
    #             st.write(f"You clicked {link}!")


    st.sidebar.title("Operations to perform")
    operation = st.sidebar.radio("Choose an operation", ["Create", "Read", "Update", "Delete"])
    if operation == "Create":
        # Implement Create operation fields and logic
        st.subheader("Create New Record")

        # Example for adding a new company
        with st.form(key='new_company'):
            company_name = st.text_input("Company Name")
            company_about = st.text_area("About Company")
            submit_button = st.form_submit_button(label='Submit')
            if submit_button:
                # Logic to insert the new company into the Company table
                pass
    elif operation == "Read":   
        # Implement Read operation
        st.subheader("View Records")
        st.write(pd.read_sql_query("SELECT * from JobPost order by id desc limit 2", conn))
    

    # Show job post list        
    st.sidebar.subheader('Jobs list:')
    # Create a button in the sidebar
    for i,j in enumerate(df.title):
        if st.sidebar.button(j, key='b'+str(i), use_container_width=True):
            st.write(j)
        
git remote add origin https://github.iu.edu/ssuvarn/ADT-Fall2023-JobConnect_RecruitmentPortal


git push -u origin master

   
code_main()



