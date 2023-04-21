#input_value = input("M or F\n")
#count_employees = df_employee.loc[df_employee['Sex'] == input_value.upper()]
#print(len(count_employees))
#input_value = input("Which job title?\n")
#count_jobtitle = count_employees.loc[df_employee['JobTitle'] == input_value.title()]
#print(len(count_jobtitle))
#input_value = input("What is their start year?\n")
#count_start_year = count_jobtitle.loc[df_employee['StartYear'] == int(input_value)]
#print(count_start_year)

import pandas as pd
import time

df_employee = pd.read_csv('Employee+Demographics.csv')
type(df_employee)

def get_job_title(df_filter):
    input_value = input("Enter job title?\n")
    job_title = input_value
    df_filter = df_filter.loc[df_employee['JobTitle'] == job_title.title()]
    return job_title, df_filter

def get_job_title_count(job_title, df_filter):
    count_jobtitle = df_filter.loc[df_employee['JobTitle'] == job_title.title()]
    count_jobtitle = (len(count_jobtitle))
    return count_jobtitle

def get_job_title_list(job_title, df_filter):
    list_jobtitle = df_filter.loc[df_employee['JobTitle'] == job_title.title()]
    return list_jobtitle

def get_sex(df_filter):
    input_value = input("Enter sex (M or F):\n")
    sex = input_value
    df_filter = df_filter.loc[df_employee['Sex'] == sex.upper()]
    return sex, df_filter

def get_sex_count(sex, df_filter):
    count_sex = df_filter.loc[df_employee['Sex'] == sex.upper()]
    count_sex = (len(count_sex))
    return count_sex

def get_sex_list(sex, df_filter):
    list_sex = df_filter.loc[df_employee['Sex'] == sex.upper()]
    return list_sex

def get_race(df_filter):
    input_value = input("Enter race:\n")
    race = input_value
    df_filter = df_filter.loc[df_employee['Race'] == race]
    return race, df_filter

def get_race_count(race, df_filter):
    count_race = df_filter.loc[df_employee['Race'] == race]
    count_race = (len(count_race))
    return count_race

def get_race_list(race, df_filter):
    list_race = df_filter.loc[df_employee['Race'] == race]
    return list_race

def get_job_type(df_filter):
    input_value = input("Enter job type:\n")
    job_type = input_value
    df_filter = df_filter.loc[df_employee['JobType'] == job_type]
    return job_type, df_filter

def get_job_type_count(job_type, df_filter):
    count_job_type = df_filter.loc[df_employee['JobType'] == job_type]
    count_job_type = (len(count_job_type))
    return count_job_type

def get_job_type_list(job_type, df_filter):
    list_job_type = df_filter.loc[df_employee['JobType'] == job_type]
    return list_job_type

def get_start_year(df_filter):
    input_value = input("Enter start year:\n")
    start_year = input_value
    df_filter = df_filter.loc[df_employee['StartYear'] == start_year]
    return start_year, df_filter

def get_start_year_count(StartYear, df_filter):
    count_start_year = df_filter.loc[df_employee['StartYear'] == StartYear]
    count_start_year = (len(count_start_year))
    return count_start_year

def get_start_year_list(StartYear, df_filter):
    list_start_year = df_filter.loc[df_employee['StartYear'] == StartYear]
    return list_start_year



def main():
    print('What are you searching for?')
    
    while True:    
        input_value = input('\n1:Job Titles\n2:Sex\n3:Race\n4:Job Type\n5:Start Year\n')

        if input_value == "1":
            df_filter = df_employee
            job_title, df_filter = get_job_title(df_filter)
            input_value = input('\n1:Count\n2:List\n3:Filter Further\n')
            if input_value == '1':
                job_count = get_job_title_count(job_title, df_filter)
                print(f'There are {job_count} listed under {job_title}.')
            if input_value == '2':
                job_list = get_job_title_list(job_title, df_filter)
                print(f'Here is a list of {job_title}s:')
                time.sleep(5)
                print(job_list)
            if input_value == '3':
                input_value = input('\n1:Sex\n2:Race\n3:Job Type\n4:Start Year\n')
                if input_value == '1':
                    sex, df_filter = get_sex(df_filter)
                    input_value = input('\n1:Count\n2:List\n3:Filter Further\n')
                    if input_value == '1':
                        sex_count = get_sex_count(sex, df_filter)
                        print(f'There are {sex_count} listed using these parameters.\n')
                    if input_value == '2':
                        sex_list = get_sex_list(sex, df_filter)
                        time.sleep(5)
                        print(sex_list)
                    if input_value == '3':
                        input_value = input('\n1:Race\n2:Job Type\n3:Start Year\n')
                        if input_value == '1':
                            race, df_filter = get_race(df_filter)
                            input_value = input('\n1:Count\n2:List\n3:Filter Further\n')
                            if input_value == '1':
                                race_count = get_race_count(race, df_filter)
                                print(f'There are {race_count} listed using these parameters.\n')
                            if input_value == '2':
                                race_list = get_race_list(race, df_filter)
                                time.sleep(5)
                                print(race_list)
                            if input_value == '3':
                                input_value = input('\n1:Job Type\n2:Start Year\n')
                                if input_value == '1':
                                    job_type, df_filter = get_job_type(df_filter)
                                    input_value = input('\n1:Count\n2:List\n3:Filter Further\n')
                                    if input_value == '1':
                                        job_type_count = get_job_type_count(job_type, df_filter)
                                        print(f'There are {job_type_count} listed using these parameters.\n')
                                    if input_value == '2':
                                        job_type_list = get_job_type_list(job_type, df_filter)
                                        time.sleep(5)
                                        print(job_type_list)
                                    if input_value == '3':
                                        start_year, df_filter = get_start_year(df_filter)
                                        input_value = input('\n1:Count\n2:List\n')
                                        if input_value == '1':
                                            start_year_count = get_start_year_count(start_year, df_filter)
                                            print(f'There are {start_year_count} listed using these parameters.\n')
                                        if input_value == '2':
                                            start_year_list = get_start_year_list(start_year, df_filter)
                                            time.sleep(5)
                                            print(start_year_list)
                                            time.sleep(10)
                                            continue



                    
                    
main()


    
        

