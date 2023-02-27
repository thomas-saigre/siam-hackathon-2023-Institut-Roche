clear
close all

load brca_mRNA_1977patients.mat


M(A, A)

[ m, n ] = size(A)

load brca_mRNA_patients_BayNet_n20_deg2_eps0_seed_3.mat
BayNet = M(A, A_1)

load brca_mRNA_patients_embedding_dim128_gen_dim256_dis_dim256_l2scale1e-06_batch_size500_epochs500.mat
CTGAN = M(A, A_1)

load syntheticData_mixedNetwork_test_fast_root_index_11.mat
MIIC = M(A, A_1)

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
axis([-inf, inf, 0.1, 0.9])
ylabel('Probability')
xlabel('Population')
set(gca, 'FontSize', 16)


load brca_mRNA_patients_PrivBayes_n20_deg2_eps1_seed_8.mat
privBayes = M(A,A_1)

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
axis([-inf, inf, 0.1, 0.9])
ylabel('Probability')
xlabel('Population')
set(gca, 'FontSize', 16)

load brca_mRNA_1977patients_iteration_12_.mat
Synthpop = M(A, A_1)