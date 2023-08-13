# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 12:32:17 2023

@author: surya
"""

# ChatGPT constructed TSP problem using Ising model

#### Change this code --> apply logic for combination of dest changes as well as interaction matrix variation ---> decide what variable will you take as spins

import numpy as np
import random
from scipy.spatial.distance import squareform, pdist
import matplotlib.pyplot as plt

def create_distance_matrix(points):
    """ Create distance matrix from point coordinates """
    return squareform(pdist(points))

def create_ising_model(distance_matrix):
    """ Create Ising spin glass model from distance matrix """
    num_cities = distance_matrix.shape[0]
    interactions = np.zeros((num_cities, num_cities))
    state_matrix = np.zeros((num_cities, num_cities))
    node_vector = np.concatenate((np.arange(0, num_cities, 1), np.array([0])))  # Order of city/node connectivity

    for i in range(num_cities):
        state_matrix[node_vector[i], node_vector[i+1]] = 1
        for j in range(i + 1, num_cities):
            interactions[i, j] = distance_matrix[i, j]
            if state_matrix[i, j] != 1:
                state_matrix[i, j] = 0
                
    interactions = distance_matrix
    
    return interactions, state_matrix, node_vector

def update_spin_mat(node_vector, swap_pair):
    
    # Update node_vector with the swap
    indices = [np.where(node_vector==swap_pair[0]), np.where(node_vector==swap_pair[1])]
    t = node_vector[indices[0]]
    node_vector[indices[0]] = node_vector[indices[1]]
    node_vector[indices[1]] = t
    
    num_cities = len(node_vector) - 1
    state_matrix = np.zeros((num_cities, num_cities))
    
    for i in range(num_cities):
        state_matrix[node_vector[i], node_vector[i+1]] = 1
        for j in range(i + 1, num_cities):
            if state_matrix[i, j] != 1:
                state_matrix[i, j] = 0
                
    return state_matrix, node_vector

def simulate_annealing(ising_model, state_matrix, node_vector, num_iterations):
    """ Simulate annealing to find optimal spin configuration """
    
    epoch = 800
    optimal_points = []
    
    for i in range(epoch):
        temperature = 5000       # 5
        annealing_rate = 0.9**(2*(ising_model.shape[0]))     # 0.95**((4*ising_model.shape[0]))
        #spin_config = np.random.choice([-1, 1], size=ising_model.shape[0])
        num_cities = ising_model.shape[0]
        energy = np.sum(np.multiply(ising_model, state_matrix))  # sum(-(Jik)*sig(i)*sig(j))
    
        for i in range(num_iterations):
            temperature *= annealing_rate
            new_node_vector = node_vector.copy()
            new_state_matrix = state_matrix.copy()
            swap_pair = random.sample(range(1, num_cities), 2)
            new_state_matrix, new_node_vector = update_spin_mat(new_node_vector, swap_pair)
            new_energy = np.sum(np.multiply(ising_model, new_state_matrix))
            delta_energy = new_energy - energy
            #print(energy, node_vector, np.exp(-delta_energy / temperature))
    
            if delta_energy < 0 or np.random.rand() < np.exp(-delta_energy / temperature):
                node_vector = new_node_vector
                state_matrix = new_state_matrix
                energy = new_energy
                
        optimal_points.append([energy, node_vector])
        
    optimal_points = np.array(optimal_points)
    optimal_index = np.argmin(optimal_points[:,0])   
    optimal_points = optimal_points[optimal_index]
    print(optimal_points[0])
    
    return optimal_points[1]

def find_shortest_path(points, num_iterations):
    """ Find shortest path through all points using Ising model """
    distance_matrix = create_distance_matrix(points)
    ising_model, spin_mat, n_vec = create_ising_model(distance_matrix)
    optimal_path = simulate_annealing(ising_model, spin_mat, n_vec, num_iterations)
    #print(spin_mat)
    #path_indices = np.where(optimal_spin_config == 1)[0]
    # if path_indices.size > 0:
    #     path_indices = np.concatenate((path_indices, [path_indices[0]]))
    # shortest_path = points[path_indices]

    return optimal_path

P = []
for i in range(4):

    for j in range(4):
        P.append([i,j])
#points = np.array(P)
points = np.array([[0, 0], [15, 5], [4, 4], [6, 4], [2, 2], [12,0], [16,4], [3,6], [8, 8], [4,2], [2,4], [8,1], [23,-1], [20,6], [-1,-4]])
#points = np.array([[0, 0], [1, 1], [2,2], [3,2], [4,0], [0,1], [0,2], [1,0], [1,2], [2,0], [2,1], [3,0], [3,1], [4,1], [4,2], [5,0], [5,1], [5,2]])
num_iterations = 60*(points.shape[0])  # 60*(points.shape[0])
shortest_path = find_shortest_path(points, num_iterations)
optimal_seq_points = points[shortest_path]
plt.scatter(points[:,0], points[:,1])
plt.plot(optimal_seq_points[:,0], optimal_seq_points[:,1], 'r-')
print(optimal_seq_points)


