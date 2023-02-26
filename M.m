function result = M(A, A1)

[ m, n ] = size(A);
a_mean = mean(A);
a1_mean = mean(A1);

max_A = max(A);

M_max_1 = diag(1./(max_A - a_mean));

result = 0;
for i=1:m
    a_i = A1(i,:);    
    pp = probability(a_i, a1_mean, A, a_mean);
    
    if(pp >= 1)
        error()
    end
    
    result = result + distance_2(a_i, a1_mean, M_max_1)*( 1 - probability(a_i, a1_mean, A, a_mean) );
end
result/m

end
