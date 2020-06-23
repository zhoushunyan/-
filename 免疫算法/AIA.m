% ʹ�������㷨�����������h = @(x) x + 10.*sin(5.*x) + 7.*cos(4.*x) ��[-10,10]�ϵ����ֵ
% �����������ֵ��x = 7.8568����
% ������ö����Ʊ��뷨����Ҫ���������ɺ����Ͷ����ƽ��뺯����֧��
% �������ѡȡ����λ������ת��ʵ�ֱ���
clc;
clear all;
close all;
bounds = [-10,10]; %�������
precision = 0.0001; %��⾫��
N = ceil(log2((bounds(2)-bounds(1))/precision)); %��������;���������볤��N
NP = 200; %��Ⱥ��Ŀ
G = 20; %������
Ncl = 10; %���ο�¡������
Fn = 0.5; %��Ⱥˢ�±���
f = @(x) bounds(1)+x*(bounds(2)-bounds(1))/(2^N); %�����ʮ�����鵽��������ӳ�亯��
h = @(x) x + 10.*sin(5.*x) + 7.*cos(4.*x); %ֱ�ӰѴ�������Ϊ�׺ͶȺ���

%��ʼ��������Ⱥ
pop = round(rand(NP,N)); %ÿ����һ�����壬��NP��

%��ʼ����
gen = 0;
while 1
    %����Ƿ�ﵽ������
    gen = gen + 1;
    if gen > G
        break
    end
    
    %������Ⱥ�׺Ͷ�
    affinity = zeros(NP,1);
    for i = 1:NP
        affinity(i) = h(f(decode2to10(pop(i,:))));
    end
    
    %�����׺Ͷȴ�С����
    [~,index] = sort(affinity,'descend');
    sortpop = pop(index,:);
    
    %�����ǰNP*(1-Fn)������������߲���
    for i = 1:round(NP*(1-Fn))
        %��¡��
        ca = repmat(sortpop(i,:), Ncl, 1);
        %����:��ÿ����¡�壬���ѡȡ��λȡ��
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
        %��¡����
        affi_ca = zeros(1,Ncl);
        for j = 1:Ncl
            affi_ca(j) = h(f(decode2to10(ca(j,:))));
        end
        [~,indexx] = sort(affi_ca,'descend');
        pop(i,:) = ca(indexx(1),:);
    end
    
    %��Ⱥˢ��
    pop((round(NP*(1-Fn))+1):NP,:) = round(rand((NP-round(NP*(1-Fn))),N));
    
end

%��������������������Ⱥ���׺Ͷ�
final_pop = zeros(1,NP);
for i = 1:NP
    final_pop(i) = f(decode2to10(pop(i,:)));
end
affinity = h(final_pop);

%���ǰ10��������
final_pop(1:10)
affinity(1:10)