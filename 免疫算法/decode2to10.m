function value10 = decode2to10( vector2 )
%�ú��������������ƴ�ת��Ϊʮ����
%   ֻ������ת��������ʽ���ַ���������о���Ӧʹ��for����
    %��⴫������Ƿ�Ϊ����������ȡ��������
    [a,b] = size(vector2);
    if (a == 1) && (b > 1)
        BitLen = b;
    elseif (b == 1) && (a > 1)
        BitLen = a;
    else
        BitLen = 0;
    end
    %ת��Ϊʮ����
    value10 = vector2(BitLen);
    for i = 1:BitLen-1
        value10 = value10+vector2(BitLen-i)*power(2,i);
    end
end