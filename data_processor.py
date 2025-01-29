import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

class MLBDataProcessor:
    def __init__(self):
        # Generate engaging sample player data
        self.generate_sample_data()

    def generate_sample_data(self):
        # Generate engaging sample player data
        player_achievements = [
            'Led the league in OPS+ for 3 consecutive seasons',
            'Achieved 40-40 season with 45 home runs and 42 stolen bases',
            'Youngest player to reach 500 career hits',
            'Set franchise record with 35-game hitting streak',
            'First player in team history with 3 grand slams in a month',
            'Made diving catch to save perfect game in 9th inning',
            'Hit for the cycle twice in one season',
            'Broke single-season team RBI record',
            'First rookie to lead league in doubles and triples',
            'Set MLB record for most extra-base hits in April'
        ]

        career_highlights = [
            "Walk-off home run in playoffs",
            "Gold Glove winner",
            "Silver Slugger recipient",
            "All-Star game MVP",
            "Rookie of the Year runner-up",
            "30-30 club member",
            "Perfect game in debut",
            "World Series MVP",
            "Batting title winner"
        ]

        self.players_df = pd.DataFrame({
            'player_id': range(1, 101),
            'name': [
                'Mike Trout', 'Shohei Ohtani', 'Juan Soto', 'Mookie Betts', 'Aaron Judge',
                'Ronald Acuña Jr.', 'Freddie Freeman', 'Trea Turner', 'Carlos Correa', 'Pete Alonso'
            ] + [f'Player {i}' for i in range(11, 101)],
            'team': np.random.choice(['Yankees', 'Red Sox', 'Cubs', 'Dodgers', 'Giants'], 100),
            'position': np.random.choice(['P', 'C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF'], 100),
            'avg': np.random.uniform(0.250, 0.380, 100).round(3),
            'hr': np.random.randint(5, 52, 100),
            'rbi': np.random.randint(20, 135, 100),
            'story': player_achievements + [f'Career highlight: {random.choice(career_highlights)}' for _ in range(90)],
            'video_highlights': [
                [
                    "Spectacular diving catch",
                    "Walk-off grand slam",
                    "Inside-the-park home run",
                    "Double play without glove",
                    "Three-homer game"
                ] for _ in range(100)
            ]
        })

        # Generate exciting game data with video analysis
        self.games_df = pd.DataFrame({
            'game_id': range(1, 51),
            'home_team': np.random.choice(['Yankees', 'Red Sox', 'Cubs', 'Dodgers', 'Giants'], 50),
            'away_team': np.random.choice(['Yankees', 'Red Sox', 'Cubs', 'Dodgers', 'Giants'], 50),
            'home_score': np.random.randint(0, 12, 50),
            'away_score': np.random.randint(0, 12, 50),
            'status': ['Live' if i < 3 else np.random.choice(['Final', 'Scheduled'], p=[0.7, 0.3]) for i in range(50)],
            'video_metrics': [
                {
                    'pitch_velocity': round(np.random.uniform(88, 103), 1),
                    'exit_velocity': round(np.random.uniform(85, 118), 1),
                    'launch_angle': round(np.random.uniform(10, 45), 1),
                    'spin_rate': round(np.random.uniform(2000, 3000), 0),
                    'distance': round(np.random.uniform(300, 450), 1)
                } for _ in range(50)
            ],
            'highlights': [
                random.choice([
                    "Perfect game through 7 innings!",
                    "Back-to-back home runs in the 9th!",
                    "Triple play alert!",
                    "Immaculate inning achieved!",
                    "Four stolen bases in one inning!",
                    "No-hitter alert in progress!"
                ]) if random.random() < 0.3 else "" for _ in range(50)
            ]
        })

    def get_top_players(self, stat='avg', n=10):
        return self.players_df.nlargest(n, stat)

    def get_live_games(self):
        return self.games_df[self.games_df['status'] == 'Live']

    def get_player_stats(self, player_id):
        player_data = self.players_df[self.players_df['player_id'] == player_id].iloc[0]
        return {
            'basic_stats': {
                'avg': player_data['avg'],
                'hr': player_data['hr'],
                'rbi': player_data['rbi']
            },
            'story': player_data['story'],
            'video_highlights': player_data['video_highlights']
        }

    def get_game_video_analysis(self, game_id):
        game = self.games_df[self.games_df['game_id'] == game_id].iloc[0]
        return {
            'game_info': {
                'home_team': game['home_team'],
                'away_team': game['away_team'],
                'score': f"{game['home_score']} - {game['away_score']}",
                'highlight': game['highlights']
            },
            'video_metrics': game['video_metrics']
        }

    def get_real_time_insights(self, game_id):
        """Get AI-powered real-time insights for a game"""
        game = self.games_df[self.games_df['game_id'] == game_id].iloc[0]
        metrics = game['video_metrics']

        insights = []
        if metrics['pitch_velocity'] > 98:
            insights.append(f"🔥 Elite velocity detected: {metrics['pitch_velocity']} mph! Top 1% of all pitches!")
        if metrics['exit_velocity'] > 110:
            insights.append(f"💥 Monster hit with exit velocity: {metrics['exit_velocity']} mph! Potential home run!")
        if 25 <= metrics['launch_angle'] <= 35:
            insights.append(f"📈 Perfect launch angle: {metrics['launch_angle']}° - Optimal for home runs!")
        if metrics['spin_rate'] > 2800:
            insights.append(f"🌪️ Elite spin rate: {metrics['spin_rate']} RPM - Exceptional movement!")
        if metrics['distance'] > 420:
            insights.append(f"🚀 Massive shot! Projected distance: {metrics['distance']} feet!")
        if game['highlights']:
            insights.append(f"⚡ {game['highlights']}")

        return insights

    def get_team_stats(self, team_name):
        team_players = self.players_df[self.players_df['team'] == team_name]
        return {
            'avg_batting': team_players['avg'].mean().round(3),
            'total_hr': team_players['hr'].sum(),
            'total_rbi': team_players['rbi'].sum()
        }