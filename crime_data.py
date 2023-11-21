import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
df = pd.read_csv("Crime_Data_from_2020_to_Present_cleaned.csv")
pages = st.sidebar.radio("Select Page", ["Learn About data", "Descriptive Statistics", "Analysis", "Play With Me"])
if pages == "Learn About data":
    def main():
        st.header('Learn About data')
        st.image("crime.png")
        st.header("Crime Data from 2020 to Present In Los Angeles")
        st.write("""Crime, as a complex social phenomenon, is influenced by a myriad of factors including socio-economic conditions, geographical features, and community dynamics. Analyzing crime data becomes imperative to identify patterns and understand the underlying factors that contribute to the occurrence of criminal incidents. From the onset of 2020, Los Angeles has undergone notable changes and faced unique challenges, making an analysis of crime data during this period particularly relevant and insightful.""")
        st.header("Data Columns")
        st.write('''date_rptd : Date the crime was reported. This is when law enforcement or relevant authorities were made aware of the incident.

date_occ : Date of the actual occurrence of the crime. This is when the crime took place.

time_occ : Time of day when the crime occurred.

area_name : Name of the geographic area where the crime occurred. This could be a neighborhood, district, or other designated area.

part_1-2 : This is a categorical variable indicating whether the crime is of type "Part 1" or "Part 2." Part 1 crimes are more serious and include offenses like homicide and robbery, while Part 2 crimes are less serious and include offenses like simple assault and vandalism.

crm_cd_desc : Description of the crime code. This provides information about the type of crime that was committed.

vict_age : Age of the victim.

vict_sex : Gender of the victim.

vict_descent : Descent or ethnicity of the victim.

premis_desc : Description of the premises where the crime occurred. This could include information about whether it happened in a residence, business, street, etc.

weapon_desc : Description of the weapon, if any, used in the commission of the crime.

status_desc : Status of the crime report. This could indicate whether the case is open, closed, under investigation, etc.

location : Specific location where the crime occurred.

cross_street : The cross street or intersection near the location of the crime.

lat : Latitude coordinate of the crime location.

lon : Longitude coordinate of the crime location.

 ''')
        st.header("Data Location On Map")
        st.map(df[["lat", "lon"]])
    if __name__ == "__main__":
        main()
if pages == "Descriptive Statistics":
    def main():
        tab1, tab2 = st.tabs(["Statistics For Categorical", "Statistics For Numerical "])
        with tab1:
            st.dataframe(df.describe(include="O"))
            st.header("Value Counts For Each Categorical Column")
            categoricals = df.describe(include="O").columns
            for cat in categoricals:
                st.write(f"Value Counts For {cat.replace('_',' ')} :")
                dff = pd.DataFrame(df[cat].value_counts())
                dff.reset_index(inplace=True)
                dff.rename(columns={"index":cat,cat:f"count of {cat}"}, inplace=True)
                st.dataframe(dff)
        with tab2:
            st.dataframe(df.describe())
            st.header("Value Counts For Each Numerical Column")
            numericals = df.describe().columns
            for num in numericals:
                dff = pd.DataFrame(df[num].value_counts())
                dff.reset_index(inplace=True)
                dff.rename(columns={"index":num,num:f"count of {num}"}, inplace=True)
                st.dataframe(dff)
    if __name__ == "__main__":
        main()
if pages == "Analysis":
    def main():
        tab1, tab2 = st.tabs(["Uni-Variate Analysis", "Bi-Variate Analysis"])
        with tab1:
            st.header("Uni-Variate Analysis")
            st.image("vs.png")
            st.header("which area has most crimes ?")
            fig = px.histogram(df, df["area_name"], color_discrete_sequence=px.colors.qualitative.Dark24)
            fig.update_layout(xaxis_title_text='Area Name', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("What is the range of ages ?")
            fig = px.histogram(df, df["vict_age"])
            fig.update_layout(xaxis_title_text='Victim Range Of Ages')
            st.plotly_chart(fig)
            st.header("which age of victims has most crimes ?")
            fig = px.histogram(df["age_desc"], color_discrete_sequence=px.colors.qualitative.Dark24)
            fig.update_layout(xaxis_title_text='Age Description', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("what is the most victim sex ?")
            fig = px.histogram(df["vict_sex"], color_discrete_sequence=px.colors.qualitative.Dark24)
            fig.update_layout(xaxis_title_text='Victim Sex', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("what is the most victim descent ?")
            fig = px.histogram(df, df["vict_descent"], color_discrete_sequence=px.colors.qualitative.Dark24)
            fig.update_layout(xaxis_title_text='Victim Descent', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("what is the most year has crimes ?")
            fig = px.histogram(df, df["year"], color_discrete_sequence=px.colors.qualitative.Dark24)
            fig.update_layout(bargap = 0.2, yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("what is the most cases status ?")
            fig = px.histogram(df["status_desc"], color_discrete_sequence=px.colors.qualitative.Dark24)
            fig.update_layout(xaxis_title_text='Status Description', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("What is the most level of crime danger ?")
            fig = px.histogram(df["part_1-2"], color_discrete_sequence=px.colors.qualitative.Dark24)
            fig.update_layout(bargap = 0.2, xaxis_title_text="Level Of Crime Danger", yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header(" what is the 10 most days of the months has crimes ?")
            fig = px.histogram(df["10_days"], color_discrete_sequence=px.colors.qualitative.Dark24)
            fig.update_layout(xaxis_title_text='10 Days Of Months', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("what is most length between date of occurrence and reported date ?")
            dff_date_difference = df.groupby("date_difference")["vict_age"].count().sort_values(ascending = False).reset_index()
            dff_date_difference.rename(columns={"vict_age":"count of crimes"}, inplace=True)
            fig = px.histogram(dff_date_difference, x=dff_date_difference["date_difference"].head(25), y=dff_date_difference["count of crimes"].head(25), color_discrete_sequence=px.colors.qualitative.Dark24)
            fig.update_layout(xaxis_title_text='', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("which places have most crimes ?")
            dff_pr = df.groupby("premis_desc")["vict_age"].count().sort_values(ascending = False).reset_index()
            dff_pr.rename(columns={"vict_age":"count of crimes"}, inplace=True)
            fig = px.histogram(dff_pr, x=dff_pr["premis_desc"].head(25), y=dff_pr["count of crimes"].head(25), color_discrete_sequence=px.colors.qualitative.Dark24)
            fig.update_layout(xaxis_title_text='', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("what is most crimes happend ?")
            dff_cim_desc = df.groupby("crm_cd_desc")["vict_age"].count().sort_values(ascending = False).reset_index()
            dff_cim_desc.rename(columns={"vict_age":"count of crimes"}, inplace=True)
            fig = px.histogram(x=dff_cim_desc["crm_cd_desc"].head(10), y=dff_cim_desc["count of crimes"].head(10), color_discrete_sequence=px.colors.qualitative.Dark24)
            fig.update_layout(xaxis_title_text='', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("What are the most commonly used weapons?")
            dff_weapon_desc = df.groupby("weapon_desc")["vict_age"].count().sort_values(ascending = False).reset_index()
            dff_weapon_desc.rename(columns={"vict_age":"count of crimes"}, inplace=True)
            fig = px.histogram(x=dff_weapon_desc["weapon_desc"].head(10), y=dff_cim_desc["count of crimes"].head(10), color_discrete_sequence=px.colors.qualitative.Dark24)
            fig.update_layout(xaxis_title_text='', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
        with tab2:
            st.header("Bi-Variate Analysis")
            st.image("vs.png")
            st.header("which area has most serious crimes ?")
            fig = px.histogram(df ,x=df["area_name"] ,color=df["part_1-2"] ,color_discrete_sequence=["rgb(55,126,184)", "rgb(228,26,28)"], barmode="group" )
            fig.update_layout(xaxis_title_text='Area name And Dangerous Level', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("which victim sex has most serious crimes ?")
            fig = px.histogram(df ,x=df["vict_sex"] ,color=df["part_1-2"] ,color_discrete_sequence=["rgb(55,126,184)", "rgb(228,26,28)"] ,barmode="group")
            fig.update_layout(xaxis_title_text='Victim Sex And Dangerous Level', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("which quarter of the year has a serious  crimes ?")
            fig = px.histogram(df ,x=df["year_quarter"] ,color=df["part_1-2"] ,color_discrete_sequence=["rgb(55,126,184)", "rgb(228,26,28)"] ,barmode="group")
            fig.update_layout(xaxis_title_text='Year Quarter And Dangerous Level', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("which 10 days of the month has a serious crimes ?")
            fig = px.histogram(df ,x=df["10_days"] ,color=df["part_1-2"] ,color_discrete_sequence=["rgb(55,126,184)", "rgb(228,26,28)"] ,barmode="group")
            fig.update_layout(xaxis_title_text='10 Days of Month And Dangerous Level', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("which year has a lot of serious  crimes ?")
            fig = px.histogram(df ,x=df["year"] ,color=df["part_1-2"] ,color_discrete_sequence=["rgb(55,126,184)", "rgb(228,26,28)"] ,barmode="group")
            fig.update_layout(xaxis_title_text='Year And Dangerous Level', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("what is serious level for each status ?")
            fig = px.histogram(df ,x=df["status_desc"] ,color=df["part_1-2"] ,color_discrete_sequence=["rgb(55,126,184)", "rgb(228,26,28)"], barmode="group" )
            fig.update_layout(xaxis_title_text='Status And Dangerous Level', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("what most victim descent has dangours crimes ?")
            fig = px.histogram(df ,x=df["vict_descent"] ,color=df["part_1-2"] ,color_discrete_sequence=["rgb(55,126,184)", "rgb(228,26,28)"], barmode="group" )
            fig.update_layout(xaxis_title_text='Victim Descent And Dangerous Level', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("what most victim age has dangours crimes ?")
            fig = px.histogram(df ,x=df["age_desc"] ,color=df["part_1-2"] ,color_discrete_sequence=["rgb(55,126,184)", "rgb(228,26,28)"], barmode="group" )
            fig.update_layout(xaxis_title_text='Victim Age And Dangerous Level', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("which victim sex has most crimes in each area ?")
            fig = px.histogram(df ,x=df["area_name"] ,color=df["vict_sex"] ,color_discrete_sequence=px.colors.qualitative.Set1, barmode="group" )
            fig.update_layout(xaxis_title_text='Area Name And Victim Sex', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("which victim age has most crimes in each area ?")
            fig = px.histogram(df ,x=df["area_name"] ,color=df["age_desc"] ,color_discrete_sequence=px.colors.qualitative.Set1, barmode="group" )
            fig.update_layout(xaxis_title_text='Area Name And Victim Age', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("which area has most closed cases ?")
            fig = px.histogram(df ,x=df["area_name"] ,color=df["status_desc"] ,color_discrete_sequence=px.colors.qualitative.Set1, barmode="group" )
            fig.update_layout(xaxis_title_text='Area Name And Status Description', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("quarter of year by area")
            fig = px.histogram(df ,x=df["area_name"] ,color=df["year_quarter"] ,color_discrete_sequence=px.colors.qualitative.Set1, barmode="group" )
            fig.update_layout(xaxis_title_text='Area Name And Year Quarter', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("10 days of month by area ")
            fig = px.histogram(df ,x=df["area_name"] ,color=df["10_days"] ,color_discrete_sequence=px.colors.qualitative.Set1, barmode="group" )
            fig.update_layout(xaxis_title_text='Area Name And 10 Days Of The Month', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("year by area ")
            fig = px.histogram(df ,x=df["area_name"] ,color=df["year"] ,color_discrete_sequence=px.colors.qualitative.Set1, barmode="group" )
            fig.update_layout(xaxis_title_text='Area Name And Year', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("which most age victim in each area ?")
            fig = px.histogram(df ,x=df["area_name"] ,color=df["age_desc"] ,color_discrete_sequence=px.colors.qualitative.Set1, barmode="group" )
            fig.update_layout(xaxis_title_text='Area Name And Victim Age', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("what is the most victim age for each gender ?")
            fig = px.histogram(df ,x=df["vict_sex"] ,color=df["age_desc"] ,color_discrete_sequence=px.colors.qualitative.Set1, barmode="group" )
            fig.update_layout(xaxis_title_text='Victim Sex And Victim Age', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("which year has most crimes by quarter ?")
            fig = px.histogram(df ,color=df["year_quarter"] ,x=df["year"] ,color_discrete_sequence=px.colors.qualitative.Set1, barmode="group" )
            fig.update_layout(xaxis_title_text='Year And Year Quarter', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
            st.header("which sex has most crimes by year ?")
            fig = px.histogram(df ,color=df["vict_sex"] ,x=df["year"] ,color_discrete_sequence=px.colors.qualitative.Set1, barmode="group" )
            fig.update_layout(xaxis_title_text='Victim Sex And Year', yaxis_title_text='Count Of Crimes')
            st.plotly_chart(fig)
    if __name__ == "__main__":
        main()
if pages == "Play With Me":
    def main():
        st.header("Lets Have Some Fun")
        st.image("l.jpg")
        st.header("Do You Think You Have Better Insights ?")
        st.header("Show Me")
        plots = ["histogram", "box plot", "violin plot"]
        ch_plot = st.selectbox('Select a plot', plots) 
        my_columns = ["None"]
        for e in df.columns:
            my_columns.append(e)
        x_c =  st.selectbox('Select X Axis column' , my_columns) 
        y_c =  st.selectbox('Select Y Axis column' , my_columns)
        col =  st.selectbox('Select Color column' , my_columns)
        user_input = st.text_input("Enter your question here")
        if user_input:
            if user_input[-1] == "?":
                st.write(user_input)
            else:
                st.write(f"{user_input} ?")
        if ch_plot == "histogram" :
            if  x_c == "None" and y_c == "None" and col == "None":
                st.header("Still Thinking !?")
            elif y_c == "None" and col == "None":
                fig = px.histogram(x=df[x_c])
                st.plotly_chart(fig)
            elif  x_c == "None" and col == "None":
                fig = histogram(x=df[y_c])
                st.plotly_chart(fig)
            elif x_c == "None":
                fig = px.histogram(y=df[y_c], color=df[col])
                st.plotly_chart(fig)
            elif y_c == "None":
                fig = px.histogram(y=df[x_c], color=df[col])
                st.plotly_chart(fig)
        elif ch_plot == "box plot" :
            if  x_c == "None" and y_c == "None" and col == "None":
                st.header("Still Thinking !?")
            elif y_c == "None" and col == "None":
                fig = px.box(x=df[x_c])
                st.plotly_chart(fig)
            elif  x_c == "None" and col == "None":
                fig = box(x=df[y_c])
                st.plotly_chart(fig)
            elif x_c == "None":
                fig = px.box(y=df[y_c], color=df[col])
                st.plotly_chart(fig)
            elif y_c == "None":
                fig = px.box(y=df[x_c], color=df[col])
                st.plotly_chart(fig)
        else :
            if  x_c == "None" and y_c == "None" and col == "None":
                st.header("Still Thinking !?")
            elif y_c == "None" and col == "None":
                fig = px.violin(x=df[x_c])
                st.plotly_chart(fig)
            elif  x_c == "None" and col == "None":
                fig = px.violin(x=df[y_c])
                st.plotly_chart(fig)
            elif x_c == "None":
                fig = px.violin(y=df[y_c], color=df[col])
                st.plotly_chart(fig)
            elif y_c == "None":
                fig = px.violin(y=df[x_c], color=df[col])
                st.plotly_chart(fig)
    if __name__ == "__main__":
        main()
