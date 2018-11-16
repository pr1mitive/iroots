import pandas as pd

def Analyze():
    file_name = input("Please input CSV filename which you'd like to analyze.\n" +
    "CSV filename: ")
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

    """
    ############################################################################
    ####################分析結果をresult.txtファイルに出力########################
    ############################################################################

    result_file_name = "result.txt"
    f = open(result_file_name, mode="w")

    #延べ来店人数の結果を出力
    f.write("阪大全体の延べ来店人数：" + str(handai_all) +"\n")
    f.write("阪大１回の延べ来店人数：" + str(handai_1_all) +"\n")
    f.write("阪大２回の延べ来店人数：" + str(handai_2_all) +"\n")
    f.write("阪大３回の延べ来店人数：" + str(handai_3_all) +"\n")
    f.write("阪大４回の延べ来店人数：" + str(handai_4_all) +"\n")
    f.write("阪大５回の延べ来店人数：" + str(handai_5_all) +"\n")
    f.write("阪大６回の延べ来店人数：" + str(handai_6_all) +"\n")
    f.write("阪大M１の延べ来店人数：" + str(handai_M1_all) +"\n")
    f.write("阪大M２の延べ来店人数：" + str(handai_M2_all) +"\n\n")

    f.write("阪大１回理系の延べ来店人数：" + str(handai_1r_all) +"\n")
    f.write("阪大１回文系の延べ来店人数：" + str(handai_1b_all) +"\n")
    f.write("阪大２回理系の延べ来店人数：" + str(handai_2r_all) +"\n")
    f.write("阪大２回文系の延べ来店人数：" + str(handai_2b_all) +"\n")
    f.write("阪大３回理系の延べ来店人数：" + str(handai_3r_all) +"\n")
    f.write("阪大３回文系の延べ来店人数：" + str(handai_3b_all) +"\n")
    f.write("阪大４回理系の延べ来店人数：" + str(handai_4r_all) +"\n")
    f.write("阪大４回文系の延べ来店人数：" + str(handai_4b_all) +"\n")
    f.write("阪大５回理系の延べ来店人数：" + str(handai_5r_all) +"\n")
    f.write("阪大５回文系の延べ来店人数：" + str(handai_5b_all) +"\n")
    f.write("阪大６回理系の延べ来店人数：" + str(handai_6r_all) +"\n")
    f.write("阪大６回文系の延べ来店人数：" + str(handai_6b_all) +"\n")
    f.write("阪大M１理系の延べ来店人数：" + str(handai_M1r_all) +"\n")
    f.write("阪大M１回文系の延べ来店人数：" + str(handai_M1b_all) +"\n")
    f.write("阪大M２回理系の延べ来店人数：" + str(handai_M2r_all) +"\n")
    f.write("阪大M２回文系の延べ来店人数：" + str(handai_M2b_all) +"\n\n")

    #新規来店人数の結果を出力
    f.write("阪大全体の新規来店人数：" + str(handai_new) +"\n")
    f.write("阪大１回の新規来店人数：" + str(handai_1_new) +"\n")
    f.write("阪大２回の新規来店人数：" + str(handai_2_new) +"\n")
    f.write("阪大４回の延べ来店人数：" + str(handai_4_new) +"\n")
    f.write("阪大３回の新規来店人数：" + str(handai_3_new) +"\n")
    f.write("阪大５回の新規来店人数：" + str(handai_5_new) +"\n")
    f.write("阪大６回の新規来店人数：" + str(handai_6_new) +"\n")
    f.write("阪大M１の新規来店人数：" + str(handai_M1_new) +"\n")
    f.write("阪大M２の新規来店人数：" + str(handai_M2_new) +"\n\n")

    f.write("阪大１回理系の新規来店人数：" + str(handai_1r_new) +"\n")
    f.write("阪大１回文系の新規来店人数：" + str(handai_1b_new) +"\n")
    f.write("阪大２回理系の新規来店人数：" + str(handai_2r_new) +"\n")
    f.write("阪大２回文系の新規来店人数：" + str(handai_2b_new) +"\n")
    f.write("阪大３回理系の新規来店人数：" + str(handai_3r_new) +"\n")
    f.write("阪大３回文系の新規来店人数：" + str(handai_3b_new) +"\n")
    f.write("阪大４回理系の新規来店人数：" + str(handai_4r_new) +"\n")
    f.write("阪大４回文系の新規来店人数：" + str(handai_4b_new) +"\n")
    f.write("阪大５回理系の新規来店人数：" + str(handai_5r_new) +"\n")
    f.write("阪大５回文系の新規来店人数：" + str(handai_5b_new) +"\n")
    f.write("阪大６回理系の新規来店人数：" + str(handai_6r_new) +"\n")
    f.write("阪大６回文系の新規来店人数：" + str(handai_6b_new) +"\n")
    f.write("阪大M１文系の新規来店人数：" + str(handai_M1b_new) +"\n")
    f.write("阪大M１理系の新規来店人数：" + str(handai_M1r_new) +"\n")
    f.write("阪大M２理系の新規来店人数：" + str(handai_M2r_new) +"\n")
    f.write("阪大M２文系の新規来店人数：" + str(handai_M2b_new) +"\n")

    f.close()
    """

if __name__ == "__main__":
    Analyze()
