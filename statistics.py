import scipy.stats as stats

before = [-0.001900, -0.002565, -0.001803, -0.002425, -0.001979, -0.002022, -0.002627, -0.002258, -0.002811, -0.002087, -0.001928, -0.002327, -0.001528, -0.001777, -0.002458]

after = [-0.000749, -0.002134, -0.001594, -0.001740, -0.001784, -0.001786, -0.001616, -0.001620, -0.002175, -0.001768, -0.001731, -0.001775, -0.000723, -0.000739, -0.002309]

stats.ttest_rel(before, after)
