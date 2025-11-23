import pandas as pd

# 載入場景層級資料（轉換後）
train_scene = pd.read_csv("data/processed/featured_data.csv")

# 或者用你的 transformer 輸出
# train_scene = 已轉換的 DataFrame

# ========================================
# 診斷1：檢查衝突場景 vs 非衝突場景的分佈
# ========================================
if 'lawful_vs_majority_conflict' in train_scene.columns:
    print("=" * 60)
    print("診斷1：衝突場景分析")
    print("=" * 60)
    
    conflict = train_scene[train_scene['lawful_vs_majority_conflict'] == 1]
    non_conflict = train_scene[train_scene['lawful_vs_majority_conflict'] == 0]
    
    print(f"衝突場景數: {len(conflict):,} ({len(conflict)/len(train_scene)*100:.1f}%)")
    print(f"非衝突場景數: {len(non_conflict):,} ({len(non_conflict)/len(train_scene)*100:.1f}%)")
    
    print(f"\n衝突場景守法率: {conflict['chose_lawful'].mean()*100:.1f}%")
    print(f"非衝突場景守法率: {non_conflict['chose_lawful'].mean()*100:.1f}%")
    print(f"整體守法率: {train_scene['chose_lawful'].mean()*100:.1f}%")

# ========================================
# 診斷2：檢查 chose_lawful 與 chose_majority 的關係
# ========================================
print("\n" + "=" * 60)
print("診斷2：chose_lawful vs chose_majority 交叉表")
print("=" * 60)

crosstab = pd.crosstab(
    train_scene['chose_lawful'], 
    train_scene['chose_majority'],
    margins=True
)
print(crosstab)

# ========================================
# 診斷3：回到原始選項層級資料驗證
# ========================================
print("\n" + "=" * 60)
print("診斷3：選項層級原始資料驗證")
print("=" * 60)

train_raw = pd.read_csv("data/processed/train_data.csv")

# 選項層級的 chose_lawful mean
print(f"選項層級 chose_lawful.mean(): {train_raw['chose_lawful'].mean()*100:.2f}%")

# 場景層級：取守法方的 Saved 值
scene_lawful = train_raw[train_raw['is_lawful'] == 1].groupby('ResponseID')['Saved'].first()
print(f"場景層級守法率（重新計算）: {scene_lawful.mean()*100:.2f}%")

# 只看衝突場景
if 'lawful_vs_majority_conflict' in train_raw.columns:
    conflict_ids = train_raw[train_raw['lawful_vs_majority_conflict'] == 1]['ResponseID'].unique()
    conflict_lawful = scene_lawful[scene_lawful.index.isin(conflict_ids)]
    print(f"衝突場景守法率: {conflict_lawful.mean()*100:.2f}%")