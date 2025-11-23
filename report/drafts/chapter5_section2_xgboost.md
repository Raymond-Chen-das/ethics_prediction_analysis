## 5.2 機器學習驗證

**分析時間**: 2025-11-24 00:10:10

### 研究目的

以 XGBoost 機器學習模型驗證第4章統計推論的發現，
並透過 SHAP 可解釋性分析比較特徵重要性排序。

### 資料與特徵

- **訓練樣本數**: 74,847
- **特徵數**: 11
- **目標變數分佈**: chose_lawful=1 佔 45.1%

**特徵列表**：
- DiffNumberOFCharacters
- PedPed
- Review_age
- Review_political
- Review_religious
- country_law_preference
- country_utilitarian
- lawful_requires_intervention
- Cluster_Western
- Cluster_Eastern
- Cluster_Southern

### 模型性能

| 指標 | 測試集 | 5-fold CV |
|------|--------|-----------|
| Accuracy | 0.6059 | 0.6099 ± 0.0026 |
| Precision | 0.5869 | - |
| Recall | 0.4482 | - |
| F1 Score | 0.5083 | - |
| ROC-AUC | 0.6382 | 0.6383 ± 0.0009 |

### SHAP 特徵重要性

| 排序 | 特徵 | SHAP 重要性 | 影響方向 |
|------|------|------------|----------|
| 1 | DiffNumberOFCharacters | 0.3650 | ↑守法 |
| 2 | lawful_requires_intervention | 0.1351 | ↓效益 |
| 3 | country_utilitarian | 0.0956 | ↓效益 |
| 4 | country_law_preference | 0.0858 | ↑守法 |
| 5 | Review_religious | 0.0803 | ↑守法 |
| 6 | Review_political | 0.0787 | ↓效益 |
| 7 | Review_age | 0.0771 | ↓效益 |
| 8 | Cluster_Eastern | 0.0097 | ↓效益 |
| 9 | Cluster_Western | 0.0062 | ↑守法 |
| 10 | Cluster_Southern | 0.0034 | ↓效益 |

### 與第4章的比較

**一致性驗證**：
- 模型 ROC-AUC = 0.6382，顯示預測能力有限
- 與第4章 Pseudo R² = 0.0004 的發現一致：個人/文化因素對道德選擇的解釋力有限
- SHAP 排序與第4章效果量方向一致

### 關鍵發現

1. **最重要特徵**：DiffNumberOFCharacters (SHAP = 0.3650)
2. **預測能力有限**：AUC = 0.6382，略優於隨機猜測
3. **驗證情境主義**：即使使用非線性模型，個人/文化因素仍難以預測道德選擇

### 視覺化結果

- [ROC 曲線](../outputs/figures/chapter5/roc_curve.html)
- [混淆矩陣](../outputs/figures/chapter5/confusion_matrix.html)
- [SHAP 特徵重要性](../outputs/figures/chapter5/shap_importance.html)
