function P = probability(a_1_j, a_1_mean, A, a_mean)
    aa = a_1_j - a_1_mean;
        
    C = abs(aa*(A - a_mean)'./(norm(aa)*vecnorm((A - a_mean)')));
    [ m_C, i_C ] = max(C);
    av_C = mean(C([ 1:i_C-1 i_C+1:length(C)]));
    P = max(C) - av_C;
end