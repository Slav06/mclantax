#!/usr/bin/env python3
"""
McLan Tax Baby Video Creator - Web Dashboard
Flask backend for the visual dashboard interface
"""

from flask import Flask, jsonify, request, render_template, send_from_directory
from flask_cors import CORS
import json
import os
import sqlite3
from datetime import datetime, timedelta
import uuid
from crew import BabyTaxVideoCrew
from config import Config
import threading
import time

app = Flask(__name__)
CORS(app)

# Database setup
def init_db():
    """Initialize the SQLite database."""
    conn = sqlite3.connect('baby_videos.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            id TEXT PRIMARY KEY,
            trend TEXT NOT NULL,
            script TEXT NOT NULL,
            video_url TEXT,
            captions TEXT,
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            approved_at TIMESTAMP,
            posted_platforms TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def get_db_connection():
    """Get database connection."""
    conn = sqlite3.connect('baby_videos.db')
    conn.row_factory = sqlite3.Row
    return conn

# API Routes
@app.route('/api/videos', methods=['GET'])
def get_videos():
    """Get all pending videos for review."""
    conn = get_db_connection()
    
    # Get filter parameters
    status = request.args.get('status', 'pending')
    limit = request.args.get('limit', 20, type=int)
    
    videos = conn.execute(
        'SELECT * FROM videos WHERE status = ? ORDER BY created_at DESC LIMIT ?',
        (status, limit)
    ).fetchall()
    
    conn.close()
    
    # Convert to JSON format
    video_list = []
    for video in videos:
        captions = json.loads(video['captions']) if video['captions'] else {}
        video_data = {
            'id': video['id'],
            'trend': video['trend'],
            'script': video['script'],
            'videoUrl': video['video_url'],
            'captions': captions,
            'status': video['status'],
            'created_at': video['created_at'],
            'approved_at': video['approved_at'],
            'posted_platforms': video['posted_platforms']
        }
        video_list.append(video_data)
    
    return jsonify(video_list)

@app.route('/api/videos/<video_id>/approve', methods=['POST'])
def approve_video(video_id):
    """Approve a video and post it to social media."""
    conn = get_db_connection()
    
    # Update video status
    conn.execute(
        'UPDATE videos SET status = ?, approved_at = ? WHERE id = ?',
        ('approved', datetime.now().isoformat(), video_id)
    )
    conn.commit()
    
    # Get video data for posting
    video = conn.execute(
        'SELECT * FROM videos WHERE id = ?', (video_id,)
    ).fetchone()
    
    conn.close()
    
    if video:
        # TODO: Integrate with actual social media posting
        # For now, simulate posting
        posted_platforms = ['tiktok', 'instagram', 'youtube_shorts']
        
        conn = get_db_connection()
        conn.execute(
            'UPDATE videos SET posted_platforms = ? WHERE id = ?',
            (json.dumps(posted_platforms), video_id)
        )
        conn.commit()
        conn.close()
        
        return jsonify({
            'success': True, 
            'message': 'Video approved and posted to all platforms',
            'platforms': posted_platforms
        })
    
    return jsonify({'success': False, 'message': 'Video not found'}), 404

@app.route('/api/videos/<video_id>/reject', methods=['POST'])
def reject_video(video_id):
    """Reject a video."""
    conn = get_db_connection()
    
    conn.execute(
        'UPDATE videos SET status = ? WHERE id = ?',
        ('rejected', video_id)
    )
    conn.commit()
    conn.close()
    
    return jsonify({'success': True, 'message': 'Video rejected'})

@app.route('/api/videos/generate', methods=['POST'])
def generate_video():
    """Generate a new video using CrewAI."""
    try:
        # Run CrewAI in background thread
        def run_crew():
            baby_crew = BabyTaxVideoCrew()
            result = baby_crew.run_daily_content_creation()
            
            # Parse CrewAI result and save to database
            # For demo purposes, create mock data
            video_id = str(uuid.uuid4())
            
            mock_data = {
                'id': video_id,
                'trend': 'Tax Season Memes Go Viral on TikTok',
                'script': 'Hey grownups! So I heard you\'re all stressed about taxes again? I\'m literally three months old and even I know you should call McLan Tax! They make taxes as easy as taking candy from a baby! 👶💰',
                'video_url': f'https://example.com/videos/baby_tax_video_{int(time.time())}.mp4',
                'captions': json.dumps({
                    'tiktok': 'When this baby knows more about taxes than you do 😂👶 #BabyTax #TaxSeason #McLanTax #FYP',
                    'instagram': 'POV: A baby gives better tax advice than your accountant 💀 This little one knows what\'s up! 👶✨ @mclantax #reels #viral #tax',
                    'youtube': 'Baby Gives SAVAGE Tax Advice (You Won\'t Believe What Happens Next!) #shorts #tax #baby #viral'
                }),
                'status': 'pending'
            }
            
            conn = get_db_connection()
            conn.execute('''
                INSERT INTO videos (id, trend, script, video_url, captions, status)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                mock_data['id'], mock_data['trend'], mock_data['script'],
                mock_data['video_url'], mock_data['captions'], mock_data['status']
            ))
            conn.commit()
            conn.close()
        
        # Start generation in background
        thread = threading.Thread(target=run_crew)
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'success': True, 
            'message': 'Video generation started in background'
        })
        
    except Exception as e:
        return jsonify({
            'success': False, 
            'message': f'Error generating video: {str(e)}'
        }), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get dashboard statistics."""
    conn = get_db_connection()
    
    # Get counts by status
    pending_count = conn.execute(
        'SELECT COUNT(*) FROM videos WHERE status = ?', ('pending',)
    ).fetchone()[0]
    
    approved_count = conn.execute(
        'SELECT COUNT(*) FROM videos WHERE status = ?', ('approved',)
    ).fetchone()[0]
    
    rejected_count = conn.execute(
        'SELECT COUNT(*) FROM videos WHERE status = ?', ('rejected',)
    ).fetchone()[0]
    
    # Get recent activity
    recent_videos = conn.execute(
        'SELECT COUNT(*) FROM videos WHERE created_at > ?',
        (datetime.now() - timedelta(days=7),)
    ).fetchone()[0]
    
    conn.close()
    
    return jsonify({
        'pending': pending_count,
        'approved': approved_count,
        'rejected': rejected_count,
        'recent_videos': recent_videos,
        'total_videos': pending_count + approved_count + rejected_count
    })

# Web Routes
@app.route('/')
def dashboard():
    """Serve the main dashboard page."""
    return render_template('dashboard.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    """Serve static files."""
    return send_from_directory('static', filename)

# Initialize database on startup
if __name__ == '__main__':
    init_db()
    
    # Add some sample data for demo
    conn = get_db_connection()
    
    # Check if we already have sample data
    existing = conn.execute('SELECT COUNT(*) FROM videos').fetchone()[0]
    
    if existing == 0:
        sample_videos = [
            {
                'id': str(uuid.uuid4()),
                'trend': 'Tax Season Memes Go Viral on TikTok',
                'script': 'Hey grownups! *giggles* So I heard you\'re all stressed about taxes again? I\'m literally three months old and even I know you should call McLan Tax! 👶💰',
                'video_url': 'https://example.com/videos/sample1.mp4',
                'captions': json.dumps({
                    'tiktok': 'When this baby knows more about taxes than you do 😂👶 #BabyTax #TaxSeason #McLanTax #FYP',
                    'instagram': 'POV: A baby gives better tax advice than your accountant 💀 @mclantax #reels #viral #tax',
                    'youtube': 'Baby Gives SAVAGE Tax Advice (You Won\'t Believe What Happens Next!) #shorts #tax #baby'
                })
            },
            {
                'id': str(uuid.uuid4()),
                'trend': 'Inflation Concerns Dominate Social Media',
                'script': 'Listen up adults! *baby babbles* I may only eat milk and baby food, but even I know inflation is crazy! My diapers cost more than your tax deductions! Call McLan Tax! 👶💸',
                'video_url': 'https://example.com/videos/sample2.mp4',
                'captions': json.dumps({
                    'tiktok': 'This baby understands inflation better than economists 📈👶 #InflationBaby #TaxTips #McLanTax',
                    'instagram': 'When even babies are worried about the economy 😅 Let @mclantax help! #inflation #baby #tax',
                    'youtube': 'Baby Explains Inflation Crisis (Adults Are Shocked!) #shorts #inflation #baby #finance'
                })
            }
        ]
        
        for video in sample_videos:
            conn.execute('''
                INSERT INTO videos (id, trend, script, video_url, captions, status)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                video['id'], video['trend'], video['script'],
                video['video_url'], video['captions'], 'pending'
            ))
        
        conn.commit()
    
    conn.close()
    
    print("🍼 McLan Tax Baby Video Dashboard Starting...")
    print("📱 Dashboard: http://localhost:5000")
    print("🔌 API: http://localhost:5000/api/videos")
    
    app.run(debug=True, port=5000) 