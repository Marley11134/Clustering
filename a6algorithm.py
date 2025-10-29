"""
Primary algorithm for k-Means clustering
it is the last part of the assignment, it is the heart of the clustering
algorithm. You need this class to view the complete visualizer.

Marley Diallo (Md2239)
11/16/2024
"""
import math
import random
import numpy


# For accessing the previous parts of the assignment
import a6dataset
import a6cluster

# TASK 3: ALGORITHM
# Part A
def valid_seeds(value, size):
    """
    Returns True if value is a valid list of seeds for clustering.

    A list of seeds is a k-element list of integers between 0 and size-1. In
    addition, no seed element can appear twice.

    Parameter valiud: a value to check
    Precondition: value can be anything

    Paramater size: The database size
    Precondition: size is an int > 0
    """
    # IMPLEMENT ME


    assert isinstance(size, int) and size > 0

    if isinstance(value, list):
        for val in value:
            if not isinstance(val, int):
                return False
        if len(set(value))== len(value) and max(value)<size and min(value)>-1:
            return True
    return False




class Algorithm(object):
    """
    A class to manage and run the k-means algorithm.

    The method step() performs one step of the calculation. The method run()
    will continue the calculation until it converges (or reaches a maximum
    number of steps).
    """
    # IMMUTABLE ATTRIBUTES (Fixed after initialization with no DIRECT access)
    # Attribute _dataset: The Dataset for this algorithm
    # Invariant: _dataset is an instance of Dataset
    #
    # Attribute _cluster: The clusters to use at each step
    # Invariant: _cluster is a non-empty list of Cluster instances

    # Part B
    def getClusters(self):
        """
        Returns the list of clusters in this object.

        This method returns the cluster list directly (it does not copy). Any
        changes made to this list will modify the set of clusters.
        """
        # IMPLEMENT ME
        return self._clusters

    def __init__(self, dset, k, seeds=None):
        """
        Initializes the algorithm for the dataset ds, using k clusters.

        If the optional argument seeds is supplied, those seeds will be a list
        of indices into the dataset. They specify which points should be the
        initial cluster centroids. Otherwise, the clusters are initialized by
        randomly selecting k different points from the database to be the
        cluster centroids.

        Parameter dset: the dataset
        Precondition: dset is an instance of Dataset

        Parameter k: the number of clusters
        Precondition: k is an int, 0 < k <= dset.getSize()

        Paramter seeds: the initial cluster indices (OPTIONAL)
        Precondition: seeds is None, or a list of valid seeds.
        """
        # IMPLEMENT ME
        assert isinstance(k, int)
        assert k in range(dset.getSize() + 1)
        assert isinstance(dset, a6dataset.Dataset)
        assert seeds == None or valid_seeds(seeds, dset.getSize())

        self._dataset = dset
        self._clusters = []

        value = self._dataset.getContents()[:]

        if seeds is not None:
            for i in range(k):
                self._clusters.append(a6cluster.Cluster(self._dataset,value[seeds[i]]))
        else:
            for i in range(k):
                find = random.choice(value)
                self._clusters.append(a6cluster.Cluster(self._dataset,random.choice(value)))
                value.remove(find)

    # Part C
    def _nearest(self, point):
        """
        Returns the cluster nearest to point

        This method uses the distance method of each Cluster to compute the
        distance between point and the cluster centroid. It returns the Cluster
        that is closest.

        Ties are broken in favor of clusters occurring earlier in the list
        returned by getClusters().

        Parameter point: The point to compare.
        Precondition: point is a list of numbers (int or float). Its length is
        the same as the dataset dimension.
        """
        # IMPLEMENT ME
        assert a6dataset.is_point(point) and len(point)==self._dataset.getDimension()

        dist1 = self.getClusters()[0]
        dist2 = dist1.distance(point)

        for i in self.getClusters():
            current_distance = i.distance(point)
            if current_distance < dist2:
                dist2 = current_distance
                dist1 = i

        return dist1




    def _partition(self):
        """
        Repartitions the dataset so each point is in exactly one Cluster.
        """


        for cluster in self.getClusters():
            cluster.clear()

        for i in range(len(self._dataset.getContents())):
            dist = []
            for cluster in self.getClusters():
                dist.append(cluster.distance(self._dataset.getContents()[i]))

            self.getClusters()[dist.index(min(dist))].addIndex(i)


    # Part D
    def _update(self):
        """
        Returns True if all centroids are unchanged after an update; False otherwise.

        This method first updates the centroids of all clusters'. When it is done,
        it checks whether any of them have changed. It returns False if just one
        has  changed. Otherwise, it returns True.
        """


        cent1 = []
        for val in self.getClusters():
            cent1.append(val.getCentroid())
            val.update()

        cent2 = [val.getCentroid() for val in self.getClusters()]

        for num in range(len(cent1)):
            if not numpy.allclose(cent1[num], cent2[num]):
                return False
        return True





    def step(self):
        """
        Returns True if the algorithm converges after one step; False otherwise.

        This method performs one cycle of the k-means algorithm. It then checks
        if the algorithm has converged and returns the appropriate result (True
        if converged, false otherwise).
        """

        self._partition()

        return self._update()


    def run(self, maxstep):
        """
        Continues clustering until either it converges or performs maxstep steps.

        After the maxstep call to step, if this calculation did not converge,
        this method will stop.

        Parameter maxstep: The maximum number of steps to perform
        Precondition: maxstep is an int >= 0
        """

        # IMPLEMENT ME

        assert isinstance(maxstep, int)
        assert maxstep >= 0

        for i in range(maxstep):
            step = self.step()
            if step:
                return
