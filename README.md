# MIT Moral Machine 資料分析專案

## 專案簡介

本專案分析MIT Moral Machine資料集，探討全球道德判斷的跨文化差異，聚焦於「守法vs.效益主義」的核心衝突。

## 研究問題

1. 全球在「守法少數vs.違法多數」衝突的選擇分佈為何？
2. 台灣在東亞文化圈的道德定位為何？
3. 哪些個人特徵預測道德選擇？是否受文化調節？
4. 是否存在跨文化的「道德人格類型」？

## 專案結構
```
ethics_prediction_analysis/
├── data/              # 資料目錄
├── src/               # 原始碼
├── scripts/           # 執行腳本
├── outputs/           # 分析結果
├── report/            # 報告文件
└── references/        # 學術文獻
```

## 安裝與執行

### 1. 安裝套件
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 下載資料

請至 [MIT Moral Machine OSF](https://osf.io/3hvt2/) 下載以下檔案至 `data/raw/`:
- SharedResponsesSurvey.csv
- CountriesChangePr.csv
- country_cluster_map.csv
- moral_distance.csv

### 3. 生成資料字典（可選）
```python
from src.utils.codebook_generator import CodebookGenerator

generator = CodebookGenerator('data/raw')
generator.generate_codebook('markdown')
generator.generate_codebook('excel')
```

### 4. 執行分析流程
```bash
# 環境檢查
python scripts/00_setup_environment.py

# 資料處理
python scripts/01_data_loading.py
python scripts/02_data_cleaning.py
python scripts/03_feature_engineering.py

# 探索性分析（第3章）
python scripts/04_descriptive_analysis.py
python scripts/05_global_mapping.py
python scripts/06_east_asia_analysis.py
python scripts/07_hierarchical_clustering.py
python scripts/08_latent_class_analysis.py

# 統計推論（第4章）
python scripts/09_hypothesis_testing.py
python scripts/10_logistic_regression.py
python scripts/11_interaction_analysis.py
python scripts/12_hierarchical_linear_model.py

# 預測模型（第5章）
python scripts/13_model_training.py
python scripts/14_model_evaluation.py
python scripts/15_shap_analysis.py

# 生成所有圖表
python scripts/16_generate_all_figures.py
```

## 主要分析模組

### 資料處理 (src/data/)
- **loader.py**: 資料載入
- **cleaner.py**: 資料清理
- **feature_engineer.py**: 特徵工程

### 分析模組 (src/analysis/)
- **descriptive/**: 描述性統計與視覺化
- **clustering/**: 階層分群與潛在類別分析
- **inference/**: 假設檢定、迴歸、交互作用、階層模型

### 建模模組 (src/modeling/)
- **logistic_model.py**: 邏輯迴歸
- **random_forest_model.py**: 隨機森林
- **xgboost_model.py**: XGBoost
- **explainability.py**: SHAP可解釋性分析

### 工具模組 (src/utils/)
- **codebook_generator.py**: 自動生成資料字典
- **config.py**: 配置管理
- **logger.py**: 日誌記錄

## 作者

資料科學系碩士生

## 授權

本專案僅供學術研究使用。
