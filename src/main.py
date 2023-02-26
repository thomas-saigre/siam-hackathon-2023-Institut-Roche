from distances import *
import sys
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def justOne():
    df = pd.read_csv("data/MIXED50patients_subsamples/1/Baynet/brca_mRNA_patients_BayNet_n20_deg2_eps0_seed_1.csv")
    df_true = pd.read_csv("data/MIXED50patients_subsamples/1/brca_mRNA_50patients.csv")

    
    d1, d2, d_theta = getDistances(df_true, df)

    fig = go.Figure()
    fig.add_trace(go.Box(y=d1, name="d1"))
    fig.add_trace(go.Box(y=d2, name="d2"))
    fig.update_traces(boxpoints='all', jitter=0)
    fig.update_layout(
        title="Boxplot of distances",
        xaxis_title="Distance",
        yaxis_title="Value",
    )
    fig.update_yaxes(type="log")
    fig.show()

    print("Max for d1", np.argmax(d1))
    print("Max for d2", np.argmax(d2))
    plt.plot(d1, label="d1")
    plt.plot(d2, label="d2")
    # for i, theta in enumerate([0.25, 0.5, 0.75]):
        # plt.plot(d_theta[i], label=f"d_theta {theta}")
    plt.legend()
    plt.yscale("log")
    plt.show()

def allPop():

    POPULATIONS = [50, 100, 200, 500, 1000, 1977]
    n_pop = len(POPULATIONS)

    fig, ax = plt.subplots(1, n_pop, figsize=(n_pop*5, 5))
    for i, pop in enumerate(POPULATIONS):
        df = pd.read_csv(f"data/MIXED{pop}patients_subsamples/1/Baynet/brca_mRNA_patients_BayNet_n20_deg2_eps0_seed_1.csv")
        df_true = pd.read_csv(f"data/MIXED{pop}patients_subsamples/1/brca_mRNA_{pop}patients.csv")

        d1, d2, d_theta = getDistances(df_true, df)

        ax[i].scatter(list(range(len(d1))), d1, label="d1", s=1, alpha=0.5)
        ax[i].scatter(list(range(len(d2))), d2, label="d2", s=1, alpha=0.5)
        # ax[i].scatter(list(d2), label="d2")
        # for i, theta in enumerate([0.25, 0.5, 0.75]):
            # ax[i].plot(d_theta[i], label=f"d_theta {theta}")
        ax[i].set_title(f"Population {pop}")
        ax[i].set_yscale("log")
        ax[i].legend()

    plt.show()

def allPopBoxPlot():
    POPULATIONS = [50, 100, 200, 500, 1000, 1977]
    n_pop = len(POPULATIONS)

    fig = make_subplots(rows=1, cols=n_pop, subplot_titles=[f"Population {pop}" for pop in POPULATIONS])

    for i, pop in enumerate(POPULATIONS):
        df = pd.read_csv(f"data/MIXED{pop}patients_subsamples/1/Baynet/brca_mRNA_patients_BayNet_n20_deg2_eps0_seed_1.csv")
        df_true = pd.read_csv(f"data/MIXED{pop}patients_subsamples/1/brca_mRNA_{pop}patients.csv")

        d1, d2, d_theta = getDistances(df_true, df)

        fig.add_trace(go.Box(y=d1, name="d1", legendgroup="d1", showlegend=pop==50, line=dict(color="blue")), row=1, col=i+1)
        fig.add_trace(go.Box(y=d2, name="d2", legendgroup="d2", showlegend=pop==50, line=dict(color="red")), row=1, col=i+1)
        fig.update_traces(boxpoints='all', jitter=0, row=1, col=i+1)
        fig.update_yaxes(type="log", row=1, col=i+1)

    fig.show()

def allPopAllMethBoxPlot():
    POPULATIONS = [50, 100, 200, 500, 1000, 1977]
    n_pop = len(POPULATIONS)

    fig1 = make_subplots(rows=1, cols=n_pop, subplot_titles=[f"Population {pop}" for pop in POPULATIONS])

    for i, pop in enumerate(POPULATIONS):
        df = pd.read_csv(f"data/MIXED{pop}patients_subsamples/1/Baynet/brca_mRNA_patients_BayNet_n20_deg2_eps0_seed_1.csv")
        df_true = pd.read_csv(f"data/MIXED{pop}patients_subsamples/1/brca_mRNA_{pop}patients.csv")

        d1, d2, d_theta = getDistances(df_true, df)

        fig1.add_trace(go.Box(y=d1, name="d1", legendgroup="d1", showlegend=pop==50, line=dict(color="blue")), row=1, col=i+1)
        fig1.add_trace(go.Box(y=d2, name="d2", legendgroup="d2", showlegend=pop==50, line=dict(color="red")), row=1, col=i+1)
        fig1.update_traces(boxpoints='all', jitter=0, row=1, col=i+1)
        fig1.update_yaxes(type="log", row=1, col=i+1)
    
    fig1.update_layout(
        title="Baynet",
    )
    fig1.show()

    fig2 = make_subplots(rows=1, cols=n_pop, subplot_titles=[f"Population {pop}" for pop in POPULATIONS])

    for i, pop in enumerate(POPULATIONS):
        df2 = pd.read_csv(f'data/MIXED{pop}patients_subsamples/1/CTGAN/brca_mRNA_patients_embedding_dim128_gen_dim256_dis_dim256_l2scale1e-06_batch_size500_epochs500.csv')
        df_true = pd.read_csv(f"data/MIXED{pop}patients_subsamples/1/brca_mRNA_{pop}patients.csv")

        d1, d2, d_theta = getDistances(df_true, df2)

        fig2.add_trace(go.Box(y=d1, name="d1", legendgroup="d1", showlegend=pop==50, line=dict(color="blue")), row=1, col=i+1)
        fig2.add_trace(go.Box(y=d2, name="d2", legendgroup="d2", showlegend=pop==50, line=dict(color="red")), row=1, col=i+1)
        fig2.update_traces(boxpoints='all', jitter=0, row=1, col=i+1)
        fig2.update_yaxes(type="log", row=1, col=i+1)

    fig2.update_layout(
        title="CTGAN",
    )
    fig2.show()

    fig3 = make_subplots(rows=1, cols=n_pop, subplot_titles=[f"Population {pop}" for pop in POPULATIONS])

    for i, pop in enumerate(POPULATIONS):
        df3 = pd.read_csv(f'data/MIXED{pop}patients_subsamples/1/MIIC/syntheticData_mixedNetwork_test_fast_root_index_4.csv')
        df_true = pd.read_csv(f"data/MIXED{pop}patients_subsamples/1/brca_mRNA_{pop}patients.csv")

        d1, d2, d_theta = getDistances(df_true, df3)

        fig3.add_trace(go.Box(y=d1, name="d1", legendgroup="d1", showlegend=pop==50, line=dict(color="blue")), row=1, col=i+1)
        fig3.add_trace(go.Box(y=d2, name="d2", legendgroup="d2", showlegend=pop==50, line=dict(color="red")), row=1, col=i+1)
        fig3.update_traces(boxpoints='all', jitter=0, row=1, col=i+1)
        fig3.update_yaxes(type="log", row=1, col=i+1)

    fig3.update_layout(
        title="MICC",
    )
    fig3.show()


    fig4 = make_subplots(rows=1, cols=n_pop, subplot_titles=[f"Population {pop}" for pop in POPULATIONS])

    for i, pop in enumerate(POPULATIONS):
        df4 = pd.read_csv(f'data/MIXED{pop}patients_subsamples/1/PrivBayes/brca_mRNA_patients_PrivBayes_n20_deg2_eps1_seed_7.csv')
        df_true = pd.read_csv(f"data/MIXED{pop}patients_subsamples/1/brca_mRNA_{pop}patients.csv")

        d1, d2, d_theta = getDistances(df_true, df4)

        fig4.add_trace(go.Box(y=d1, name="d1", legendgroup="d1", showlegend=pop==50, line=dict(color="blue")), row=1, col=i+1)
        fig4.add_trace(go.Box(y=d2, name="d2", legendgroup="d2", showlegend=pop==50, line=dict(color="red")), row=1, col=i+1)
        fig4.update_traces(boxpoints='all', jitter=0, row=1, col=i+1)
        fig4.update_yaxes(type="log", row=1, col=i+1)

    fig4.update_layout(
        title="PrivBayes",
    )
    fig4.show()

    fig5 = make_subplots(rows=1, cols=n_pop, subplot_titles=[f"Population {pop}" for pop in POPULATIONS])

    for i, pop in enumerate(POPULATIONS):
        df5 = pd.read_csv(f'data/MIXED{pop}patients_subsamples/1/Synthpop/brca_mRNA_{pop}patients_iteration_5_.csv')
        df_true = pd.read_csv(f"data/MIXED{pop}patients_subsamples/1/brca_mRNA_{pop}patients.csv")

        d1, d2, d_theta = getDistances(df_true, df5)

        fig5.add_trace(go.Box(y=d1, name="d1", legendgroup="d1", showlegend=pop==50, line=dict(color="blue")), row=1, col=i+1)
        fig5.add_trace(go.Box(y=d2, name="d2", legendgroup="d2", showlegend=pop==50, line=dict(color="red")), row=1, col=i+1)
        fig5.update_traces(boxpoints='all', jitter=0, row=1, col=i+1)
        fig5.update_yaxes(type="log", row=1, col=i+1)

    fig5.update_layout(
        title="Synthpop",
    )
    fig5.show()


if __name__ == "__main__":
    # justOne()
    # allPop()
    # allPopBoxPlot()
    allPopAllMethBoxPlot()
