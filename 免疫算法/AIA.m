% 使用免疫算法计算这个函数h = @(x) x + 10.*sin(5.*x) + 7.*cos(4.*x) 在[-10,10]上的最大值
% 它真正的最大值在x = 7.8568附近
% 编码采用二进制编码法，需要二进制生成函数和二进制解码函数的支持
% 采用随机选取三个位发生反转来实现变异
clc;
clear all;
close all;
bounds = [-10,10]; %求解区间
precision = 0.0001; %求解精度
N = ceil(log2((bounds(2)-bounds(1))/precision)); %根据区间和精度求出编码长度N
NP = 200; %种群数目
G = 20; %最大代数
Ncl = 10; %单次克隆个体数
Fn = 0.5; %种群刷新比例
f = @(x) bounds(1)+x*(bounds(2)-bounds(1))/(2^N); %解码后十进制书到求解区间的映射函数
h = @(x) x + 10.*sin(5.*x) + 7.*cos(4.*x); %直接把待求函数作为亲和度函数

%初始化抗体种群
pop = round(rand(NP,N)); %每行是一个抗体，共NP个

%开始迭代
gen = 0;
while 1
    %检查是否达到最大代数
    gen = gen + 1;
    if gen > G
        break
    end
    
    %计算种群亲和度
    affinity = zeros(NP,1);
    for i = 1:NP
        affinity(i) = h(f(decode2to10(pop(i,:))));
    end
    
    %根据亲和度大小排序
    [~,index] = sort(affinity,'descend');
    sortpop = pop(index,:);
    
    %活化：对前NP*(1-Fn)个个体进行免疫操作
    for i = 1:round(NP*(1-Fn))
        %克隆：
        ca = repmat(sortpop(i,:), Ncl, 1);
        %变异:对每个克隆体，随机选取三位取反
        for j = 2:Ncl
            indexx = ceil(18*rand(1,3));
            for k = 1:3
                if ca(j,indexx(k)) == 0
                    ca(j,indexx(k)) = 1;
                else
                    ca(j,indexx(k)) = 0;
                end
            end
        end
        %克隆抑制
        affi_ca = zeros(1,Ncl);
        for j = 1:Ncl
            affi_ca(j) = h(f(decode2to10(ca(j,:))));
        end
        [~,indexx] = sort(affi_ca,'descend');
        pop(i,:) = ca(indexx(1),:);
    end
    
    %种群刷新
    pop((round(NP*(1-Fn))+1):NP,:) = round(rand((NP-round(NP*(1-Fn))),N));
    
end

%迭代结束，计算最终种群的亲和度
final_pop = zeros(1,NP);
for i = 1:NP
    final_pop(i) = f(decode2to10(pop(i,:)));
end
affinity = h(final_pop);

%输出前10个看看？
final_pop(1:10)
affinity(1:10)