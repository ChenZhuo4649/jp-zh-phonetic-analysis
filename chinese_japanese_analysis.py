# filename: linguistic_analysis.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

class PhoneticAnalyzer:
    """中日语音对应分析系统（兼容图像特征）"""
    
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None
        self.results = {}
        
        # 基于图像特征的视觉参数配置
        plt.rcParams.update({
            'font.family': 'Arial Unicode MS',  # 中文字体支持
            'axes.unicode_minus': False,         # 修复负号显示
            'savefig.dpi': 300                   # 匹配图像分辨率
        })
        sns.set_theme(style="whitegrid", font_scale=0.85)

    def load_data(self):
        """加载数据并验证字段"""
        try:
            self.df = pd.read_csv(self.data_path)
            required_cols = {'S_汉1', 'S_汉2', 'S_日1', 'S_日2'}
            if not required_cols.issubset(self.df.columns):
                missing = required_cols - set(self.df.columns)
                raise KeyError(f"缺失字段: {', '.join(missing)}")
            print(f"成功加载 {len(self.df)} 条数据")
            return True
        except FileNotFoundError:
            print(f"错误：文件 {self.data_path} 不存在")
            exit()

    def generate_matrices(self):
        """生成双对比矩阵（对应图像布局）"""
        # 声母矩阵（左侧蓝色）
        self.results['initial'] = pd.crosstab(
            self.df['S_汉1'], self.df['S_日1'],
            rownames=['汉语声母'], colnames=['日语声部']
        )
        
        # 韵母矩阵（右侧红色）
        self.results['final'] = pd.crosstab(
            self.df['S_汉2'], self.df['S_日2'],
            rownames=['汉语韵母'], colnames=['日语韵部']
        )

    def visualize(self):
        """生成图像风格的可视化图表"""
        fig, axes = plt.subplots(1, 2, figsize=(20, 8))
        
        # 左侧声母矩阵（深蓝色调）
        sns.heatmap(self.results['initial'], 
                    cmap="Blues", annot=True, fmt="d",
                    linewidths=0.5, ax=axes,       # 关键修正点：axes
                    annot_kws={"size": 10})
        axes.set_title("声母对应 (S_汉1 vs S_日1)", fontsize=12)
        axes.set_xticklabels(axes.get_xticklabels(), 
                              rotation=45, ha='right', fontsize=10)
        axes.set_yticklabels(axes.get_yticklabels(), 
                              fontsize=10, rotation=0)

        # 右侧韵母矩阵（橙红色调）
        sns.heatmap(self.results['final'], 
                    cmap="OrRd", annot=True, fmt="d",
                    linewidths=0.5, ax=axes,      # 关键修正点：axes
                    annot_kws={"size": 10})
        axes.set_title("韵母对应 (S_汉2 vs S_日2)", fontsize=12)
        axes.set_xticklabels(axes.get_xticklabels(),
                              rotation=45, ha='right', fontsize=10)
        axes.set_yticklabels(axes.get_yticklabels(),
                              fontsize=10, rotation=0)

        plt.tight_layout()
        plt.savefig("analysis_result.png", bbox_inches='tight')
        print("图表已生成（匹配图像布局）")

    def analyze_significance(self):
        """执行卡方检验（匹配图像数据逻辑）"""
        chi2_init = chi2_contingency(self.results['initial'])[:2]
        chi2_final = chi2_contingency(self.results['final'])[:2]
        
        print("\n=== 统计显著性 ===")
        print(f"声母关联性: χ²={chi2_init:.2f} (p={chi2_init:.4f})")
        print(f"韵母关联性: χ²={chi2_final:.2f} (p={chi2_final:.4f})")

if __name__ == "__main__":
    # 运行示例（路径需匹配图像数据源）
    analyzer = PhoneticAnalyzer("/Users/chenzhuo/Documents/Program_file/data/kj.csv")
    if analyzer.load_data():
        analyzer.generate_matrices()
        analyzer.visualize()
        analyzer.analyze_significance()