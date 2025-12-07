# MIT Moral Machine 跨文化道德判斷分析

## 🎯 研究問題

**道德判斷究竟是由個人特質還是情境因素主導？**

本專案分析MIT Moral Machine資料集（1128萬筆 → 37萬筆有效場景），探討全球在「守法vs.效益主義」衝突中的選擇模式，並定位台灣在東亞的道德座標。

---

## 📊 核心發現

1. **情境主義主導**：約86%變異來自情境，文化僅0.25% (ICC)，個人<0.1% (R²)
2. **全球偏好效益**：77%選擇拯救多數，守法率僅22.6%
3. **文化差異微弱**：Eastern vs. Western差5% (p<.001)，但效果量僅0.032
4. **台灣定位特殊**：效益主義0.393（全球倒數二）、守法0.347（東亞最低）、最近似韓國
5. **「道德人格」是假象**：92%使用者僅1次觀測，極端比例100%→54.7%（觀測增加時）

---

## 🗂️ 專案結構

```
ethics_prediction_analysis/
├── data/              # 資料（raw/processed/codebook）
├── src/               # 原始碼（data/analysis/modeling/visualization/utils）
├── scripts/           # 執行腳本（00-15按章節編號）
├── outputs/           # 分析結果（tables/figures/models）
├── report/            # 第2-6章報告.md
└── requirements.txt   # 套件依賴
```

**核心模組**：

- `src/data/`: 載入、清理、特徵工程
- `src/analysis/`: 描述統計、分群、推論統計（卡方、迴歸、HLM）
- `src/modeling/`: XGBoost、SHAP解釋
- `src/visualization/`: 道德光譜、距離矩陣、SHAP圖表

---

## 🚀 快速開始

### 環境設定

```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 資料下載

至 [MIT Moral Machine OSF](https://osf.io/3hvt2/) 下載以下檔案至 `data/raw/`:

- **SharedResponsesSurvey.csv** (283.7 MB) - 主要資料
- CountriesChangePr.csv (21.1 KB) - 國家效應值
- country_cluster_map.csv (2.0 KB) - 文化圈分組
- moral_distance.csv (2.5 KB) - 道德距離矩陣

### 完整分析流程

```bash
# 依序執行scripts/中的腳本（00-16）
python scripts/00_setup_environment.py
python scripts/01_data_loading.py
# ... 依此類推
python scripts/15_moral_spectrum.py
```

---

## 📖 研究架構

### 第2章：資料處理（11M → 377K）

資料清理、篩選「守法=少數」衝突場景、特徵工程

### 第3章：探索性分析

全球道德地圖、台灣vs東亞定位、階層分群（失敗案例）、**LCA敏感度分析（揭示測量假象）**

### 第4章：統計推論

卡方檢定（V=0.032）、邏輯迴歸（R²=0.04%）、**HLM（ICC=0.25%）**

### 第5章：預測模型

XGBoost（AUC=63.8%）、SHAP分析（場景53% > 個人25% > 文化10%）、**跨層級整合（大數法則）**

### 第6章：哲學批判

從數據到意義的跨越、方法論盲點、is-ought區分

---

## 🏆 主要貢獻

**學術貢獻**：

- 情境主義的實證支持（130國、86%變異）
- 跨層級整合方法論（個人vs.國家的統一解釋）
- 測量假象識別（LCA敏感度分析）
- 台灣道德定位的首次系統性研究

**方法論創新**：

- 三角驗證策略（描述→推論→機器學習）
- 誠實報告失敗（分群→連續光譜洞察）
- 效果量優先於p值（大數據時代的統計思維）
- SHAP跨方法驗證

---

## ⚠️ 研究限制

**資料**：自我選擇偏誤、92%使用者僅1次觀測、極端情境篩選  
**方法**：觀察性研究（無因果推論）、文化效度未充分檢驗、二維簡化  
**詮釋**：點擊≠道德判斷、虛擬≠真實、is≠ought

---

**作者**：CHIA-HSIANG CHEN

**課程**：東吳大學資料科學系-資料分析軟體與應用課程（在職專班）  

---

**最後更新**：2024年12月7日 | **狀態**：✅ 已完成

---

## 📌 快速參考

| 問題 | 答案 | 證據 |
|-----|------|------|
| 道德判斷由什麼主導？ | 情境（~86%） | HLM: ICC=0.25% |
| 文化影響多大？ | 極微（0.25%） | Cramér's V=0.032 |
| 全球偏好？ | 效益主義（77%） | 守法率22.6% |
| 台灣定位？ | 效益最低、最近似韓國 | AMCE=0.393 |
| 道德人格存在？ | 主要是假象 | 100%→54.7% |
| 預測上限？ | 中等（AUC=63.8%） | XGBoost |

**文件索引**：  
完整方法論→`第2-5章統整報告.md` | 哲學反思→`第6章.md` | 資料處理→`第2章.md`

---

**End of README** 🎓
