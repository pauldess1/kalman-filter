import plotly.graph_objects as go


def plot_with_plotly(true_pos, measured_pos, predicted_pos):
    fig = go.Figure()

    # Trajectoire réelle
    fig.add_trace(
        go.Scatter(
            x=true_pos[:, 0],
            y=true_pos[:, 1],
            mode="lines+markers",
            name="True Position",
            line=dict(color="green"),
            marker=dict(size=4),
        )
    )

    # Mesures bruitées
    fig.add_trace(
        go.Scatter(
            x=measured_pos[:, 0],
            y=measured_pos[:, 1],
            mode="markers",
            name="Measured Position (noisy)",
            marker=dict(size=6, color="red", opacity=0.5),
        )
    )

    # Kalman Filter
    fig.add_trace(
        go.Scatter(
            x=predicted_pos[:, 0],
            y=predicted_pos[:, 1],
            mode="lines+markers",
            name="Kalman Estimate",
            line=dict(color="blue"),
            marker=dict(size=4),
        )
    )

    fig.update_layout(
        title="Kalman Filter - 2D Tracking",
        xaxis_title="x",
        yaxis_title="y",
        width=900,
        height=600,
        legend=dict(x=0.01, y=0.99),
        margin=dict(l=50, r=50, t=50, b=50),
        template="plotly_white",
    )

    fig.show()
