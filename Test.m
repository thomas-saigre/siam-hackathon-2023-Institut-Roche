clear
close all

load brca_mRNA_1977patients.mat
load brca_mRNA_1977patients_iteration_12_.mat

M(A, A)

[ m, n ] = size(A)
priv_Bayes = M(A, A_1)

a_mean = mean(A);
a1_mean = mean(A_1);

probs = zeros(1,m);
for i=1:m
    a_i = A_1(i,:);    
    probs(i) = probability(a_i, a1_mean, A, a_mean);     
end

figure
plot(probs,'.')
title('Probaility of retrieving A, starting from Private Bayes privatized data')
set(gca, 'FontSize', 16)

load brca_mRNA_1977patients_iteration_12_.mat

BayNet = M(A, A_1)

load brca_mRNA_patients_embedding_dim128_gen_dim256_dis_dim256_l2scale1e-06_batch_size500_epochs500.mat

CTGAN = M(A, A_1)

