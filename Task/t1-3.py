import pandas as pd
import matplotlib.pyplot as plt

data = {
    "姓名": ["A", "B", "C", "D", "E", "Z"],
    "Python": [85, 92, 78, 96, 88, 70],
    "数学": [76, 89, 82, 95, 80, 85],
    "英语": [90, 85, 75, 91, 86, 80]
}

df = pd.DataFrame(data)

df["平均分"] = df[["Python", "数学", "英语"]].mean(axis=1)

# 绘制折线图
plt.plot(df["姓名"], df["平均分"], marker="o")

plt.title("学生平均成绩折线图")
plt.xlabel("学生")
plt.ylabel("平均分")

plt.ylim(0, 100)
plt.show()
