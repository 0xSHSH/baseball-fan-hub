import streamlit as st
from datetime import datetime, timedelta
import random

class NewsFeeder:
    def __init__(self):
        self.news_items = self._generate_sample_news()

    def _generate_sample_news(self):
        news_templates = [
            "🎯 {player} demonstrates exceptional power hitting in latest analysis session",
            "⭐ Rising star {player} sets new personal records in today's metrics",
            "📊 Baseball Hub Analysis: {team}'s innovative defensive strategies paying dividends",
            "🏟️ Fan engagement hits record levels at {team}'s latest home game",
            "🔄 Real-time insights: {team} showing strong improvement in key metrics",
            "🏆 {player} unlocks rare achievement milestone in fan engagement system",
            "📈 Baseball Hub Stats: {team} leads in advanced analytics metrics",
            "🌟 Featured Story: {player}'s journey from rookie to analytics superstar",
            "🎮 Fan Zone Update: New interactive challenges available for {team} fans",
            "📱 Baseball Hub Feature: {player}'s performance metrics break new ground"
        ]

        teams = ['Yankees', 'Red Sox', 'Cubs', 'Dodgers', 'Giants']
        players = ['Mike Trout', 'Shohei Ohtani', 'Juan Soto', 'Mookie Betts', 'Aaron Judge']

        news = []
        for i in range(10):
            template = random.choice(news_templates)
            news_item = template.format(
                team=random.choice(teams),
                player=random.choice(players)
            )
            news.append({
                'timestamp': datetime.now() - timedelta(minutes=i*30),
                'content': news_item
            })

        return sorted(news, key=lambda x: x['timestamp'], reverse=True)

    def get_latest_news(self, limit=5):
        return self.news_items[:limit]

    def format_timestamp(self, timestamp):
        now = datetime.now()
        delta = now - timestamp

        if delta.days == 0:
            if delta.seconds < 3600:
                return f"{delta.seconds // 60}m ago"
            return f"{delta.seconds // 3600}h ago"
        return f"{delta.days}d ago"