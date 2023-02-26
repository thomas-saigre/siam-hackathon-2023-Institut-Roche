clear
close all

load brca_mRNA_50patients.mat


M_d_1_square(A, A)

[ m, n ] = size(A)

load brca_mRNA_patients_BayNet_n20_deg2_eps0_seed_12.mat
BayNet = M_d_1_square(A, A_1)

load brca_mRNA_patients_embedding_dim128_gen_dim256_dis_dim256_l2scale1e-06_batch_size500_epochs500.mat
CTGAN = M_d_1_square(A, A_1)

load syntheticData_mixedNetwork_test_fast_root_index_5.mat
MIIC = M_d_1_square(A, A_1)

a_mean = mean(A);
a1_mean = mean(A_1);

probs = zeros(1,m);
for i=1:m
    a_i = A_1(i,:);    
    probs(i) = probability(a_i, a1_mean, A, a_mean);     
end

figure
plot(probs,'.')
title('Probaility of retrieving A, starting from MIIC privatized data')
set(gca, 'FontSize', 16)


load brca_mRNA_patients_PrivBayes_n20_deg2_eps1_seed_11.mat
privBayes = M_d_1_square(A,A_1)

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

load brca_mRNA_50patients_iteration_3_.mat
Synthpop = M_d_1_square(A, A_1)