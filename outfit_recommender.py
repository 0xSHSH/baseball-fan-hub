import streamlit as st
import random
from datetime import datetime

class OutfitRecommender:
    def __init__(self):
        self.team_colors = {
            'Yankees': {
                'primary': '#003087',  # Navy Blue
                'secondary': '#E4002C',  # Red
                'accent': '#FFFFFF'  # White
            },
            'Red Sox': {
                'primary': '#BD3039',  # Red
                'secondary': '#0C2340',  # Navy Blue
                'accent': '#FFFFFF'  # White
            },
            'Cubs': {
                'primary': '#0E3386',  # Blue
                'secondary': '#CC3433',  # Red
                'accent': '#FFFFFF'  # White
            },
            'Dodgers': {
                'primary': '#005A9C',  # Blue
                'secondary': '#EF3E42',  # Red
                'accent': '#FFFFFF'  # White
            },
            'Giants': {
                'primary': '#FD5A1E',  # Orange
                'secondary': '#27251F',  # Black
                'accent': '#FFFFFF'  # White
            }
        }
        
        self.outfit_templates = {
            'casual': [
                {'name': 'Classic Jersey Look', 'items': [
                    'Team jersey',
                    'Jeans',
                    'Team-colored sneakers',
                    'Team cap'
                ]},
                {'name': 'Sporty Casual', 'items': [
                    'Team t-shirt',
                    'Khaki shorts',
                    'Baseball cap',
                    'White sneakers'
                ]},
                {'name': 'Fan Spirit', 'items': [
                    'Team hoodie',
                    'Dark jeans',
                    'Team socks',
                    'Comfortable sneakers'
                ]}
            ],
            'premium': [
                {'name': 'Premium Fan', 'items': [
                    'Authentic team jersey',
                    'Team jacket',
                    'Premium denim',
                    'Limited edition cap'
                ]},
                {'name': 'Collector\'s Choice', 'items': [
                    'Vintage team shirt',
                    'Team varsity jacket',
                    'Designer jeans',
                    'Exclusive team sneakers'
                ]}
            ]
        }

    def get_color_palette(self, team):
        """Get the color palette for a specific team."""
        return self.team_colors.get(team, {
            'primary': '#000000',
            'secondary': '#FFFFFF',
            'accent': '#CCCCCC'
        })

    def generate_recommendation(self, team, weather_temp=None, style_preference='casual'):
        """Generate a personalized outfit recommendation."""
        colors = self.get_color_palette(team)
        
        # Select outfit template based on style preference
        templates = self.outfit_templates.get(style_preference, self.outfit_templates['casual'])
        base_outfit = random.choice(templates)
        
        # Adjust for weather if provided
        if weather_temp is not None:
            if weather_temp < 60:
                base_outfit['items'].append('Team jacket or sweater')
            elif weather_temp > 85:
                base_outfit['items'] = [item for item in base_outfit['items'] if 'jacket' not in item.lower()]
                base_outfit['items'].append('Team cap for sun protection')
                base_outfit['items'].append('Sunglasses in team colors')

        return {
            'outfit_name': base_outfit['name'],
            'items': base_outfit['items'],
            'color_scheme': colors,
            'styling_tips': [
                f"Match your accessories with the team's {list(colors.keys())[0]} color",
                "Layer pieces for versatility and comfort",
                "Don't forget team-specific accessories"
            ]
        }

    def render_outfit_ui(self):
        """Render the outfit recommender UI in Streamlit."""
        st.markdown("""
            <div style="text-align: center; margin-bottom: 2rem;">
                <h2 style="color: #9C27B0;">👕 Game Day Outfit Recommender</h2>
                <p style="font-size: 1.1rem; opacity: 0.8;">
                    Get personalized outfit recommendations based on your team's colors!
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Team selection
        selected_team = st.selectbox(
            "Select Your Team",
            list(self.team_colors.keys())
        )

        # Style preference
        style_preference = st.radio(
            "Style Preference",
            ['casual', 'premium'],
            format_func=lambda x: x.title()
        )

        # Weather input (optional)
        include_weather = st.checkbox("Include weather in recommendation")
        weather_temp = None
        if include_weather:
            weather_temp = st.slider("Temperature (°F)", 30, 100, 70)

        if st.button("Get Outfit Recommendation"):
            recommendation = self.generate_recommendation(
                selected_team,
                weather_temp,
                style_preference
            )

            # Display color palette
            st.markdown("### Team Colors")
            cols = st.columns(3)
            for i, (color_name, color_hex) in enumerate(recommendation['color_scheme'].items()):
                with cols[i]:
                    st.markdown(
                        f'<div style="background-color: {color_hex}; '
                        f'padding: 20px; border-radius: 10px; '
                        f'text-align: center; color: white; '
                        f'text-shadow: 1px 1px 2px black;">'
                        f'{color_name.title()}</div>',
                        unsafe_allow_html=True
                    )

            # Display outfit recommendation
            st.markdown("""
                <div class="stat-card">
                    <h3 style="color: #9C27B0;">Recommended Outfit</h3>
                    <h4 style="margin-top: 1rem;">{}</h4>
                </div>
            """.format(recommendation['outfit_name']), unsafe_allow_html=True)

            # Display items
            st.markdown("### What to Wear")
            for item in recommendation['items']:
                st.markdown(f"- {item}")

            # Display styling tips
            st.markdown("### Styling Tips")
            for tip in recommendation['styling_tips']:
                st.info(tip)

if __name__ == "__main__":
    recommender = OutfitRecommender()
    recommender.render_outfit_ui()
