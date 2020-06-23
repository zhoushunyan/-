import numpy as np
import matplotlib.pyplot as plt
import random 
 
class PSO(object):
    def __init__(self, population_size, max_steps):
        self.w = 0.4  # 惯性权重
        self.c1 = self.c2 = 2
        self.population_size = population_size  # 粒子群数量
        self.dim = 2  # 搜索空间的维度
        self.max_steps = max_steps  # 迭代次数
        self.x_bound = [-10, 10]  # 解空间范围
        self.x = np.random.uniform(self.x_bound[0], self.x_bound[1],
                                   (self.population_size, self.dim))  # 初始化粒子群位置
        self.v = np.random.rand(self.population_size, self.dim)  # 初始化粒子群速度
        fitness = self.calculate_fitness(self.x)
        self.p = self.x  # 个体的最佳位置
        self.pg = self.x[np.argmin(fitness)]  # 全局最佳位置
        self.individual_best_fitness = fitness  # 个体的最优适应度
        self.colors=np.random.rand(self.population_size)
        #self.area=(30*np.random.rand(100))**2
        self.global_best_fitness = np.max(fitness)  # 全局最佳适应度

    def calculate_fitness(self, x):
        return np.sum(np.square(x), axis=1)
 
    def evolve(self):
        fig = plt.figure()#建立一个图表
        for step in range(self.max_steps):
            r1 = np.random.rand(self.population_size, self.dim)
            r2 = np.random.rand(self.population_size, self.dim)
            # 更新速度和权重
            self.v = self.w*self.v+self.c1*r1*(self.p-self.x)+self.c2*r2*(self.pg-self.x)

            self.x = self.v + self.x
            plt.clf()#清除图表的点
            #构造一个散列图
            plt.scatter(self.x[:, 0], self.x[:, 1], s=30, c=self.colors)
            plt.xlim(self.x_bound[0], self.x_bound[1])
            plt.ylim(self.x_bound[0], self.x_bound[1])
            plt.pause(1)
            fitness = self.calculate_fitness(self.x)
            # 需要更新的个体
            # greater指的是前面的大于后面的则为真
            update_id = np.greater(self.individual_best_fitness, fitness)
            self.p[update_id] = self.x[update_id]#改变目标函数值大的个体的位置，使其目标函数值更小。
            self.individual_best_fitness[update_id] = fitness[update_id]#改变起目标函数值。
            # 新一代出现了更小的fitness，所以更新全局最优fitness和位置
            if np.min(fitness) < self.global_best_fitness:
                self.pg = self.x[np.argmin(fitness)]
                self.global_best_fitness = np.min(fitness)
            print('best fitness: %.5f, mean fitness: %.5f' % (self.global_best_fitness, np.mean(fitness)))
 
 
pso = PSO(10, 10)
pso.evolve()
plt.show()