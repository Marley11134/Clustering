"""
Cluster class for k-Means clustering

This file contains the class cluster, which is the second part of the assignment.
With this class done, the visualization can display the centroid of a single
cluster.56

Marley Diallo (Md2239)
11/16/2024
"""
import math
import random
import numpy

# For accessing the previous parts of the assignment
import a6dataset

# TASK 2: CLUSTER
class Cluster(object):
    """
    A class representing a cluster, a subset of the points in a dataset.

    A cluster is represented as a list of integers that give the indices in the
    dataset of the points contained in the cluster. For instance, a cluster
    consisting of the points with indices 0, 4, and 5 in the dataset's data
    array would be represented by the index list [0,4,5].

    A cluster instance also contains a centroid that is used as part of the
    k-means algorithm. This centroid is list of n numbers, where n is the
    dimension of the dataset. While this looks like a point in the dataset, it
    typically is not actually in the dataset (as it is usually in between the
    data points).
    """
    # IMMUTABLE ATTRIBUTES (Fixed after initialization with no DIRECT access)
    # Attribute _dataset: The Dataset for this cluster
    # Invariant: _dataset is an instance of Dataset
    #
    # Attribute _centroid: The centroid of this cluster
    # Invariant: _centroid is a point (list of int/float) whose length is equal
    # to the dimension of _dataset.
    #
    # MUTABLE ATTRIBUTES (Can be changed at any time, via addIndex, or clear)
    # Attribute _indices: the indices of this cluster's points in the dataset
    # Invariant: _indices is a list of ints. For each element ind in _indices,
    # 0 <= ind <= _dataset.getSize()

    # Part A
    def getIndices(self):
        """
        Returns the indices of points in this cluster

        This method returns the indices directly (not a copy). Any changes made
        to this list will modify the cluster.
        """
        # IMPLEMENT ME
        return self._indices

    def getCentroid(self):
        """
        Returns a COPY centroid of this cluster.

        This getter method is to protect access to the centroid, and prevent
        someone from changing it accidentally. That means this method has to
        copy the centroid before returning it.
        """
        # IMPLEMENT ME

        return self._centroid[:]

    def __init__(self, dset, centroid):
        """
        Initializes a new empty cluster whose centroid is a copy the given one

        This method COPIES the centroid. It does not use the original centroid
        passed as an argument.

        Parameter dset: the dataset
        Precondition: dset is an instance of Dataset

        Parameter centroid: the cluster centroid
        Precondition: centroid is a list of ds.getDimension() numbers
        """
        # IMPLEMENT ME
        assert isinstance(dset, a6dataset.Dataset)
        assert len(centroid) == dset.getDimension()
        assert a6dataset.is_point(centroid)


        self._indices = []
        self._dataset = dset
        self._centroid = centroid

    def addIndex(self, index):
        """
        Adds the given dataset index to this cluster.
        If the index is already in this cluster, this method leaves the
        cluster unchanged.

        Precondition: index is a valid index into this cluster's dataset.
        That is, index is an int >= 0, but less than the dataset size.
        """

        assert index >= 0
        assert index < self._dataset.getSize()

        if not index in self._indices:
            self._indices.append(index)

    def clear(self):
        """
        Removes all points from this cluster, but leaves the centroid unchanged.
        """
        # IMPLEMENT ME
        self._indices = []

    def getContents(self):
        """
        Returns a new list containing copies of the points in this cluster.

        The result is a list of points (lists of int/float). It has to be
        computed from the list of indices.
        """
        # IMPLEMENT ME

        end = []
        for value in self._indices:
            end.append(self._dataset.getContents()[value])
        return end

    # Part B
    def distance(self, point):
        """
        Returns the euclidean distance from point to this cluster's centroid.

        Parameter point: The point to be measured
        Precondition: point is a list of numbers (int or float), with the same
        dimension as the centroid.
        """
        # IMPLEMENT ME

        assert a6dataset.is_point(point)
        assert len(point) == len(self._centroid)

        centroid = self._centroid
        total_val = 0
        y = point

        for x in range(len(y)):
            total_val = total_val + ((y[x] - centroid[x])**2)
        result = math.sqrt(total_val)
        return result



    def getRadius(self):
        """
        Returns the maximum distance from any cluster point to the centroid.

        This method loops over the contents of this cluster to find the maximum
        distance  from the centroid.
        """
        # IMPLEMENT ME
        value  = 0
        for x in self.getContents():
            if self.distance(x) > value:
                value = self.distance(x)

        return value

    def update(self):
        """
        Returns True if the centroid remains unchanged; False otherwise.

        This method recomputes the centroid of this cluster. The new centroid is
        the average of the of the contents (To average a point, average each
        coordinate separately).

        Whether the centroid "remained unchanged" after recomputation is
        determined by numpy.allclose. The return value should be interpreted as
        an indication of whether the starting centroid was a "stable" position
        or not.

        If there are no points in the cluster, the centroid. does not change.
        """
        # IMPLEMENT ME

        get_contents= self.getContents()
        len_contents= len(self.getContents())
        centroid= self._centroid

        if len_contents == 0:
            return True
        else:
            centroid= self._centroid
            added  = [0] * len(self._centroid)
            for point in get_contents:
                for i in range(len(self._centroid)):
                    added[i] += point[i]

            point1 = [item/len(get_contents) for item in added]
            if numpy.allclose(list(point1), self._centroid):
                return True
            else:
                self._centroid = point1
                return False




    def __str__(self):
        """
        Returns a String representation of the centroid of this cluster.
        """
        return str(self._centroid)+':'+str(self._indices)

    def __repr__(self):
        """
        Returns an unambiguous representation of this cluster.
        """
        return str(self.__class__) + str(self)
