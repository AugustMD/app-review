{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pandas import DataFrame,Series\n",
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(333385, 6)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "review_data_list = []\n",
    "app_source_list = []\n",
    "app_file_name_list = []\n",
    "app_rating_list = []\n",
    "app_size_list = []\n",
    "for i in range(0, 1021):\n",
    "    index = i + 8240\n",
    "#     print(index)\n",
    "    review_data_list.append(pd.read_csv(\"app-review-data/data/export-\" + str(index) + \"-all-full.csv\"))\n",
    "    if i == 0:\n",
    "        review_data = DataFrame(review_data_list[i], columns=[\"Source\",\"Date\",\"Name\",\"Title\",\"Content\",\"Rating\",\"App_Name_Categorical\"])\n",
    "    else :\n",
    "        temp_review_data = DataFrame(review_data_list[i], columns=[\"Source\",\"Date\",\"Name\",\"Title\",\"Content\",\"Rating\"])\n",
    "        review_data  = pd.concat([temp_review_data, review_data]).reset_index(drop=True)\n",
    "    app_source_list.append(review_data_list[i][\"Source\"][0])\n",
    "    app_file_name_list.append(\"export-\" + str(index) + \"-all-full\")\n",
    "    review_rating_array = np.array(review_data_list[i][\"Rating\"])\n",
    "    app_rating_list.append(np.mean(review_rating_array))\n",
    "    app_size_list.append(review_data_list[i][\"Source\"].size)\n",
    "\n",
    "review_data.shape\n",
    "# print(review_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 487,
   "metadata": {},
   "outputs": [],
   "source": [
    "review_data.to_csv(\"app-review-data/review-data-origin.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 488,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1021, 4)"
      ]
     },
     "execution_count": 488,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "raw_app_data = {\"Source\": app_source_list,\n",
    "                \"Rating\": app_rating_list,\n",
    "                \"Size\": app_size_list,\n",
    "                \"FileName\": app_file_name_list}\n",
    "app_data = DataFrame(raw_app_data, columns=[\"Source\",\"Rating\",\"Size\",\"FileName\"])\n",
    "app_data.shape\n",
    "# print(app_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 489,
   "metadata": {},
   "outputs": [],
   "source": [
    "app_data.to_csv(\"app-review-data/app-data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 490,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(333385, 6)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Source</th>\n",
       "      <th>Date</th>\n",
       "      <th>Name</th>\n",
       "      <th>Title</th>\n",
       "      <th>Content</th>\n",
       "      <th>Rating</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-28</td>\n",
       "      <td>갑질?</td>\n",
       "      <td>토스로 돈빠져나간것은 따로 체크 못하나요 ㅠㅠ</td>\n",
       "      <td>토스랑 카카오페이로 빠져나간거요</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-25</td>\n",
       "      <td>클락업</td>\n",
       "      <td>비번 찾기가 안되요</td>\n",
       "      <td>아이디 찾아서 \\n비밀번호  찾으려고 하는데 \\n등록되지않은 메일 이라고 나옵니다 ...</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-25</td>\n",
       "      <td>밥주세요</td>\n",
       "      <td>머니 캘린더에</td>\n",
       "      <td>다른 항목을 같은 날짜로 지정하면 금액이 덮어씌워지네요. 동일한 날에 자동 이체 시...</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-24</td>\n",
       "      <td>Woochu</td>\n",
       "      <td>카카오뱅크도 업데이트 해주시겠죠 ㅎ</td>\n",
       "      <td>모바일증권 나무도 연동 부탁드립니다\\n\\n자동연계되는 가계부라니 !!\\n매번 일일히...</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-24</td>\n",
       "      <td>얍은조은데</td>\n",
       "      <td>비밀번호 넣어도 접속 안돼요</td>\n",
       "      <td>초기화 해도\\n000000으로 해도\\n000000 입력하니 로그인안되네요 \\n탈퇴하...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Source        Date    Name                      Title  \\\n",
       "0   브로콜리  2018-05-28     갑질?  토스로 돈빠져나간것은 따로 체크 못하나요 ㅠㅠ   \n",
       "1   브로콜리  2018-05-25     클락업                 비번 찾기가 안되요   \n",
       "2   브로콜리  2018-05-25    밥주세요                    머니 캘린더에   \n",
       "3   브로콜리  2018-05-24  Woochu        카카오뱅크도 업데이트 해주시겠죠 ㅎ   \n",
       "4   브로콜리  2018-05-24   얍은조은데            비밀번호 넣어도 접속 안돼요   \n",
       "\n",
       "                                             Content  Rating  \n",
       "0                                  토스랑 카카오페이로 빠져나간거요       3  \n",
       "1  아이디 찾아서 \\n비밀번호  찾으려고 하는데 \\n등록되지않은 메일 이라고 나옵니다 ...       4  \n",
       "2  다른 항목을 같은 날짜로 지정하면 금액이 덮어씌워지네요. 동일한 날에 자동 이체 시...       4  \n",
       "3  모바일증권 나무도 연동 부탁드립니다\\n\\n자동연계되는 가계부라니 !!\\n매번 일일히...       5  \n",
       "4  초기화 해도\\n000000으로 해도\\n000000 입력하니 로그인안되네요 \\n탈퇴하...       1  "
      ]
     },
     "execution_count": 490,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "origin_review_data = review_data\n",
    "print(origin_review_data.shape)\n",
    "origin_review_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 491,
   "metadata": {},
   "outputs": [],
   "source": [
    "# review_data[\"Content\"] = review_data[\"Content(Origin)\"].copy()\n",
    "# review_data[\"Title\"] = review_data[\"Title(Origin)\"].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 492,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(333385, 7)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Content</th>\n",
       "      <th>Content(Origin)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>토스랑 카카오페이로 빠져나간거요</td>\n",
       "      <td>토스랑 카카오페이로 빠져나간거요</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>아이디 찾아서 \\n비밀번호  찾으려고 하는데 \\n등록되지않은 메일 이라고 나옵니다 ...</td>\n",
       "      <td>아이디 찾아서 \\n비밀번호  찾으려고 하는데 \\n등록되지않은 메일 이라고 나옵니다 ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>다른 항목을 같은 날짜로 지정하면 금액이 덮어씌워지네요. 동일한 날에 자동 이체 시...</td>\n",
       "      <td>다른 항목을 같은 날짜로 지정하면 금액이 덮어씌워지네요. 동일한 날에 자동 이체 시...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>모바일증권 나무도 연동 부탁드립니다\\n\\n자동연계되는 가계부라니 !!\\n매번 일일히...</td>\n",
       "      <td>모바일증권 나무도 연동 부탁드립니다\\n\\n자동연계되는 가계부라니 !!\\n매번 일일히...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>초기화 해도\\n000000으로 해도\\n000000 입력하니 로그인안되네요 \\n탈퇴하...</td>\n",
       "      <td>초기화 해도\\n000000으로 해도\\n000000 입력하니 로그인안되네요 \\n탈퇴하...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                             Content  \\\n",
       "0                                  토스랑 카카오페이로 빠져나간거요   \n",
       "1  아이디 찾아서 \\n비밀번호  찾으려고 하는데 \\n등록되지않은 메일 이라고 나옵니다 ...   \n",
       "2  다른 항목을 같은 날짜로 지정하면 금액이 덮어씌워지네요. 동일한 날에 자동 이체 시...   \n",
       "3  모바일증권 나무도 연동 부탁드립니다\\n\\n자동연계되는 가계부라니 !!\\n매번 일일히...   \n",
       "4  초기화 해도\\n000000으로 해도\\n000000 입력하니 로그인안되네요 \\n탈퇴하...   \n",
       "\n",
       "                                     Content(Origin)  \n",
       "0                                  토스랑 카카오페이로 빠져나간거요  \n",
       "1  아이디 찾아서 \\n비밀번호  찾으려고 하는데 \\n등록되지않은 메일 이라고 나옵니다 ...  \n",
       "2  다른 항목을 같은 날짜로 지정하면 금액이 덮어씌워지네요. 동일한 날에 자동 이체 시...  \n",
       "3  모바일증권 나무도 연동 부탁드립니다\\n\\n자동연계되는 가계부라니 !!\\n매번 일일히...  \n",
       "4  초기화 해도\\n000000으로 해도\\n000000 입력하니 로그인안되네요 \\n탈퇴하...  "
      ]
     },
     "execution_count": 492,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "review_data[\"Content(Origin)\"] = review_data[\"Content\"].copy()\n",
    "\n",
    "print(review_data.shape)\n",
    "review_data[[\"Content\", \"Content(Origin)\"]].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 493,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(333385, 8)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Title</th>\n",
       "      <th>Title(Origin)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>토스로 돈빠져나간것은 따로 체크 못하나요 ㅠㅠ</td>\n",
       "      <td>토스로 돈빠져나간것은 따로 체크 못하나요 ㅠㅠ</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>비번 찾기가 안되요</td>\n",
       "      <td>비번 찾기가 안되요</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>머니 캘린더에</td>\n",
       "      <td>머니 캘린더에</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>카카오뱅크도 업데이트 해주시겠죠 ㅎ</td>\n",
       "      <td>카카오뱅크도 업데이트 해주시겠죠 ㅎ</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>비밀번호 넣어도 접속 안돼요</td>\n",
       "      <td>비밀번호 넣어도 접속 안돼요</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                       Title              Title(Origin)\n",
       "0  토스로 돈빠져나간것은 따로 체크 못하나요 ㅠㅠ  토스로 돈빠져나간것은 따로 체크 못하나요 ㅠㅠ\n",
       "1                 비번 찾기가 안되요                 비번 찾기가 안되요\n",
       "2                    머니 캘린더에                    머니 캘린더에\n",
       "3        카카오뱅크도 업데이트 해주시겠죠 ㅎ        카카오뱅크도 업데이트 해주시겠죠 ㅎ\n",
       "4            비밀번호 넣어도 접속 안돼요            비밀번호 넣어도 접속 안돼요"
      ]
     },
     "execution_count": 493,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "review_data[\"Title(Origin)\"] = review_data[\"Title\"].copy()\n",
    "\n",
    "print(review_data.shape)\n",
    "review_data[[\"Title\", \"Title(Origin)\"]].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 494,
   "metadata": {},
   "outputs": [],
   "source": [
    "def clean_purchase_text(content):\n",
    "    content = str(content)\n",
    "    word1 = \"내역\"\n",
    "    word2 = \"구매\"\n",
    "    word3 = \"용량\"\n",
    "    word4 = \"삭제\"\n",
    "    if word1 in content :\n",
    "        return 0\n",
    "    elif word2 in content :\n",
    "        return 0\n",
    "    elif word3 in content :\n",
    "        return 0\n",
    "    elif word4 in content :\n",
    "        return 0\n",
    "    else : \n",
    "        return content"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 496,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(54386, 8)\n"
     ]
    }
   ],
   "source": [
    "review_data[\"Content\"] = review_data[\"Content\"].apply(clean_purchase_text)\n",
    "print(review_data[review_data[\"Content\"] == \"0\"].shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 498,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(41481, 8)\n"
     ]
    }
   ],
   "source": [
    "review_data[\"Title\"] = review_data[\"Title\"].apply(clean_purchase_text)\n",
    "print(review_data[review_data[\"Title\"] == \"0\"].shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 499,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(59244, 8)\n"
     ]
    }
   ],
   "source": [
    "review_data.loc[review_data[\"Title\"] == \"0\", \"Content\"] = \"0\"\n",
    "print(review_data[review_data[\"Content\"] == \"0\"].shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 500,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(274141, 8)\n"
     ]
    }
   ],
   "source": [
    "print(review_data[review_data[\"Content\"] != \"0\"].shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 501,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(274141, 6)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Source</th>\n",
       "      <th>Date</th>\n",
       "      <th>Name</th>\n",
       "      <th>Title</th>\n",
       "      <th>Content</th>\n",
       "      <th>Rating</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-28</td>\n",
       "      <td>갑질?</td>\n",
       "      <td>토스로 돈빠져나간것은 따로 체크 못하나요 ㅠㅠ</td>\n",
       "      <td>토스랑 카카오페이로 빠져나간거요</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-25</td>\n",
       "      <td>클락업</td>\n",
       "      <td>비번 찾기가 안되요</td>\n",
       "      <td>아이디 찾아서 \\n비밀번호  찾으려고 하는데 \\n등록되지않은 메일 이라고 나옵니다 ...</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-25</td>\n",
       "      <td>밥주세요</td>\n",
       "      <td>머니 캘린더에</td>\n",
       "      <td>다른 항목을 같은 날짜로 지정하면 금액이 덮어씌워지네요. 동일한 날에 자동 이체 시...</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-24</td>\n",
       "      <td>Woochu</td>\n",
       "      <td>카카오뱅크도 업데이트 해주시겠죠 ㅎ</td>\n",
       "      <td>모바일증권 나무도 연동 부탁드립니다\\n\\n자동연계되는 가계부라니 !!\\n매번 일일히...</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-20</td>\n",
       "      <td>ohj0522</td>\n",
       "      <td>탈퇴</td>\n",
       "      <td>탈퇴는 어디서 하나요?</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Source        Date     Name                      Title  \\\n",
       "0   브로콜리  2018-05-28      갑질?  토스로 돈빠져나간것은 따로 체크 못하나요 ㅠㅠ   \n",
       "1   브로콜리  2018-05-25      클락업                 비번 찾기가 안되요   \n",
       "2   브로콜리  2018-05-25     밥주세요                    머니 캘린더에   \n",
       "3   브로콜리  2018-05-24   Woochu        카카오뱅크도 업데이트 해주시겠죠 ㅎ   \n",
       "5   브로콜리  2018-05-20  ohj0522                         탈퇴   \n",
       "\n",
       "                                             Content  Rating  \n",
       "0                                  토스랑 카카오페이로 빠져나간거요       3  \n",
       "1  아이디 찾아서 \\n비밀번호  찾으려고 하는데 \\n등록되지않은 메일 이라고 나옵니다 ...       4  \n",
       "2  다른 항목을 같은 날짜로 지정하면 금액이 덮어씌워지네요. 동일한 날에 자동 이체 시...       4  \n",
       "3  모바일증권 나무도 연동 부탁드립니다\\n\\n자동연계되는 가계부라니 !!\\n매번 일일히...       5  \n",
       "5                                       탈퇴는 어디서 하나요?       3  "
      ]
     },
     "execution_count": 501,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "review_data_except_purchase = DataFrame(review_data[review_data[\"Content\"] != \"0\"], columns=[\"Source\",\"Date\",\"Name\",\"Title\",\"Content\",\"Rating\"])\n",
    "print(review_data_except_purchase.shape)\n",
    "review_data_except_purchase.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 502,
   "metadata": {},
   "outputs": [],
   "source": [
    "def clean_exchange_text(content):\n",
    "    content = str(content)\n",
    "    word1 = \"환불\"\n",
    "    if word1 in content :\n",
    "        return 0\n",
    "    else :\n",
    "        return content"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 503,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(274141, 6)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Source</th>\n",
       "      <th>Date</th>\n",
       "      <th>Name</th>\n",
       "      <th>Title</th>\n",
       "      <th>Content</th>\n",
       "      <th>Rating</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-28</td>\n",
       "      <td>갑질?</td>\n",
       "      <td>토스로 돈빠져나간것은 따로 체크 못하나요 ㅠㅠ</td>\n",
       "      <td>토스랑 카카오페이로 빠져나간거요</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-25</td>\n",
       "      <td>클락업</td>\n",
       "      <td>비번 찾기가 안되요</td>\n",
       "      <td>아이디 찾아서 \\n비밀번호  찾으려고 하는데 \\n등록되지않은 메일 이라고 나옵니다 ...</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-25</td>\n",
       "      <td>밥주세요</td>\n",
       "      <td>머니 캘린더에</td>\n",
       "      <td>다른 항목을 같은 날짜로 지정하면 금액이 덮어씌워지네요. 동일한 날에 자동 이체 시...</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-24</td>\n",
       "      <td>Woochu</td>\n",
       "      <td>카카오뱅크도 업데이트 해주시겠죠 ㅎ</td>\n",
       "      <td>모바일증권 나무도 연동 부탁드립니다\\n\\n자동연계되는 가계부라니 !!\\n매번 일일히...</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-20</td>\n",
       "      <td>ohj0522</td>\n",
       "      <td>탈퇴</td>\n",
       "      <td>탈퇴는 어디서 하나요?</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Source        Date     Name                      Title  \\\n",
       "0   브로콜리  2018-05-28      갑질?  토스로 돈빠져나간것은 따로 체크 못하나요 ㅠㅠ   \n",
       "1   브로콜리  2018-05-25      클락업                 비번 찾기가 안되요   \n",
       "2   브로콜리  2018-05-25     밥주세요                    머니 캘린더에   \n",
       "3   브로콜리  2018-05-24   Woochu        카카오뱅크도 업데이트 해주시겠죠 ㅎ   \n",
       "5   브로콜리  2018-05-20  ohj0522                         탈퇴   \n",
       "\n",
       "                                             Content  Rating  \n",
       "0                                  토스랑 카카오페이로 빠져나간거요       3  \n",
       "1  아이디 찾아서 \\n비밀번호  찾으려고 하는데 \\n등록되지않은 메일 이라고 나옵니다 ...       4  \n",
       "2  다른 항목을 같은 날짜로 지정하면 금액이 덮어씌워지네요. 동일한 날에 자동 이체 시...       4  \n",
       "3  모바일증권 나무도 연동 부탁드립니다\\n\\n자동연계되는 가계부라니 !!\\n매번 일일히...       5  \n",
       "5                                       탈퇴는 어디서 하나요?       3  "
      ]
     },
     "execution_count": 503,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(review_data_except_purchase.shape)\n",
    "review_data_except_purchase.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 504,
   "metadata": {},
   "outputs": [],
   "source": [
    "review_data_except_purchase[\"Rating_5_Content\"] = review_data_except_purchase[\"Content\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 506,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(815, 7)\n"
     ]
    }
   ],
   "source": [
    "review_data_except_purchase[\"Rating_5_Content\"] = review_data_except_purchase[review_data_except_purchase[\"Rating\"] == 5][\"Rating_5_Content\"].apply(clean_exchange_text)\n",
    "print(review_data_except_purchase[review_data_except_purchase[\"Rating_5_Content\"] == \"0\"].shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 507,
   "metadata": {},
   "outputs": [],
   "source": [
    "review_data_except_purchase[\"Rating_4_Content\"] = review_data_except_purchase[\"Content\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 509,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(347, 8)\n"
     ]
    }
   ],
   "source": [
    "review_data_except_purchase[\"Rating_4_Content\"] = review_data_except_purchase[review_data_except_purchase[\"Rating\"] == 4][\"Rating_4_Content\"].apply(clean_exchange_text)\n",
    "print(review_data_except_purchase[review_data_except_purchase[\"Rating_4_Content\"] == \"0\"].shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 510,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Source</th>\n",
       "      <th>Date</th>\n",
       "      <th>Name</th>\n",
       "      <th>Title</th>\n",
       "      <th>Content</th>\n",
       "      <th>Rating</th>\n",
       "      <th>Rating_5_Content</th>\n",
       "      <th>Rating_4_Content</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-28</td>\n",
       "      <td>갑질?</td>\n",
       "      <td>토스로 돈빠져나간것은 따로 체크 못하나요 ㅠㅠ</td>\n",
       "      <td>토스랑 카카오페이로 빠져나간거요</td>\n",
       "      <td>3</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-25</td>\n",
       "      <td>클락업</td>\n",
       "      <td>비번 찾기가 안되요</td>\n",
       "      <td>아이디 찾아서 \\n비밀번호  찾으려고 하는데 \\n등록되지않은 메일 이라고 나옵니다 ...</td>\n",
       "      <td>4</td>\n",
       "      <td>NaN</td>\n",
       "      <td>아이디 찾아서 \\n비밀번호  찾으려고 하는데 \\n등록되지않은 메일 이라고 나옵니다 ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-25</td>\n",
       "      <td>밥주세요</td>\n",
       "      <td>머니 캘린더에</td>\n",
       "      <td>다른 항목을 같은 날짜로 지정하면 금액이 덮어씌워지네요. 동일한 날에 자동 이체 시...</td>\n",
       "      <td>4</td>\n",
       "      <td>NaN</td>\n",
       "      <td>다른 항목을 같은 날짜로 지정하면 금액이 덮어씌워지네요. 동일한 날에 자동 이체 시...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-24</td>\n",
       "      <td>Woochu</td>\n",
       "      <td>카카오뱅크도 업데이트 해주시겠죠 ㅎ</td>\n",
       "      <td>모바일증권 나무도 연동 부탁드립니다\\n\\n자동연계되는 가계부라니 !!\\n매번 일일히...</td>\n",
       "      <td>5</td>\n",
       "      <td>모바일증권 나무도 연동 부탁드립니다\\n\\n자동연계되는 가계부라니 !!\\n매번 일일히...</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-20</td>\n",
       "      <td>ohj0522</td>\n",
       "      <td>탈퇴</td>\n",
       "      <td>탈퇴는 어디서 하나요?</td>\n",
       "      <td>3</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Source        Date     Name                      Title  \\\n",
       "0   브로콜리  2018-05-28      갑질?  토스로 돈빠져나간것은 따로 체크 못하나요 ㅠㅠ   \n",
       "1   브로콜리  2018-05-25      클락업                 비번 찾기가 안되요   \n",
       "2   브로콜리  2018-05-25     밥주세요                    머니 캘린더에   \n",
       "3   브로콜리  2018-05-24   Woochu        카카오뱅크도 업데이트 해주시겠죠 ㅎ   \n",
       "5   브로콜리  2018-05-20  ohj0522                         탈퇴   \n",
       "\n",
       "                                             Content  Rating  \\\n",
       "0                                  토스랑 카카오페이로 빠져나간거요       3   \n",
       "1  아이디 찾아서 \\n비밀번호  찾으려고 하는데 \\n등록되지않은 메일 이라고 나옵니다 ...       4   \n",
       "2  다른 항목을 같은 날짜로 지정하면 금액이 덮어씌워지네요. 동일한 날에 자동 이체 시...       4   \n",
       "3  모바일증권 나무도 연동 부탁드립니다\\n\\n자동연계되는 가계부라니 !!\\n매번 일일히...       5   \n",
       "5                                       탈퇴는 어디서 하나요?       3   \n",
       "\n",
       "                                    Rating_5_Content  \\\n",
       "0                                                NaN   \n",
       "1                                                NaN   \n",
       "2                                                NaN   \n",
       "3  모바일증권 나무도 연동 부탁드립니다\\n\\n자동연계되는 가계부라니 !!\\n매번 일일히...   \n",
       "5                                                NaN   \n",
       "\n",
       "                                    Rating_4_Content  \n",
       "0                                                NaN  \n",
       "1  아이디 찾아서 \\n비밀번호  찾으려고 하는데 \\n등록되지않은 메일 이라고 나옵니다 ...  \n",
       "2  다른 항목을 같은 날짜로 지정하면 금액이 덮어씌워지네요. 동일한 날에 자동 이체 시...  \n",
       "3                                                NaN  \n",
       "5                                                NaN  "
      ]
     },
     "execution_count": 510,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "review_data_except_purchase.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 511,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1162, 8)\n"
     ]
    }
   ],
   "source": [
    "review_data_except_purchase.loc[review_data_except_purchase[\"Rating_4_Content\"] == \"0\", \"Content\"] = \"0\"\n",
    "review_data_except_purchase.loc[review_data_except_purchase[\"Rating_5_Content\"] == \"0\", \"Content\"] = \"0\"\n",
    "print(review_data_except_purchase[review_data_except_purchase[\"Content\"] == \"0\"].shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 512,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(272979, 6)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Source</th>\n",
       "      <th>Date</th>\n",
       "      <th>Name</th>\n",
       "      <th>Title</th>\n",
       "      <th>Content</th>\n",
       "      <th>Rating</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-28</td>\n",
       "      <td>갑질?</td>\n",
       "      <td>토스로 돈빠져나간것은 따로 체크 못하나요 ㅠㅠ</td>\n",
       "      <td>토스랑 카카오페이로 빠져나간거요</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-25</td>\n",
       "      <td>클락업</td>\n",
       "      <td>비번 찾기가 안되요</td>\n",
       "      <td>아이디 찾아서 \\n비밀번호  찾으려고 하는데 \\n등록되지않은 메일 이라고 나옵니다 ...</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-25</td>\n",
       "      <td>밥주세요</td>\n",
       "      <td>머니 캘린더에</td>\n",
       "      <td>다른 항목을 같은 날짜로 지정하면 금액이 덮어씌워지네요. 동일한 날에 자동 이체 시...</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-24</td>\n",
       "      <td>Woochu</td>\n",
       "      <td>카카오뱅크도 업데이트 해주시겠죠 ㅎ</td>\n",
       "      <td>모바일증권 나무도 연동 부탁드립니다\\n\\n자동연계되는 가계부라니 !!\\n매번 일일히...</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>브로콜리</td>\n",
       "      <td>2018-05-20</td>\n",
       "      <td>ohj0522</td>\n",
       "      <td>탈퇴</td>\n",
       "      <td>탈퇴는 어디서 하나요?</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Source        Date     Name                      Title  \\\n",
       "0   브로콜리  2018-05-28      갑질?  토스로 돈빠져나간것은 따로 체크 못하나요 ㅠㅠ   \n",
       "1   브로콜리  2018-05-25      클락업                 비번 찾기가 안되요   \n",
       "2   브로콜리  2018-05-25     밥주세요                    머니 캘린더에   \n",
       "3   브로콜리  2018-05-24   Woochu        카카오뱅크도 업데이트 해주시겠죠 ㅎ   \n",
       "5   브로콜리  2018-05-20  ohj0522                         탈퇴   \n",
       "\n",
       "                                             Content  Rating  \n",
       "0                                  토스랑 카카오페이로 빠져나간거요       3  \n",
       "1  아이디 찾아서 \\n비밀번호  찾으려고 하는데 \\n등록되지않은 메일 이라고 나옵니다 ...       4  \n",
       "2  다른 항목을 같은 날짜로 지정하면 금액이 덮어씌워지네요. 동일한 날에 자동 이체 시...       4  \n",
       "3  모바일증권 나무도 연동 부탁드립니다\\n\\n자동연계되는 가계부라니 !!\\n매번 일일히...       5  \n",
       "5                                       탈퇴는 어디서 하나요?       3  "
      ]
     },
     "execution_count": 512,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "review_data_except = DataFrame(review_data_except_purchase[review_data_except_purchase[\"Content\"] != \"0\"], columns=[\"Source\",\"Date\",\"Name\",\"Title\",\"Content\",\"Rating\"])\n",
    "print(review_data_except.shape)\n",
    "review_data_except.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 513,
   "metadata": {},
   "outputs": [],
   "source": [
    "rating_1 = review_data_except[review_data_except[\"Rating\"] == 1]\n",
    "rating_2 = review_data_except[review_data_except[\"Rating\"] == 2]\n",
    "rating_3 = review_data_except[review_data_except[\"Rating\"] == 3]\n",
    "rating_4 = review_data_except[review_data_except[\"Rating\"] == 4]\n",
    "rating_5 = review_data_except[review_data_except[\"Rating\"] == 5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 514,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rating_1_Size : 84267   |   Rating_1_Percent : 30.7385615431475\n",
      "Rating_2_Size : 14406   |   Rating_2_Percent : 5.254960038812144\n",
      "Rating_3_Size : 23336   |   Rating_3_Percent : 8.51240784851591\n",
      "Rating_4_Size : 32005   |   Rating_4_Percent : 11.674649176883428\n",
      "Rating_5_Size : 118965   |   Rating_5_Percent : 43.39555192400991\n"
     ]
    }
   ],
   "source": [
    "print(\"Rating_1_Size : \" + str(rating_1[\"Rating\"].size) + \"   |   Rating_1_Percent : \" + str((rating_1[\"Rating\"].size / review_data_except[\"Rating\"].size) * 100))\n",
    "print(\"Rating_2_Size : \" + str(rating_2[\"Rating\"].size) + \"   |   Rating_2_Percent : \" + str((rating_2[\"Rating\"].size / review_data_except[\"Rating\"].size) * 100))\n",
    "print(\"Rating_3_Size : \" + str(rating_3[\"Rating\"].size) + \"   |   Rating_3_Percent : \" + str((rating_3[\"Rating\"].size / review_data_except[\"Rating\"].size) * 100))\n",
    "print(\"Rating_4_Size : \" + str(rating_4[\"Rating\"].size) + \"   |   Rating_4_Percent : \" + str((rating_4[\"Rating\"].size / review_data_except[\"Rating\"].size) * 100))\n",
    "print(\"Rating_5_Size : \" + str(rating_5[\"Rating\"].size) + \"   |   Rating_5_Percent : \" + str((rating_5[\"Rating\"].size / review_data_except[\"Rating\"].size) * 100))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 515,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(154014, 6)\n",
      "(85942, 6)\n",
      "(239956, 6)\n"
     ]
    }
   ],
   "source": [
    "review_data_rating_except_rating_5 = DataFrame(review_data_except[review_data_except[\"Rating\"] != 5], columns=[\"Source\",\"Date\",\"Name\",\"Title\",\"Content\",\"Rating\"])\n",
    "print(review_data_rating_except_rating_5.shape)\n",
    "sample_review_data_rating_5 = DataFrame(review_data_except[review_data_except[\"Rating\"] == 5].sample(n=85942), columns=[\"Source\",\"Date\",\"Name\",\"Title\",\"Content\",\"Rating\"])\n",
    "print(sample_review_data_rating_5.shape)\n",
    "review_data_except = pd.concat([review_data_rating_except_rating_5, sample_review_data_rating_5]).reset_index(drop=True)\n",
    "print(review_data_except.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 516,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(216620, 6)\n",
      "(18336, 6)\n",
      "(234956, 6)\n"
     ]
    }
   ],
   "source": [
    "review_data_rating_except_rating_3 = DataFrame(review_data_except[review_data_except[\"Rating\"] != 3], columns=[\"Source\",\"Date\",\"Name\",\"Title\",\"Content\",\"Rating\"])\n",
    "print(review_data_rating_except_rating_3.shape)\n",
    "sample_review_data_rating_3 = DataFrame(review_data_except[review_data_except[\"Rating\"] == 3].sample(n=18336), columns=[\"Source\",\"Date\",\"Name\",\"Title\",\"Content\",\"Rating\"])\n",
    "print(sample_review_data_rating_3.shape)\n",
    "review_data_except = pd.concat([review_data_rating_except_rating_3, sample_review_data_rating_3]).reset_index(drop=True)\n",
    "print(review_data_except.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 517,
   "metadata": {},
   "outputs": [],
   "source": [
    "rating_1 = review_data_except[review_data_except[\"Rating\"] == 1]\n",
    "rating_2 = review_data_except[review_data_except[\"Rating\"] == 2]\n",
    "rating_3 = review_data_except[review_data_except[\"Rating\"] == 3]\n",
    "rating_4 = review_data_except[review_data_except[\"Rating\"] == 4]\n",
    "rating_5 = review_data_except[review_data_except[\"Rating\"] == 5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 519,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rating_1_Size : 84267   |   Rating_1_Percent : 35.86501302371508\n",
      "Rating_2_Size : 14406   |   Rating_2_Percent : 6.131360765419909\n",
      "Rating_3_Size : 18336   |   Rating_3_Percent : 7.804014368647747\n",
      "Rating_4_Size : 32005   |   Rating_4_Percent : 13.62169938201195\n",
      "Rating_5_Size : 85942   |   Rating_5_Percent : 36.57791246020531\n"
     ]
    }
   ],
   "source": [
    "print(\"Rating_1_Size : \" + str(rating_1[\"Rating\"].size) + \"   |   Rating_1_Percent : \" + str((rating_1[\"Rating\"].size / review_data_except[\"Rating\"].size) * 100))\n",
    "print(\"Rating_2_Size : \" + str(rating_2[\"Rating\"].size) + \"   |   Rating_2_Percent : \" + str((rating_2[\"Rating\"].size / review_data_except[\"Rating\"].size) * 100))\n",
    "print(\"Rating_3_Size : \" + str(rating_3[\"Rating\"].size) + \"   |   Rating_3_Percent : \" + str((rating_3[\"Rating\"].size / review_data_except[\"Rating\"].size) * 100))\n",
    "print(\"Rating_4_Size : \" + str(rating_4[\"Rating\"].size) + \"   |   Rating_4_Percent : \" + str((rating_4[\"Rating\"].size / review_data_except[\"Rating\"].size) * 100))\n",
    "print(\"Rating_5_Size : \" + str(rating_5[\"Rating\"].size) + \"   |   Rating_5_Percent : \" + str((rating_5[\"Rating\"].size / review_data_except[\"Rating\"].size) * 100))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 520,
   "metadata": {},
   "outputs": [],
   "source": [
    "review_data_234000 = DataFrame(review_data_except, columns=[\"Content\",\"Rating\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "review_data_234000.to_csv(\"app-review-data/review-data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 523,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(117009, 2)\n",
      "(117947, 2)\n"
     ]
    }
   ],
   "source": [
    "review_data_234000.loc[review_data_234000[\"Rating\"] == 1,\"Rating\"] = 0\n",
    "review_data_234000.loc[review_data_234000[\"Rating\"] == 2,\"Rating\"] = 0\n",
    "review_data_234000.loc[review_data_234000[\"Rating\"] == 3,\"Rating\"] = 0\n",
    "review_data_234000.loc[review_data_234000[\"Rating\"] == 4,\"Rating\"] = 1\n",
    "review_data_234000.loc[review_data_234000[\"Rating\"] == 5,\"Rating\"] = 1\n",
    "\n",
    "print(review_data_234000[review_data_234000[\"Rating\"] == 0].shape)\n",
    "print(review_data_234000[review_data_234000[\"Rating\"] == 1].shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 537,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(81906, 2)\n",
      "(35103, 2)\n"
     ]
    }
   ],
   "source": [
    "train_negative, test_negative = np.split(review_data_234000[review_data_234000[\"Rating\"] == 0], [int(.7*len(review_data_234000[review_data_234000[\"Rating\"] == 0]))])\n",
    "print(train_negative.shape)\n",
    "print(test_negative.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 538,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(82562, 2)\n",
      "(35385, 2)\n"
     ]
    }
   ],
   "source": [
    "train_positive, test_positive = np.split(review_data_234000[review_data_234000[\"Rating\"] == 1], [int(.7*len(review_data_234000[review_data_234000[\"Rating\"] == 1]))])\n",
    "print(train_positive.shape)\n",
    "print(test_positive.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 540,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(164468, 2)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Content</th>\n",
       "      <th>Rating</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>맘에 들어요 완전~\\n저는 아이폰 유저인데요, 앱을 받은 이후로 밧데리가 좀 빨리 ...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>리뷰장난</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>배속재생 안되는거는 참을만 한데 자동로그인 안되는건 진짜 개빡침. 내가 리뷰 분명 ...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>I love this app and I don’t usually write recv...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>키보드문제인지 앱문제인지 ?\\n\\n데스크탑은 괞찮은데...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>저만 그런건지 모르겠는데 나갔다들어와야해서 불편합니다..</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>이런게임처음이지만 재미있게 잘하고있어여</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>ㅎㅎㅎㅎㅎ</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>홈팀만 찍으라는건지 ㅋㅋㅋ</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>동영상을 찍었는데 소리가 안나요 왜이러나요?</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>유니클로 회장은 쓰지도 않나보군🤬😱🤮\\n\\n🈲❌고객의 쇼핑 의지를 꺽어서 돈을 절약...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>갑자기 어제 결제되었는데  결제 취소해주세요</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>관고만없어진다면중간에끊김없이수월하게사용할수있을것같네여</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>어플잘쓰고있어요. 노트마다 암호만걸수있으면 더할나위없을거같아요.\\n일기를쓰고싶은사람...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>뭐죠</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>날씨어플을 쓰려고 검색했는데 호우호우가 있더라구요! 너무 귀여워서 고민하지 않고 다...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>x버튼 한 열번눌러도 화면 안남어가고 뻑하면 튕겨 ㅗ 좃으로 만들었냐 시벌년아</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>좋음</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>덕분에 다음달 결제금액도 정확히 알고\\n얼마나 왜 썼는지 알게되었어요 ㅠㅠ\\n카드가...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>지출 액수를 기억못해 너무 많이쓰는것에대해 고민이던 찰나에 페이스북 광고를 통해 사...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>RT랑 트윗이랑 분류할수 있는 기능이랑 , 트윗 수정 가능하게 해주셨으면 좋겠어요 ...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>재밌네요</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>많은 사람들이 정보를 공유해주길 ..</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>렉 진짜너무심해요  유난히 요즘들어 심해져ㅆ어요</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>이번에 업데이트를 하니깐 들어가지지도 않고 검은화면만 뜨고 튕기네요.. 빨리 검토좀요</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>분류에 수입/지출말고도 있었으면...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>유용하게 잘 쓰고 있어요. \\n아이 키우면서 꼭 있음 좋을 어플!!</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>ㅇㅇ</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>이제배그짭겜다망하겠구먼</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                              Content  Rating\n",
       "0   맘에 들어요 완전~\\n저는 아이폰 유저인데요, 앱을 받은 이후로 밧데리가 좀 빨리 ...       1\n",
       "1                                                리뷰장난       0\n",
       "2   배속재생 안되는거는 참을만 한데 자동로그인 안되는건 진짜 개빡침. 내가 리뷰 분명 ...       0\n",
       "3   I love this app and I don’t usually write recv...       1\n",
       "4                    키보드문제인지 앱문제인지 ?\\n\\n데스크탑은 괞찮은데...       1\n",
       "5                     저만 그런건지 모르겠는데 나갔다들어와야해서 불편합니다..       0\n",
       "6                               이런게임처음이지만 재미있게 잘하고있어여       1\n",
       "7                                               ㅎㅎㅎㅎㅎ       1\n",
       "8                                      홈팀만 찍으라는건지 ㅋㅋㅋ       0\n",
       "9                            동영상을 찍었는데 소리가 안나요 왜이러나요?       0\n",
       "10  유니클로 회장은 쓰지도 않나보군🤬😱🤮\\n\\n🈲❌고객의 쇼핑 의지를 꺽어서 돈을 절약...       0\n",
       "11                           갑자기 어제 결제되었는데  결제 취소해주세요       0\n",
       "12                      관고만없어진다면중간에끊김없이수월하게사용할수있을것같네여       1\n",
       "13  어플잘쓰고있어요. 노트마다 암호만걸수있으면 더할나위없을거같아요.\\n일기를쓰고싶은사람...       1\n",
       "14                                                 뭐죠       1\n",
       "15  날씨어플을 쓰려고 검색했는데 호우호우가 있더라구요! 너무 귀여워서 고민하지 않고 다...       1\n",
       "16        x버튼 한 열번눌러도 화면 안남어가고 뻑하면 튕겨 ㅗ 좃으로 만들었냐 시벌년아       0\n",
       "17                                                 좋음       1\n",
       "18  덕분에 다음달 결제금액도 정확히 알고\\n얼마나 왜 썼는지 알게되었어요 ㅠㅠ\\n카드가...       1\n",
       "19  지출 액수를 기억못해 너무 많이쓰는것에대해 고민이던 찰나에 페이스북 광고를 통해 사...       1\n",
       "20  RT랑 트윗이랑 분류할수 있는 기능이랑 , 트윗 수정 가능하게 해주셨으면 좋겠어요 ...       1\n",
       "21                                               재밌네요       1\n",
       "22                               많은 사람들이 정보를 공유해주길 ..       1\n",
       "23                                                ...       0\n",
       "24                         렉 진짜너무심해요  유난히 요즘들어 심해져ㅆ어요       0\n",
       "25    이번에 업데이트를 하니깐 들어가지지도 않고 검은화면만 뜨고 튕기네요.. 빨리 검토좀요       0\n",
       "26                               분류에 수입/지출말고도 있었으면...       1\n",
       "27              유용하게 잘 쓰고 있어요. \\n아이 키우면서 꼭 있음 좋을 어플!!       1\n",
       "28                                                 ㅇㅇ       1\n",
       "29                                       이제배그짭겜다망하겠구먼       1"
      ]
     },
     "execution_count": 540,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train = pd.concat([train_positive, train_negative]).reset_index(drop=True)\n",
    "train = train.sample(frac=1).reset_index(drop=True)\n",
    "print(train.shape)\n",
    "train.head(30)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'pd' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-1-1d4060c4c711>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mtest\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconcat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mtest_positive\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtest_negative\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mreset_index\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdrop\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mtest\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtest\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msample\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfrac\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mreset_index\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdrop\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;31m# print(test.shape)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;31m# test.head(30)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'pd' is not defined"
     ]
    }
   ],
   "source": [
    "test = pd.concat([test_positive, test_negative]).reset_index(drop=True)\n",
    "test = test.sample(frac=1).reset_index(drop=True)\n",
    "# print(test.shape)\n",
    "# test.head(30)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 565,
   "metadata": {},
   "outputs": [],
   "source": [
    "def clean_text(phrase):\n",
    "    phrase = phrase.replace(\"\\n\", \" \")\n",
    "    \n",
    "    return phrase\n",
    "\n",
    "train[\"Content\"] = train[\"Content\"].apply(clean_text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 567,
   "metadata": {},
   "outputs": [],
   "source": [
    "test[\"Content\"] = test[\"Content\"].apply(clean_text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 568,
   "metadata": {},
   "outputs": [],
   "source": [
    "train.to_csv(\"app-review-data/train.tsv\",sep='\\t', index = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 569,
   "metadata": {},
   "outputs": [],
   "source": [
    "test.to_csv(\"app-review-data/test.tsv\",sep='\\t', index = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 570,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(164468, 2)\n",
      "(70488, 2)\n"
     ]
    }
   ],
   "source": [
    "train_train = pd.read_csv(\"app-review-data/train.tsv\",sep='\\t')\n",
    "test_train = pd.read_csv(\"app-review-data/test.tsv\",sep='\\t')\n",
    "print(train.shape)\n",
    "print(test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 562,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                             Content  Rating\n",
      "0  맘에 들어요 완전~\\n저는 아이폰 유저인데요, 앱을 받은 이후로 밧데리가 좀 빨리 ...       1\n",
      "1                                               리뷰장난       0\n",
      "2  배속재생 안되는거는 참을만 한데 자동로그인 안되는건 진짜 개빡침. 내가 리뷰 분명 ...       0\n",
      "3  I love this app and I don’t usually write recv...       1\n",
      "4                   키보드문제인지 앱문제인지 ?\\n\\n데스크탑은 괞찮은데...       1\n"
     ]
    }
   ],
   "source": [
    "print(train_train.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 479,
   "metadata": {},
   "outputs": [],
   "source": [
    "# review_data[\"Check\"] = 0\n",
    "# review_data[\"Remarks\"] = 0\n",
    "# review_data_file_list = []\n",
    "# for i in range(0, 26):\n",
    "#     if i == 0:\n",
    "#         review_data_file_list.append(review_data[:10000])\n",
    "#     else :\n",
    "#         review_data_file_list.append(review_data[i*10000:(i+1)*10000])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 480,
   "metadata": {},
   "outputs": [],
   "source": [
    "# count = 0\n",
    "# for i in range(0, 26):\n",
    "#     count = review_data_file_list[i][\"Rating\"].size + count\n",
    "#     review_data_file_list[i].to_csv(\"app-review-data/review-data\" + str(i+1) + \".csv\")\n",
    "# print(count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 481,
   "metadata": {},
   "outputs": [],
   "source": [
    "# modified_review_data_list = []\n",
    "# modified_app_source_list = []\n",
    "# modified_app_file_name_list = []\n",
    "# modified_app_rating_list = []\n",
    "# modified_app_size_list = []\n",
    "# index_list = [1,2,3,6,11,12,16,17,18,19,20,21,22,23]\n",
    "# count = 0\n",
    "# for index in index_list:\n",
    "# # for i in range(0, 3):\n",
    "#     count = count + 1\n",
    "#     print(index)\n",
    "#     modified_review_data_list.append(pd.read_csv(\"app-review-data/data/check-data-1/review-data\" + str(index) + \".csv\"))\n",
    "    \n",
    "# for i in range(0, count):\n",
    "#     if i == 0:\n",
    "#         modified_review_data = DataFrame(modified_review_data_list[i], columns=[\"Source\",\"Date\",\"Name\",\"Title\",\"Content\",\"Rating\",\"Check\",\"Remarks\"])\n",
    "#     else :\n",
    "#         temp_modified_review_data = DataFrame(modified_review_data_list[i], columns=[\"Source\",\"Date\",\"Name\",\"Title\",\"Content\",\"Rating\",\"Check\",\"Remarks\"])\n",
    "#         modified_review_data  = pd.concat([temp_modified_review_data, modified_review_data]).reset_index(drop=True)\n",
    "#     modified_app_source_list.append(modified_review_data_list[i][\"Source\"][0])\n",
    "#     modified_app_file_name_list.append(\"review-data\" + str(index))\n",
    "#     modified_review_rating_array = np.array(modified_review_data_list[i][\"Rating\"])\n",
    "#     modified_app_rating_list.append(np.mean(modified_review_rating_array))\n",
    "#     modified_app_size_list.append(modified_review_data_list[i][\"Source\"].size)\n",
    "\n",
    "# modified_review_data.shape\n",
    "# print(modified_review_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 482,
   "metadata": {},
   "outputs": [],
   "source": [
    "# modified_review_data[modified_review_data[\"Check\"] == 11].shape\n",
    "# # print(modified_review_data[modified_review_data[\"Check\"] == 11])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 483,
   "metadata": {},
   "outputs": [],
   "source": [
    "# modified_review_data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 484,
   "metadata": {},
   "outputs": [],
   "source": [
    "# modified_review_data.to_csv(\"app-review-data/data/check-data-1/modified-review-data1.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 478,
   "metadata": {},
   "outputs": [],
   "source": [
    "# temp = pd.read_csv(\"app-review-data/data/check-data-1/modified-review-data1.csv\")\n",
    "# temp.shape"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
