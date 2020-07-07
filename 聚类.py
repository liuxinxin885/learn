from sklearn.cluster import KMeans
km=KMeans(n_clusters=3).fit(X)
#预处理
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)#归一化
# X_scaled
# 度量，轮廓系数
from sklearn import metrics
score_scaled=metrics.silhouette_score(X,coordinate.km)
score_scaled
for i in range(2, 5):
    lables_1 = KMeans(i).fit(X_scaled).labels_
    score = metrics.silhouette_score(X, lables_1)
    print(score)
# 密度聚类
from sklearn.cluster import DBSCAN
db=DBSCAN(eps=0.017,min_samples=12).fit(X)

import numpy as np
x=np.random.random(10)
y=np.random.random(10)

#方法一：根据公式求解
d1=np.sqrt(np.sum(np.square(x-y)))