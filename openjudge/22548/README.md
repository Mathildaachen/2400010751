# 机智的股民老张
------

总时间限制: 1000ms 内存限制: 65536kB

### 描述

股民老张通过某种渠道事先知道了一支股票在未来几天的价格。老张获得了一个数组 a，其中 a[i] 是给定股票在第 i 天的价格。
现在老张希望通过选择某一天购买该股票并选择未来的另一天出售该股票来最大化他的利润。
返回老张可以从这次交易中获得的最大利润。 如果价格一直下跌，老张无法获得任何利润，则返回 0

### 输入

由空格分开的若干非负整数，数组 a 的长度不超过 100,000，各元素 a[i] 满足 0 <= a[i] <= 10000。

### 输出

一个数，可以从这次交易中获得的最大利润<br>

### 样例输入

7 1 5 3 6 4

### 样例输出

5

### 提示

在第二天买入（价格为 1），在第五天买出（价格为 6），因此收益为 5。
相反，如果输入为 7 6 5 4 3 1，则老张怎么买都不可能获得利润，因此返回 0。

