from django.shortcuts import render

def index(request):
    games = [
        {
            'id': 'tictactoe',
            'title': 'XO Cyber Duel',
            'icon': 'fa-solid fa-xmark-large',
            'badge': 'Strategy',
            'badge_color': 'var(--primary)',
            'description': 'Classic Tic-Tac-Toe re-imagined with futuristic UI, dual Player vs Player and unbeatable AI Minimax modes.',
            'url': 'tictactoe:index',
            'stats': ['PvP & PvAI Modes', 'Minimax AI Engine', 'Score Tracker']
        },
        {
            'id': 'memory_match',
            'title': 'Memory Match Arcade',
            'icon': 'fa-solid fa-brain',
            'badge': 'Puzzle',
            'badge_color': 'var(--secondary)',
            'description': 'Train your focus! Flip futuristic cards, match paired symbols, beat the timer, and claim your high score.',
            'url': 'memory_match:index',
            'stats': ['Multiple Grid Sizes', '3D Card Flips', 'Timer & Stars']
        },
        {
            'id': 'rock_paper_scissors',
            'title': 'RPS Supreme',
            'icon': 'fa-solid fa-hand-back-fist',
            'badge': 'Action',
            'badge_color': 'var(--cyan-accent)',
            'description': 'The ultimate showdown! Battle the computer in Classic RPS or extended Rock-Paper-Scissors-Lizard-Spock mode.',
            'url': 'rock_paper_scissors:index',
            'stats': ['RPS & RPSLS Rules', 'Win Streak Multipliers', 'Showdown Logs']
        }
    ]
    return render(request, 'hub/index.html', {'games': games})
