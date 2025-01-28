import streamlit as st
from data_processor import MLBDataProcessor
from visualizations import (
    create_batting_avg_chart,
    create_hr_leaderboard,
    create_team_comparison,
    create_video_metrics_chart
)
from fan_engagement import FanEngagementSystem
from news_feed import NewsFeeder
from styles import apply_custom_styles, create_stat_card
from highlight_generator import HighlightGenerator # Added import statement
from outfit_recommender import OutfitRecommender # Add this import at the top with other imports

# Page configuration
st.set_page_config(
    page_title="Baseball Fan Hub",
    page_icon="⚾",
    layout="wide"
)

# Initialize components
apply_custom_styles()
data_processor = MLBDataProcessor()
fan_system = FanEngagementSystem()
news_feeder = NewsFeeder()
highlight_gen = HighlightGenerator() # Added highlight generator initialization
outfit_recommender = OutfitRecommender() # Add this line

# Header
st.title("⚾ Baseball Fan Hub")

# Add welcome message and description
st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <h2 style="color: #9C27B0; margin-bottom: 1rem;">Welcome to Baseball Fan Hub</h2>
        <p style="font-size: 1.1rem; opacity: 0.8;">
            Your ultimate destination for real-time baseball stats, player stories, and fan engagement.
            Join our community of baseball enthusiasts and start earning achievements today!
        </p>
    </div>
""", unsafe_allow_html=True)

# Top navigation with improved styling
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([ # Added tab6 for highlights and tab7 for outfit recommender
    "🏟️ Live Dashboard", 
    "👤 Player Stories", 
    "📊 Video Analysis",
    "🏆 Fan Zone",
    "📰 News Feed",
    "🎬 Highlights", #Added comma here
    "👕 Outfit Recommender"  # New tab
])

with tab1:
    st.header("Live Games & Statistics")

    # Live games section
    st.subheader("Live Games")
    live_games = data_processor.get_live_games()
    if not live_games.empty:
        for _, game in live_games.iterrows():
            st.markdown(f"""
                <div class="stat-card">
                    🏟️ **{game['away_team']} ({game['away_score']}) @ 
                    {game['home_team']} ({game['home_score']})**
                    <div style="margin-top: 10px;">
                        {"🔴 LIVE" if game['status'] == 'Live' else game['status']}
                    </div>
                </div>
            """, unsafe_allow_html=True)

            # Real-time insights
            insights = data_processor.get_real_time_insights(game['game_id'])
            if insights:
                st.markdown("### 🎯 AI Insights")
                for insight in insights:
                    st.info(insight)
    else:
        st.info("No live games at the moment")

    # Statistics Dashboard
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            create_batting_avg_chart(data_processor.get_top_players('avg')),
            use_container_width=True
        )

    with col2:
        st.plotly_chart(
            create_hr_leaderboard(data_processor.get_top_players('hr')),
            use_container_width=True
        )

    st.plotly_chart(
        create_team_comparison(data_processor.games_df),
        use_container_width=True
    )

with tab2:
    st.header("Player Stories & Profiles")

    # Team and player selection
    selected_team = st.selectbox(
        "Select Team",
        ['Yankees', 'Red Sox', 'Cubs', 'Dodgers', 'Giants']
    )

    team_players = data_processor.players_df[
        data_processor.players_df['team'] == selected_team
    ]

    selected_player = st.selectbox(
        "Select Player",
        team_players['name'].tolist()
    )

    if selected_player:
        player_id = team_players[
            team_players['name'] == selected_player
        ]['player_id'].iloc[0]
        player_data = data_processor.get_player_stats(player_id)

        # Player story and stats
        st.markdown(f"""
            <div class="stat-card">
                <h2>{selected_player}</h2>
                <p>{player_data['story']}</p>
            </div>
        """, unsafe_allow_html=True)

        # Stats display
        col1, col2, col3 = st.columns(3)
        with col1:
            create_stat_card("Batting Average", f"{player_data['basic_stats']['avg']:.3f}")
        with col2:
            create_stat_card("Home Runs", player_data['basic_stats']['hr'])
        with col3:
            create_stat_card("RBIs", player_data['basic_stats']['rbi'])

        # Video highlights
        st.subheader("Video Highlights")
        for highlight in player_data['video_highlights']:
            st.markdown(f"🎥 {highlight}")

with tab3:
    st.header("Video Analysis Dashboard")

    # Game selection for video analysis
    selected_game = st.selectbox(
        "Select Game",
        data_processor.games_df['game_id'].tolist(),
        format_func=lambda x: f"Game {x}"
    )

    if selected_game:
        game_data = data_processor.get_game_video_analysis(selected_game)

        # Game info
        st.markdown(f"""
            <div class="stat-card">
                <h3>{game_data['game_info']['home_team']} vs {game_data['game_info']['away_team']}</h3>
                <p>Score: {game_data['game_info']['score']}</p>
            </div>
        """, unsafe_allow_html=True)

        # Video metrics
        metrics = game_data['video_metrics']
        col1, col2, col3 = st.columns(3)

        with col1:
            create_stat_card("Pitch Velocity", f"{metrics['pitch_velocity']} mph")
        with col2:
            create_stat_card("Exit Velocity", f"{metrics['exit_velocity']} mph")
        with col3:
            create_stat_card("Launch Angle", f"{metrics['launch_angle']}°")

        # Video metrics chart
        st.plotly_chart(
            create_video_metrics_chart(metrics),
            use_container_width=True
        )

with tab4:
    st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h2 style="color: #9C27B0;">🏆 Fan Zone</h2>
            <p style="font-size: 1.1rem; opacity: 0.8;">
                Track your achievements, earn badges, and compete with other fans!
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Team Selection with improved styling
    if not st.session_state.get('favorite_team'):
        st.markdown("""
            <div class="stat-card" style="text-align: center;">
                <h3 style="color: #9C27B0;">Select Your Favorite Team</h3>
                <p style="opacity: 0.8;">Choose your team and start your fan journey!</p>
            </div>
        """, unsafe_allow_html=True)

        selected_team = st.selectbox(
            "Choose your team",
            ['Yankees', 'Red Sox', 'Cubs', 'Dodgers', 'Giants']
        )
        if st.button("Set as Favorite"):
            fan_system.set_favorite_team(selected_team)
            st.success(f"You've selected {selected_team} as your favorite team! +10 points")
            st.rerun()

    # Display fan stats with enhanced cards
    col1, col2, col3 = st.columns(3)
    with col1:
        create_stat_card("🌟 Fan Points", fan_system.get_points())
    with col2:
        streak_info = fan_system.get_streak_info()
        create_stat_card(
            "🔥 Daily Streak", 
            f"{streak_info['current_streak']} days\n"
            f"Next milestone: {streak_info['next_milestone']}"
        )
    with col3:
        create_stat_card(
            "⚡ Points Multiplier", 
            f"{streak_info['points_multiplier']}x"
        )

    # Achievements with improved visualization
    st.markdown("""
        <div style="margin: 2rem 0;">
            <h2 style="color: #9C27B0; text-align: center;">🏅 Achievements</h2>
        </div>
    """, unsafe_allow_html=True)

    progress_col1, progress_col2 = st.columns(2)

    def create_progress_bar(title, progress, total, icon):
        st.markdown(f"**{title}:**")
        st.progress(min(1.0, progress / total))
        st.markdown(f"{icon} {progress}/{total}")

    def create_badge_card(badge, icon, description):
        st.markdown(f"""
            <div class="stat-card" style="text-align: center;">
                <h3 style="color: #9C27B0;">{badge}</h3>
                <p style="font-size: 2em;">{icon}</p>
                <p><em>{description}</em></p>
            </div>
        """, unsafe_allow_html=True)

    with progress_col1:
        achievements = fan_system.get_achievements_progress()
        st.markdown("### 📊 Progress Tracking")

        create_progress_bar(
            "Video Analyst Progress",
            achievements['video_analyses_watched'],
            10,
            "📹"
        )
        create_progress_bar(
            "Scout Progress",
            achievements['player_profiles_viewed'],
            20,
            "🔍"
        )
        create_progress_bar(
            "Social Butterfly Progress",
            achievements['social_shares'],
            5,
            "🦋"
        )

    with progress_col2:
        st.markdown("### 🎖️ Earned Badges")
        badge_cols = st.columns(2)
        for idx, (badge, info) in enumerate(fan_system.get_badges()):
            with badge_cols[idx % 2]:
                create_badge_card(badge, info['icon'], info['description'])

    # Daily Challenge with enhanced styling
    st.markdown("""
        <div style="margin: 2rem 0;">
            <h2 style="color: #9C27B0; text-align: center;">📋 Daily Challenge</h2>
        </div>
    """, unsafe_allow_html=True)

    challenge = fan_system.generate_challenge()
    st.markdown(f"""
        <div class="stat-card" style="text-align: center;">
            <h3 style="color: #9C27B0; margin-bottom: 1rem;">Today's Challenge</h3>
            <p style="font-size: 1.2rem; margin-bottom: 1rem;">{challenge['task']}</p>
            <p style="font-size: 1.1rem; color: #9C27B0;">
                Reward: {challenge['points'] * streak_info['points_multiplier']} points
                <span style="opacity: 0.8;">({challenge['points']} × {streak_info['points_multiplier']})</span>
            </p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Complete Challenge"):
        points = challenge['points'] * streak_info['points_multiplier']
        fan_system.add_points(points, challenge['task'])
        st.balloons()
        st.success(f"Congratulations! You earned {points} points!")
        st.rerun()

with tab5:
    st.header("Latest News")

    # Display news feed
    for news in news_feeder.get_latest_news():
        st.markdown(f"""
            <div class="stat-card">
                <h3>{news['content']}</h3>
                <p><em>{news_feeder.format_timestamp(news['timestamp'])}</em></p>
            </div>
        """, unsafe_allow_html=True)

with tab6: #New tab content added
    highlight_gen.render_highlight_ui()

with tab7:
    outfit_recommender.render_outfit_ui()

# Footer
st.markdown("---")
st.markdown(
    "Made with ❤️ for baseball fans everywhere. "
    "Data and statistics are simulated for demonstration purposes."
)