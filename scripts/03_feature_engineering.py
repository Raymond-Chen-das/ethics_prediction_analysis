"""
03_feature_engineering.py
==========================
第三步：特徵工程

功能：
1. 建立場景層級特徵（守法、多數、衝突等）
2. 建立使用者道德側寫
3. 分割訓練/測試集
4. 產生特徵說明文件

執行方式：
    python scripts/03_feature_engineering.py
"""

import sys
from pathlib import Path

# 將專案根目錄加入路徑
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.data.feature_engineer import FeatureEngineer
import pandas as pd
import logging
from datetime import datetime
import json

def setup_file_logger(log_dir: str = 'outputs/logs') -> logging.Logger:
    """設定檔案日誌記錄器"""
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)
    
    log_file = log_path / 'feature_engineering.log'
    file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    
    logger = logging.getLogger()
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    
    return logger

def save_featured_data(df: pd.DataFrame, output_dir: str = 'data/processed'):
    """儲存增加特徵的資料"""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    output_file = output_path / 'featured_data.csv'
    
    print(f"\n儲存特徵化資料...")
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    
    file_size_mb = output_file.stat().st_size / 1024**2
    print(f"✅ 已儲存: {output_file}")
    print(f"   檔案大小: {file_size_mb:.2f} MB")
    print(f"   欄位數: {len(df.columns)}")

def save_user_profiles(profiles_df: pd.DataFrame, output_dir: str = 'data/processed'):
    """儲存使用者道德側寫"""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    output_file = output_path / 'user_moral_profiles.csv'
    
    print(f"\n儲存使用者道德側寫...")
    profiles_df.to_csv(output_file, index=False, encoding='utf-8-sig')
    
    print(f"✅ 已儲存: {output_file}")
    print(f"   使用者數: {len(profiles_df):,}")
    
    # 檢查是否有分割標記
    if 'split' in profiles_df.columns:
        train_count = (profiles_df['split'] == 'train').sum()
        test_count = (profiles_df['split'] == 'test').sum()
        print(f"   訓練集: {train_count:,} 位")
        print(f"   測試集: {test_count:,} 位")
        print(f"   ⚠️  注意：側寫已分別基於訓練/測試集計算，避免資料洩漏")

def save_train_test_split(train_df: pd.DataFrame, 
                          test_df: pd.DataFrame,
                          output_dir: str = 'data/processed'):
    """儲存訓練/測試集"""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"\n儲存訓練/測試集...")
    
    # 儲存訓練集
    train_file = output_path / 'train_data.csv'
    train_df.to_csv(train_file, index=False, encoding='utf-8-sig')
    train_size_mb = train_file.stat().st_size / 1024**2
    print(f"✅ 訓練集: {train_file}")
    print(f"   {len(train_df):,} 行, {train_size_mb:.2f} MB")
    
    # 儲存測試集
    test_file = output_path / 'test_data.csv'
    test_df.to_csv(test_file, index=False, encoding='utf-8-sig')
    test_size_mb = test_file.stat().st_size / 1024**2
    print(f"✅ 測試集: {test_file}")
    print(f"   {len(test_df):,} 行, {test_size_mb:.2f} MB")
    
    # 儲存分割索引
    split_index = {
        'train_users': train_df['UserID'].unique().tolist(),
        'test_users': test_df['UserID'].unique().tolist(),
        'split_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'test_size': len(test_df) / (len(train_df) + len(test_df))
    }
    
    index_file = output_path / 'train_test_split.json'
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(split_index, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 分割索引: {index_file}")

def save_feature_descriptions(descriptions: dict, output_dir: str = 'outputs/tables/chapter2'):
    """儲存特徵說明文件"""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"\n生成特徵說明文件...")
    
    # 1. CSV格式
    desc_df = pd.DataFrame([
        {'特徵名稱': name, '說明': desc}
        for name, desc in descriptions.items()
    ])
    
    csv_file = output_path / 'feature_descriptions.csv'
    desc_df.to_csv(csv_file, index=False, encoding='utf-8-sig')
    print(f"✅ CSV格式: {csv_file}")
    
    # 2. JSON格式
    json_file = output_path / 'feature_descriptions.json'
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(descriptions, f, ensure_ascii=False, indent=2)
    print(f"✅ JSON格式: {json_file}")

def generate_feature_statistics(df: pd.DataFrame, output_dir: str = 'outputs/tables/chapter2'):
    """生成特徵統計報告"""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"\n生成特徵統計報告...")
    
    # 場景特徵統計
    scenario_stats = []
    
    feature_cols = ['is_lawful', 'is_majority', 'chose_lawful', 
                   'chose_majority', 'lawful_vs_majority_conflict']
    
    for col in feature_cols:
        if col in df.columns:
            scenario_stats.append({
                '特徵': col,
                '平均值': f"{df[col].mean():.3f}",
                '標準差': f"{df[col].std():.3f}",
                '最小值': int(df[col].min()),
                '最大值': int(df[col].max()),
                '總和': f"{df[col].sum():,}"
            })
    
    stats_df = pd.DataFrame(scenario_stats)
    stats_file = output_path / 'scenario_feature_stats.csv'
    stats_df.to_csv(stats_file, index=False, encoding='utf-8-sig')
    print(f"✅ 場景特徵統計: {stats_file}")

def generate_markdown_report(df: pd.DataFrame,
                            profiles_df: pd.DataFrame,
                            descriptions: dict,
                            output_dir: str = 'report/drafts'):
    """生成Markdown格式的報告草稿"""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    report_file = output_path / 'chapter2_section3_feature_engineering.md'
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# 第2章 資料處理\n\n")
        f.write("## 2.3 特徵工程\n\n")
        
        f.write("### 特徵工程目標\n\n")
        f.write("為了深入分析「守法vs.效益」的道德兩難，本研究建立以下特徵：\n\n")
        f.write("1. **場景層級特徵**：標記每個選擇的守法性、多數性、衝突性\n")
        f.write("2. **國家層級特徵**：整合國家的道德偏好 AMCE 值（用於階層模型）\n")
        f.write("3. **使用者道德側寫**：量化每位使用者的道德傾向（僅用於探索）\n\n")
        
        f.write("### 場景層級特徵\n\n")
        f.write("| 特徵名稱 | 說明 | 平均值 |\n")
        f.write("|---------|------|--------|\n")
        
        scenario_features = ['is_lawful', 'is_majority', 'chose_lawful', 
                            'chose_majority', 'lawful_vs_majority_conflict']
        
        for feat in scenario_features:
            if feat in df.columns:
                desc = descriptions.get(feat, '')
                mean_val = df[feat].mean()
                f.write(f"| {feat} | {desc} | {mean_val:.3f} |\n")
        
        f.write("\n#### 關鍵發現\n\n")
        
        # 統計守法選擇率
        if 'chose_lawful' in df.columns and 'Saved' in df.columns:
            chose_lawful_rate = df[df['Saved'] == 1]['is_lawful'].mean()
            f.write(f"- **守法選擇率**: {chose_lawful_rate*100:.1f}%\n")
        
        # 統計多數選擇率
        if 'chose_majority' in df.columns and 'Saved' in df.columns:
            chose_majority_rate = df[df['Saved'] == 1]['is_majority'].mean()
            f.write(f"- **多數選擇率**: {chose_majority_rate*100:.1f}%\n")
        
        # 衝突場景比例
        if 'lawful_vs_majority_conflict' in df.columns:
            conflict_rate = df.groupby('ResponseID')['lawful_vs_majority_conflict'].first().mean()
            f.write(f"- **衝突場景比例**: {conflict_rate*100:.1f}%\n\n")
        
        # 國家層級特徵
        country_features = [col for col in df.columns if col.startswith('country_')]
        if country_features:
            f.write("### 國家層級特徵\n\n")
            f.write("從 `CountriesChangePr.csv` 整合國家的道德偏好 AMCE 值，用於階層線性模型分析。\n\n")
            f.write("**已整合的國家特徵**:\n\n")
            
            for feat in country_features:
                desc = descriptions.get(feat, '')
                if feat in df.columns:
                    mean_val = df[feat].mean()
                    std_val = df[feat].std()
                    f.write(f"- `{feat}`: {desc}\n")
                    f.write(f"  - 平均值: {mean_val:.3f}, 標準差: {std_val:.3f}\n")
            f.write("\n")
        
        f.write("### 使用者道德側寫\n\n")
        f.write("基於使用者在衝突場景中的選擇，建立道德傾向側寫。\n\n")
        f.write("**⚠️ 重要：為避免資料洩漏，使用者側寫分別基於訓練集和測試集計算**\n\n")
        f.write("- 訓練集使用者側寫：僅使用訓練集資料計算\n")
        f.write("- 測試集使用者側寫：僅使用測試集資料計算\n")
        f.write("- 使用者側寫**不應用於預測模型**，僅用於探索性分析\n\n")
        
        f.write("| 側寫指標 | 說明 | 平均值 | 標準差 |\n")
        f.write("|---------|------|--------|--------|\n")
        
        profile_features = ['utilitarian_score', 'deontology_score', 
                           'consistency_score', 'n_scenarios']
        
        for feat in profile_features:
            if feat in profiles_df.columns:
                desc = descriptions.get(feat, '')
                mean_val = profiles_df[feat].mean()
                std_val = profiles_df[feat].std()
                f.write(f"| {feat} | {desc} | {mean_val:.3f} | {std_val:.3f} |\n")
        
        f.write(f"\n- **側寫使用者數**: {len(profiles_df):,} 位\n")
        f.write(f"- **平均完成場景數**: {profiles_df['n_scenarios'].mean():.1f} 個\n\n")
        
        f.write("### 道德傾向分佈\n\n")
        
        if 'utilitarian_score' in profiles_df.columns:
            # 分類使用者
            strong_util = (profiles_df['utilitarian_score'] > 0.7).sum()
            moderate_util = ((profiles_df['utilitarian_score'] >= 0.3) & 
                           (profiles_df['utilitarian_score'] <= 0.7)).sum()
            weak_util = (profiles_df['utilitarian_score'] < 0.3).sum()
            
            f.write("**效益主義傾向分佈**:\n\n")
            f.write(f"- 強效益主義 (>0.7): {strong_util:,} 位 ({strong_util/len(profiles_df)*100:.1f}%)\n")
            f.write(f"- 中間派 (0.3-0.7): {moderate_util:,} 位 ({moderate_util/len(profiles_df)*100:.1f}%)\n")
            f.write(f"- 強義務論 (<0.3): {weak_util:,} 位 ({weak_util/len(profiles_df)*100:.1f}%)\n\n")
        
        f.write("### 訓練/測試集分割\n\n")
        f.write("採用使用者層級分割（80/20），確保同一使用者的資料不會同時出現在訓練集和測試集，避免資料洩漏。\n\n")
        
        train_file = Path('data/processed/train_data.csv')
        test_file = Path('data/processed/test_data.csv')
        
        if train_file.exists() and test_file.exists():
            train_df_check = pd.read_csv(train_file, nrows=1000)
            test_df_check = pd.read_csv(test_file, nrows=1000)
            
            f.write(f"- **訓練集**: 約 {len(df)*0.8:,.0f} 行\n")
            f.write(f"- **測試集**: 約 {len(df)*0.2:,.0f} 行\n\n")
        
        f.write("### 特徵使用注意事項\n\n")
        f.write("不同分析階段適用的特徵：\n\n")
        f.write("**第3章 探索性分析**:\n")
        f.write("- ✅ 場景層級特徵\n")
        f.write("- ✅ 國家層級特徵\n")
        f.write("- ✅ 使用者道德側寫（用於分群和描述）\n\n")
        f.write("**第4章 統計推論**:\n")
        f.write("- ✅ 場景層級特徵\n")
        f.write("- ✅ 國家層級特徵（用於階層線性模型）\n")
        f.write("- ❌ 使用者道德側寫（避免循環論證）\n\n")
        f.write("**第5章 預測模型**:\n")
        f.write("- ✅ 場景層級特徵\n")
        f.write("- ✅ 人口統計變數\n")
        f.write("- ✅ 文化圈分類\n")
        f.write("- ❌ 使用者道德側寫（會造成資料洩漏）\n\n")
        
        f.write("特徵工程完成後，資料已準備好進行探索性分析和建模。\n\n")
    
    print(f"✅ Markdown報告: {report_file}")

def main():
    """主執行函數"""
    print("\n" + "=" * 60)
    print("🔧 MIT Moral Machine - 特徵工程 (Step 03)")
    print("=" * 60)
    
    # 設定檔案日誌
    logger = setup_file_logger()
    logger.info("開始執行特徵工程腳本...")
    
    try:
        # Step 1: 載入資料
        print("\n【Step 1】載入資料...")
        
        # 載入清理後的資料
        cleaned_file = Path('data/processed/cleaned_survey.csv')
        if not cleaned_file.exists():
            print(f"\n❌ 錯誤: 找不到檔案 {cleaned_file}")
            print("請先執行 02_data_cleaning.py")
            return
        
        df = pd.read_csv(cleaned_file)
        print(f"✅ 載入清理後資料: {len(df):,} 行")
        
        # 載入國家變化概率資料
        countries_change_file = Path('data/raw/CountriesChangePr.csv')
        if not countries_change_file.exists():
            print(f"\n⚠️  警告: 找不到 {countries_change_file}")
            print("將跳過國家層級特徵合併")
            countries_change_df = None
        else:
            countries_change_df = pd.read_csv(countries_change_file)
            print(f"✅ 載入國家層級資料: {len(countries_change_df)} 個國家")
        
        # Step 2: 建立場景特徵
        print("\n【Step 2】建立場景特徵...")
        engineer = FeatureEngineer()
        df_featured = engineer.engineer_features(df)
        
        # Step 3: 合併國家層級特徵
        if countries_change_df is not None:
            print("\n【Step 3】合併國家層級特徵...")
            df_featured = engineer.merge_country_features(df_featured, countries_change_df)
            
            # 新增：增加特徵可用性標記
            df_featured = engineer.add_feature_availability_flag(df_featured)
        else:
            print("\n【Step 3】跳過國家層級特徵合併")
        
        # Step 4: 分割訓練/測試集（在計算使用者側寫之前！）
        print("\n【Step 4】分割訓練/測試集...")
        train_df, test_df = engineer.split_train_test(df_featured)
        
        # Step 5: 分別計算訓練集和測試集的使用者側寫（避免資料洩漏）
        print("\n【Step 5】建立使用者道德側寫...")
        print("\n  計算訓練集使用者側寫...")
        train_user_profiles = engineer.create_user_profiles(train_df)
        train_user_profiles['split'] = 'train'  # 標記為訓練集
        
        print("\n  計算測試集使用者側寫...")
        test_user_profiles = engineer.create_user_profiles(test_df)
        test_user_profiles['split'] = 'test'  # 標記為測試集
        
        # 合併側寫（僅用於儲存和報告，不用於預測）
        all_user_profiles = pd.concat([train_user_profiles, test_user_profiles], ignore_index=True)
        
        print(f"\n  總計: {len(all_user_profiles):,} 位使用者")
        print(f"    訓練集: {len(train_user_profiles):,} 位")
        print(f"    測試集: {len(test_user_profiles):,} 位")
        
        # Step 6: 儲存結果
        print("\n【Step 6】儲存結果...")
        save_featured_data(df_featured)
        save_user_profiles(all_user_profiles)
        save_train_test_split(train_df, test_df)
        
        # Step 7: 產生報告
        print("\n【Step 7】產生報告...")
        feature_descriptions = engineer.get_feature_descriptions()
        save_feature_descriptions(feature_descriptions)
        generate_feature_statistics(df_featured)
        generate_markdown_report(df_featured, all_user_profiles, feature_descriptions)
        
        # 完成
        print("\n" + "=" * 60)
        print("✅ 特徵工程完成！")
        print("=" * 60)
        print("\n📊 已產生以下輸出:")
        print("  - data/processed/featured_data.csv")
        print("  - data/processed/user_moral_profiles.csv")
        print("  - data/processed/train_data.csv")
        print("  - data/processed/test_data.csv")
        print("  - data/processed/train_test_split.json")
        print("  - outputs/logs/feature_engineering.log")
        print("  - outputs/tables/chapter2/feature_descriptions.csv")
        print("  - outputs/tables/chapter2/scenario_feature_stats.csv")
        print("  - report/drafts/chapter2_section3_feature_engineering.md")
        print("\n⚠️  重要提醒：")
        print("  - 使用者側寫已分別基於訓練集和測試集計算")
        print("  - 預測模型時請勿使用使用者側寫特徵（避免資料洩漏）")
        print("  - 使用者側寫僅用於第3章探索性分析")
        print("\n💡 下一步: python scripts/04_descriptive_analysis.py")
        print("=" * 60 + "\n")
        
        logger.info("特徵工程腳本執行完成")
        
    except Exception as e:
        logger.error(f"執行失敗: {e}", exc_info=True)
        print(f"\n❌ 錯誤: {e}")
        raise

if __name__ == '__main__':
    main()