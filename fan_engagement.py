import streamlit as st
import random
from datetime import datetime

class FanEngagementSystem:
    def __init__(self):
        if 'points' not in st.session_state:
            st.session_state.points = 0
        if 'badges' not in st.session_state:
            st.session_state.badges = set()
        if 'activities' not in st.session_state:
            st.session_state.activities = []
        if 'favorite_team' not in st.session_state:
            st.session_state.favorite_team = None
        if 'streak' not in st.session_state:
            st.session_state.streak = 0
        if 'achievements' not in st.session_state:
            st.session_state.achievements = {
                'games_watched': 0,
                'predictions_made': 0,
                'correct_predictions': 0,
                'social_shares': 0,
                'player_profiles_viewed': 0,
                'video_analyses_watched': 0,
                'team_selection': 0
            }

    def set_favorite_team(self, team):
        st.session_state.favorite_team = team
        self.add_points(10, f"Selected {team} as favorite team")
        self._track_achievement('team_selection')

    def _track_achievement(self, achievement_type, value=1):
        """Track various achievement types"""
        if achievement_type in st.session_state.achievements:
            st.session_state.achievements[achievement_type] += value
        self._check_badges()

    def add_points(self, points, activity):
        st.session_state.points += points
        st.session_state.activities.append({
            'timestamp': datetime.now(),
            'activity': activity,
            'points': points
        })
        self._check_badges()
        self._update_streak()

    def _update_streak(self):
        """Update daily login streak"""
        today = datetime.now().date()
        if 'last_login' not in st.session_state:
            st.session_state.last_login = today
            st.session_state.streak = 1
        elif (today - st.session_state.last_login).days == 1:
            st.session_state.streak += 1
            self.add_points(st.session_state.streak * 5, f"Daily streak: {st.session_state.streak} days!")
        elif (today - st.session_state.last_login).days > 1:
            st.session_state.streak = 1
        st.session_state.last_login = today

    def _check_badges(self):
        """Check and award badges based on achievements"""
        badges_criteria = {
            'Rookie Fan': {'points': 100, 'description': 'Earn your first 100 points', 'icon': '👶'},
            'All-Star Fan': {'points': 500, 'description': 'Reach 500 points', 'icon': '⭐'},
            'MVP Fan': {'points': 1000, 'description': 'Achieve 1000 points', 'icon': '🏆'},
            'Perfect Attendance': {'streak': 7, 'description': 'Login 7 days in a row', 'icon': '📅'},
            'Super Fan': {'streak': 30, 'description': '30-day login streak', 'icon': '🌟'},
            'Game Guru': {'predictions': 10, 'description': 'Make 10 correct game predictions', 'icon': '🎯'},
            'Social Butterfly': {'social_shares': 5, 'description': 'Share 5 times on social media', 'icon': '🦋'},
            'Scout': {'player_profiles': 20, 'description': 'View 20 different player profiles', 'icon': '🔍'},
            'Video Analyst': {'video_analyses': 10, 'description': 'Watch 10 video analyses', 'icon': '📹'},
            'Team Loyalist': {'team_selection': 1, 'description': 'Select your favorite team', 'icon': '⚾'}
        }

        achievements = st.session_state.achievements
        for badge, criteria in badges_criteria.items():
            if badge not in st.session_state.badges:
                if 'points' in criteria and st.session_state.points >= criteria['points']:
                    st.session_state.badges.add(badge)
                elif 'streak' in criteria and st.session_state.streak >= criteria['streak']:
                    st.session_state.badges.add(badge)
                elif 'predictions' in criteria and achievements.get('correct_predictions', 0) >= criteria['predictions']:
                    st.session_state.badges.add(badge)
                elif 'social_shares' in criteria and achievements.get('social_shares', 0) >= criteria['social_shares']:
                    st.session_state.badges.add(badge)
                elif 'player_profiles' in criteria and achievements.get('player_profiles_viewed', 0) >= criteria['player_profiles']:
                    st.session_state.badges.add(badge)
                elif 'video_analyses' in criteria and achievements.get('video_analyses_watched', 0) >= criteria['video_analyses']:
                    st.session_state.badges.add(badge)
                elif 'team_selection' in criteria and achievements.get('team_selection', 0) >= criteria['team_selection']:
                    st.session_state.badges.add(badge)

    def get_points(self):
        return st.session_state.points

    def get_badges(self):
        badges_info = {
            'Rookie Fan': {'icon': '👶', 'description': 'Earn your first 100 points'},
            'All-Star Fan': {'icon': '⭐', 'description': 'Reach 500 points'},
            'MVP Fan': {'icon': '🏆', 'description': 'Achieve 1000 points'},
            'Perfect Attendance': {'icon': '📅', 'description': 'Login 7 days in a row'},
            'Super Fan': {'icon': '🌟', 'description': '30-day login streak'},
            'Game Guru': {'icon': '🎯', 'description': 'Make 10 correct game predictions'},
            'Social Butterfly': {'icon': '🦋', 'description': 'Share 5 times on social media'},
            'Scout': {'icon': '🔍', 'description': 'View 20 different player profiles'},
            'Video Analyst': {'icon': '📹', 'description': 'Watch 10 video analyses'},
            'Team Loyalist': {'icon': '⚾', 'description': 'Select your favorite team'}
        }
        return [(badge, badges_info[badge]) for badge in st.session_state.badges]

    def get_activities(self):
        return st.session_state.activities

    def get_achievements_progress(self):
        """Get progress towards achievements"""
        return st.session_state.achievements

    def track_video_analysis(self):
        """Track when user watches a video analysis"""
        self._track_achievement('video_analyses_watched')
        self.add_points(15, "Watched video analysis")

    def track_profile_view(self):
        """Track when user views a player profile"""
        self._track_achievement('player_profiles_viewed')
        self.add_points(5, "Viewed player profile")

    def track_social_share(self):
        """Track when user shares content"""
        self._track_achievement('social_shares')
        self.add_points(20, "Shared content on social media")

    def get_streak_info(self):
        return {
            'current_streak': st.session_state.streak,
            'next_milestone': self._get_next_streak_milestone(),
            'points_multiplier': max(1, st.session_state.streak // 5)
        }

    def _get_next_streak_milestone(self):
        streak = st.session_state.streak
        milestones = [7, 30, 60, 90, 180, 365]
        for milestone in milestones:
            if streak < milestone:
                return milestone
        return milestones[-1]

    def generate_challenge(self):
        """Generate personalized challenges based on user's favorite team and current achievements"""
        team_specific_challenges = [
            {'task': f'Watch a full {st.session_state.favorite_team} game', 'points': 50},
            {'task': f'Predict the winner of next {st.session_state.favorite_team} game', 'points': 30},
            {'task': f'Share {st.session_state.favorite_team} highlights on social media', 'points': 20}
        ] if st.session_state.favorite_team else []

        # Dynamic challenges based on missing achievements
        achievement_based_challenges = []
        achievements = st.session_state.achievements

        if achievements['video_analyses_watched'] < 10:
            achievement_based_challenges.append(
                {'task': 'Watch a video analysis of today\'s game', 'points': 15}
            )
        if achievements['player_profiles_viewed'] < 20:
            achievement_based_challenges.append(
                {'task': 'View 3 new player profiles', 'points': 15}
            )
        if achievements['social_shares'] < 5:
            achievement_based_challenges.append(
                {'task': 'Share your favorite player stats', 'points': 20}
            )

        general_challenges = [
            {'task': 'Complete daily baseball trivia', 'points': 25},
            {'task': 'Predict total runs in today\'s games', 'points': 35},
            {'task': 'Create a game day prediction', 'points': 40},
            {'task': 'Analyze a player\'s performance', 'points': 45}
        ]

        all_challenges = team_specific_challenges + achievement_based_challenges + general_challenges
        return random.choice(all_challenges)