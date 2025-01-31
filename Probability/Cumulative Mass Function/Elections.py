import random

def simulate_election(candidate_a_prob, candidate_b_prob, num_simulations=10000):
    candidate_a_wins = 0
    candidate_b_wins = 0

    for _ in range(num_simulations):
        candidate_a_votes = 0
        candidate_b_votes = 0

        for _ in range(3):  # First 3 counts
            if random.random() < candidate_a_prob:
                candidate_a_votes += 1
            else:
                candidate_b_votes += 1

        if candidate_a_votes > candidate_b_votes:
            candidate_a_wins += 1
        else:
            candidate_b_wins += 1

    candidate_a_win_prob = candidate_a_wins / num_simulations
    candidate_b_win_prob = candidate_b_wins / num_simulations

    return candidate_a_win_prob, candidate_b_win_prob

# Example usage
candidate_a_prob = 0.6  # Probability of candidate A winning a single count
candidate_b_prob = 0.4  # Probability of candidate B winning a single count

a_win_prob, b_win_prob = simulate_election(candidate_a_prob, candidate_b_prob)
print(f"Candidate A win probability: {a_win_prob:.2f}")
print(f"Candidate B win probability: {b_win_prob:.2f}")