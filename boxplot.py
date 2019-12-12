import matplotlib.pyplot as plt

# 数学の点数
math = [82, 75, 50, 73, 65, 95, 78, 93, 71, 83]
# 英語の点数
english = [77, 92, 62, 77, 64, 45, 28, 60, 37, 86]

# 点数のタプル
points = (math, english)

# 箱ひげ図
fig, ax = plt.subplots()


bp = ax.boxplot(points) # 複数指定する場合はタプル型で渡します。
ax.set_xticklabels(['math', 'english'])

plt.title('exam')
plt.grid() # 横線ラインを入れることができます。

# 描画
plt.show()
