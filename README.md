# Japanese-Chinese Phonetic Correspondence Analysis

中日语音对应关系的数据分析项目：构建日本教育汉字音韵数据库，运用统计检验量化中日语音对应规律。

## 功能特性

- 构建包含 **1,026** 个日本教育汉字的音韵特征数据库
- 使用 Pandas 完成中日声母-韵母交叉统计与多维度数据透视
- 运用 SciPy 卡方独立性检验（χ²）量化对应关系的统计显著性
- 基于 Seaborn / Matplotlib 绘制声母 / 韵母对应热力图（300dpi 学术级输出）
- 分析结果以 Excel 多工作表形式导出，支持日语教学应用

## 技术栈

Python · Pandas · NumPy · SciPy · Seaborn · Matplotlib

## 目录结构

```
jp-zh-phonetic-analysis/
├── chinese_japanese_analysis.py  # 主分析脚本
└── data/
    └── kj.csv                     # 汉字音韵特征数据
```

## 运行方式

```bash
pip install pandas numpy scipy seaborn matplotlib openpyxl
python chinese_japanese_analysis.py
```

## 输出

- 声母对应热力图 / 韵母对应热力图（300dpi）
- 卡方检验统计报告
- Excel 多工作表分析结果
