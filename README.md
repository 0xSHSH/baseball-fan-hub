# ⚾ Baseball Fan Hub

A cutting-edge baseball fan engagement platform that transforms MLB data into immersive, interactive experiences for baseball enthusiasts. The application leverages advanced AI technologies and cloud computing to provide deep insights, personalized content, and innovative fan interaction tools.

## Features and Functionality

### 🎬 AI-Powered Highlight Generation
- Real-time game footage analysis using Google Cloud Video Intelligence
- Automated key play detection and highlight creation
- Personalized highlight reels based on user preferences

### 📊 Interactive Analytics Dashboard
- Real-time statistical analysis and visualizations
- Team performance comparisons
- Player achievement tracking
- Advanced metrics visualization using Plotly

### 🏆 Fan Engagement System
- Achievement-based progression system
- Interactive badge collection
- Daily challenges and rewards
- Team-specific content personalization

### 👕 Game Day Outfit Recommender
- Team color-based outfit suggestions
- Weather-adaptive recommendations
- Multiple style options (casual/premium)
- Personalized styling tips

## Technologies Used

### Cloud Services
- Google Cloud Video Intelligence API
- Google Cloud AI Platform
- Google Cloud BigQuery

### Frontend
- Streamlit for interactive web interface
- Plotly for dynamic visualizations
- Custom CSS for responsive design

### Data Processing
- Python for core logic
- NumPy and Pandas for statistical analysis
- Custom AI models for play prediction

## Data Sources
The application currently uses simulated data for demonstration, including:
- Player statistics (batting averages, home runs, RBIs)
- Team performance metrics
- Game scores and schedules
- Video analysis metrics

## Key Findings and Learnings
- Successfully implemented complex data visualizations using Plotly
- Created an engaging achievement system that drives user interaction
- Developed a flexible recommendation system for game day outfits
- Implemented real-time statistical analysis and data processing
- Created an intuitive user interface using Streamlit's components

## Screenshots

### 📊 Live Dashboard
![Live Dashboard] ![image alt](https://github.com/0xSHSH/baseball-fan-hub/blob/6e4ef30f036573688afccf38243816665524b47c/LiveDashboard%20.png)
Real-time game tracking and statistical visualizations

### 🏆 Fan Achievement System
![Achievement System] ![image alt](https://github.com/0xSHSH/baseball-fan-hub/blob/48c6b9659375e5e547be68d31b05e25bef2d8ce6/screenshotsachievement.png)
Interactive badge system and progress tracking

### 👕 Outfit Recommender
![Outfit Recommender] ![image alt](https://github.com/0xSHSH/baseball-fan-hub/blob/47205ab71f598c0c58d1c821be689f4a12f8a6f9/screenshotsoutfit.png)
Personalized game day outfit recommendations

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Getting Started

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/0xSHSH/baseball-fan-hub.git
cd baseball-fan-hub
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
export GOOGLE_CLOUD_API_KEY=your_api_key
```

4. Run the application:
```bash
streamlit run main.py
