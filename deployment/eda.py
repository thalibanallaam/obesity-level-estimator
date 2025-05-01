# Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

def run():
    # Title
    st.title('Estimation of Obesity Levels Based On Eating Habits and Physical Condition')

    # Front Image
    img = Image.open('BMI-1024x569.png')
    st.image(img)

    # Load Data
    st.write('# Dataset')
    df = pd.read_csv('ObesityDataSet_raw_and_data_sinthetic.csv')
    st.dataframe(df)
    st.markdown('''
    **Description:** 
                
    The dataset contains information regarding an individual's obesity level based on their physical condition 
                and daily habits. The people in the dataset represents people from Mexico, Peru, and Colombia. 
                The data was collected through a web platform survey and the final result was a total of 2111 entries 
                with 17 features. The features represents the individual's physical condition as well as their daily 
                habits. The target is "Obesity Level" which is represented by NObesity in the original dataset and divided 
                into seven different classes, including `Insufficient Weight`, `Normal Weight`, `Overweight Level I`, 
                `Overweight Level II`, `Obesity Type I`, `Obesity Type II` and `Obesity Type III`.
    ''')

    # Interactive exploration - Choose the chart you want to view
    st.write('# Explore Obesity Levels')
    option = st.selectbox('Choose the feature: ', ['Amount', 'Gender', 'Age', 'Family History'])
    
    # Conditional plotting based on the previous interactive exploration
    if option == 'Amount':
        # Plot 1 - Amount
        # Calculate obesity level counts
        obesity_counts = df['Obesity Level'].value_counts()
        # Create the pie chart
        fig1 = px.pie(
        obesity_counts,
        values=obesity_counts.values, 
        names=obesity_counts.index,
        title='Distribution of Individuals by Obesity Level')
        # Display the chart in Streamlit
        st.plotly_chart(fig1)
        st.markdown('''
        **Insights:**
        - Obesity type I has the most patient with 351 followed by obesity type III and II with 324 and 297 patients respectively.
        - Based on the pie chart, the majority of people are unhealthy (either suffering from overweight, obesity, or
                    insufficient weight). Only the minority of the people (13.5%) are considered healthy.
        - The amount of patients is spread relatively even between each levels, but a bit higher in the higher spectrum. 
                    This is concerning and we should find out why more people are suffering from obesity compared to the healthy ones.
        ''')

    elif option == 'Gender':
        # Plot 2 - Gender
        # Define the figure
        fig2 = px.histogram(df, x="Obesity Level", color="Gender", 
                title="Obesity Levels based on Gender",
                labels={"Obesity Level": "Obesity Level", "Gender": "Gender"},
                category_orders={"Obesity Level": ['Insufficient_Weight', 'Normal_Weight', 
                                                    'Overweight_Level_I', 'Overweight_Level_II', 
                                                    'Obesity_Type_I', 'Obesity_Type_II', 
                                                    'Obesity_Type_III']})
        # Show in Streamlit
        st.plotly_chart(fig2)
        st.markdown('''
        **Insights:**
        - For males and females, the distribution of amount between each level is relatively similar, except for obesity type II and III.
        - There are more males suffering from obesity type II compared to the other levels, whereas for females, they only have two 
                    people suffering from it.
        - On the contrary, more females are suffering from obesity type III compared to the other levels, whereas for males, there is 
                    only one person suffering from it.
        - Based on the results, female are more prone to suffer obesity compared to male due to their high amount in the higher end 
                    of the spectrum.
        ''')

    elif option == 'Age':
        # Plot 3 - Age
        # Define age groups
        age_bins = [0, 25, 35, 45, 55, 65, 100]  
        age_labels = ['0-24', '25-34', '35-44', '45-54', '55-64', '65+']
        df['Age Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)

        # Create the bar chart
        fig3 = px.bar(
            df, 
            x='Age Group', 
            color='Obesity Level',  
            title='Obesity Levels Across Age Groups',
            labels={'count':'Number of Individuals'}, # Customize axis labels if needed
            category_orders={"Age Group": age_labels}, # Ensure age group order
        )
        # Customize layout for better readability
        fig3.update_layout(
            xaxis_title='Age Group',
            yaxis_title='Number of Individuals',
            legend_title='Obesity Level',
            xaxis={'tickangle': -45},  # Rotate x-axis labels for readability
        )
        # Show in Streamlit
        st.plotly_chart(fig3)
        st.markdown('''
        **Insights:**
        - Most kids and young adults (0-24) don't suffer as much from obesity compared to the other age groups. 
                    Instead, a large part of them actually suffers from insufficient weight. The reason for this 
                    is most likely due to nutrition deficiency.
        - Obesity is more prone to adults (25-34) compared to other age groups.
        - The amount of obesity patients starts to fade as the age group progress to older ages. The majority of 
                    obesity patients comes from younger fellows.
        ''')

    elif option == 'Family History':
        # Define the figure
        fig4 = px.bar(df, x="Overweight Family History", color="Obesity Level", 
        title="Obesity Levels Based on Family Overweight History",
        barmode='group',  # or 'stack' for stacked bars
        labels={'Overweight Family History': 'Family History', 'count': 'Number of Individuals'})

        # Show in Streamlit
        st.plotly_chart(fig4)
        st.markdown('''
        **Insights:**
        - People with a history of overweight family members have more obese patients compared to the people with no 
                    history of overweight family members.
        - The majority of people with no history of overweight family members are either normal or has insufficient weight.
        - People with a history of overweight family members are more likely to have overweight. There are two possible reasons for this.
            1. There is a genetic influence that may have cause them to get overweight easier.
            2. Bad diet that has become a habit among the family.
        ''')

if __name__ == '__main__':
    run()