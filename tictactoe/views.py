import json
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'tictactoe/index.html')

def evaluate_board(board):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for p in win_patterns:
        if board[p[0]] and board[p[0]] == board[p[1]] == board[p[2]]:
            return board[p[0]]
    if "" not in board:
        return "tie"
    return None

def minimax(board, depth, is_maximizing):
    result = evaluate_board(board)
    if result == 'O':
        return 10 - depth
    if result == 'X':
        return depth - 10
    if result == 'tie':
        return 0

    if is_maximizing:
        best_score = -1000
        for i in range(9):
            if board[i] == "":
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for i in range(9):
            if board[i] == "":
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ""
                best_score = min(score, best_score)
        return best_score

def ai_move(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            board = data.get('board', [""] * 9)
            
            best_score = -1000
            best_move = -1
            
            for i in range(9):
                if board[i] == "":
                    board[i] = 'O'
                    score = minimax(board, 0, False)
                    board[i] = ""
                    if score > best_score:
                        best_score = score
                        best_move = i
            
            return JsonResponse({'move': best_move})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
