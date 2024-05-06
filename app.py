import streamlit as st
import pandas as pd
import  awa , overall , castwise;
import  random;

import fc

area = pd.read_csv('Datasets/Distdata.csv');
area = awa.preProcessing(area);
st.set_page_config(layout="wide")
st.title("Student Drop Out Analysis" )
st.header("")
menu = st.sidebar.radio(
    'Select option',
    ('Home' , 'Overall Analysis' , 'Area wise Analysis' , 'School wise Analysis' , 'Cast wise Analysis' , 'Feedback', 'Contribute')
)

if menu == 'Home':
    st.header('🤔 Why dropout analysis is important ?')
    st.markdown("👉 Student dropout analysis is crucial in a country as it provides valuable insights into the effectiveness of its education system and the challenges students face. Understanding the reasons behind student dropouts helps policymakers and educators identify and address systemic issues such as inadequate infrastructure, curriculum relevance, teacher quality, and socioeconomic disparities. By reducing dropout rates, a country can enhance its workforce's skills and productivity, promote social equity, and support mechanisms to prevent students from leaving school prematurely, ensuring that more individuals have access to quality education and the opportunities.")
    st.header('🤓 Why we choose analysis on West Bengal ?')
    st.markdown("👉 Because we are from West Bengal , that’s why we have domain knowledge about our state.We have ideas about our local employment status, financial conditions of different regions(Urban and Rural Area) in West Bengal.")
    st.header('🧐 What we have analysed : ')
    st.markdown("👉 According to our acquired data , we got district wise dropout rates and school wise enrollment data , cast and age , gender wise data . By these we made graphs and bars according to the data to visualize the whole scenario . and compare between two entities and give some reason why they are different from each other .")
    st.header("😞 Our Limitations : ")
    st.markdown("👉 The data about the  dropout rate and dropout students’ survey report of a state is confidential so that our data may not be accurate in some places. Due to lack of time, we are not able to make the user interface good enough and we mainly focused on the backend.")
    st.header('🤗 Our Future Vision :')
    st.markdown("👉 If we get proper dataset about ,Student dropout number, employment status of the family members of the students  from the government surveys, we can be able to predict the dropout rate of a particular area , if a student may drop or not  in the upcoming years. Thus we can cooperate with the NGOs to reduce the dropout rate of the particular area.")
    pass
elif menu == 'Overall Analysis':
    cl1 , cl2 , cl3= st.columns(3);
    with cl1:
        st.header('Analysis of the State')
        st.title('West Bengal')
    with cl2:
        st.header('Total District')
        st.title(area['District Name'].unique().shape[0])
    t1 , t2 ,t3 = overall.tables();
    with cl3:
        st.header('Analysed Total School')
        st.title('219')
    st.header('Key factors : ')
    st.table(t1)
    st.header("Example : ")
    fig1 , fig2 = awa.distGraph(area , 'Purba Medinipur');
    st.plotly_chart(fig1)
    st.header('Reasons of Dropout Before Covid-19 : ')
    st.table(t2)
    st.header('Reason of Dropout rate During Covid-19')
    st.table(t3)


    pass
elif menu == 'Area wise Analysis':
    st.header('District wise Analysis : ')
    ls = awa.disList(area);
    ls.insert(0,'overall')
    dist = st.selectbox('Select District' ,ls )
    if dist =='overall':
        fig1, fig2= awa.overallGraph(area);
        st.plotly_chart(fig1)
        st.plotly_chart(fig2)
    else:
        avg , stravg , avgt = awa.distvals(area , dist);
        col1 , col2 , col3= st.columns(3);
        with col1:
            st.header('Average student count ')
            st.title('{0:.2f}'.format(avg))
        with col2:
            st.header('average Teacher count')
            st.title('{0:.2f}'.format(avgt));
        with col3:
            st.header('Average student teacher ratio')
            st.title('{0:.2f}'.format(stravg))

        fg1 , fg2 = awa.distGraph(area , dist);
        st.plotly_chart(fg1);
        st.plotly_chart(fg2);
    st.header("Compare Two district : ")
    col1 , col2 = st.columns(2);
    lis1 = awa.disList(area)
    lis2 = awa.disList(area)

    with col1:
        dist1 = st.selectbox('Select First Distroce : ' , lis1);
    with col2:
        dist2 = st.selectbox('Select Second District ' , lis2);

    btn = st.button('Compare', type='primary');
    if btn:
        if dist1 == dist2:
            st.header("[ERROR!] Both District are same , Please select Different!")
        else:
            fig = awa.compDist(area , dist1 , dist2);
            st.plotly_chart(fig);




    pass
elif menu == 'School wise Analysis':
    pass
elif menu == 'Cast wise Analysis':
    cast = castwise.getdf();
    lis1 =castwise.getList(cast);
    lis2 =castwise.getList(cast);
    lis2.insert(0,'overall');
    st.header('Caste wise Analysis : ')
    dist = st.selectbox('Select Caste', lis2);
    if dist == 'overall':
        fig5 = castwise.overallGraph(cast);
        st.plotly_chart(fig5);
    else:
        fig1 = castwise.GetGraph(cast , dist)
        st.plotly_chart(fig1);
    lis1.sort();
    st.header('Compare two Caste : ')
    col1, col2 = st.columns(2);
    with col1:
        dist1 = st.selectbox('Select First Caste : ' , lis1);
    with col2:
        dist2 = st.selectbox('Select Second Caste ' , lis1);
    btn = st.button('Compare', type='primary');


    if btn:
        if dist1 == dist2:
            st.header("[ERROR!] Both District are same , Please select Different!")
        else:
            fig = castwise.compCast(cast , dist1 , dist2);
            st.plotly_chart(fig);
    pass
elif menu == 'Feedback':
    st.header('Suggestions are always open!')
    nme1 = st.text_input("Enter Your name" , placeholder="ex: Ranit Das")
    email1 = st.text_input("Enter Your Email id " , placeholder="example@gmail.com")
    txt = st.text_area('Give us Your Feedback',placeholder= "The data analytics website provides a user-friendly interface with effective data visualization and analysis tools, making it easy for users to gain insights. However, there is room for improvement in optimizing data import and processing speed, particularly when handling larger datasets, to enhance overall performance and usability.")
    btn1 = st.button('Submit' , type='primary')
    if btn1:
        if (len(nme1) == 0 or len(email1) == 0 or len(txt) == 0):
            st.markdown('You have filled **Incomplete Data !**')
        else:
            # st.markdown(f"You Entered :{nme1} {email1} {txt}");
            fc.update(nme1 , email1 , txt);
            # df = pd.read_csv('Datasets/feedback.csv')
            # st.table(df.drop('Unnamed: 0' ,axis='columns'))
            st.header('Thank You for Your Feedback!')
            pass;

    pass

elif menu == 'Contribute':
    st.header('You are welcome to contribute !')
    nme2 = st.text_input("Enter Your name : ", placeholder="ex: Ranit Das")
    email2 = st.text_input("Enter Your Email id : ", placeholder="example@gmail.com")
    link = st.text_input("Enter Drive Link ",
                         placeholder="ex : https://drive.google.com/file/d/1TA47-oROWakfU1KEpLRY08L4fgmDUNuV/view")
    btn2 = st.button('Contribute', type='primary')
    if btn2:
        if (len(nme2) == 0 or len(email2) == 0 or len(link) == 0):
            st.markdown('You have filled **Incomplete Data !**');
        else:
            fc.updatec(nme2 , email2 , link);
            # df = pd.read_csv('Datasets/contribution.csv')
            # st.table(df.drop('Unnamed: 0' ,axis='columns'))
            st.header('Thank You for Your Contribution!')
            pass;

    pass;