import streamlit as st
from google.cloud import videointelligence
from google.cloud import aiplatform
import numpy as np
from datetime import datetime

class HighlightGenerator:
    def __init__(self):
        self.video_client = videointelligence.VideoIntelligenceServiceClient()
        self.ai_client = aiplatform.gapic.PredictionServiceClient(client_options={
            "api_endpoint": "us-central1-aiplatform.googleapis.com"
        })

    def analyze_game_footage(self, video_uri):
        """
        Analyze game footage using Google Cloud Video Intelligence API

        Args:
            video_uri: GCS URI of the video to analyze

        Returns:
            List of detected key moments with timestamps and confidence scores
        """
        try:
            features = [
                videointelligence.Feature.OBJECT_TRACKING,
                videointelligence.Feature.ACTION_RECOGNITION
            ]

            operation = self.video_client.annotate_video(
                request={
                    "input_uri": video_uri,
                    "features": features
                }
            )

            result = operation.result(timeout=180)

            # Process video analysis results
            key_moments = []
            for annotation in result.annotation_results[0].object_annotations:
                if annotation.confidence > 0.8:  # High confidence threshold
                    key_moments.append({
                        'timestamp': annotation.frames[0].time_offset.seconds,
                        'event_type': annotation.entity.description,
                        'confidence': annotation.confidence,
                        'description': self._generate_moment_description(annotation)
                    })

            return key_moments

        except Exception as e:
            st.error(f"Error analyzing video: {str(e)}")
            return []

    def _generate_moment_description(self, annotation):
        """Generate natural language description of detected moment"""
        entity = annotation.entity.description
        confidence = annotation.confidence
        frame = annotation.frames[0]

        descriptions = {
            'baseball_pitch': 'Powerful pitch delivered',
            'baseball_swing': 'Impressive batting technique',
            'baseball_catch': 'Spectacular fielding play',
            'slide': 'Athletic base running displayed'
        }

        return descriptions.get(entity, 'Notable baseball play')

    def render_highlight_ui(self):
        """Render the highlight generator interface"""
        st.markdown("""
            <div style="text-align: center; margin-bottom: 2rem;">
                <h2 style="color: #9C27B0;">🎬 Game Highlight Generator</h2>
                <p style="font-size: 1.1rem; opacity: 0.8;">
                    Create personalized game highlights powered by advanced AI analysis
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Game selection
        st.subheader("Select Game Footage")
        uploaded_file = st.file_uploader("Upload game video", type=['mp4', 'avi', 'mov'])

        if uploaded_file:
            # Process video and generate highlights
            with st.spinner("Analyzing game footage with AI..."):
                # Assuming uploaded_file is a file-like object.  May need adjustment based on Streamlit's file_uploader behavior.
                key_moments = self.analyze_game_footage(uploaded_file)

                if key_moments:
                    st.success("🎉 Analysis complete! Here are your highlights:")

                    for moment in key_moments:
                        st.markdown(f"""
                            <div class="stat-card">
                                <h3>{moment['event_type'].replace('_', ' ').title()}</h3>
                                <p>{moment['description']}</p>
                                <p><em>Confidence: {moment['confidence']:.2%}</em></p>
                                <div class="progress-bar" 
                                     style="width: {moment['confidence']*100}%">
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                else:
                    st.warning("No significant highlights detected in the footage.")

if __name__ == "__main__":
    generator = HighlightGenerator()
    generator.render_highlight_ui()