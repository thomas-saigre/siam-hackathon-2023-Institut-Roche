clear
close all

load brca_mRNA_1977patients.mat
load brca_mRNA_1977patients_iteration_12_.mat

priv_Bayes = M(A, A_1)

load brca_mRNA_1977patients_iteration_12_.mat

BayNet = M(A, A_1)

load brca_mRNA_patients_embedding_dim128_gen_dim256_dis_dim256_l2scale1e-06_batch_size500_epochs500.mat

CTGAN = M(A, A_1)
