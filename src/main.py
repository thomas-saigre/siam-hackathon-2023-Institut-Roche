from distances import *

if __name__ == "__main__":

    df = pd.read_csv("data/MIXED50patients_subsamples/1/Baynet/brca_mRNA_patients_BayNet_n20_deg2_eps0_seed_1.csv")
    df_true = pd.read_csv("data/MIXED50patients_subsamples/1/brca_mRNA_50patients.csv")

    Sig = np.linalg.inv(np.array(df.cov()))
    a = np.array(df_true.iloc[0])
    abar = df.mean(axis=0)

    M = computeM(df)
    Mm1 = np.linalg.inv(M)

    d1 = []
    d2 = []
    d_theta = [[], [], []]
    for i in range(50):
        d1_ = distance1(df_true.iloc[i], abar, Sig)
        d2_ = distance2(df_true.iloc[i], abar, Mm1)
        d1.append( d1_ )
        d2.append( d2_ )
        for i, theta in enumerate([0.25, 0.5, 0.75]):
            d_theta[i].append( theta * d1_ + (1-theta) * d2_ )

    print("Max for d1", np.argmax(d1))
    print("Max for d2", np.argmax(d2))
    plt.plot(d1, label="d1")
    plt.plot(d2, label="d2")
    # for i, theta in enumerate([0.25, 0.5, 0.75]):
        # plt.plot(d_theta[i], label=f"d_theta {theta}")
    plt.legend()
    plt.yscale("log")
    plt.show()
