# -*- coding: utf-8 -*-
"""
Created on Wed May 19 23:29:38 2021

@author: noridomi_shuzo
"""

"""
100本ノックの１章のコード

ECサイトの顧客データ分析

customer_master.csv:顧客データ. 名前、性別など
item_master.csv: 取り扱い商品データ.商品名、価格など
transaction_1.csv: 購入明細データ1
transaction_2.csv: 購入明細データ1の続き
transaction_detail_1.csv: 購入明細の詳細データ1
transaction_detail_2.csv: 購入明細の詳細データ2
"""

import pandas as pd




customer_master = pd.read_csv('customer_master.csv')
# customer_master.head()
item_master     = pd.read_csv('item_master.csv')
transaction_1   = pd.read_csv('transaction_1.csv')
transaction_detail_1 = pd.read_csv('transaction_detail_1.csv')

transaction_2   = pd.read_csv('transaction_2.csv')
transaction_detail_2 = pd.read_csv('transaction_detail_2.csv')

#　データを縦に結合
transaction_union = pd.concat([transaction_1,transaction_2],ignore_index=True)
transaction_detail_union = pd.concat([transaction_detail_1,transaction_detail_2],ignore_index=True)


# 結合できてるか、行数で確認すると本には書いてあった
print(len(transaction_1))
print(len(transaction_2))
print(len(transaction_union))

# 