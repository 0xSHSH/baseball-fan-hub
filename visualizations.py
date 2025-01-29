import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_batting_avg_chart(players_df):
    fig = px.bar(
        players_df.head(10),
        x='name',
        y='avg',
        title='Top 10 Batting Averages',
        color='avg',
        color_continuous_scale='Viridis',
        template='plotly_dark'
    )
    fig.update_layout(
        xaxis_title="Player",
        yaxis_title="Batting Average",
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        title_font=dict(size=24, color='#9C27B0'),
        hoverlabel=dict(bgcolor='#1E1E1E'),
        margin=dict(t=50, b=50, l=50, r=50)
    )
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>AVG: %{y:.3f}<extra></extra>",
        marker_line_color='#9C27B0',
        marker_line_width=1.5
    )
    return fig

def create_hr_leaderboard(players_df):
    fig = px.bar(
        players_df.nlargest(10, 'hr'),
        x='name',
        y='hr',
        title='Home Run Leaders',
        color='hr',
        color_continuous_scale='Magma',
        template='plotly_dark'
    )
    fig.update_layout(
        xaxis_title="Player",
        yaxis_title="Home Runs",
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        title_font=dict(size=24, color='#9C27B0'),
        hoverlabel=dict(bgcolor='#1E1E1E'),
        margin=dict(t=50, b=50, l=50, r=50)
    )
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>HR: %{y}<extra></extra>",
        marker_line_color='#9C27B0',
        marker_line_width=1.5
    )
    return fig

def create_team_comparison(games_df):
    team_stats = {}

    for team in games_df['home_team'].unique():
        team_games = games_df[
            (games_df['home_team'] == team) | 
            (games_df['away_team'] == team)
        ]

        wins = len(team_games[
            ((team_games['home_team'] == team) & 
             (team_games['home_score'] > team_games['away_score'])) |
            ((team_games['away_team'] == team) & 
             (team_games['away_score'] > team_games['home_score']))
        ])

        total_games = len(team_games)
        win_pct = (wins / total_games) * 100 if total_games > 0 else 0

        team_stats[team] = {
            'wins': wins,
            'total_games': total_games,
            'win_pct': win_pct
        }

    fig = go.Figure()

    colors = px.colors.sequential.Viridis

    for i, (team, stats) in enumerate(team_stats.items()):
        fig.add_trace(go.Bar(
            name=team,
            x=[team],
            y=[stats['wins']],
            text=[f"{stats['wins']} W<br>{stats['win_pct']:.1f}%"],
            textposition='auto',
            marker_color=colors[i],
            hovertemplate=(
                f"<b>{team}</b><br>"
                f"Wins: {stats['wins']}<br>"
                f"Win %: {stats['win_pct']:.1f}%<br>"
                f"Games: {stats['total_games']}"
                "<extra></extra>"
            )
        ))

    fig.update_layout(
        title='Team Performance Analysis',
        title_font=dict(size=24, color='#9C27B0'),
        xaxis_title="Team",
        yaxis_title="Wins",
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        hoverlabel=dict(bgcolor='#1E1E1E'),
        margin=dict(t=50, b=50, l=50, r=50),
        template='plotly_dark'
    )
    return fig

def create_video_metrics_chart(metrics):
    """Create an enhanced radar chart for video metrics visualization"""
    categories = ['Pitch Velocity', 'Exit Velocity', 'Launch Angle']
    max_values = [105, 120, 45]  # Maximum expected values for each metric

    # Normalize values to 0-10 scale
    values = [
        metrics['pitch_velocity'] / max_values[0] * 10,
        metrics['exit_velocity'] / max_values[1] * 10,
        metrics['launch_angle'] / max_values[2] * 10
    ]

    fig = go.Figure()

    # Add the main radar chart
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Current Metrics',
        fillcolor='rgba(156, 39, 176, 0.3)',
        line=dict(color='#9C27B0', width=2),
        hovertemplate=(
            "<b>%{theta}</b><br>"
            "Score: %{r:.1f}/10<br>"
            "<extra></extra>"
        )
    ))

    # Add a reference line for average values
    fig.add_trace(go.Scatterpolar(
        r=[7, 7, 7],  # Example reference values
        theta=categories,
        fill='toself',
        name='League Average',
        fillcolor='rgba(233, 30, 99, 0.1)',
        line=dict(color='#E91E63', width=1, dash='dash'),
        hovertemplate=(
            "<b>League Average</b><br>"
            "%{theta}: %{r:.1f}/10<br>"
            "<extra></extra>"
        )
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10],
                showline=False,
                gridcolor='rgba(255, 255, 255, 0.1)',
                tickfont=dict(color='white')
            ),
            angularaxis=dict(
                gridcolor='rgba(255, 255, 255, 0.1)',
                linecolor='rgba(255, 255, 255, 0.2)'
            ),
            bgcolor='rgba(0,0,0,0)'
        ),
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            font=dict(color='white'),
            bgcolor='rgba(0,0,0,0)'
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        margin=dict(t=10, b=10)
    )
    return fig

def create_app_logo():
    """Generate an SVG logo for the application"""
    return '''
    <svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
        <!-- Baseball background -->
        <circle cx="100" cy="100" r="90" fill="#FFFFFF" stroke="#9C27B0" stroke-width="4"/>
        <path d="M100,10 Q150,100 100,190 Q50,100 100,10" 
              fill="none" stroke="#9C27B0" stroke-width="2"/>
        <path d="M10,100 Q100,150 190,100 Q100,50 10,100" 
              fill="none" stroke="#9C27B0" stroke-width="2"/>

        <!-- Stitches -->
        <path d="M95,15 L105,15 M95,185 L105,185" 
              stroke="#E91E63" stroke-width="3"/>
        <path d="M15,95 L15,105 M185,95 L185,105" 
              stroke="#E91E63" stroke-width="3"/>

        <!-- Text -->
        <text x="100" y="105" font-family="Arial" font-size="24" 
              fill="#9C27B0" text-anchor="middle" font-weight="bold">
            Baseball
        </text>
        <text x="100" y="130" font-family="Arial" font-size="24" 
              fill="#9C27B0" text-anchor="middle" font-weight="bold">
            Fan Hub
        </text>
    </svg>
    '''