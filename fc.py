import pandas as pd
import  plotly.express as px
import  plotly.graph_objects as go
import  numpy as np



def encrypt_string(input_string):
    encrypted_string = ""
    for char in input_string:
        shifted_char = chr((ord(char) + 2))
        encrypted_string += shifted_char
    return encrypted_string
def decrypt_string(input_string):
    decrypted_string = ""
    for char in input_string:
        shifted_char = chr((ord(char) - 2))
        decrypted_string += shifted_char
    return decrypted_string



def update(name , email , feedback):
    str = encrypt_string(email)
    dict = {"Name" :[name] , "Email" : [str] , "Feedback" : [feedback]}
    new = pd.DataFrame(dict);
    df = pd.read_csv('Datasets/feedback.csv')
    df = df.drop('Unnamed: 0' ,axis='columns');
    df = pd.concat([new , df] , axis=0)
    df.to_csv('Datasets/feedback.csv');


def updatec(name , email , feedback):
    str = encrypt_string(email)
    dict = {"Name" :[name] , "Email" : [str] , "Contribution Link" : [feedback]}
    new = pd.DataFrame(dict);
    df = pd.read_csv('Datasets/contribution.csv')
    df = df.drop('Unnamed: 0' ,axis='columns');
    df = pd.concat([new , df] , axis=0)
    df.to_csv('Datasets/contribution.csv');







if __name__ == '__main__':
    print(encrypt_string('ranitdas24@gmail.com'))