function d = distance_2(a_i, a_mean, M_max_1)
    dd = a_i - a_mean;
    d = dd*M_max_1*dd';
end