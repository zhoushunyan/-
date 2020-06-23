function value10 = decode2to10( vector2 )
%该函数用来将二进制串转化为十进制
%   只能用来转化向量形式的字符串，如果有矩阵，应使用for迭代
    %检测传入参数是否为向量，并提取向量长度
    [a,b] = size(vector2);
    if (a == 1) && (b > 1)
        BitLen = b;
    elseif (b == 1) && (a > 1)
        BitLen = a;
    else
        BitLen = 0;
    end
    %转化为十进制
    value10 = vector2(BitLen);
    for i = 1:BitLen-1
        value10 = value10+vector2(BitLen-i)*power(2,i);
    end
end