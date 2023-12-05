import streamlit as st
import sqlite3
import pandas as pd

# Function to connect to the SQLite database
def connect_to_db(path):
    conn = sqlite3.connect(path)
    return conn

# Function to fetch data from a table
def fetch_data(query, conn, params=None):
    return pd.read_sql_query(query, conn, params=params)

# Function to insert a job post record into the JobPost table
def insert_job_post(conn, job_post_data):
    cursor = conn.cursor()
    query = '''
    INSERT INTO JobPost (ID, title, term, duration, jobdescription, jobrequirement, requiredqualification, salary, isIT, isPosted,companyid)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    cursor.execute(query, job_post_data)
    conn.commit()

# Function to get a single job post record by ID
def get_job_post_by_id(conn, job_id):
    cursor = conn.cursor()
    query = '''SELECT ID, Title, Term, Duration, JobDescription, JobRequirement, RequiredQualification, Salary, isIT, 
             isPosted, companyid, locationID, timelineID, additional_InfoID FROM JobPost WHERE id = ?'''
    cursor.execute(query, (job_id,))
    return cursor.fetchone()

# Function to update a job post record in the JobPost table
def update_job_post(conn, job_id, update_data):
    cursor = conn.cursor()
    query = '''
    UPDATE JobPost
    SET title = ?, term = ?, duration = ?, jobdescription = ?, jobrequirement = ?, requiredqualification = ?, salary = ?, isIT = ?, isPosted = ?
    WHERE id = ?
    '''
    cursor.execute(query, update_data + (job_id,))
    conn.commit()

# Function to check if the company exists and return its ID or create a new one
def get_or_create_company(conn, company_name, about_text):
    cursor = conn.cursor()
    # Check if company already exists
    cursor.execute('SELECT ID FROM Company WHERE name = ?', (company_name,))
    result = cursor.fetchone()
    if result:
        return result[0]  # Return the existing company ID
    else:
        # Insert new company since it does not exist
        cursor.execute('INSERT INTO Company (name, about) VALUES (?, ?)', (company_name, about_text))
        conn.commit()
        return cursor.lastrowid  # Return the new company ID

def update_job_post_fields(conn, job_id, update_data):
    cursor = conn.cursor()
    # Construct the SQL update query dynamically based on the fields provided in update_data
    set_clause = ', '.join([f"{k} = ?" for k in update_data])
    query = f"UPDATE JobPost SET {set_clause} WHERE ID = ?"
    params = list(update_data.values()) + [job_id]
    cursor.execute(query, params)
    conn.commit()

# Streamlit app layout  
def main():
    st.title("Job Connect Recruitment Portal")

    # Connect to the SQLite database
    db_path = 'Project.db'  # Replace with your database path
    conn = connect_to_db(db_path)

    # Sidebar for CRUD operations
    st.sidebar.title("Operations to perform")
    operation = st.sidebar.radio("Choose an operation", ["Create", "Read", "Update", "Delete"])

    if operation == "Create":
        # Implement Create operation fields and logic
        st.subheader("Create New Record")

        # Form for adding a new job post
        with st.form(key='new_job_post'):
            st.write("Add a New Job Post")
            id = st.number_input('id')
            title = st.text_input('Title')
            # Text input for company name and about text
            company_name = st.text_input('Company Name')
            about_text = st.text_area('About Company')

            term = st.text_area('Term')
            duration = st.text_area('Duration')
            jobdescription = st.text_area('Job Description')
            jobrequirement = st.text_area('Job Requirement')
            requiredqualification = st.text_area('Required Qualification')
            salary = st.text_input('Salary')
            isIT = st.checkbox('Is IT')
            isPosted = st.checkbox('Is Posted', value=False)
            
            submit_button = st.form_submit_button(label='Submit Job Post')
            if submit_button:
                companyid = get_or_create_company(conn, company_name, about_text)
                job_post_data = (
                    id, title, term, duration, jobdescription, jobrequirement,
                    requiredqualification, salary, isIT, isPosted,companyid
                )
                insert_job_post(conn, job_post_data)
                st.success("The job post has been added successfully!")

    elif operation == "Read":
        # Implement Read operation
        st.subheader("View Records")
        # Example to view job postings
        jobposts_query = "SELECT * FROM JobPost"
        jobposts_data = fetch_data(jobposts_query, conn)
        st.write(jobposts_data)

    elif operation == "Update":
        st.subheader("Update a Job Post")
        job_id = st.number_input("Enter the Job Post ID to update", min_value=0, format="%d")
        job_post = None

        if st.button('Load Job Post'):
            job_post = get_job_post_by_id(conn, job_id)
             
            if job_post:
                 job_post_df = pd.DataFrame([job_post], columns=['ID', 'Title', 'Term', 'Duration', 'JobDescription', 'JobRequirement', 'RequiredQualification', 'Salary', 'isIT', 'isPosted', 'companyid', 'locationID', 'timelineID', 'additional_InfoID'])
                 st.table(job_post_df)

        # Allow user to enter new values for the fields they want to update
        with st.form(key='update_job_post_form'):
            new_title = st.text_input('Title', value=job_post[1] if job_post else '')
            new_term = st.text_area('Term', value=job_post[2] if job_post else '')
            new_duration = st.text_area('Duration', value=job_post[3] if job_post else '')
            new_jobdescription = st.text_area('Job Description', value=job_post[4] if job_post else '')
            new_jobrequirement = st.text_area('Job Requirement', value=job_post[5] if job_post else '')
            new_requiredqualification = st.text_area('Required Qualification', value=job_post[6] if job_post else '')
            new_salary = st.text_input('Salary', value=job_post[7] if job_post else '')
            new_isIT = st.checkbox('Is IT', value=job_post[8] if job_post else False)
            new_isPosted = st.checkbox('Is Posted', value=job_post[9] if job_post else False)

            submit_update = st.form_submit_button('Update Job Post')

        if submit_update:
            update_data = {}
            if job_post:
                if new_title != job_post[1]: update_data['title'] = new_title
                if new_term != job_post[2]: update_data['term'] = new_term
                if new_duration != job_post[3]: update_data['duration'] = new_duration
                if new_jobdescription != job_post[4]: update_data['jobdescription'] = new_jobdescription
                if new_jobrequirement != job_post[5]: update_data['jobrequirement'] = new_jobrequirement
                if new_requiredqualification != job_post[6]: update_data['requiredqualification'] = new_requiredqualification
                if str(new_salary) != str(job_post[7]): update_data['salary'] = new_salary
                if new_isIT is not job_post[8]: update_data['isIT'] = new_isIT
                if new_isPosted is not job_post[9]: update_data['isPosted'] = new_isPosted

                # Update the job post record with the new values
                update_job_post_fields(conn, job_id, update_data)
                st.success("Job post updated successfully.")
            else:
                st.error("Please load a job post before updating.")


    # elif operation == "Update":
    #     st.subheader("Update a Job Post")
    #     job_id = st.number_input("Enter the Job Post ID to update", min_value=1, format="%d")

    #     # Define a dictionary to hold the form values
    #     form_data = {}

    #     if st.button('Load Job Post'):
    #         job_post = get_job_post_by_id(conn, job_id)
    #         #st.table(job_post)

    #         if job_post:
    #             job_post_df = pd.DataFrame([job_post], columns=['ID', 'Title', 'Term', 'Duration', 'JobDescription', 'JobRequirement', 'RequiredQualification', 'Salary', 'isIT', 'isPosted', 'companyid', 'locationID', 'timelineID', 'additional_InfoID'])
    #             st.table(job_post_df)
    #             # Fetch company details
    #             company_id = job_post[9]  # Assuming index 9 is companyid
    #             company_query = "SELECT * FROM Company WHERE ID = ?"
    #             company = fetch_data(company_query, conn, params=(company_id,))
    #             if company.empty:
    #                 st.error("Associated company not found.")
    #                 return
            
    #             company_name = company.iloc[0]['name']
    #             about_text = company.iloc[0]['about']

    #             # Define the update form
    #             with st.form(key='update_job_post'):
    #                 new_title = st.text_input('Title', value=job_post[1])
    #                 new_company_name = st.text_input('Company Name', value=company_name)
    #                 new_about_text = st.text_area('About Company', value=about_text)
    #                 new_term = st.text_area('Term', value=job_post[2])
    #                 # ... other fields for the job post ...
                
    #                 # Define the submit button for the form
    #                 submit_button = st.form_submit_button(label='Update Job Post')
    #                 if submit_button:
    #                     # Dictionary to hold the updated values
    #                     update_fields = {}
    #                     if new_title != job_post[1]: update_fields['title'] = new_title
    #                     if new_term != job_post[2]: update_fields['term'] = new_term
    #                      # ... other fields to check ...

    #                     # Check if company name or about text has changed
    #                     if new_company_name != company_name or new_about_text != about_text:
    #                          # Update the Company record
    #                          update_company_query = "UPDATE Company SET name = ?, about = ? WHERE ID = ?"
    #                          cursor = conn.cursor()
    #                          cursor.execute(update_company_query, (new_company_name, new_about_text, company_id))
    #                          conn.commit()

    #                     # Update the JobPost record if there are fields to update
    #                     if update_fields:
    #                         update_query = "UPDATE JobPost SET "
    #                         update_query += ', '.join(f"{k} = ?" for k in update_fields.keys())
    #                         update_query += " WHERE id = ?"

    #                         # List of values to pass into the SQL statement
    #                         update_values = list(update_fields.values())
    #                         update_values.append(job_id)  # Make sure to append the job ID at the end

    #                         # Execute the update query
    #                         cursor.execute(update_query, update_values)
    #                         conn.commit()

    #                         st.success("The job post has been updated successfully!")
    #         else:
    #             st.error("Job Post not found. Please enter a valid Job Post ID.")

    elif operation == "Delete":
        # Implement Delete operation fields and logic
        st.subheader("Delete a Record")

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()
