function result = M_d_1_square(A, A1)

[ m, n ] = size(A);
a_mean = mean(A);
a1_mean = mean(A1);

Cov_A = (A - a_mean)'*(A - a_mean)/(m-1);

M_max_1 = pinv(Cov_A);

result = 0;
for i=1:m
    a_i = A1(i,:);    
    pp = probability(a_i, a1_mean, A, a_mean);
    if(pp >= 1)
        error()
    end   
    result = result + distance_2(a_i, a1_mean, M_max_1)*( 1 - pp )^2;
end
result/m;

end
