# とりあえず線形回帰をやる前にsin関数をランダムに出力してみる
import matplotlib.pyplot as plt
import numpy as np

z = np.arange(-7, 7, 0.1)
## 誤差は正規分布とする
e = [x for x = np.random.randn() in range(140)]
phi_z = np.sin(z) + e
plt.plot(z, phi_z)

## プロットを散布図に変える
plt.scatter(z, phi_z)

# 以上のデータを元に線形回帰を行いたい

