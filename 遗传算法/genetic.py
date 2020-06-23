# -*-coding:utf-8 -*-
# 文件名：genetic.py
# 文件编号：NCU-18-0130
# 版本号：1.3
# 作者：周顺
# 创建时间：2018-11-2
# 文件描述：目标求解2*cos(x)+sinx的最大值
# 
# 
#---------------------------------------------------- 
#版本号：random 2 1.0.1
#作者：PSF
#维护人员：Srichter
#时间：2013.4.15
#random是随机数的moudle，常用操作有randint(begin,end),
#其中begin是开始的整数，end是结束的整数#如random.randint(0,1)
#就是随机取0和1中的一个数字.#还有random.random()随机产生0到1的
#浮点数#random.uniform(begin,end),随机产生begin到end的浮点数。
import random
#版本号：math123 0.4
#作者：Jaga123
#维护人员：Jagamtsl
#时间：2017.6.22
#math是数学公式的moudle，使用这个模块可以调用很多数学上复杂的函数，
#如：math.cos(),math.tan(),math.e"e=2.718 是一个常量"#math.factorrial(x)"
#这是求x的阶乘"，等等。你可以使用很多数学符号。
import math
#版本号：matplotlib 3.0.2
#作者：John D.Hunter,Michael Droettboom
#维护人员：cmoad，jdh2368,matthew.brett,mdboom2,Thomas.Caswell
#时间：2018.11.11
#matplotlib是一个可视化的模块,可以将数据以图表、曲线等方式可显现出来。
#这里重点介绍一下plt，plt.plot(x,y),其中x和y可以#是一个列表，也可以
#是一个数组，plt.plot(x,y)是以x和y相对应的点组成坐标，然后绘制曲线
#如plt.plot([1,2,3,4],[1,2,3,4]),绘制就就是y=x这条线段（0<x，y<4).
#plt.show()可以将曲线可视化。
import matplotlib.pyplot as plt

#构造一个GA的类。这里构造的方法和Python2版本不一样，
#Python2 “class GA：”就可以了，而Python3要加上object，即构造object的
#子类。这样统一了类和实例的类型，都为“type”。
class GA(object):

#构造一个__init__ 设置初值的函数，可以内部赋值，也可以外部赋值。
#生成chromosome_length大小的population_size个个体的种群
 
    def __init__(self,population_size,chromosome_length,max_value,pc,pm):
 
        self.population_size=population_size#种群的数量
        self.choromosome_length=chromosome_length#每个个体基因的长度]
        self.max_value=max_value#添加一个常量，之后会用到
        self.pc=pc#发生基因重组的概率
        self.pm=pm#发生基因变异的概率
 
 
# 构造一个species_origin的初始化种群的函数，给这个种群的每一个个体赋值随机的
# 基因，即种群的编码。编码方式有很多种：浮点数编码、格雷编码、二进制编码等等。
# 这里我们用二进制编码，二进制是由0和1组成的二进制作为个体的基因对。这里举个例子
# 比如：10110101011010101111，这样一串代码即表示为一个个体的基因对。
# 执行这函数，将会生成一个随机的种群。返回的这个种群是一个二维列表，第一维是个体
# ，第二维是该个体的基因。
    def species_origin(self):
        population=[[]]#构造一个二维列表
        for i in range(self.population_size):#生成想要的数量的个体，数量为self.population_size
 
            temporary=[]#构造一个空的列表，作为基因对的暂存器
            for j in range(self.choromosome_length):#生成每一个个体的基因,
            #每一个基因对的长度为self.choromosome_length.
                temporary.append(random.randint(0,1))
            #随机产生一个基因对,由二进制数组成,append
            #函数是将生成的0或者1加进temporary列表中
 
            population.append(temporary)
            #将一位列表temporary加进population二维列表中
            #即将每个个体加进种群中
        return population[1:]
            # 将种群返回，种群是个二维列表，个体和基因对两维
 
    #构造一个translation的从二进制转变成十进制的函数，使得可以对基因对进行处理。
    def translation(self,population):
 
        temporary=[]
        for i in range(len(population)):#len是求长度，len(population)是得到种群的个数
            total=0#暂存十进制的值
            for j in range(self.choromosome_length):
                total+=population[i][j]*(math.pow(2,j))
                #math.pow(a,b)即求a的b次方的值。
            #从第一个基因开始，每位对2求幂，再求和
            # 如：1100 转成十进制为：0 * 2(0) + 0 * 2(0) + 1 * 2(2) + 1 * 2(3) =12
            temporary.append(total)
        #一个基因转变完成，由一个二进制数转变为一个十进制数
        return temporary
   # 返回种群中所有个体编码完成后的十进制数
 
 
 
#这里构造一个function函数，来模拟自然环境。
# 目标函数就相当于一个自然环境 对个体进行筛选，这里用2*math.cos(x)+math.sin(x)作为目标函数
# 输入的是一个种群，输出的是这个种群每个个体对自然环境的产生的反应，也可以称为适应值，即函数的值。
    def function(self,population):
        temporary=[]#用来暂存基因对的十进制值
        function1=[]#用来存储通过目标函数转换的值。
        temporary=self.translation(population)#调用transslation函数，将二进制转换为十进制
        for i in range(len(temporary)):
          #这里的x取值可以取很多值，比如x=temporary[i]或者x=temporary[i]
          #/(math.pow(2,self.chromosom_length)-1),或者是下面的值。但是每
          #一种取值的方式都会产生不同的优化效果，而且种群的进化的效果也不一样。
            x=temporary[i]*self.max_value/(math.pow(2,self.choromosome_length)-1)
            #执行目标函数，将其结果加进function1列表中。
            function1.append(2*math.sin(x-1)/(x-1))
          #返回function1.
        return function1
 
#构造一个fitness函数，重新适应值进行改变，即为了模拟自然过程，为了使适应值都在>=0,
#所以当适应值为负数是，将其赋值为0.
#输入function1列表，输出改变后的适应值列表。
    def fitness(self,function1):
        #构造一个适应值列表
        fitness_value=[]
        #得到function1列表的长度
        num=len(function1)
        #循环num次
        for i in range(num):
            #如果funtion[i]>0,将function1[i]的值加进fitness_value函数中
            #否则将0 加进fitness_value函数中
            if(function1[i]>0):
                temporary=function1[i]
            else:
                temporary=0.0
 
            fitness_value.append(temporary)
        #返回新的适应值列表
        return fitness_value
 
#构造一个sum函数，用来计算适应值的和。
#输入适应值列表，输出所有适应值的和。
 
    def sum(self,fitness_value):
        total=0
 
        for i in range(len(fitness_value)):
            total+=fitness_value[i]
        return total
 
#构造一个cumsum函数，计算适应值斐伯那契列表，从后面开始计算，
#如第n项的值赋值为前n项的值之和、第n-1项的值赋值为前n-1值之和。
#输入一个适应值列表，输出适应值对应的斐波那契列表。
    def cumsum(self,fitness1):
      #这里的range(begin,end,step),begin是开始的位置，end是
      #结束的位置，step是步长。
      #下面的循环是从后往前循环。
        for i in range(len(fitness1)-1,-1,-1):
            total=0#设置一个存储和的变量
            j=0#循环的变量
 
            while(j<=i):#while循环
                 total+=fitness1[j]
                 j+=1#j加一
            #将和从新赋值给列表。
            fitness1[i]=total
 
 #构造一个selection函数，用来选择适应值较大的个体，首先将通过fitness
#函数的得到的适应值列表，将其每个个体的适应值概率化，也可以说是正则化。
#然后再通过轮盘赌的方法将适应值较大的个体选择出来。
#输入是种群和适应值列表，输出是新的适应值更大的种群
    def selection(self,population,fitness_value):
        #构造一个列表，存储每个个体适应值占总适应值的比例。
        new_fitness=[]
        #计算总的适应值
        total_fitness=self.sum(fitness_value)
        #通过这个循环计算每个个体所占比例
        for i in range(len(fitness_value)):
            new_fitness.append(fitness_value[i]/total_fitness)
            #cumsum是计算列表的斐波那契列表。
        self.cumsum(new_fitness)
    #用来存储存活的种群，
        ms=[]
        #计算种群的长度
        population_length=pop_len=len(population)

    #随机一连串0到1的数字，可能大也可能小，将其存储在ms数组中。
 
        for i in range(pop_len):
            ms.append(random.random())
        #将ms数组排序
        ms.sort()
       
        fitin=0#设置一个变量来记录new_fitness的进度
        newin=0#设置一个变量来记录ms的进度
        new_pop=population#复制种群
 
    #轮盘赌方法是一种选取的方式。
    #举个例子，我要从十个个体中选取适应值更大的个体延续下去，
    #假如，每个个体适应值位1，0，1，4，1，3，1，0，1，0.
    #它们对应的比例为：0.083，0，0.083，0.33，0.083，0.25，0.083，0，0.083，0.
    #它们对于的斐波那契列表：0.083，0.083，0.166，0.496，0.579，0.829，0912，0.912，1，1.
    #假设ms数组为：0.1，0.2，0.3，0.4，0.5，0.6，0.7，0.8，0.9，0.99.
    #执行轮盘赌方法后，0.166>0.1,所以选择一次第三个个体，之后，0.496>0.4>0.3>0.2,所以选择3次第四个个体
    #下面类似，以此可见，当适应值更高的个体，被选择的次数越多。
        while newin<pop_len:
              if(ms[newin]<new_fitness[fitin]):#斐波那契列表内数值大于ms数组内的数值。
                 new_pop[newin]=population[fitin]#将个体保存在新种群内。
                 newin+=1#ms数组加1
              else:
                 fitin+=1#列表加1
        population=new_pop#将旧种群替换成新种群
 
#4.构造一个crossover函数，用来实现基因重组。
#简单点说就是将一个基因对的一部分和另一个基因对的另一相同位置的部分交换。
#可以是单点，也可以是多点，在这个实验，我们比较一下双点和单点。
#输入一个种群，输出一个新的种群。
    def crossover(self,population):
        pop_len=len(population)#种群的长度
 
        for i in range(pop_len-1):
            #pc是基因重组的概率，
            if(random.random()<self.pc):

              # 双点基因重组
                #cpoint是开始的点，epoint是终点
                #cpoint在0到10内取一点
                #epoint在10到20内取一点
               cpoint=random.randint(0,len(population[0])-10)
               epoint=random.randint(10,len(population[0]))
              #temporary1 和2是用来暂存基因对。
               temporary1=[]
               temporary2=[]
                  #将第i个基因对的0到cpoint、第i+1个基因对的cpoint到epoint、第i个基因对的epoint到结尾
                  #。加到temporary1列表里面
               temporary1.extend(population[i][0:cpoint])
               temporary1.extend(population[i+1][cpoint:epoint])
               temporary1.extend(population[i][epoint:len(population[i])])
               #将第i+1个基因对的0到cpoint、第i个基因对的cpoint到epoint、第i+1个基因对的epoint到结尾
               #。加到temporary2列表里
               temporary2.extend(population[i+1][0:cpoint])
               temporary2.extend(population[i][cpoint:epoint])
               temporary2.extend(population[i+1][epoint:len(population[i])])
               #然后将tem1赋值个第i个个体，tem2赋值个第i+1个个体。
               population[i]=temporary1
               population[i+1]=temporary2

              #单点基因重组
               # cpoint=random.randint(0,len(population[0]))
               # temporary1=[]
               # temporary2=[]
               # temporary1.extend(population[i][0:cpoint])
               # temporary1.extend(population[i+1][cpoint:len(population[i])])
               # temporary2.extend(population[i+1][0:cpoint])
               # temporary2.extend(population[i][cpoint:len(population[i])])
      
               # population[i]=temporary1
               # population[i+1]=temporary2

     #构造一个mutation函数，用来模拟基因突变，即某个个体有可能突然变得很好，变得很坏。
     #这里我们采用两种变异方式来模拟基因突变，一种是正交变异算子，这种方法是选取两个基因
     #对执行异或操作，得到新的基因对，然后执行取反操作。第二种是直接执行取反操作。
     #输入一个种群，输出一个新的种群          
    def mutation(self,population):
        #px是种群的长度减1
         px=len(population)-1
        #py是基因对的长度
         py=len(population[0])
         #pm是发生基因突变的概率
         for i in range(px):
             if(random.random()<self.pm):
              #正交基因突变
                tem1=[]#用来存储异或操作后的新的基因对
                for j in range(len(population[0])):
                  #执行异或操作，当相同时为0，不相同时为1
                  if(population[i][j]==population[i+1][j]):
                    tem1.append(0)
                  else:
                    tem1.append(1)
                #将tem1覆盖给第i+1个基因对
                population[i+1]=tem1

            #取反基因突变
                #随机在基因对中取一点，用来取反操作
                mpoint=random.randint(0,py-1)
                if(population[i][mpoint]==1):
                   population[i][mpoint]=0
                else:
                   population[i][mpoint]=1
 
#构造一个b2d函数，
# 用来每一个基因对转化成十进制,
    def b2d(self,best_individual):
        total=0
        b=len(best_individual)
        for i in range(b):
            total=total+best_individual[i]*math.pow(2,i)
 
        total=total*self.max_value/(math.pow(2,self.choromosome_length)-1)
        return total
 
#构造一个best函数，用来寻找适应值最大的个体
#输入种群，适应值列表，输出适应值最大的个体的基因对和适应值
 
    def best(self,population,fitness_value):
 
        px=len(population)
        bestindividual=[]
        bestfitness=fitness_value[0]
        # print(fitness_value)
        #找到适应值最大的个体，并且将其保存起来
        for i in range(1,px):
            if(fitness_value[i]>bestfitness):
 
               bestfitness=fitness_value[i]
               bestindividual=population[i]
          #返回一个列表，列表包含个体基因对和适应值。
        return [bestindividual,bestfitness]
 
  #构造一个plot函数，用来画出（x，y）的函数。
  #输入results列表，输出x，y的函数。
    def plot(self, results):
        X = []
        Y = []
        for i in range(500):
            X.append(i)
            Y.append(results[i][0])
        #plot是将函数画出
        plt.plot(X, Y)
        #show时将函数显示
        plt.show()
 #主函数，实现种群的初始化，选择、基因重组、突变，所有的过程。
    def main(self):
 
        results = [[]]#二维列表，存储每一轮自然选择后的个体适应值和基因对对应的x的值
        fitness_value = []
 
        population = pop = self.species_origin()#随机给出一个初始的种群
 
        for i in range(500):#500次自然选择
            #建立目标函数，以该函数来计算每个个体的适应值，并且保存起来，调用了function函数
            function_value = self.function(population)
            #选择个体，大于0的个体保持不变，小于0的个体赋值为0.调用了fitness函数
            fitness_value = self.fitness(function_value)
            #选择最优的个体，将其保存起来，调用了best，b2d函数
            best_individual, best_fitness = self.best(population,fitness_value)
            results.append([best_fitness, self.b2d(best_individual)])
            self.selection(population,fitness_value)#某个个体的适应度越强，让其个体数越多，调用了selection函数。
            self.crossover(population)#实现基因重组
            self.mutation(population)#实现基因变异
        results = results[1:]#选取1到500次的结果
        results.sort()#排序
        #画出函数图
        self.plot(results)
 
if __name__ == '__main__':
 
 
   population_size=400#设置种群个体数为400
   max_value=10#设置这个常数为10
   chromosome_length=20#设置基因对长度为20
   pc=0.6#设置基因重组的概率为0.6
   pm=0.01#设置基因突变的概率为0.01
   g=GA(population_size,chromosome_length,max_value,pc,pm)#构造一个对象g
   g.main()#调用里面的主函数
