# Clustering
# k-Means Clustering Implementation

This project implements the k-Means clustering algorithm in Python.  
Originally developed as part of an academic assignment, it has been refined for portfolio purposes to demonstrate skills in algorithm design, object-oriented programming, and data structures.

## Files
- `a6algorithm.py`  
  Contains the primary `Algorithm` class that manages the k-Means process (initialization, iteration, convergence).
- `a6cluster.py`  
  Defines the `Cluster` class, representing groups of points and their centroids.
- `a6dataset.py`  
  Provides dataset utilities for storing points, retrieving dimensions, and validating inputs.

## Features
- Implementation of k-Means clustering from scratch (no external ML libraries).
- Validates cluster seeds and dataset consistency.
- Iterative updates with convergence detection using `numpy.allclose`.
- Support for centroid computation, cluster radius, and distance metrics.
- Modular object-oriented design with clear separation of concerns.

