# -*-coding:utf-8 -*-
# �ļ�����genetic.py
# �ļ���ţ�NCU-18-0130
# �汾�ţ�1.3
# ���ߣ���˳
# ����ʱ�䣺2018-11-2
# �ļ�������Ŀ�����2*cos(x)+sinx�����ֵ
# 
# 
#---------------------------------------------------- 
#�汾�ţ�random 2 1.0.1
#���ߣ�PSF
#ά����Ա��Srichter
#ʱ�䣺2013.4.15
#random���������moudle�����ò�����randint(begin,end),
#����begin�ǿ�ʼ��������end�ǽ���������#��random.randint(0,1)
#�������ȡ0��1�е�һ������.#����random.random()�������0��1��
#������#random.uniform(begin,end),�������begin��end�ĸ�������
import random
#�汾�ţ�math123 0.4
#���ߣ�Jaga123
#ά����Ա��Jagamtsl
#ʱ�䣺2017.6.22
#math����ѧ��ʽ��moudle��ʹ�����ģ����Ե��úܶ���ѧ�ϸ��ӵĺ�����
#�磺math.cos(),math.tan(),math.e"e=2.718 ��һ������"#math.factorrial(x)"
#������x�Ľ׳�"���ȵȡ������ʹ�úܶ���ѧ���š�
import math
#�汾�ţ�matplotlib 3.0.2
#���ߣ�John D.Hunter,Michael Droettboom
#ά����Ա��cmoad��jdh2368,matthew.brett,mdboom2,Thomas.Caswell
#ʱ�䣺2018.11.11
#matplotlib��һ�����ӻ���ģ��,���Խ�������ͼ�����ߵȷ�ʽ�����ֳ�����
#�����ص����һ��plt��plt.plot(x,y),����x��y����#��һ���б�Ҳ����
#��һ�����飬plt.plot(x,y)����x��y���Ӧ�ĵ�������꣬Ȼ���������
#��plt.plot([1,2,3,4],[1,2,3,4]),���ƾ;���y=x�����߶Σ�0<x��y<4).
#plt.show()���Խ����߿��ӻ���
import matplotlib.pyplot as plt

#����һ��GA���ࡣ���ﹹ��ķ�����Python2�汾��һ����
#Python2 ��class GA�����Ϳ����ˣ���Python3Ҫ����object��������object��
#���ࡣ����ͳһ�����ʵ�������ͣ���Ϊ��type����
class GA(object):

#����һ��__init__ ���ó�ֵ�ĺ����������ڲ���ֵ��Ҳ�����ⲿ��ֵ��
#����chromosome_length��С��population_size���������Ⱥ
 
    def __init__(self,population_size,chromosome_length,max_value,pc,pm):
 
        self.population_size=population_size#��Ⱥ������
        self.choromosome_length=chromosome_length#ÿ���������ĳ���]
        self.max_value=max_value#���һ��������֮����õ�
        self.pc=pc#������������ĸ���
        self.pm=pm#�����������ĸ���
 
 
# ����һ��species_origin�ĳ�ʼ����Ⱥ�ĺ������������Ⱥ��ÿһ�����帳ֵ�����
# ���򣬼���Ⱥ�ı��롣���뷽ʽ�кܶ��֣����������롢���ױ��롢�����Ʊ���ȵȡ�
# ���������ö����Ʊ��룬����������0��1��ɵĶ�������Ϊ����Ļ���ԡ�����ٸ�����
# ���磺10110101011010101111������һ�����뼴��ʾΪһ������Ļ���ԡ�
# ִ���⺯������������һ���������Ⱥ�����ص������Ⱥ��һ����ά�б���һά�Ǹ���
# ���ڶ�ά�Ǹø���Ļ���
    def species_origin(self):
        population=[[]]#����һ����ά�б�
        for i in range(self.population_size):#������Ҫ�������ĸ��壬����Ϊself.population_size
 
            temporary=[]#����һ���յ��б���Ϊ����Ե��ݴ���
            for j in range(self.choromosome_length):#����ÿһ������Ļ���,
            #ÿһ������Եĳ���Ϊself.choromosome_length.
                temporary.append(random.randint(0,1))
            #�������һ�������,�ɶ����������,append
            #�����ǽ����ɵ�0����1�ӽ�temporary�б���
 
            population.append(temporary)
            #��һλ�б�temporary�ӽ�population��ά�б���
            #����ÿ������ӽ���Ⱥ��
        return population[1:]
            # ����Ⱥ���أ���Ⱥ�Ǹ���ά�б�����ͻ������ά
 
    #����һ��translation�ĴӶ�����ת���ʮ���Ƶĺ�����ʹ�ÿ��ԶԻ���Խ��д���
    def translation(self,population):
 
        temporary=[]
        for i in range(len(population)):#len���󳤶ȣ�len(population)�ǵõ���Ⱥ�ĸ���
            total=0#�ݴ�ʮ���Ƶ�ֵ
            for j in range(self.choromosome_length):
                total+=population[i][j]*(math.pow(2,j))
                #math.pow(a,b)����a��b�η���ֵ��
            #�ӵ�һ������ʼ��ÿλ��2���ݣ������
            # �磺1100 ת��ʮ����Ϊ��0 * 2(0) + 0 * 2(0) + 1 * 2(2) + 1 * 2(3) =12
            temporary.append(total)
        #һ������ת����ɣ���һ����������ת��Ϊһ��ʮ������
        return temporary
   # ������Ⱥ�����и��������ɺ��ʮ������
 
 
 
#���ﹹ��һ��function��������ģ����Ȼ������
# Ŀ�꺯�����൱��һ����Ȼ���� �Ը������ɸѡ��������2*math.cos(x)+math.sin(x)��ΪĿ�꺯��
# �������һ����Ⱥ��������������Ⱥÿ���������Ȼ�����Ĳ����ķ�Ӧ��Ҳ���Գ�Ϊ��Ӧֵ����������ֵ��
    def function(self,population):
        temporary=[]#�����ݴ����Ե�ʮ����ֵ
        function1=[]#�����洢ͨ��Ŀ�꺯��ת����ֵ��
        temporary=self.translation(population)#����transslation��������������ת��Ϊʮ����
        for i in range(len(temporary)):
          #�����xȡֵ����ȡ�ܶ�ֵ������x=temporary[i]����x=temporary[i]
          #/(math.pow(2,self.chromosom_length)-1),�����������ֵ������ÿ
          #һ��ȡֵ�ķ�ʽ���������ͬ���Ż�Ч����������Ⱥ�Ľ�����Ч��Ҳ��һ����
            x=temporary[i]*self.max_value/(math.pow(2,self.choromosome_length)-1)
            #ִ��Ŀ�꺯�����������ӽ�function1�б��С�
            function1.append(2*math.sin(x-1)/(x-1))
          #����function1.
        return function1
 
#����һ��fitness������������Ӧֵ���иı䣬��Ϊ��ģ����Ȼ���̣�Ϊ��ʹ��Ӧֵ����>=0,
#���Ե���ӦֵΪ�����ǣ����丳ֵΪ0.
#����function1�б�����ı�����Ӧֵ�б�
    def fitness(self,function1):
        #����һ����Ӧֵ�б�
        fitness_value=[]
        #�õ�function1�б�ĳ���
        num=len(function1)
        #ѭ��num��
        for i in range(num):
            #���funtion[i]>0,��function1[i]��ֵ�ӽ�fitness_value������
            #����0 �ӽ�fitness_value������
            if(function1[i]>0):
                temporary=function1[i]
            else:
                temporary=0.0
 
            fitness_value.append(temporary)
        #�����µ���Ӧֵ�б�
        return fitness_value
 
#����һ��sum����������������Ӧֵ�ĺ͡�
#������Ӧֵ�б����������Ӧֵ�ĺ͡�
 
    def sum(self,fitness_value):
        total=0
 
        for i in range(len(fitness_value)):
            total+=fitness_value[i]
        return total
 
#����һ��cumsum������������Ӧֵ쳲������б��Ӻ��濪ʼ���㣬
#���n���ֵ��ֵΪǰn���ֵ֮�͡���n-1���ֵ��ֵΪǰn-1ֵ֮�͡�
#����һ����Ӧֵ�б������Ӧֵ��Ӧ��쳲������б�
    def cumsum(self,fitness1):
      #�����range(begin,end,step),begin�ǿ�ʼ��λ�ã�end��
      #������λ�ã�step�ǲ�����
      #�����ѭ���ǴӺ���ǰѭ����
        for i in range(len(fitness1)-1,-1,-1):
            total=0#����һ���洢�͵ı���
            j=0#ѭ���ı���
 
            while(j<=i):#whileѭ��
                 total+=fitness1[j]
                 j+=1#j��һ
            #���ʹ��¸�ֵ���б�
            fitness1[i]=total
 
 #����һ��selection����������ѡ����Ӧֵ�ϴ�ĸ��壬���Ƚ�ͨ��fitness
#�����ĵõ�����Ӧֵ�б�����ÿ���������Ӧֵ���ʻ���Ҳ����˵�����򻯡�
#Ȼ����ͨ�����̶ĵķ�������Ӧֵ�ϴ�ĸ���ѡ�������
#��������Ⱥ����Ӧֵ�б�������µ���Ӧֵ�������Ⱥ
    def selection(self,population,fitness_value):
        #����һ���б��洢ÿ��������Ӧֵռ����Ӧֵ�ı�����
        new_fitness=[]
        #�����ܵ���Ӧֵ
        total_fitness=self.sum(fitness_value)
        #ͨ�����ѭ������ÿ��������ռ����
        for i in range(len(fitness_value)):
            new_fitness.append(fitness_value[i]/total_fitness)
            #cumsum�Ǽ����б��쳲������б�
        self.cumsum(new_fitness)
    #�����洢������Ⱥ��
        ms=[]
        #������Ⱥ�ĳ���
        population_length=pop_len=len(population)

    #���һ����0��1�����֣����ܴ�Ҳ����С������洢��ms�����С�
 
        for i in range(pop_len):
            ms.append(random.random())
        #��ms��������
        ms.sort()
       
        fitin=0#����һ����������¼new_fitness�Ľ���
        newin=0#����һ����������¼ms�Ľ���
        new_pop=population#������Ⱥ
 
    #���̶ķ�����һ��ѡȡ�ķ�ʽ��
    #�ٸ����ӣ���Ҫ��ʮ��������ѡȡ��Ӧֵ����ĸ���������ȥ��
    #���磬ÿ��������Ӧֵλ1��0��1��4��1��3��1��0��1��0.
    #���Ƕ�Ӧ�ı���Ϊ��0.083��0��0.083��0.33��0.083��0.25��0.083��0��0.083��0.
    #���Ƕ��ڵ�쳲������б�0.083��0.083��0.166��0.496��0.579��0.829��0912��0.912��1��1.
    #����ms����Ϊ��0.1��0.2��0.3��0.4��0.5��0.6��0.7��0.8��0.9��0.99.
    #ִ�����̶ķ�����0.166>0.1,����ѡ��һ�ε��������壬֮��0.496>0.4>0.3>0.2,����ѡ��3�ε��ĸ�����
    #�������ƣ��Դ˿ɼ�������Ӧֵ���ߵĸ��壬��ѡ��Ĵ���Խ�ࡣ
        while newin<pop_len:
              if(ms[newin]<new_fitness[fitin]):#쳲������б�����ֵ����ms�����ڵ���ֵ��
                 new_pop[newin]=population[fitin]#�����屣��������Ⱥ�ڡ�
                 newin+=1#ms�����1
              else:
                 fitin+=1#�б��1
        population=new_pop#������Ⱥ�滻������Ⱥ
 
#4.����һ��crossover����������ʵ�ֻ������顣
#�򵥵�˵���ǽ�һ������Ե�һ���ֺ���һ������Ե���һ��ͬλ�õĲ��ֽ�����
#�����ǵ��㣬Ҳ�����Ƕ�㣬�����ʵ�飬���ǱȽ�һ��˫��͵��㡣
#����һ����Ⱥ�����һ���µ���Ⱥ��
    def crossover(self,population):
        pop_len=len(population)#��Ⱥ�ĳ���
 
        for i in range(pop_len-1):
            #pc�ǻ�������ĸ��ʣ�
            if(random.random()<self.pc):

              # ˫���������
                #cpoint�ǿ�ʼ�ĵ㣬epoint���յ�
                #cpoint��0��10��ȡһ��
                #epoint��10��20��ȡһ��
               cpoint=random.randint(0,len(population[0])-10)
               epoint=random.randint(10,len(population[0]))
              #temporary1 ��2�������ݴ����ԡ�
               temporary1=[]
               temporary2=[]
                  #����i������Ե�0��cpoint����i+1������Ե�cpoint��epoint����i������Ե�epoint����β
                  #���ӵ�temporary1�б�����
               temporary1.extend(population[i][0:cpoint])
               temporary1.extend(population[i+1][cpoint:epoint])
               temporary1.extend(population[i][epoint:len(population[i])])
               #����i+1������Ե�0��cpoint����i������Ե�cpoint��epoint����i+1������Ե�epoint����β
               #���ӵ�temporary2�б���
               temporary2.extend(population[i+1][0:cpoint])
               temporary2.extend(population[i][cpoint:epoint])
               temporary2.extend(population[i+1][epoint:len(population[i])])
               #Ȼ��tem1��ֵ����i�����壬tem2��ֵ����i+1�����塣
               population[i]=temporary1
               population[i+1]=temporary2

              #�����������
               # cpoint=random.randint(0,len(population[0]))
               # temporary1=[]
               # temporary2=[]
               # temporary1.extend(population[i][0:cpoint])
               # temporary1.extend(population[i+1][cpoint:len(population[i])])
               # temporary2.extend(population[i+1][0:cpoint])
               # temporary2.extend(population[i][cpoint:len(population[i])])
      
               # population[i]=temporary1
               # population[i+1]=temporary2

     #����һ��mutation����������ģ�����ͻ�䣬��ĳ�������п���ͻȻ��úܺã���úܻ���
     #�������ǲ������ֱ��췽ʽ��ģ�����ͻ�䣬һ���������������ӣ����ַ�����ѡȡ��������
     #��ִ�����������õ��µĻ���ԣ�Ȼ��ִ��ȡ���������ڶ�����ֱ��ִ��ȡ��������
     #����һ����Ⱥ�����һ���µ���Ⱥ          
    def mutation(self,population):
        #px����Ⱥ�ĳ��ȼ�1
         px=len(population)-1
        #py�ǻ���Եĳ���
         py=len(population[0])
         #pm�Ƿ�������ͻ��ĸ���
         for i in range(px):
             if(random.random()<self.pm):
              #��������ͻ��
                tem1=[]#�����洢����������µĻ����
                for j in range(len(population[0])):
                  #ִ��������������ͬʱΪ0������ͬʱΪ1
                  if(population[i][j]==population[i+1][j]):
                    tem1.append(0)
                  else:
                    tem1.append(1)
                #��tem1���Ǹ���i+1�������
                population[i+1]=tem1

            #ȡ������ͻ��
                #����ڻ������ȡһ�㣬����ȡ������
                mpoint=random.randint(0,py-1)
                if(population[i][mpoint]==1):
                   population[i][mpoint]=0
                else:
                   population[i][mpoint]=1
 
#����һ��b2d������
# ����ÿһ�������ת����ʮ����,
    def b2d(self,best_individual):
        total=0
        b=len(best_individual)
        for i in range(b):
            total=total+best_individual[i]*math.pow(2,i)
 
        total=total*self.max_value/(math.pow(2,self.choromosome_length)-1)
        return total
 
#����һ��best����������Ѱ����Ӧֵ���ĸ���
#������Ⱥ����Ӧֵ�б������Ӧֵ���ĸ���Ļ���Ժ���Ӧֵ
 
    def best(self,population,fitness_value):
 
        px=len(population)
        bestindividual=[]
        bestfitness=fitness_value[0]
        # print(fitness_value)
        #�ҵ���Ӧֵ���ĸ��壬���ҽ��䱣������
        for i in range(1,px):
            if(fitness_value[i]>bestfitness):
 
               bestfitness=fitness_value[i]
               bestindividual=population[i]
          #����һ���б��б�����������Ժ���Ӧֵ��
        return [bestindividual,bestfitness]
 
  #����һ��plot����������������x��y���ĺ�����
  #����results�б����x��y�ĺ�����
    def plot(self, results):
        X = []
        Y = []
        for i in range(500):
            X.append(i)
            Y.append(results[i][0])
        #plot�ǽ���������
        plt.plot(X, Y)
        #showʱ��������ʾ
        plt.show()
 #��������ʵ����Ⱥ�ĳ�ʼ����ѡ�񡢻������顢ͻ�䣬���еĹ��̡�
    def main(self):
 
        results = [[]]#��ά�б��洢ÿһ����Ȼѡ���ĸ�����Ӧֵ�ͻ���Զ�Ӧ��x��ֵ
        fitness_value = []
 
        population = pop = self.species_origin()#�������һ����ʼ����Ⱥ
 
        for i in range(500):#500����Ȼѡ��
            #����Ŀ�꺯�����Ըú���������ÿ���������Ӧֵ�����ұ���������������function����
            function_value = self.function(population)
            #ѡ����壬����0�ĸ��屣�ֲ��䣬С��0�ĸ��帳ֵΪ0.������fitness����
            fitness_value = self.fitness(function_value)
            #ѡ�����ŵĸ��壬���䱣��������������best��b2d����
            best_individual, best_fitness = self.best(population,fitness_value)
            results.append([best_fitness, self.b2d(best_individual)])
            self.selection(population,fitness_value)#ĳ���������Ӧ��Խǿ�����������Խ�࣬������selection������
            self.crossover(population)#ʵ�ֻ�������
            self.mutation(population)#ʵ�ֻ������
        results = results[1:]#ѡȡ1��500�εĽ��
        results.sort()#����
        #��������ͼ
        self.plot(results)
 
if __name__ == '__main__':
 
 
   population_size=400#������Ⱥ������Ϊ400
   max_value=10#�����������Ϊ10
   chromosome_length=20#���û���Գ���Ϊ20
   pc=0.6#���û�������ĸ���Ϊ0.6
   pm=0.01#���û���ͻ��ĸ���Ϊ0.01
   g=GA(population_size,chromosome_length,max_value,pc,pm)#����һ������g
   g.main()#���������������
