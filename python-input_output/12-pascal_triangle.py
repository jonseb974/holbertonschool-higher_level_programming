#!/usr/bin/python3
# 12-pascal_triangle.py
""" Defines a Pascal's triangle. """


def pascal_triangle(n):
        """
        Represent a pascal triangle of size n.
        Return a list of integers representing a triangle.
        """
        if n <= 0:
            return[]

        triangles = [[1]]
        while len(triangles) != n:
            tri = triangles[-1]
            tmp = [1]
            for i in range(len(tri) - 1):
                tmp.append(tri[i] + tri[i + 1])
            tmp.append(1)
            triangles.append(tmp)
        return triangles
