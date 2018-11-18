from selenium import webdriver
import datetime
from time import sleep

driver = webdriver.Chrome("c:/driver/chromedriver.exe")
driver.get("https://iroots.jp/lounge/admin/login/")


elem_search_word = driver.find_element_by_id("admin_email")
elem_search_word.send_keys("[iroots管理画面ID]")
elem_search_word = driver.find_element_by_id("admin_password")
elem_search_word.send_keys("[iroots管理画面PW]")
elem_search_btn = driver.find_element_by_id("form_button")
elem_search_btn.click()

data_page = driver.find_element_by_xpath("//*[@id='sidebar']/ul/li[2]/a")
data_page.click()

today = datetime.date.today()#今日の日付
day = today.day - 1
weeks = 0
while day > 0:
    weeks += 1
    day -= 7

beforeXPATHE = "//*[@id='ui-datepicker-div']/table/tbody/tr[" + str(weeks) + "]/td[" + str(today.weekday() + 1) + "]/a"

day_from = driver.find_element_by_xpath("//*[@id='from_date']")
day_from.click()
day_from = driver.find_element_by_xpath(beforeXPATHE)
day_from.click()
day_to = driver.find_element_by_xpath("//*[@id='to_date']")
day_to.click()
day_to = driver.find_element_by_xpath(beforeXPATHE)
day_to.click()

sleep(1)
bunkatu = driver.find_element_by_xpath("//*[@id='frmAnalysis']/div/table/tbody/tr[5]/td/div/label[2]")
bunkatu.click()
bunkatu = driver.find_element_by_xpath("//*[@id='frmAnalysis']/div/table/tbody/tr[6]/td/div/label[2]")
bunkatu.click()
bunkatu = driver.find_element_by_xpath("//*[@id='frmAnalysis']/div/table/tbody/tr[7]/td/div/label[2]")
bunkatu.click()
bunkatu = driver.find_element_by_xpath("//*[@id='frmAnalysis']/div/table/tbody/tr[8]/td/div/label[2]")
bunkatu.click()
bunkatu = driver.find_element_by_xpath("//*[@id='frmAnalysis']/div/table/tbody/tr[9]/td/div/label[2]")
bunkatu.click()

export = driver.find_element_by_xpath("//*[@id='submitCancel']")
export.click()

sleep(3)
driver.close()

import shutil

download_file = "データ分析_ユーザー集計情報_" + str(today.year) + str(today.month) + str(today.day)
place_of_file = "C:/Users/pr1mi/Downloads/" + download_file + ".csv"
shutil.copy(place_of_file, "result.csv")

import os
os.remove(place_of_file)

########################################################################################
#ここからは分析


import pandas as pd

def Analyze():
    file_name = "result.csv"
    data = pd.read_csv(file_name)

    #学年ごとにデータを分割
    handai = data[data["大学名"] == "大阪大学"]
    handai_1 = handai[(handai["学年"] == 1) & (handai["大学課程"] == "学部")]
    handai_2 = handai[(handai["学年"] == 2) & (handai["大学課程"] == "学部")]
    handai_3 = handai[(handai["学年"] == 3) & (handai["大学課程"] == "学部")]
    handai_4 = handai[(handai["学年"] == 4) & (handai["大学課程"] == "学部")]
    handai_5 = handai[(handai["学年"] == 5) & (handai["大学課程"] == "学部")]
    handai_6 = handai[(handai["学年"] == 6) & (handai["大学課程"] == "学部")]
    handai_M1 = handai[(handai["学年"] == 1) & (handai["大学課程"] == "修士")]
    handai_M2 = handai[(handai["学年"] == 1) & (handai["大学課程"] == "修士")]

    #学年と文理ごとにデータを分割
    handai_1r = handai_1[handai_1["文理区分"] == "理系"]
    handai_1b = handai_1[handai_1["文理区分"] == "文系"]
    handai_2r = handai_2[handai_2["文理区分"] == "理系"]
    handai_2b = handai_2[handai_2["文理区分"] == "文系"]
    handai_3r = handai_3[handai_3["文理区分"] == "理系"]
    handai_3b = handai_3[handai_3["文理区分"] == "文系"]
    handai_4r = handai_4[handai_4["文理区分"] == "理系"]
    handai_4b = handai_4[handai_4["文理区分"] == "文系"]
    handai_5r = handai_5[handai_5["文理区分"] == "理系"]
    handai_5b = handai_5[handai_5["文理区分"] == "文系"]
    handai_6r = handai_6[handai_6["文理区分"] == "理系"]
    handai_6b = handai_6[handai_6["文理区分"] == "文系"]
    handai_M1r = handai_M1[handai_M1["文理区分"] == "理系"]
    handai_M1b = handai_M1[handai_M1["文理区分"] == "文系"]
    handai_M2r = handai_M2[handai_M2["文理区分"] == "理系"]
    handai_M2b = handai_M2[handai_M2["文理区分"] == "文系"]

    #阪大生の全体での新規来店人数と学年ごとの延べ来店人数
    handai_all = handai["延べ来店人数"].sum()
    handai_1_all = handai_1["延べ来店人数"].sum()
    handai_2_all = handai_2["延べ来店人数"].sum()
    handai_3_all = handai_3["延べ来店人数"].sum()
    handai_4_all = handai_4["延べ来店人数"].sum()
    handai_5_all = handai_5["延べ来店人数"].sum()
    handai_6_all = handai_6["延べ来店人数"].sum()
    handai_M1_all = handai_M1["延べ来店人数"].sum()
    handai_M2_all = handai_M2["延べ来店人数"].sum()

    #阪大生の学年と文理区分ごとの延べ来店人数
    handai_1r_all = handai_1r["延べ来店人数"].sum()
    handai_1b_all = handai_1b["延べ来店人数"].sum()
    handai_2r_all = handai_2r["延べ来店人数"].sum()
    handai_2b_all = handai_2b["延べ来店人数"].sum()
    handai_3r_all = handai_3r["延べ来店人数"].sum()
    handai_3b_all = handai_3b["延べ来店人数"].sum()
    handai_4r_all = handai_4r["延べ来店人数"].sum()
    handai_4b_all = handai_4b["延べ来店人数"].sum()
    handai_5r_all = handai_5r["延べ来店人数"].sum()
    handai_5b_all = handai_5b["延べ来店人数"].sum()
    handai_6r_all = handai_6r["延べ来店人数"].sum()
    handai_6b_all = handai_6b["延べ来店人数"].sum()
    handai_M1r_all = handai_M1r["延べ来店人数"].sum()
    handai_M1b_all = handai_M1b["延べ来店人数"].sum()
    handai_M2r_all = handai_M2r["延べ来店人数"].sum()
    handai_M2b_all = handai_M2b["延べ来店人数"].sum()

    #阪大生の全体での新規来店人数と学年ごとの新規来店人数
    handai_new = handai["新規来店人数"].sum()
    handai_1_new = handai_1["新規来店人数"].sum()
    handai_2_new = handai_2["新規来店人数"].sum()
    handai_3_new = handai_3["新規来店人数"].sum()
    handai_4_new = handai_4["新規来店人数"].sum()
    handai_5_new = handai_5["新規来店人数"].sum()
    handai_6_new = handai_6["新規来店人数"].sum()
    handai_M1_new = handai_M1["新規来店人数"].sum()
    handai_M2_new = handai_M2["新規来店人数"].sum()

    #阪大生の学年と文理区分ごとの新規来店人数
    handai_1r_new = handai_1r["新規来店人数"].sum()
    handai_1b_new = handai_1b["新規来店人数"].sum()
    handai_2r_new = handai_2r["新規来店人数"].sum()
    handai_2b_new = handai_2b["新規来店人数"].sum()
    handai_3r_new = handai_3r["新規来店人数"].sum()
    handai_3b_new = handai_3b["新規来店人数"].sum()
    handai_4r_new = handai_4r["新規来店人数"].sum()
    handai_4b_new = handai_4b["新規来店人数"].sum()
    handai_5r_new = handai_5r["新規来店人数"].sum()
    handai_5b_new = handai_5b["新規来店人数"].sum()
    handai_6r_new = handai_6r["新規来店人数"].sum()
    handai_6b_new = handai_6b["新規来店人数"].sum()
    handai_M1r_new = handai_M1r["新規来店人数"].sum()
    handai_M1b_new = handai_M1b["新規来店人数"].sum()
    handai_M2r_new = handai_M2r["新規来店人数"].sum()
    handai_M2b_new = handai_M2b["新規来店人数"].sum()

    ############################################################################
    ####################分析結果をresult.csvファイルに出力########################
    ############################################################################

    result = pd.DataFrame({
        "延べ来店人数":[
        str(handai_all),
        str(handai_1_all),
        str(handai_2_all),
        str(handai_3_all),
        str(handai_4_all),
        str(handai_5_all),
        str(handai_6_all),
        str(handai_M1_all),
        str(handai_M2_all),
        str(handai_1r_all),
        str(handai_1b_all),
        str(handai_2r_all),
        str(handai_2b_all),
        str(handai_3r_all),
        str(handai_3b_all),
        str(handai_4r_all),
        str(handai_4b_all),
        str(handai_5r_all),
        str(handai_5b_all),
        str(handai_6r_all),
        str(handai_6b_all),
        str(handai_M1r_all),
        str(handai_M1b_all),
        str(handai_M2r_all),
        str(handai_M2b_all),
        ],
        "新規来店人数":[
        str(handai_new),
        str(handai_1_new),
        str(handai_2_new),
        str(handai_3_new),
        str(handai_4_new),
        str(handai_5_new),
        str(handai_6_new),
        str(handai_M1_new),
        str(handai_M2_new),
        str(handai_1r_new),
        str(handai_1b_new),
        str(handai_2r_new),
        str(handai_2b_new),
        str(handai_3r_new),
        str(handai_3b_new),
        str(handai_4r_new),
        str(handai_4b_new),
        str(handai_5r_new),
        str(handai_5b_new),
        str(handai_6r_new),
        str(handai_6b_new),
        str(handai_M1r_new),
        str(handai_M1b_new),
        str(handai_M2r_new),
        str(handai_M2b_new),
        ]},
        index = [
            "全体",
            "１回",
            "２回",
            "３回",
            "４回",
            "５回",
            "６回",
            "M1回",
            "M2回",
            "１回理系",
            "１回文系",
            "２回理系",
            "２回文系",
            "３回理系",
            "３回文系",
            "４回理系",
            "４回文系",
            "５回理系",
            "５回文系",
            "６回理系",
            "６回文系",
            "M1回理系",
            "M1回文系",
            "M2回理系",
            "M2回文系",
        ])

    result.to_csv("result.csv",encoding="shift_jis")

if __name__ == "__main__":
    Analyze()
