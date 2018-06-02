
# coding: utf-8

# In[2]:


from pandas import DataFrame,Series
import pandas as pd
import numpy as np


# In[3]:


review_data_list = []
app_source_list = []
app_file_name_list = []
app_rating_list = []
app_size_list = []
for i in range(0, 1021):
    index = i + 8240
#     print(index)
    review_data_list.append(pd.read_csv("app-review-data/data/export-" + str(index) + "-all-full.csv"))
    if i == 0:
        review_data = DataFrame(review_data_list[i], columns=["Source","Date","Name","Title","Content","Rating","App_Name_Categorical"])
    else :
        temp_review_data = DataFrame(review_data_list[i], columns=["Source","Date","Name","Title","Content","Rating"])
        review_data  = pd.concat([temp_review_data, review_data]).reset_index(drop=True)
    app_source_list.append(review_data_list[i]["Source"][0])
    app_file_name_list.append("export-" + str(index) + "-all-full")
    review_rating_array = np.array(review_data_list[i]["Rating"])
    app_rating_list.append(np.mean(review_rating_array))
    app_size_list.append(review_data_list[i]["Source"].size)

review_data.shape
# print(review_data)


# In[487]:


review_data.to_csv("app-review-data/review-data-origin.csv")


# In[488]:


raw_app_data = {"Source": app_source_list,
                "Rating": app_rating_list,
                "Size": app_size_list,
                "FileName": app_file_name_list}
app_data = DataFrame(raw_app_data, columns=["Source","Rating","Size","FileName"])
app_data.shape
# print(app_data)


# In[489]:


app_data.to_csv("app-review-data/app-data.csv")


# In[490]:


origin_review_data = review_data
print(origin_review_data.shape)
origin_review_data.head()


# In[491]:


# review_data["Content"] = review_data["Content(Origin)"].copy()
# review_data["Title"] = review_data["Title(Origin)"].copy()


# In[492]:


review_data["Content(Origin)"] = review_data["Content"].copy()

print(review_data.shape)
review_data[["Content", "Content(Origin)"]].head()


# In[493]:


review_data["Title(Origin)"] = review_data["Title"].copy()

print(review_data.shape)
review_data[["Title", "Title(Origin)"]].head()


# In[494]:


def clean_purchase_text(content):
    content = str(content)
    word1 = "내역"
    word2 = "구매"
    word3 = "용량"
    word4 = "삭제"
    if word1 in content :
        return 0
    elif word2 in content :
        return 0
    elif word3 in content :
        return 0
    elif word4 in content :
        return 0
    else : 
        return content


# In[496]:


review_data["Content"] = review_data["Content"].apply(clean_purchase_text)
print(review_data[review_data["Content"] == "0"].shape)


# In[498]:


review_data["Title"] = review_data["Title"].apply(clean_purchase_text)
print(review_data[review_data["Title"] == "0"].shape)


# In[499]:


review_data.loc[review_data["Title"] == "0", "Content"] = "0"
print(review_data[review_data["Content"] == "0"].shape)


# In[500]:


print(review_data[review_data["Content"] != "0"].shape)


# In[501]:


review_data_except_purchase = DataFrame(review_data[review_data["Content"] != "0"], columns=["Source","Date","Name","Title","Content","Rating"])
print(review_data_except_purchase.shape)
review_data_except_purchase.head()


# In[502]:


def clean_exchange_text(content):
    content = str(content)
    word1 = "환불"
    if word1 in content :
        return 0
    else :
        return content


# In[503]:


print(review_data_except_purchase.shape)
review_data_except_purchase.head()


# In[504]:


review_data_except_purchase["Rating_5_Content"] = review_data_except_purchase["Content"]


# In[506]:


review_data_except_purchase["Rating_5_Content"] = review_data_except_purchase[review_data_except_purchase["Rating"] == 5]["Rating_5_Content"].apply(clean_exchange_text)
print(review_data_except_purchase[review_data_except_purchase["Rating_5_Content"] == "0"].shape)


# In[507]:


review_data_except_purchase["Rating_4_Content"] = review_data_except_purchase["Content"]


# In[509]:


review_data_except_purchase["Rating_4_Content"] = review_data_except_purchase[review_data_except_purchase["Rating"] == 4]["Rating_4_Content"].apply(clean_exchange_text)
print(review_data_except_purchase[review_data_except_purchase["Rating_4_Content"] == "0"].shape)


# In[510]:


review_data_except_purchase.head()


# In[511]:


review_data_except_purchase.loc[review_data_except_purchase["Rating_4_Content"] == "0", "Content"] = "0"
review_data_except_purchase.loc[review_data_except_purchase["Rating_5_Content"] == "0", "Content"] = "0"
print(review_data_except_purchase[review_data_except_purchase["Content"] == "0"].shape)


# In[512]:


review_data_except = DataFrame(review_data_except_purchase[review_data_except_purchase["Content"] != "0"], columns=["Source","Date","Name","Title","Content","Rating"])
print(review_data_except.shape)
review_data_except.head()


# In[513]:


rating_1 = review_data_except[review_data_except["Rating"] == 1]
rating_2 = review_data_except[review_data_except["Rating"] == 2]
rating_3 = review_data_except[review_data_except["Rating"] == 3]
rating_4 = review_data_except[review_data_except["Rating"] == 4]
rating_5 = review_data_except[review_data_except["Rating"] == 5]


# In[514]:


print("Rating_1_Size : " + str(rating_1["Rating"].size) + "   |   Rating_1_Percent : " + str((rating_1["Rating"].size / review_data_except["Rating"].size) * 100))
print("Rating_2_Size : " + str(rating_2["Rating"].size) + "   |   Rating_2_Percent : " + str((rating_2["Rating"].size / review_data_except["Rating"].size) * 100))
print("Rating_3_Size : " + str(rating_3["Rating"].size) + "   |   Rating_3_Percent : " + str((rating_3["Rating"].size / review_data_except["Rating"].size) * 100))
print("Rating_4_Size : " + str(rating_4["Rating"].size) + "   |   Rating_4_Percent : " + str((rating_4["Rating"].size / review_data_except["Rating"].size) * 100))
print("Rating_5_Size : " + str(rating_5["Rating"].size) + "   |   Rating_5_Percent : " + str((rating_5["Rating"].size / review_data_except["Rating"].size) * 100))


# In[515]:


review_data_rating_except_rating_5 = DataFrame(review_data_except[review_data_except["Rating"] != 5], columns=["Source","Date","Name","Title","Content","Rating"])
print(review_data_rating_except_rating_5.shape)
sample_review_data_rating_5 = DataFrame(review_data_except[review_data_except["Rating"] == 5].sample(n=85942), columns=["Source","Date","Name","Title","Content","Rating"])
print(sample_review_data_rating_5.shape)
review_data_except = pd.concat([review_data_rating_except_rating_5, sample_review_data_rating_5]).reset_index(drop=True)
print(review_data_except.shape)


# In[516]:


review_data_rating_except_rating_3 = DataFrame(review_data_except[review_data_except["Rating"] != 3], columns=["Source","Date","Name","Title","Content","Rating"])
print(review_data_rating_except_rating_3.shape)
sample_review_data_rating_3 = DataFrame(review_data_except[review_data_except["Rating"] == 3].sample(n=18336), columns=["Source","Date","Name","Title","Content","Rating"])
print(sample_review_data_rating_3.shape)
review_data_except = pd.concat([review_data_rating_except_rating_3, sample_review_data_rating_3]).reset_index(drop=True)
print(review_data_except.shape)


# In[517]:


rating_1 = review_data_except[review_data_except["Rating"] == 1]
rating_2 = review_data_except[review_data_except["Rating"] == 2]
rating_3 = review_data_except[review_data_except["Rating"] == 3]
rating_4 = review_data_except[review_data_except["Rating"] == 4]
rating_5 = review_data_except[review_data_except["Rating"] == 5]


# In[519]:


print("Rating_1_Size : " + str(rating_1["Rating"].size) + "   |   Rating_1_Percent : " + str((rating_1["Rating"].size / review_data_except["Rating"].size) * 100))
print("Rating_2_Size : " + str(rating_2["Rating"].size) + "   |   Rating_2_Percent : " + str((rating_2["Rating"].size / review_data_except["Rating"].size) * 100))
print("Rating_3_Size : " + str(rating_3["Rating"].size) + "   |   Rating_3_Percent : " + str((rating_3["Rating"].size / review_data_except["Rating"].size) * 100))
print("Rating_4_Size : " + str(rating_4["Rating"].size) + "   |   Rating_4_Percent : " + str((rating_4["Rating"].size / review_data_except["Rating"].size) * 100))
print("Rating_5_Size : " + str(rating_5["Rating"].size) + "   |   Rating_5_Percent : " + str((rating_5["Rating"].size / review_data_except["Rating"].size) * 100))


# In[520]:


review_data_234000 = DataFrame(review_data_except, columns=["Content","Rating"])


# In[ ]:


review_data_234000.to_csv("app-review-data/review-data.csv")


# In[523]:


review_data_234000.loc[review_data_234000["Rating"] == 1,"Rating"] = 0
review_data_234000.loc[review_data_234000["Rating"] == 2,"Rating"] = 0
review_data_234000.loc[review_data_234000["Rating"] == 3,"Rating"] = 0
review_data_234000.loc[review_data_234000["Rating"] == 4,"Rating"] = 1
review_data_234000.loc[review_data_234000["Rating"] == 5,"Rating"] = 1

print(review_data_234000[review_data_234000["Rating"] == 0].shape)
print(review_data_234000[review_data_234000["Rating"] == 1].shape)


# In[537]:


train_negative, test_negative = np.split(review_data_234000[review_data_234000["Rating"] == 0], [int(.7*len(review_data_234000[review_data_234000["Rating"] == 0]))])
print(train_negative.shape)
print(test_negative.shape)


# In[538]:


train_positive, test_positive = np.split(review_data_234000[review_data_234000["Rating"] == 1], [int(.7*len(review_data_234000[review_data_234000["Rating"] == 1]))])
print(train_positive.shape)
print(test_positive.shape)


# In[540]:


train = pd.concat([train_positive, train_negative]).reset_index(drop=True)
train = train.sample(frac=1).reset_index(drop=True)
print(train.shape)
train.head(30)


# In[1]:


test = pd.concat([test_positive, test_negative]).reset_index(drop=True)
test = test.sample(frac=1).reset_index(drop=True)
# print(test.shape)
# test.head(30)


# In[565]:


def clean_text(phrase):
    phrase = phrase.replace("\n", " ")
    
    return phrase

train["Content"] = train["Content"].apply(clean_text)


# In[567]:


test["Content"] = test["Content"].apply(clean_text)


# In[568]:


train.to_csv("app-review-data/train.tsv",sep='\t', index = False)


# In[569]:


test.to_csv("app-review-data/test.tsv",sep='\t', index = False)


# In[570]:


train_train = pd.read_csv("app-review-data/train.tsv",sep='\t')
test_train = pd.read_csv("app-review-data/test.tsv",sep='\t')
print(train.shape)
print(test.shape)


# In[562]:


print(train_train.head())