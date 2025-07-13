#!/usr/bin/env python3
"""
McLan Tax Baby Video Creator - Vercel Deployment
Serverless Flask app for Vercel deployment
"""

from flask import Flask, jsonify, request, render_template_string
import json
import os
from datetime import datetime, timedelta
import uuid
import time

app = Flask(__name__)

# HTML Template (inline since Vercel has issues with template folders)
DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🍼 McLan Tax Baby Video Dashboard</title>
    <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        .baby-gradient {
            background: linear-gradient(45deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
        }
        .viral-button {
            background: linear-gradient(45deg, #ff6b6b, #ee5a24);
            transition: all 0.3s ease;
        }
        .viral-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(238, 90, 36, 0.3);
        }
        .reject-button {
            background: linear-gradient(45deg, #ff6b6b, #c44569);
        }
        .reject-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(196, 69, 105, 0.3);
        }
        .stat-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
    </style>
</head>
<body>
    <div id="dashboard-root"></div>

    <script type="text/babel">
        const { useState, useEffect } = React;

        function Dashboard() {
            const [videos, setVideos] = useState([]);
            const [stats, setStats] = useState({});
            const [loading, setLoading] = useState(true);
            const [generating, setGenerating] = useState(false);

            useEffect(() => {
                fetchVideos();
                fetchStats();
                const interval = setInterval(() => {
                    fetchVideos();
                    fetchStats();
                }, 30000);
                return () => clearInterval(interval);
            }, []);

            const fetchVideos = async () => {
                try {
                    const response = await fetch('/api/videos');
                    const data = await response.json();
                    setVideos(data);
                    setLoading(false);
                } catch (error) {
                    console.error('Error fetching videos:', error);
                    setLoading(false);
                }
            };

            const fetchStats = async () => {
                try {
                    const response = await fetch('/api/stats');
                    const data = await response.json();
                    setStats(data);
                } catch (error) {
                    console.error('Error fetching stats:', error);
                }
            };

            const handleApprove = async (id) => {
                try {
                    const response = await fetch(`/api/videos/${id}/approve`, { 
                        method: 'POST' 
                    });
                    const result = await response.json();
                    
                    if (result.success) {
                        setVideos(prev => prev.filter(v => v.id !== id));
                        fetchStats();
                        alert(`✅ Video approved and posted to: ${result.platforms.join(', ')}`);
                    }
                } catch (error) {
                    console.error('Error approving video:', error);
                    alert('Error approving video');
                }
            };

            const handleReject = async (id) => {
                try {
                    const response = await fetch(`/api/videos/${id}/reject`, { 
                        method: 'POST' 
                    });
                    const result = await response.json();
                    
                    if (result.success) {
                        setVideos(prev => prev.filter(v => v.id !== id));
                        fetchStats();
                        alert('❌ Video rejected');
                    }
                } catch (error) {
                    console.error('Error rejecting video:', error);
                    alert('Error rejecting video');
                }
            };

            const handleGenerateVideo = async () => {
                setGenerating(true);
                try {
                    const response = await fetch('/api/videos/generate', {
                        method: 'POST'
                    });
                    const result = await response.json();
                    
                    if (result.success) {
                        alert('🍼 New baby video generated! Refreshing...');
                        setTimeout(() => {
                            fetchVideos();
                            fetchStats();
                        }, 1000);
                    }
                } catch (error) {
                    console.error('Error generating video:', error);
                    alert('Error generating video');
                } finally {
                    setGenerating(false);
                }
            };

            if (loading) {
                return (
                    <div className="min-h-screen flex items-center justify-center">
                        <div className="text-white text-center">
                            <div className="text-6xl mb-4">🍼</div>
                            <div className="text-2xl font-bold">Loading Baby Videos...</div>
                        </div>
                    </div>
                );
            }

            return (
                <div className="min-h-screen p-6">
                    <div className="max-w-7xl mx-auto">
                        <div className="text-center mb-8">
                            <h1 className="text-5xl font-bold text-white mb-4">
                                🍼 McLan Tax Baby Video Dashboard
                            </h1>
                            <p className="text-xl text-white opacity-90">
                                AI-Powered Viral Content Creation & Management
                            </p>
                        </div>

                        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
                            <div className="stat-card rounded-2xl p-6 text-center text-white">
                                <div className="text-3xl font-bold">{stats.pending || 0}</div>
                                <div className="text-sm opacity-80">⏳ Pending Review</div>
                            </div>
                            <div className="stat-card rounded-2xl p-6 text-center text-white">
                                <div className="text-3xl font-bold">{stats.approved || 0}</div>
                                <div className="text-sm opacity-80">✅ Approved</div>
                            </div>
                            <div className="stat-card rounded-2xl p-6 text-center text-white">
                                <div className="text-3xl font-bold">{stats.total_videos || 0}</div>
                                <div className="text-sm opacity-80">📊 Total Videos</div>
                            </div>
                            <div className="stat-card rounded-2xl p-6 text-center text-white">
                                <div className="text-3xl font-bold">{stats.recent_videos || 0}</div>
                                <div className="text-sm opacity-80">📅 This Week</div>
                            </div>
                        </div>

                        <div className="text-center mb-8">
                            <button 
                                onClick={handleGenerateVideo}
                                disabled={generating}
                                className="viral-button text-white px-8 py-4 rounded-full text-lg font-bold shadow-lg disabled:opacity-50"
                            >
                                {generating ? '🔄 Generating...' : '🚀 Generate New Baby Video'}
                            </button>
                        </div>

                        {videos.length === 0 ? (
                            <div className="text-center text-white">
                                <div className="text-6xl mb-4">👶</div>
                                <div className="text-2xl font-bold mb-2">No videos pending review</div>
                                <div className="text-lg opacity-80">Generate some baby content to get started!</div>
                            </div>
                        ) : (
                            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                                {videos.map((video) => (
                                    <div key={video.id} className="card rounded-2xl shadow-xl overflow-hidden">
                                        <div className="baby-gradient p-4">
                                            <h2 className="text-xl font-bold text-gray-800 mb-2">
                                                🔥 {video.trend}
                                            </h2>
                                            <div className="text-sm text-gray-600">
                                                📅 {new Date(video.created_at).toLocaleDateString()}
                                            </div>
                                        </div>
                                        
                                        <div className="p-6 space-y-4">
                                            <div className="bg-gray-50 p-4 rounded-lg">
                                                <div className="text-sm font-semibold text-gray-600 mb-2">👶 Baby Script:</div>
                                                <p className="italic text-gray-800 text-sm leading-relaxed">
                                                    "{video.script}"
                                                </p>
                                            </div>

                                            <div className="bg-gray-100 p-4 rounded-lg text-center">
                                                <div className="text-6xl mb-2">🎬</div>
                                                <div className="text-sm text-gray-600">Video Preview</div>
                                                <div className="text-xs text-gray-500 mt-1">
                                                    {video.videoUrl}
                                                </div>
                                            </div>

                                            <div className="space-y-2">
                                                <div className="text-sm font-semibold text-gray-600">📱 Platform Captions:</div>
                                                
                                                <div className="bg-pink-50 p-3 rounded-lg">
                                                    <div className="text-xs font-semibold text-pink-700 mb-1">📺 TikTok:</div>
                                                    <div className="text-xs text-gray-700">{video.captions.tiktok}</div>
                                                </div>
                                                
                                                <div className="bg-purple-50 p-3 rounded-lg">
                                                    <div className="text-xs font-semibold text-purple-700 mb-1">📸 Instagram:</div>
                                                    <div className="text-xs text-gray-700">{video.captions.instagram}</div>
                                                </div>
                                                
                                                <div className="bg-red-50 p-3 rounded-lg">
                                                    <div className="text-xs font-semibold text-red-700 mb-1">▶️ YouTube:</div>
                                                    <div className="text-xs text-gray-700">{video.captions.youtube}</div>
                                                </div>
                                            </div>

                                            <div className="flex gap-3 pt-4">
                                                <button 
                                                    onClick={() => handleApprove(video.id)} 
                                                    className="viral-button flex-1 text-white py-3 px-4 rounded-lg font-semibold text-sm"
                                                >
                                                    ✅ Approve & Post
                                                </button>
                                                <button 
                                                    onClick={() => handleReject(video.id)} 
                                                    className="reject-button flex-1 text-white py-3 px-4 rounded-lg font-semibold text-sm"
                                                >
                                                    ❌ Reject
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        )}
                    </div>
                </div>
            );
        }

        ReactDOM.render(<Dashboard />, document.getElementById('dashboard-root'));
    </script>
</body>
</html>
"""

# Simple JSON file storage for Vercel
DATA_FILE = '/tmp/videos.json'

def load_data():
    """Load data from JSON file."""
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        else:
            # Initialize with sample data
            sample_data = {
                'videos': [
                    {
                        'id': str(uuid.uuid4()),
                        'trend': 'Tax Season Memes Go Viral on TikTok',
                        'script': 'Hey grownups! *giggles* So I heard you\'re all stressed about taxes again? I\'m literally three months old and even I know you should call McLan Tax! 👶💰',
                        'video_url': 'https://example.com/videos/sample1.mp4',
                        'captions': {
                            'tiktok': 'When this baby knows more about taxes than you do 😂👶 #BabyTax #TaxSeason #McLanTax #FYP',
                            'instagram': 'POV: A baby gives better tax advice than your accountant 💀 @mclantax #reels #viral #tax',
                            'youtube': 'Baby Gives SAVAGE Tax Advice (You Won\'t Believe What Happens Next!) #shorts #tax #baby'
                        },
                        'status': 'pending',
                        'created_at': datetime.now().isoformat()
                    },
                    {
                        'id': str(uuid.uuid4()),
                        'trend': 'Inflation Concerns Dominate Social Media',
                        'script': 'Listen up adults! *baby babbles* I may only eat milk and baby food, but even I know inflation is crazy! My diapers cost more than your tax deductions! Call McLan Tax! 👶💸',
                        'video_url': 'https://example.com/videos/sample2.mp4',
                        'captions': {
                            'tiktok': 'This baby understands inflation better than economists 📈👶 #InflationBaby #TaxTips #McLanTax',
                            'instagram': 'When even babies are worried about the economy 😅 Let @mclantax help! #inflation #baby #tax',
                            'youtube': 'Baby Explains Inflation Crisis (Adults Are Shocked!) #shorts #inflation #baby #finance'
                        },
                        'status': 'pending',
                        'created_at': datetime.now().isoformat()
                    }
                ]
            }
            save_data(sample_data)
            return sample_data
    except Exception as e:
        print(f"Error loading data: {e}")
        return {'videos': []}

def save_data(data):
    """Save data to JSON file."""
    try:
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Error saving data: {e}")

# API Routes
@app.route('/')
def dashboard():
    """Serve the main dashboard page."""
    return render_template_string(DASHBOARD_HTML)

@app.route('/api/videos', methods=['GET'])
def get_videos():
    """Get all videos."""
    try:
        data = load_data()
        status = request.args.get('status', 'pending')
        
        # Filter videos by status
        filtered_videos = [v for v in data['videos'] if v['status'] == status]
        
        return jsonify(filtered_videos)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/videos/<video_id>/approve', methods=['POST'])
def approve_video(video_id):
    """Approve a video."""
    try:
        data = load_data()
        
        # Find and update video
        for video in data['videos']:
            if video['id'] == video_id:
                video['status'] = 'approved'
                video['approved_at'] = datetime.now().isoformat()
                video['posted_platforms'] = ['tiktok', 'instagram', 'youtube_shorts']
                break
        
        save_data(data)
        
        return jsonify({
            'success': True,
            'message': 'Video approved and posted to all platforms',
            'platforms': ['tiktok', 'instagram', 'youtube_shorts']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/videos/<video_id>/reject', methods=['POST'])
def reject_video(video_id):
    """Reject a video."""
    try:
        data = load_data()
        
        # Find and update video
        for video in data['videos']:
            if video['id'] == video_id:
                video['status'] = 'rejected'
                break
        
        save_data(data)
        
        return jsonify({'success': True, 'message': 'Video rejected'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/videos/generate', methods=['POST'])
def generate_video():
    """Generate a new video."""
    try:
        data = load_data()
        
        # Mock scenarios for random generation
        mock_scenarios = [
            {
                'trend': 'Tax Season Memes Go Viral on TikTok',
                'script': 'Hey grownups! *giggles* So I heard you\'re all stressed about taxes again? I\'m literally three months old and even I know you should call McLan Tax! They make taxes as easy as taking candy from a baby! 👶💰',
                'tiktok': 'When this baby knows more about taxes than you do 😂👶 #BabyTax #TaxSeason #McLanTax #FYP',
                'instagram': 'POV: A baby gives better tax advice than your accountant 💀 This little one knows what\'s up! 👶✨ @mclantax #reels #viral #tax',
                'youtube': 'Baby Gives SAVAGE Tax Advice (You Won\'t Believe What Happens Next!) #shorts #tax #baby #viral'
            },
            {
                'trend': 'Cryptocurrency Tax Confusion Trending',
                'script': 'Wait, wait, wait! *baby confusion sounds* You adults are confused about crypto taxes? I don\'t even know what Bitcoin is but I know McLan Tax can help! They handle all that digital money stuff! 👶💻',
                'tiktok': 'Baby solves crypto tax problems adults can\'t figure out 🤯👶 #CryptoBaby #TaxHelp #McLanTax',
                'instagram': 'This baby has better financial advice than crypto influencers 💎👶 @mclantax can help! #crypto #tax #baby',
                'youtube': 'Baby Explains Crypto Taxes (Finance Bros HATE This!) #shorts #crypto #tax #baby'
            },
            {
                'trend': 'Work From Home Tax Deductions Viral',
                'script': 'So I work from home too! *points to nursery* My home office is my crib! Can I write off my baby blanket as a business expense? McLan Tax knows all the WFH deductions! 👶🏠',
                'tiktok': 'Baby CEO claims nursery as home office tax deduction 😂👶 #WFH #TaxDeductions #BabyCEO #McLanTax',
                'instagram': 'When babies understand WFH tax deductions better than adults 💼👶 @mclantax #workfromhome #tax',
                'youtube': 'Baby Claims Nursery as Business Expense (IRS Approved?) #shorts #wfh #tax #baby'
            }
        ]
        
        import random
        scenario = random.choice(mock_scenarios)
        
        new_video = {
            'id': str(uuid.uuid4()),
            'trend': scenario['trend'],
            'script': scenario['script'],
            'video_url': f'https://example.com/videos/baby_tax_video_{int(time.time())}.mp4',
            'captions': {
                'tiktok': scenario['tiktok'],
                'instagram': scenario['instagram'],
                'youtube': scenario['youtube']
            },
            'status': 'pending',
            'created_at': datetime.now().isoformat()
        }
        
        data['videos'].append(new_video)
        save_data(data)
        
        return jsonify({'success': True, 'message': 'New baby video generated successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get dashboard statistics."""
    try:
        data = load_data()
        
        pending = len([v for v in data['videos'] if v['status'] == 'pending'])
        approved = len([v for v in data['videos'] if v['status'] == 'approved'])
        rejected = len([v for v in data['videos'] if v['status'] == 'rejected'])
        
        # Recent videos (last 7 days)
        week_ago = (datetime.now() - timedelta(days=7)).isoformat()
        recent = len([v for v in data['videos'] if v['created_at'] > week_ago])
        
        return jsonify({
            'pending': pending,
            'approved': approved,
            'rejected': rejected,
            'recent_videos': recent,
            'total_videos': len(data['videos'])
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Vercel handler
def handler(request):
    """Vercel serverless handler."""
    return app(request.environ, lambda status, headers: None)

if __name__ == '__main__':
    app.run(debug=True) 