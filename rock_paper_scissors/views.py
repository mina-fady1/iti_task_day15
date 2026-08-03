import random
import json
from django.shortcuts import render
from django.http import JsonResponse

CHOICES = {
    'rock': {
        'name': 'Rock',
        'icon': 'fa-solid fa-hand-back-fist',
        'color': '#ef4444',
        'beats': {'scissors': 'crushes', 'lizard': 'crushes'}
    },
    'paper': {
        'name': 'Paper',
        'icon': 'fa-solid fa-hand',
        'color': '#3b82f6',
        'beats': {'rock': 'covers', 'spock': 'disproves'}
    },
    'scissors': {
        'name': 'Scissors',
        'icon': 'fa-solid fa-hand-scissors',
        'color': '#10b981',
        'beats': {'paper': 'cuts', 'lizard': 'decapitates'}
    },
    'lizard': {
        'name': 'Lizard',
        'icon': 'fa-solid fa-hand-lizard',
        'color': '#8b5cf6',
        'beats': {'spock': 'poisons', 'paper': 'eats'}
    },
    'spock': {
        'name': 'Spock',
        'icon': 'fa-solid fa-hand-spock',
        'color': '#f59e0b',
        'beats': {'scissors': 'smashes', 'rock': 'vaporizes'}
    }
}

def index(request):
    return render(request, 'rock_paper_scissors/index.html', {'choices': CHOICES})

def play_round(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_choice = data.get('choice')
            mode = data.get('mode', 'classic')  # 'classic' or 'rpsls'
            
            if user_choice not in CHOICES:
                return JsonResponse({'error': 'Invalid choice'}, status=400)
            
            valid_options = ['rock', 'paper', 'scissors']
            if mode == 'rpsls':
                valid_options.extend(['lizard', 'spock'])
            
            if user_choice not in valid_options:
                return JsonResponse({'error': 'Choice not allowed in this mode'}, status=400)

            computer_choice = random.choice(valid_options)
            
            if user_choice == computer_choice:
                result = 'draw'
                action = 'tie with'
            elif computer_choice in CHOICES[user_choice]['beats']:
                result = 'win'
                action = CHOICES[user_choice]['beats'][computer_choice]
            else:
                result = 'lose'
                action = CHOICES[computer_choice]['beats'][user_choice]

            return JsonResponse({
                'result': result,
                'user_choice': CHOICES[user_choice],
                'computer_choice': CHOICES[computer_choice],
                'user_key': user_choice,
                'computer_key': computer_choice,
                'action': action
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)
