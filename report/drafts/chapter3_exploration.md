# 第3章 探索性分析與類型學建構

**分析時間**: 2025-11-10 23:19:12

## 3.1 全球道德地圖

### 研究問題

- 全球在「守法vs.效益」衝突的分佈模式為何？
- 是否呈現地理聚集或文化聚集？

### 視覺化結果

- [世界地圖](outputs/figures/chapter3_exploration/global_lawful_map.html)
- [文化圈比較](outputs/figures/chapter3_exploration/cluster_comparison.html)
- [描述統計表](outputs/tables/chapter3/global_descriptive_stats.csv)

### 關鍵發現

（待填入：根據圖表結果撰寫）

## 3.2 台灣與東亞的道德定位

### 研究問題

- 台灣在9個道德維度的表現為何？
- 與日本、韓國、中國大陸的異同？

### 視覺化結果

- [東亞四國雷達圖](outputs/figures/chapter3_exploration/east_asia_radar.html)
- [距離熱圖](outputs/figures/chapter3_exploration/east_asia_distance.html)
- [比較表](國家          台灣        日本        韓國        中國  台灣_排名  日本_排名  韓國_排名  中國_排名
介入偏好  0.075286  0.073654  0.061314  0.085179      9      9      9      8
行人優先  0.084832  0.235227  0.132327 -0.026445      8      6      6      9
守法偏好  0.347283  0.412275  0.356526  0.396378      3      2      4      3
性別偏好  0.093214  0.094794  0.121054  0.103895      7      8      7      7
體型偏好  0.130987  0.124455  0.106006  0.131551      6      7      8      6
地位偏好  0.273967  0.318228  0.295447  0.334637      5      5      5      5
年齡偏好  0.345242  0.400064  0.378118  0.353740      4      3      3      4
效益主義  0.392762  0.373656  0.434162  0.422985      2      4      2      2
物種偏好  0.556790  0.596495  0.700412  0.659324      1      1      1      1)

### 關鍵發現

（待填入：根據圖表結果撰寫）

## 3.3 階層式分群：道德距離的拓撲結構

### 研究問題

- 基於道德判斷，國家如何自然分群？
- 是否存在超越地理的「道德親緣關係」？

### 視覺化結果

- [130國樹狀圖](outputs/figures/chapter3_exploration/dendrogram.html)
- [道德距離熱圖](outputs/figures/chapter3_exploration/moral_distance_heatmap.html)

### 評估指標

- **Cophenetic Correlation**: 0.3860
- **Adjusted Rand Index**: 0.1944

### 3.3補充：替代分群方法比較

- [K-means評估](outputs/figures/chapter3_exploration/kmeans_evaluation.html)
- [t-SNE視覺化](outputs/figures/chapter3_exploration/tsne_visualization.html)
- [方法比較](outputs/figures/chapter3_exploration/clustering_methods_comparison.html)

### 關鍵發現

（待填入：根據圖表結果撰寫）

## 3.4 潛在類別分析：道德人格類型學

### 研究問題

- 是否存在不同的「道德決策模式」？
- 這些模式是否對應倫理理論？

### 視覺化結果

- [BIC曲線](outputs/figures/chapter3_exploration/lca_bic_curve.html)
- [類別雷達圖](outputs/figures/chapter3_exploration/lca_class_profiles.html)
- [文化分佈](outputs/figures/chapter3_exploration/lca_culture_distribution.html)

### 最佳類別數: 5

### 3.4補充：敏感度分析

- [極端比例比較](outputs/figures/chapter3_exploration/lca_sensitivity_extreme_ratio.html)
- [詮釋報告](outputs/tables/chapter3/lca_sensitivity_interpretation.md)

### 關鍵發現

（待填入：根據圖表結果撰寫）

---

**註**: 本報告為自動生成的草稿，關鍵發現需根據圖表結果手動填寫。
