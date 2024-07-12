# JobConnect - Recruitment Portal

## Abstract
Using a dataset from Kaggle, comprising 19,000 job postings from the Armenian human resource portal CareerCenter during the years 2004-2015, JobConnect aims to offer invaluable insights to recruiters for seamlessly posting jobs on the job portal. By analyzing diverse fields including job titles, company information, employment terms, eligibility criteria, and application procedures, our application will provide recruiters with a robust platform to understand the intricacies of the local labor market dynamics.

## Introduction
JobConnect leverages comprehensive insights derived from years of online job postings to offer recruiters a competitive edge in the local job market. Our database application helps recruiters tailor job postings to meet the evolving needs of the job market, ensuring they attract the right talent for their organizations. It serves as an invaluable tool for recruiters, facilitating seamless job postings on the portal and enhancing their recruitment strategies.

## Objectives
The goal of this project is to create a user-friendly application for posting jobs using the Kaggle job posting dataset, with the intention of streamlining the laborious process of posting jobs for businesses and enhancing the job-searching experience for candidates. The application will:

* Ease the process of data entry.
* Categorize job posts.
* Offer advanced search and recommendation features for job seekers.
* Improve business efficiency and ensure a more accurate job-matching process.
* Provide data-driven insights to enhance recruitment strategies.
* Bridge the gap between employers and job seekers, helping to lower unemployment rates and promote economic growth.

## Usefulness
By streamlining the job posting process and improving the job search experience, JobConnect provides tremendous benefits. Its simple layout and practical functionality save time and effort for companies by:

* Efficient data input process.
* Categorizing job ads.
* Offering advanced search options.
* Ensuring a precise match between candidates and opportunities through sophisticated search filters.
* This user-centric approach caters to a wide range of users, including employers from different industries, hiring managers, and external contractors, making every post stand out and easily searchable.

## Tools/Database Technologies
We have used a SQL database to host all the data required for the application. The application was built using Streamlit which is an open-source Python library. All the CRUD operations were performed on this database using the SQL statements embedded in the main Python script (app.py file present in the repository).

### Tools Used
* Front End: Streamlit/Python
* Back End: Streamlit/Python
* Database: MySQL
* Tools: Visual Studio Code, MySQL Workbench, Google Colab
### Deployment Platform
* Streamlit cloud free tier
  
## Core Functionality
In this project, a web application was developed using Streamlit that interacts with a MySQL database for managing job postings. The core functionality revolves around CRUD operations:

* Create: The insert_job_post function allows for adding new job postings into the database. It ensures that all relevant details such as job title, duration, description, requirements, and company information are stored accurately.
* Read: Functions like fetch_data and get_job_post_by_id retrieve job postings from the database based on specific queries or IDs. This ensures users can view detailed information about job openings seamlessly.
* Update: The update_job_post function enables the modification of existing job postings. It allows for changes to job titles, descriptions, requirements, and other attributes while maintaining data consistency in the database.
* Delete: Using the deleteOperation function, job postings can be removed from the database by their unique identifier (ID). This ensures that outdated or no longer relevant job postings can be efficiently removed from the system.
These operations collectively support the application's functionality in managing job postings effectively, ensuring data integrity, and providing a user-friendly experience for interacting with job-related information.


* Dataset
The dataset, known as the "Job Posts dataset," comprises approximately 19,000 job postings that were originally published on the Armenian human resource portal, CareerCenter. These job postings were gathered from the Yahoo! mailing group, which served as the primary online platform for human resource-related activities during the early 2000s. The dataset reflects the years 2004 to 2015 and has undergone a cleaning process to eliminate posts that were unrelated to job listings or lacked a discernible structure. This dataset serves as a valuable resource for analyzing and understanding the evolution of job listings in the Armenian job market during the specified time period.

Link to the dataset: [Job Posts dataset](https://www.kaggle.com/datasets/madhab/jobposts)


Visit the JobConnect application [here](https://adtproject.streamlit.app/)

